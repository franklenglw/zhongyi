import win32print
from PySide6.QtWidgets import (
    QLabel, QVBoxLayout, QToolBar,
    QScrollArea
)
from PySide6.QtGui import QImage, QPixmap, QKeySequence, QAction
from PySide6.QtPrintSupport import QPrinter, QPageSetupDialog
from PySide6.QtCore import Qt, QSize, QTimer
from PySide6.QtWidgets import QDialog
import pypdfium2 as pdfium

import platform
from PySide6.QtCore import QProcess
import os

from PySide6.QtWidgets import QMessageBox, QFileDialog

class PdfViewerDialog(QDialog):
    def __init__(self, pdf_data=None, parent=None):
        super().__init__(parent)
        # 初始化变量
        self.current_page = 0
        self.pages = []
        self.pdf_data = pdf_data
        self.printer = QPrinter(QPrinter.HighResolution)
        self.zoom_factor = 1.0
        self.ZOOM_MAX = 5.0
        self.ZOOM_MIN = 0.2
        self.auto_fit = True
        self.page_ratios = []

        # 窗口设置
        self.setWindowFlags(self.windowFlags()
                            & ~Qt.WindowContextHelpButtonHint
                            | Qt.WindowMinMaxButtonsHint)
        self.setWindowTitle("PDF 查看器")

        # 初始化界面
        self.init_ui()

        # 加载PDF数据（如果存在）
        if pdf_data:
            self.load_pdf()

        # 窗口显示设置
        QTimer.singleShot(50, self.showMaximized)

    def init_ui(self):
        """初始化用户界面"""
        # 主布局
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # 工具栏
        self.toolbar = QToolBar()
        self.toolbar.setMovable(False)
        self.toolbar.setIconSize(QSize(24, 24))
        self.add_toolbar_actions()
        main_layout.addWidget(self.toolbar)

        # 滚动区域
        self.scroll_area = QScrollArea()
        self.scroll_area.setFrameShape(QScrollArea.NoFrame)
        self.scroll_area.setWidgetResizable(True)

        self.label = QLabel()
        self.label.setAlignment(Qt.AlignCenter)
        self.scroll_area.setWidget(self.label)

        main_layout.addWidget(self.scroll_area)
        self.set_zoom(self.zoom_factor * 0.2)

    def add_toolbar_actions(self):
        """配置工具栏按钮"""
        # 缩放控制
        self.add_action("➖ 缩小", self.zoom_out, "Ctrl+-")
        self.zoom_label = QLabel("100%")
        self.zoom_label.setFixedWidth(60)
        self.zoom_label.setAlignment(Qt.AlignCenter)
        self.toolbar.addWidget(self.zoom_label)
        self.add_action("➕ 放大", self.zoom_in, "Ctrl++")
        self.toolbar.addSeparator()

        # 显示模式
        self.fit_action = self.add_action("🔍 自适应", self.toggle_auto_fit,
                                          "Ctrl+F", checkable=True)
        self.fit_action.setChecked(True)
        self.toolbar.addSeparator()

        # 打印相关
        self.add_action("⬒保存文档", self.handle_save_pdf, "Ctrl+P")
        self.add_action("🖨️ 打印文档", self.handle_print_printer)
        self.add_action("⚙️ 设置", self.print_setup)

    def add_action(self, text, handler, shortcut=None, checkable=False):
        """快速创建工具栏动作"""
        action = QAction(text, self)
        action.triggered.connect(handler)
        if shortcut:
            action.setShortcut(QKeySequence(shortcut))
        if checkable:
            action.setCheckable(True)
        self.toolbar.addAction(action)
        return action


    def load_pdf(self):
        """加载并渲染PDF文档"""
        try:
            pdf = pdfium.PdfDocument(self.pdf_data)
            self.pages.clear()
            self.page_ratios.clear()

            for page_num in range(len(pdf)):
                page = pdf.get_page(page_num)
                width = page.get_width()
                height = page.get_height()
                self.page_ratios.append(width / height)

                # 设置高分辨率（600 DPI）
                scale_factor = 600 / 72
                # 组合旧版渲染标志

                render_flags_select = 0x01 | 0x02
                bitmap = page.render(
                    scale=scale_factor,
                    rotation=0,
                    may_draw_forms=True,  # 允许绘制表单内容
                    color_scheme=None,  # 使用默认颜色方案
                    fill_to_stroke=False  # 保持原始图形模式
                )

                pil_image = bitmap.to_pil()
                img_data = pil_image.tobytes("raw", "RGB")
                qimage = QImage(
                    img_data,
                    pil_image.width,
                    pil_image.height,
                    pil_image.width * 3,
                    QImage.Format_RGB888
                )
                pixmap = QPixmap.fromImage(qimage)
                self.pages.append(pixmap)

                bitmap.close()
                page.close()

            pdf.close()
            self.show_page(0)
            self.update_zoom_display()
        except Exception as e:
            import traceback
            traceback.print_exc()
            QMessageBox.critical(self, "错误", f"PDF加载失败：{str(e)}")

    def show_page(self, page_num):
        """显示指定页码"""
        if 0 <= page_num < len(self.pages):
            self.current_page = page_num
            self.update_display()

    def update_display(self):
        """更新显示内容"""
        if not self.pages:
            return

        # 计算显示尺寸
        view_size = self.scroll_area.viewport().size()
        target_width = view_size.width() - 20
        target_height = view_size.height() - 20

        # 获取当前页面
        current_pixmap = self.pages[self.current_page]
        orig_width = current_pixmap.width()
        orig_height = current_pixmap.height()

        # 计算缩放比例
        if self.auto_fit:
            width_ratio = target_width / orig_width
            height_ratio = target_height / orig_height
            self.zoom_factor = min(width_ratio, height_ratio)
            self.update_zoom_display()

        # 应用缩放
        scaled_pixmap = current_pixmap.scaled(
            orig_width * self.zoom_factor,
            orig_height * self.zoom_factor,
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation
        )

        self.label.setPixmap(scaled_pixmap)
        self.label.resize(scaled_pixmap.size())

    # 窗口事件处理
    def resizeEvent(self, event):
        if self.auto_fit:
            self.update_display()
        super().resizeEvent(event)

    def keyPressEvent(self, event):
        """键盘快捷键"""
        if event.key() == Qt.Key_Escape:
            self.close()
        super().keyPressEvent(event)

    # 缩放功能
    def zoom_in(self):
        self.set_zoom(self.zoom_factor * 1.2)

    def zoom_out(self):
        self.set_zoom(self.zoom_factor * 0.8)

    def set_zoom(self, factor):
        """设置精确缩放比例"""
        self.auto_fit = False
        self.fit_action.setChecked(False)
        self.zoom_factor = max(self.ZOOM_MIN, min(factor, self.ZOOM_MAX))
        self.update_display()
        self.update_zoom_controls()

    def toggle_auto_fit(self):
        """切换自适应模式"""
        self.auto_fit = self.fit_action.isChecked()
        self.update_display()
        self.update_zoom_controls()

    def update_zoom_display(self):
        """更新缩放显示"""
        self.zoom_label.setText(f"{int(self.zoom_factor * 100)}%")

    def update_zoom_controls(self):
        """更新按钮状态"""
        self.toolbar.actions()[5].setEnabled(self.zoom_factor > self.ZOOM_MIN)  # 缩小
        self.toolbar.actions()[7].setEnabled(self.zoom_factor < self.ZOOM_MAX)  # 放大

    # 打印功能
    def handle_save_pdf(self):
        """执行保存"""
        self.save_pdf_document()


    def print_setup(self):
        """打印设置"""
        dialog = QPageSetupDialog(self.printer, self)
        dialog.exec()

    def handle_print_printer(self):
        """指定页打印"""
        try:
            # 获取默认打印机名称
            printer_name = win32print.GetDefaultPrinter()
            if not printer_name:
                raise ValueError("未设置默认打印机")

            # 打开打印机句柄
            hprinter = win32print.OpenPrinter(printer_name)

            try:
                # 直接启动 RAW 打印作业
                job_info = ("PDF Direct Print", None, "RAW")
                job_id = win32print.StartDocPrinter(hprinter, 1, job_info)
                win32print.StartPagePrinter(hprinter)

                # 分块写入数据（避免内存溢出）
                chunk_size = 64 * 1024  # 64KB
                for i in range(0, len(self.pdf_data), chunk_size):
                    chunk = self.pdf_data[i:i + chunk_size]
                    win32print.WritePrinter(hprinter, chunk)

                win32print.EndPagePrinter(hprinter)
                win32print.EndDocPrinter(hprinter)

            finally:
                win32print.ClosePrinter(hprinter)

            QMessageBox.information(None, "成功", "打印任务已发送到打印机队列")

        except Exception as e:
            error_map = {
                1801: "打印机未连接或电源关闭",
                5: "拒绝访问（请以管理员身份运行）",
                1722: "打印机名称无效",
            }
            error_msg = error_map.get(e.winerror, f"打印失败: {str(e)}")
            QMessageBox.critical(None, "错误", error_msg)



    def parse_page_range(self, text, max_page):
        """解析页码范围"""
        pages = set()
        for part in text.replace('，', ',').split(','):
            if '-' in part:
                start, end = map(int, part.split('-'))
                if not (1 <= start <= end <= max_page):
                    raise ValueError(f"无效范围: {part}")
                pages.update(range(start - 1, end))
            else:
                page = int(part)
                if not (1 <= page <= max_page):
                    raise ValueError(f"无效页码: {page}")
                pages.add(page - 1)
        return sorted(pages)


    def save_pdf_document(self):
        """保存PDF文件到指定位置"""
        try:
            # 获取当前工作目录下的pdf子文件夹路径
            default_dir = os.path.join(os.getcwd(), "pdf")
            # 确保目录存在
            os.makedirs(default_dir, exist_ok=True)

            # 创建文件保存对话框
            file_path, _ = QFileDialog.getSaveFileName(
                self,
                "保存PDF文件",  # 对话框标题
                default_dir,  # 初始目录
                "PDF文件 (*.pdf)"  # 文件过滤器
            )

            if file_path:
                # 自动添加.pdf后缀（如果用户没写）
                if not file_path.endswith(".pdf"):
                    file_path += ".pdf"

                # 确保目标目录存在
                target_dir = os.path.dirname(file_path)
                os.makedirs(target_dir, exist_ok=True)

                # 写入二进制数据
                with open(file_path, "wb") as f:
                    f.write(self.pdf_data)

                QMessageBox.information(
                    self,
                    "保存成功",
                    f"文件已成功保存至：\n{file_path}"
                )

        except Exception as e:
            QMessageBox.critical(
                self,
                "保存错误",
                f"保存文件失败：{str(e)}\n"
                f"建议操作：\n"
                "1. 检查文件路径是否合法\n"
                "2. 确认有写权限\n"
                "3. 检查磁盘空间"
            )

    def _format_page_range(self, pages, mac_style=False):
        """将页码列表转换为打印命令接受的格式"""
        if not pages:
            return ""

        sorted_pages = sorted(pages)
        ranges = []
        start = end = sorted_pages[0]

        for page in sorted_pages[1:]:
            if page == end + 1:
                end = page
            else:
                ranges.append(f"{start + 1}-{end + 1}" if start != end else str(start + 1))
                start = end = page
        ranges.append(f"{start + 1}-{end + 1}" if start != end else str(start + 1))

        if mac_style:
            return ",".join(ranges)
        return ",".join(ranges).replace("-", ",")

    def _execute_command(self, command):
        """执行系统命令"""
        process = QProcess()
        process.setProcessChannelMode(QProcess.MergedChannels)
        process.start("cmd.exe" if platform.system() == "Windows" else "/bin/sh", ["-c", command])

        if not process.waitForFinished(30000):  # 30秒超时
            raise TimeoutError("打印命令执行超时")

        if process.exitCode() != 0:
            error = process.readAllStandardError().data().decode()
            raise RuntimeError(f"打印命令执行失败: {error}")

    # 导航控制
    def prev_page(self):
        if self.current_page > 0:
            self.show_page(self.current_page - 1)

    def next_page(self):
        if self.current_page < len(self.pages) - 1:
            self.show_page(self.current_page + 1)

