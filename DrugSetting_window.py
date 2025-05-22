import pymysql
from PySide6 import QtWidgets, QtCore
from PySide6.QtCore import QSize, QTimer
from PySide6.QtWidgets import QDialog, QMessageBox, QFileDialog, QLabel, QToolButton, QScrollArea, QVBoxLayout
from PySide6.QtGui import QPixmap, QIcon, Qt
from ui_DrugSetting import Ui_Dialog
from Database_connection import load_db_config
from DatabaseUtil import myDatabaseUtil  # 新增导入
import os
import shutil


class ImageViewer(QDialog):
    def __init__(self, image_path, parent=None):
        super().__init__(parent)
        self.setWindowTitle("图片查看器")
        self.setGeometry(100, 100, 800, 600)

        # 创建滚动区域
        self.scroll_area = QScrollArea(self)
        self.scroll_area.setWidgetResizable(True)  # 允许滚动区域内的部件调整大小

        # 创建图片标签
        self.image_label = QLabel()
        self.image_label.setAlignment(Qt.AlignCenter)  # 图片居中显示
        self.image_label.setScaledContents(False)  # 不自动缩放图片

        # 设置滚动区域的部件
        self.scroll_area.setWidget(self.image_label)

        # 设置布局
        layout = QVBoxLayout(self)
        layout.addWidget(self.scroll_area)
        self.setLayout(layout)

        # 加载图片
        self.pixmap = None
        self.scaled_pixmap = None  # 缓存缩放后的图片
        if image_path and os.path.exists(image_path):
            self.pixmap = QPixmap(image_path)
            if not self.pixmap.isNull():
                self.resize_image()  # 初始调整图片大小

        # 使用定时器延迟重绘，减少频繁缩放
        self.resize_timer = QTimer(self)
        self.resize_timer.setSingleShot(True)  # 单次触发
        self.resize_timer.timeout.connect(self.resize_image)

    def resizeEvent(self, event):
        """窗口大小变化时，延迟调整图片大小"""
        super().resizeEvent(event)
        self.resize_timer.start(100)  # 延迟 100 毫秒执行重绘

    def resize_image(self):
        """调整图片大小以适应窗口，并保持居中"""
        if self.pixmap is None or self.pixmap.isNull():
            return

        # 获取滚动区域的大小
        scroll_size = self.scroll_area.size()
        scroll_width = scroll_size.width()
        scroll_height = scroll_size.height()

        # 获取图片的原始大小
        pixmap_width = self.pixmap.width()
        pixmap_height = self.pixmap.height()

        # 计算缩放比例
        width_ratio = scroll_width / pixmap_width
        height_ratio = scroll_height / pixmap_height
        scale_ratio = min(width_ratio, height_ratio)

        # 按比例缩放图片，使用平滑变换
        self.scaled_pixmap = self.pixmap.scaled(
            QSize(int(pixmap_width * scale_ratio), int(pixmap_height * scale_ratio)),
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation  # 使用平滑变换
        )
        self.image_label.setPixmap(self.scaled_pixmap)

        # 设置 QLabel 的大小与缩放后的图片一致
        self.image_label.resize(self.scaled_pixmap.size())

        # 计算居中位置
        x = (scroll_width - self.scaled_pixmap.width()) // 2
        y = (scroll_height - self.scaled_pixmap.height()) // 2

        # 设置 QLabel 的位置
        self.image_label.move(x, y)


class DrugSettingWindow(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.conn = None
        self.original_data = {}
        self.column_names = ['编号', '药名', '价格', '常用量', '中药拼音', '备注']
        self.m_databaseUtil = myDatabaseUtil()  # 新增初始化数据库工具实例

        # 初始化图片标签
        self.pic_labels = [self.label_HerbPic_1, self.label_HerbPic_2, self.label_HerbPic_3, self.label_HerbPic_4]
        for label in self.pic_labels:
            label.installEventFilter(self)

        self.setup_connections()
        self.init_db()
        self.load_data()
        self.m_tbl_DrugSetting.setColumnHidden(0, True)  # 隐藏编号列
        self.m_tbl_DrugSetting.setColumnHidden(5, True)  # 隐藏备注列

    def eventFilter(self, source, event):
        if event.type() == QtCore.QEvent.MouseButtonDblClick and source in self.pic_labels:
            index = self.pic_labels.index(source)
            self.handle_pic_upload(index)
            return True
        return super().eventFilter(source, event)

    def handle_pic_upload(self, index):
        selected_row = self.m_tbl_DrugSetting.currentRow()
        if selected_row < 0:
            QMessageBox.warning(self, "提示", "请先选择中药")
            return

        herb_id_item = self.m_tbl_DrugSetting.item(selected_row, 0)
        if not herb_id_item:
            QMessageBox.warning(self, "错误", "无法获取中药编号")
            return

        herb_id = herb_id_item.text().strip()
        if not herb_id:
            QMessageBox.warning(self, "错误", "无效的中药编号")
            return

        files, _ = QFileDialog.getOpenFileNames(
            self, "选择中药照片", "",
            "图片文件 (*.png *.jpg *.jpeg);;所有文件 (*)"
        )

        if not files:
            return

        # 限制最多上传4张图片
        if len(files) > 4:
            QMessageBox.warning(self, "提示", "最多只能上传4张照片")
            files = files[:4]  # 只取前4张

        success_count = 0  # 记录成功上传的图片数量

        try:
            with self.conn.cursor() as cursor:
                # 从双击的位置开始，依次上传图片
                for i, file_path in enumerate(files):
                    current_index = (index + i) % 4  # 循环覆盖

                    # 文件大小校验
                    if os.path.getsize(file_path) > 200 * 1024:
                        QMessageBox.warning(self, "错误", f"图片 {os.path.basename(file_path)} 大小超过200KB")
                        continue

                    # 保存图片到相对路径
                    filename = f"{herb_id}_HerbPic_{current_index + 1}{os.path.splitext(file_path)[1]}"
                    save_path = os.path.join("Herbpic", filename)
                    os.makedirs(os.path.dirname(save_path), exist_ok=True)
                    shutil.copy(file_path, save_path)

                    # 更新数据库
                    cursor.execute(
                        f"UPDATE 中药 SET 中药图片{current_index + 1}=%s WHERE 编号=%s",
                        (save_path, herb_id)
                    )

                    # 更新图片显示
                    self.load_pic(current_index, save_path)

                    success_count += 1  # 成功上传一张图片

                self.conn.commit()
                QMessageBox.information(self, "成功", f"已成功上传 {success_count} 张照片")
        except Exception as e:
            self.conn.rollback()
            QMessageBox.warning(self, "错误", f"更新失败：{str(e)}")

    def load_pic(self, index, path):
        """加载图片到指定的 QLabel"""
        label = self.pic_labels[index]
        if not path or not os.path.exists(path):
            label.clear()
            if hasattr(label, 'mag_btn'):
                label.mag_btn.hide()
            return

        pixmap = QPixmap(path)
        if pixmap.isNull():
            label.clear()
            return

        # 修正拼写错误：scaled 而不是 scaled
        scaled_pixmap = pixmap.scaled(label.size(), QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
        label.setPixmap(scaled_pixmap)

        if not hasattr(label, 'mag_btn'):
            btn = QToolButton(label)
            btn.setIcon(QIcon(":/Resources/icons/icon_search.svg"))  # 使用放大镜图标
            btn.setStyleSheet("background-color: rgba(255, 255, 255, 150); border-radius: 8px;")
            btn.setIconSize(QtCore.QSize(16, 16))
            btn.setFixedSize(20, 20)
            btn.clicked.connect(lambda checked=False, path=path: self.show_enlarged_image(path))  # 修正 lambda 函数
            btn.move(label.width() - 25, 5)
            btn.show()
            label.mag_btn = btn
        else:
            label.mag_btn.path = path  # 更新 path
            label.mag_btn.clicked.disconnect()  # 断开之前的连接
            label.mag_btn.clicked.connect(lambda checked=False, path=path: self.show_enlarged_image(path))  # 重新连接
            label.mag_btn.show()

    def show_enlarged_image(self, image_path):
        """显示放大后的图片"""
        if not image_path or not os.path.exists(image_path):
            QMessageBox.warning(self, "错误", "图片路径无效")
            return

        viewer = ImageViewer(image_path, self)  # 将 self 作为父窗口传递
        viewer.show()  # 使用 show() 而不是 exec()，使其作为非模态窗口显示

    def setup_connections(self):
        """连接按钮信号与槽函数"""
        self.m_bt_add.clicked.connect(self.on_add_clicked)
        self.m_bt_save.clicked.connect(self.on_save_clicked)
        self.m_bt_del.clicked.connect(self.on_delete_clicked)
        self.m_edt_searchfilter_Drug.textChanged.connect(self.filter_data)
        self.m_tbl_DrugSetting.itemSelectionChanged.connect(self.update_remarks_edit)
        self.m_edt_DrugDiscrip.textChanged.connect(self.update_current_row_remarks)
        self.m_tbl_DrugSetting.itemSelectionChanged.connect(self.load_images_for_selected_row)

    def load_images_for_selected_row(self):
        """加载当前选中行的图片"""
        selected_row = self.m_tbl_DrugSetting.currentRow()
        if selected_row < 0:
            return  # 如果没有选中行，直接返回

        # 获取当前行的编号
        herb_id_item = self.m_tbl_DrugSetting.item(selected_row, 0)
        if not herb_id_item:
            return  # 如果没有编号，直接返回

        herb_id = herb_id_item.text().strip()
        if not herb_id:
            return  # 如果编号为空，直接返回

        # 从数据库中加载图片路径
        try:
            with self.conn.cursor() as cursor:
                cursor.execute("SELECT 中药图片1, 中药图片2, 中药图片3, 中药图片4 FROM 中药 WHERE 编号=%s", (herb_id,))
                result = cursor.fetchone()
                if result:
                    # 加载图片到 QLabel
                    for i in range(4):
                        pic_path = result[i] if result[i] else None
                        self.load_pic(i, pic_path)  # 只传入 i 和 pic_path
        except Exception as e:
            print(f"加载图片失败：{str(e)}")


    def init_db(self):
        """初始化数据库连接"""
        try:
            self.conn = pymysql.connect(**load_db_config())
        except Exception as e:
            QMessageBox.critical(self, "错误", f"数据库连接失败：{str(e)}")
            self.close()

    def load_data(self):
        """从数据库加载数据到表格"""
        try:
            with self.conn.cursor() as cursor:
                cursor.execute("SELECT 编号, 药名, 价格, 常用量, 中药拼音, 备注, 中药图片1, 中药图片2, 中药图片3, 中药图片4 FROM 中药")
                results = cursor.fetchall()
                self.m_tbl_DrugSetting.setRowCount(0)
                self.original_data.clear()

                for row_data in results:
                    row = self.m_tbl_DrugSetting.rowCount()
                    self.m_tbl_DrugSetting.insertRow(row)
                    drug_id = row_data[0]
                    # 保存原始数据（转换为字符串类型以便比较）
                    self.original_data[drug_id] = [str(item) if item is not None else '' for item in row_data]

                    for col, data in enumerate(row_data):
                        item = QtWidgets.QTableWidgetItem(str(data) if data is not None else "")
                        if col == 0:  # 编号列不可编辑
                            item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                        self.m_tbl_DrugSetting.setItem(row, col, item)

                # 加载完成后，默认选中第一行并显示备注和图片
                if self.m_tbl_DrugSetting.rowCount() > 0:
                    self.m_tbl_DrugSetting.setCurrentCell(0, 1)  # 选中第一行
                    self.update_remarks_edit()  # 更新备注编辑框
                    self.load_images_for_selected_row()  # 加载图片
        except Exception as e:
            QMessageBox.warning(self, "错误", f"加载数据失败：{str(e)}")

    def filter_data(self):
        """根据搜索框内容过滤数据"""
        keyword = self.m_edt_searchfilter_Drug.text().lower()
        for row in range(self.m_tbl_DrugSetting.rowCount()):
            drug_name = self.m_tbl_DrugSetting.item(row, 1).text().lower()
            pinyin = self.m_tbl_DrugSetting.item(row, 4).text().lower()
            self.m_tbl_DrugSetting.setRowHidden(row, keyword not in drug_name and keyword not in pinyin)

    def on_add_clicked(self):
        """新增空行"""
        row = self.m_tbl_DrugSetting.rowCount()
        self.m_tbl_DrugSetting.insertRow(row)
        # 初始化新行的项目
        for col in range(self.m_tbl_DrugSetting.columnCount()):
            item = QtWidgets.QTableWidgetItem("")
            if col == 0:
                item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            self.m_tbl_DrugSetting.setItem(row, col, item)
        # 自动聚焦到新行
        self.m_tbl_DrugSetting.setCurrentCell(row, 1)
        self.m_tbl_DrugSetting.edit(self.m_tbl_DrugSetting.currentIndex())

    def on_save_clicked(self):
        """保存所有修改到数据库"""
        try:
            # 记录当前选中的行
            current_row = self.m_tbl_DrugSetting.currentRow()  # 新增：记录当前选中的行

            # 第一阶段：智能生成拼音字段
            for row in range(self.m_tbl_DrugSetting.rowCount()):
                drug_id_item = self.m_tbl_DrugSetting.item(row, 0)
                drug_name_item = self.m_tbl_DrugSetting.item(row, 1)
                pinyin_item = self.m_tbl_DrugSetting.item(row, 4)

                # 获取当前值
                drug_id = drug_id_item.text().strip() if drug_id_item else ""
                drug_name = drug_name_item.text().strip() if drug_name_item else ""
                current_pinyin = pinyin_item.text().strip() if pinyin_item else ""

                # 逻辑核心修改：仅在新增或药名变更时生成拼音
                new_pinyin = None
                if not drug_id:  # 新增记录
                    if drug_name:
                        new_pinyin = self.m_databaseUtil.get_name_initials(drug_name)
                else:  # 现有记录
                    original = self.original_data.get(int(drug_id))
                    if original and drug_name != original[1]:  # 药名发生变更
                        new_pinyin = self.m_databaseUtil.get_name_initials(drug_name)

                # 更新拼音显示（仅在需要时）
                if new_pinyin is not None:
                    if not pinyin_item:
                        pinyin_item = QtWidgets.QTableWidgetItem(new_pinyin)
                        self.m_tbl_DrugSetting.setItem(row, 4, pinyin_item)
                    else:
                        pinyin_item.setText(new_pinyin)
                # 药名为空时清空拼音（无论新旧记录）
                if not drug_name:
                    if pinyin_item:
                        pinyin_item.setText("")

            # 第二阶段：数据库操作
            with self.conn.cursor() as cursor:
                # 先进行整体验证
                for row in range(self.m_tbl_DrugSetting.rowCount()):
                    drug_name = self.m_tbl_DrugSetting.item(row, 1).text().strip()
                    if not drug_name:
                        QMessageBox.warning(self, "错误", f"第{row + 1}行药名不能为空")
                        return

                    # 验证价格是否为有效数字
                    try:
                        price_item = self.m_tbl_DrugSetting.item(row, 2)
                        price = float(price_item.text().strip()) if price_item and price_item.text().strip() else 0.0
                    except ValueError:
                        QMessageBox.warning(self, "错误", f"第{row + 1}行价格必须为数字")
                        return

                    # 验证常用量是否为有效数字（允许为空）
                    common_dosage_item = self.m_tbl_DrugSetting.item(row, 3)
                    common_dosage = common_dosage_item.text().strip() if common_dosage_item else ""
                    if common_dosage:  # 如果常用量不为空，则验证是否为数字
                        try:
                            float(common_dosage)
                        except ValueError:
                            QMessageBox.warning(self, "错误", f"第{row + 1}行常用量必须为数字")
                            return

                # 正式保存数据
                for row in range(self.m_tbl_DrugSetting.rowCount()):
                    # 获取当前行数据（包含可能更新的拼音）
                    row_data = [
                        self.m_tbl_DrugSetting.item(row, col).text().strip() if self.m_tbl_DrugSetting.item(row, col) else ""
                        for col in range(self.m_tbl_DrugSetting.columnCount())
                    ]
                    drug_id = row_data[0]
                    drug_name = row_data[1]
                    price = float(row_data[2]) if row_data[2] else 0.0
                    common_dosage = row_data[3] if row_data[3] else None  # 允许常用量为空
                    pinyin = row_data[4]

                    # 如果是当前选中行，则从编辑框获取备注
                    if row == self.m_tbl_DrugSetting.currentRow():
                        remarks = self.m_edt_DrugDiscrip.toPlainText().strip()
                    else:
                        remarks_item = self.m_tbl_DrugSetting.item(row, 5)
                        remarks = remarks_item.text().strip() if remarks_item else ""

                    # 新增记录
                    if not drug_id:
                        cursor.execute(
                            "INSERT INTO 中药 (药名, 价格, 常用量, 中药拼音, 备注) VALUES (%s, %s, %s, %s, %s)",
                            (drug_name, price, common_dosage, pinyin, remarks)
                        )
                        drug_id = cursor.lastrowid
                    # 修改记录
                    else:
                        drug_id_int = int(drug_id)
                        original_data = self.original_data.get(drug_id_int, [])
                        # 检查字段是否变更（包含手动修改的拼音）
                        if original_data and (
                                drug_name != original_data[1] or
                                price != float(original_data[2]) or
                                common_dosage != original_data[3] or
                                pinyin != original_data[4] or
                                remarks != original_data[5] if len(original_data) > 5 else ""
                        ):
                            cursor.execute(
                                "UPDATE 中药 SET 药名=%s, 价格=%s, 常用量=%s, 中药拼音=%s, 备注=%s WHERE 编号=%s",
                                (drug_name, price, common_dosage, pinyin, remarks, drug_id)
                            )

                self.conn.commit()
                self.load_data()  # 重新加载数据刷新界面

                # 保存后重新选中当前行
                if current_row >= 0 and current_row < self.m_tbl_DrugSetting.rowCount():  # 新增：重新选中当前行
                    self.m_tbl_DrugSetting.setCurrentCell(current_row, 1)
                    self.update_remarks_edit()  # 更新备注编辑框

                QMessageBox.information(self, "成功", "保存成功")
        except pymysql.IntegrityError as e:
            self.conn.rollback()
            QMessageBox.warning(self, "错误", f"药名已存在: {str(e)}")
        except Exception as e:
            self.conn.rollback()
            QMessageBox.warning(self, "错误", f"保存失败：{str(e)}")

    def on_delete_clicked(self):
        """删除选中行"""
        selected_rows = list({index.row() for index in self.m_tbl_DrugSetting.selectedIndexes()})
        if not selected_rows:
            QMessageBox.warning(self, "警告", "请选择要删除的行")
            return

        reply = QMessageBox.question(
            self,
            "确认删除",
            "确定要删除选中的记录吗？",
            QMessageBox.Yes | QMessageBox.No
        )
        if reply == QMessageBox.No:
            return

        try:
            with self.conn.cursor() as cursor:
                # 按倒序删除避免行号变化问题
                selected_rows.sort(reverse=True)
                for row in selected_rows:
                    item_id = self.m_tbl_DrugSetting.item(row, 0).text()
                    if item_id:
                        cursor.execute("DELETE FROM 中药 WHERE 编号=%s", (item_id,))
                    self.m_tbl_DrugSetting.removeRow(row)
                self.conn.commit()
                QMessageBox.information(self, "成功", "删除成功")
        except Exception as e:
            self.conn.rollback()
            QMessageBox.warning(self, "错误", f"删除失败：{str(e)}")

    def update_remarks_edit(self):
        """更新备注编辑框内容"""
        selected = self.m_tbl_DrugSetting.selectedItems()
        if selected:
            row = selected[0].row()
            remarks_item = self.m_tbl_DrugSetting.item(row, 5) if self.m_tbl_DrugSetting.columnCount() > 5 else None
            self.m_edt_DrugDiscrip.blockSignals(True)
            self.m_edt_DrugDiscrip.setPlainText(remarks_item.text() if remarks_item else "")
            self.m_edt_DrugDiscrip.blockSignals(False)
        else:
            self.m_edt_DrugDiscrip.clear()

    def update_current_row_remarks(self):
        """更新当前行的备注"""
        selected = self.m_tbl_DrugSetting.selectedItems()
        if selected:
            row = selected[0].row()
            remarks = self.m_edt_DrugDiscrip.toPlainText()
            item = self.m_tbl_DrugSetting.item(row, 5) if self.m_tbl_DrugSetting.columnCount() > 5 else None
            if item:
                item.setText(remarks)
            else:
                new_item = QtWidgets.QTableWidgetItem(remarks)
                self.m_tbl_DrugSetting.setItem(row, 5, new_item)

    def keyPressEvent(self, event):
        """处理键盘上下键事件"""
        if event.key() == QtCore.Qt.Key_Up or event.key() == QtCore.Qt.Key_Down:
            current_row = self.m_tbl_DrugSetting.currentRow()
            if event.key() == QtCore.Qt.Key_Up and current_row > 0:
                self.m_tbl_DrugSetting.setCurrentCell(current_row - 1, 1)
            elif event.key() == QtCore.Qt.Key_Down and current_row < self.m_tbl_DrugSetting.rowCount() - 1:
                self.m_tbl_DrugSetting.setCurrentCell(current_row + 1, 1)
            self.update_remarks_edit()
            self.load_images_for_selected_row()  # 加载图片
        else:
            super().keyPressEvent(event)

    def closeEvent(self, event):
        """关闭时释放数据库连接"""
        if self.conn:
            self.conn.close()
        event.accept()