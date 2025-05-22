import pymysql
from PySide6 import QtWidgets, QtCore
from PySide6.QtWidgets import QDialog, QMessageBox
from ui_AcupSetting import Ui_Dialog
from Database_connection import load_db_config
from pypinyin import pinyin, Style

class AcupSettingWindow(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.conn = None
        self.original_data = {}
        self.last_selected_id = None  # 新增

        # 调整表格列设置
        self.m_tbl_AcupSetting.setColumnCount(5)
        self.m_tbl_AcupSetting.setHorizontalHeaderLabels(['编号', '项目', '价格', '项目拼音', '备注'])
        self.m_tbl_AcupSetting.setColumnHidden(0, True)

        self.setup_connections()
        self.init_db()
        self.load_data()

    def setup_connections(self):
        self.m_bt_add.clicked.connect(self.on_add_clicked)
        self.m_bt_save.clicked.connect(self.on_save_clicked)
        self.m_bt_del.clicked.connect(self.on_delete_clicked)
        self.m_edt_searchfilter_Acup.textChanged.connect(self.filter_data)

    def init_db(self):
        try:
            self.conn = pymysql.connect(**load_db_config())
        except Exception as e:
            QMessageBox.critical(self, "错误", f"数据库连接失败：{str(e)}")
            self.close()

    def load_data(self):
        try:
            with self.conn.cursor() as cursor:
                cursor.execute("SELECT 编号, 项目, 价格, 项目拼音, 备注 FROM 针灸")
                results = cursor.fetchall()
                self.m_tbl_AcupSetting.setRowCount(0)
                self.original_data.clear()

                for row_data in results:
                    row = self.m_tbl_AcupSetting.rowCount()
                    self.m_tbl_AcupSetting.insertRow(row)
                    acup_id = row_data[0]
                    self.original_data[acup_id] = [str(item) if item is not None else '' for item in row_data]

                    for col, data in enumerate(row_data):
                        item = QtWidgets.QTableWidgetItem(str(data) if data else "")
                        if col == 0:
                            item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                        self.m_tbl_AcupSetting.setItem(row, col, item)
        except Exception as e:
            QMessageBox.warning(self, "错误", f"加载数据失败：{str(e)}")

    def filter_data(self):
        keyword = self.m_edt_searchfilter_Acup.text().lower()
        for row in range(self.m_tbl_AcupSetting.rowCount()):
            project = self.m_tbl_AcupSetting.item(row, 1).text().lower()
            pinyin = self.m_tbl_AcupSetting.item(row, 3).text().lower()
            self.m_tbl_AcupSetting.setRowHidden(row, keyword not in project and keyword not in pinyin)

    def on_add_clicked(self):
        row = self.m_tbl_AcupSetting.rowCount()
        self.m_tbl_AcupSetting.insertRow(row)
        for col in range(self.m_tbl_AcupSetting.columnCount()):
            item = QtWidgets.QTableWidgetItem("")
            if col == 0:
                item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            self.m_tbl_AcupSetting.setItem(row, col, item)
        self.m_tbl_AcupSetting.setCurrentCell(row, 1)
        self.m_tbl_AcupSetting.edit(self.m_tbl_AcupSetting.currentIndex())

    def get_pinyin_initials(self, name):
        """根据项目名称生成拼音首字母"""
        if not name:
            return ""
        try:
            initials = [p[0][0].upper() for p in pinyin(name, style=Style.FIRST_LETTER)]
            return ''.join(initials)
        except Exception as e:
            print(f"生成拼音失败：{e}")
            return ""

    def on_save_clicked(self):
        # 保存当前选中行ID
        current_row = self.m_tbl_AcupSetting.currentRow()
        if current_row >= 0:
            current_id_item = self.m_tbl_AcupSetting.item(current_row, 0)
            self.last_selected_id = current_id_item.text() if current_id_item else None

        try:
            with self.conn.cursor() as cursor:
                # 第一阶段：智能生成拼音
                for row in range(self.m_tbl_AcupSetting.rowCount()):
                    acup_id_item = self.m_tbl_AcupSetting.item(row, 0)
                    project_item = self.m_tbl_AcupSetting.item(row, 1)
                    pinyin_item = self.m_tbl_AcupSetting.item(row, 3)

                    # 获取当前值
                    acup_id = acup_id_item.text().strip() if acup_id_item else ""
                    project_name = project_item.text().strip() if project_item else ""
                    current_pinyin = pinyin_item.text().strip() if pinyin_item else ""

                    new_pinyin = None
                    if not acup_id:  # 新增记录
                        if project_name:
                            new_pinyin = self.get_pinyin_initials(project_name)
                    else:  # 现有记录
                        original = self.original_data.get(int(acup_id))
                        if original and project_name != original[1]:  # 项目名称变更
                            new_pinyin = self.get_pinyin_initials(project_name)

                    # 更新拼音显示
                    if new_pinyin is not None:
                        if not pinyin_item:
                            pinyin_item = QtWidgets.QTableWidgetItem(new_pinyin)
                            self.m_tbl_AcupSetting.setItem(row, 3, pinyin_item)
                        else:
                            pinyin_item.setText(new_pinyin)

                # 第二阶段：验证数据有效性
                valid = True
                for row in range(self.m_tbl_AcupSetting.rowCount()):
                    project_item = self.m_tbl_AcupSetting.item(row, 1)
                    price_item = self.m_tbl_AcupSetting.item(row, 2)

                    if not project_item or not project_item.text().strip():
                        QMessageBox.warning(self, "错误", f"第{row + 1}行项目不能为空")
                        valid = False
                        break
                    try:
                        float(price_item.text() if price_item else "")
                    except ValueError:
                        QMessageBox.warning(self, "错误", f"第{row + 1}行价格格式错误")
                        valid = False
                        break
                if not valid:
                    return

                # 第三阶段：保存数据
                for row in range(self.m_tbl_AcupSetting.rowCount()):
                    # 获取当前行数据（包含可能更新的拼音）
                    row_data = [
                        self.m_tbl_AcupSetting.item(row, col).text().strip() if self.m_tbl_AcupSetting.item(row, col) else ""
                        for col in range(self.m_tbl_AcupSetting.columnCount())
                    ]
                    acup_id = row_data[0]
                    project_name = row_data[1]
                    price = float(row_data[2]) if row_data[2] else 0.0
                    pinyin_initials = row_data[3]
                    remark = row_data[4]

                    # 新增记录
                    if not acup_id:
                        cursor.execute(
                            "INSERT INTO 针灸 (项目, 价格, 项目拼音, 备注) VALUES (%s, %s, %s, %s)",
                            (project_name, price, pinyin_initials, remark)
                        )
                        new_id = cursor.lastrowid
                        self.last_selected_id = new_id
                    else:  # 更新记录
                        original = self.original_data.get(int(acup_id), [])
                        # 比较数值型字段时需转换类型
                        original_price = float(original[2]) if original and original[2] else 0.0
                        if original and (
                            original[1] != project_name or
                            original_price != price or
                            original[3] != pinyin_initials or
                            original[4] != remark
                        ):
                            cursor.execute(
                                "UPDATE 针灸 SET 项目=%s, 价格=%s, 项目拼音=%s, 备注=%s WHERE 编号=%s",
                                (project_name, price, pinyin_initials, remark, acup_id)
                            )

                self.conn.commit()
                self.load_data()
                QMessageBox.information(self, "成功", "保存成功")

                # 重新定位到之前选中的行
                if self.last_selected_id is not None:
                    self.select_row_by_id(self.last_selected_id)

        except Exception as e:
            self.conn.rollback()
            QMessageBox.critical(self, "错误", f"保存失败：{str(e)}")

    def select_row_by_id(self, target_id):
        """根据编号定位到指定行"""
        for row in range(self.m_tbl_AcupSetting.rowCount()):
            item = self.m_tbl_AcupSetting.item(row, 0)
            if item and item.text() == str(target_id):
                self.m_tbl_AcupSetting.selectRow(row)
                self.m_tbl_AcupSetting.setCurrentCell(row, 1)
                self.m_tbl_AcupSetting.scrollToItem(
                    self.m_tbl_AcupSetting.item(row, 1),
                    QtWidgets.QAbstractItemView.PositionAtTop
                )
                break

    def on_delete_clicked(self):
        selected_rows = list({index.row() for index in self.m_tbl_AcupSetting.selectedIndexes()})
        if not selected_rows:
            QMessageBox.warning(self, "警告", "请选择要删除的行")
            return

        if QMessageBox.Yes == QMessageBox.question(self, "确认", "确定要删除选中行吗？", QMessageBox.Yes | QMessageBox.No):
            try:
                with self.conn.cursor() as cursor:
                    for row in sorted(selected_rows, reverse=True):
                        if item_id := self.m_tbl_AcupSetting.item(row, 0).text():
                            cursor.execute("DELETE FROM 针灸 WHERE 编号=%s", item_id)
                        self.m_tbl_AcupSetting.removeRow(row)
                    self.conn.commit()
                    QMessageBox.information(self, "成功", "删除成功")
            except Exception as e:
                self.conn.rollback()
                QMessageBox.critical(self, "错误", f"删除失败：{str(e)}")

    def closeEvent(self, event):
        if self.conn:
            self.conn.close()
        super().closeEvent(event)