from PySide6.QtWidgets import *
from PySide6.QtCore import Qt
from PySide6.QtGui import QScreen, QColor


class mySearchableComboBox:
    """可搜索组合框工厂类"""

    def __init__(self, parent_table, config):
        """
        :param parent_table: 父级表格控件
        :param config: 配置字典，包含：
            - column 列号
            - data_source 数据获取方法
            - filter_logic 过滤逻辑方法
            - placeholder 搜索框提示文本
            - use_dialog 是否使用弹出对话框（默认True）
        """
        self.parent_table = parent_table
        self.config = config
        self._cached_data = None

    def create(self, row):
        """创建组合框"""
        if self.config.get('use_dialog', True):
            self._create_dialog_combo(row)
        else:
            self._create_simple_combo(row)

    def _create_dialog_combo(self, row):
        """创建带搜索对话框的组合框"""
        self._clear_existing_widget(row)

        dialog = self._create_base_dialog()
        container = QFrame(dialog)
        container.setObjectName("ShadowContainer")
        container.setStyleSheet("""
                #ShadowContainer {
                    background: #FFFFFF;
                    border-radius: 5px;
                    border: 1px solid #DDDDDD;
                }
            """)
        # 添加阴影效果
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(15)
        shadow.setXOffset(0)
        shadow.setYOffset(2)
        shadow.setColor(QColor(0, 0, 0, 50))
        container.setGraphicsEffect(shadow)

        container_layout = QVBoxLayout(container)
        container_layout.setContentsMargins(5, 5, 5, 5)
        container_layout.setSpacing(5)

        search_edit = self._create_search_box(container)
        table_widget = self._create_table()
        container_layout.addWidget(search_edit)
        container_layout.addWidget(table_widget)
        dialog.layout().addWidget(container)
        dialog.layout().setContentsMargins(25, 20, 15, 20)  # 增加边距显示阴影

        # 确保样式生效
        container.setAttribute(Qt.WA_StyledBackground, True)

        # 初始化数据加载
        self._load_initial_data(table_widget, row)

        # 信号连接
        search_edit.textChanged.connect(
            lambda text: self.config['filter_logic'](table_widget, text)
        )
        table_widget.itemClicked.connect(
            lambda: self._handle_selection(dialog, table_widget, row)
        )

        self._position_dialog(dialog, row)
        dialog.exec()

    def _create_simple_combo(self, row):
        """创建简单下拉框"""
        self._clear_existing_widget(row)

        combo = QComboBox()
        data = self.config['data_source']()
        combo.addItems(data)

        current_value = self._get_cell_value(row)
        if current_value:
            index = combo.findText(current_value)
            combo.setCurrentIndex(index if index >= 0 else 0)

        combo.activated.connect(lambda: self._update_table_value(combo, row))
        self.parent_table.setCellWidget(row, self.config['column'], combo)
        combo.showPopup()

    # ---------- 通用组件创建方法 ----------
    def _create_base_dialog(self):
        """创建基础对话框"""
        dialog = QDialog(self.parent_table)
        dialog.setWindowFlags(Qt.FramelessWindowHint | Qt.Popup)
        dialog.setFixedWidth(250)
        dialog.setLayout(QVBoxLayout())
        dialog.layout().setContentsMargins(5, 5, 5, 5)
        dialog.layout().setSpacing(5)
        return dialog

    def _create_search_box(self, dialog):
        """创建搜索框组件"""
        container = QWidget()
        container.setLayout(QHBoxLayout())
        container.layout().setContentsMargins(0, 0, 0, 0)

        lbl = QLabel("搜索：")
        edit = QLineEdit()
        edit.setPlaceholderText(self.config.get('placeholder', '输入搜索内容'))

        container.layout().addWidget(lbl)
        container.layout().addWidget(edit)
        dialog.layout().addWidget(container)
        return edit

    def _create_table(self):
        """创建表格组件"""
        table = QTableWidget()
        table.setColumnCount(1)
        table.horizontalHeader().setVisible(False)
        table.verticalHeader().setVisible(False)
        table.setSelectionMode(QAbstractItemView.SingleSelection)
        table.setEditTriggers(QTableWidget.NoEditTriggers)
        table.verticalHeader().setDefaultSectionSize(24)
        return table

    # ---------- 数据处理方法 ----------
    def _load_initial_data(self, table_widget, row):
        """加载初始数据"""
        if hasattr(self, '_cached_data'):
            self._cached_data = self.config['data_source']()

        #data = self.config['data_source']()
        table_widget.setRowCount(0)

        for text in self._cached_data:
            row_pos = table_widget.rowCount()
            table_widget.insertRow(row_pos)
            table_widget.setItem(row_pos, 0, QTableWidgetItem(text))

        self._set_initial_selection(table_widget, row)

    def _set_initial_selection(self, table_widget, row):
        """设置初始选中项"""
        if item := self.parent_table.item(row, self.config['column']):
            current_text = item.text()
            for i in range(table_widget.rowCount()):
                if table_widget.item(i, 0).text() == current_text:
                    table_widget.setCurrentCell(i, 0)
                    break

    # ---------- 事件处理方法 ----------
    def _handle_selection(self, dialog, table_widget, row):
        """处理选择事件"""
        if selected := table_widget.selectedItems():
            selected_text = selected[0].text()
            if selected_text != "未找到匹配项":
                self._update_table_value(selected_text, row)
                dialog.close()

    def _update_table_value(self, value, row):
        """更新表格值"""
        if isinstance(value, QComboBox):
            value = value.currentText()

        if not self.parent_table.item(row, self.config['column']):
            self.parent_table.setItem(row, self.config['column'], QTableWidgetItem(value))
        else:
            self.parent_table.item(row, self.config['column']).setText(value)

        self._adjust_row_height(row)

    # ---------- 通用工具方法 ----------
    def _clear_existing_widget(self, row):
        """清除现有控件"""
        if widget := self.parent_table.cellWidget(row, self.config['column']):
            widget.deleteLater()
            self.parent_table.removeCellWidget(row, self.config['column'])

    def _position_dialog(self, dialog, row):
        """定位对话框"""
        index = self.parent_table.model().index(row, self.config['column'])
        rect = self.parent_table.visualRect(index)
        point = self.parent_table.viewport().mapToGlobal(rect.topRight())
        screen_geo = QScreen.geometry(QApplication.primaryScreen())

        dialog_width = dialog.sizeHint().width()
        if point.x() + dialog_width > screen_geo.right():
            point.setX(screen_geo.right() - dialog_width)

        dialog.move(point)

    def _adjust_row_height(self, row):
        """调整行高"""
        self.parent_table.resizeRowToContents(row)
        self.parent_table.verticalHeader().setSectionResizeMode(
            row, QHeaderView.Interactive
        )

    def _get_cell_value(self, row):
        """获取单元格值"""
        item = self.parent_table.item(row, self.config['column'])
        return item.text() if item else ""
