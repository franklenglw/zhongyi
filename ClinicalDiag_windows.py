import pymysql
from PySide6 import QtWidgets, QtCore
from PySide6.QtWidgets import QDialog, QMessageBox
from ui_ClinicalDiag import Ui_Dialog
from Database_connection import load_db_config
from pypinyin import pinyin, Style  # 新增导入

class ClinicalDiagWindow(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.conn = None
        self.original_data = {}
        self.setup_connections()
        self.init_db()
        self.load_data()
        self.m_tbl_ClinicalDiag.setColumnHidden(0, True)

    def get_pinyin_initials(self, name):
        """根据诊断名称生成拼音首字母"""
        if not name:
            return ""
        try:
            initials = [p[0][0].upper() for p in pinyin(name, style=Style.FIRST_LETTER)]
            return ''.join(initials)
        except Exception as e:
            print(f"生成拼音失败：{e}")
            return ""

    def setup_connections(self):
        self.m_bt_add.clicked.connect(self.on_add_clicked)
        self.m_bt_save.clicked.connect(self.on_save_clicked)
        self.m_bt_del.clicked.connect(self.on_delete_clicked)
        self.m_edt_searchfilterDiag.textChanged.connect(self.filter_data)

    def init_db(self):
        try:
            self.conn = pymysql.connect(**load_db_config())
        except Exception as e:
            QMessageBox.critical(self, "错误", f"数据库连接失败：{str(e)}")
            self.close()

    def load_data(self):
        try:
            with self.conn.cursor() as cursor:
                cursor.execute("SELECT 编号, 诊断, 诊断拼音 FROM 诊断")
                results = cursor.fetchall()
                self.m_tbl_ClinicalDiag.setRowCount(0)
                self.original_data.clear()

                for row_data in results:
                    row = self.m_tbl_ClinicalDiag.rowCount()
                    self.m_tbl_ClinicalDiag.insertRow(row)
                    diag_id = row_data[0]
                    self.original_data[diag_id] = [str(item) if item is not None else '' for item in row_data]

                    for col, data in enumerate(row_data):
                        item = QtWidgets.QTableWidgetItem(str(data) if data is not None else "")
                        if col == 0:
                            item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                        self.m_tbl_ClinicalDiag.setItem(row, col, item)
        except Exception as e:
            QMessageBox.warning(self, "错误", f"加载数据失败：{str(e)}")

    def filter_data(self):
        keyword = self.m_edt_searchfilterDiag.text().lower()
        for row in range(self.m_tbl_ClinicalDiag.rowCount()):
            diag_name = self.m_tbl_ClinicalDiag.item(row, 1).text().lower()
            pinyin = self.m_tbl_ClinicalDiag.item(row, 2).text().lower()
            self.m_tbl_ClinicalDiag.setRowHidden(row, keyword not in diag_name and keyword not in pinyin)

    def on_add_clicked(self):
        row = self.m_tbl_ClinicalDiag.rowCount()
        self.m_tbl_ClinicalDiag.insertRow(row)
        for col in range(self.m_tbl_ClinicalDiag.columnCount()):
            item = QtWidgets.QTableWidgetItem("")
            if col == 0:
                item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            self.m_tbl_ClinicalDiag.setItem(row, col, item)
        self.m_tbl_ClinicalDiag.setCurrentCell(row, 1)
        self.m_tbl_ClinicalDiag.edit(self.m_tbl_ClinicalDiag.currentIndex())

    def on_save_clicked(self):
        """优化后的保存逻辑（遵循ClinicalSymptoms的智能生成策略）"""
        try:
            # 第一阶段：智能生成拼音
            for row in range(self.m_tbl_ClinicalDiag.rowCount()):
                diag_id_item = self.m_tbl_ClinicalDiag.item(row, 0)
                diag_name_item = self.m_tbl_ClinicalDiag.item(row, 1)
                pinyin_item = self.m_tbl_ClinicalDiag.item(row, 2)

                # 获取当前值
                diag_id = diag_id_item.text().strip() if diag_id_item else ""
                diag_name = diag_name_item.text().strip() if diag_name_item else ""
                current_pinyin = pinyin_item.text().strip() if pinyin_item else ""

                # 智能生成策略
                new_pinyin = None
                if not diag_id:  # 新增记录
                    if diag_name:
                        new_pinyin = self.get_pinyin_initials(diag_name)
                else:  # 现有记录
                    original = self.original_data.get(int(diag_id))
                    if original and diag_name != original[1]:  # 名称变更时更新
                        new_pinyin = self.get_pinyin_initials(diag_name)

                # 更新表格显示
                if new_pinyin is not None:
                    if not pinyin_item:
                        pinyin_item = QtWidgets.QTableWidgetItem(new_pinyin)
                        self.m_tbl_ClinicalDiag.setItem(row, 2, pinyin_item)
                    else:
                        pinyin_item.setText(new_pinyin)

            # 第二阶段：数据库操作
            with self.conn.cursor() as cursor:
                # 先进行整体验证
                for row in range(self.m_tbl_ClinicalDiag.rowCount()):
                    diag_name = self.m_tbl_ClinicalDiag.item(row, 1).text().strip()
                    if not diag_name:
                        QMessageBox.warning(self, "错误", f"第{row + 1}行诊断不能为空")
                        return

                # 正式保存数据
                for row in range(self.m_tbl_ClinicalDiag.rowCount()):
                    # 获取当前行数据（包含可能更新的拼音）
                    row_data = [
                        self.m_tbl_ClinicalDiag.item(row, col).text().strip()
                        if self.m_tbl_ClinicalDiag.item(row, col) else ""
                        for col in range(self.m_tbl_ClinicalDiag.columnCount())
                    ]
                    diag_id = row_data[0]
                    diag_name = row_data[1]
                    pinyin = row_data[2]

                    # 新增记录
                    if not diag_id:
                        cursor.execute(
                            "INSERT INTO 诊断 (诊断, 诊断拼音) VALUES (%s, %s)",
                            (diag_name, pinyin)
                        )
                    # 修改记录
                    else:
                        diag_id_int = int(diag_id)
                        original = self.original_data.get(diag_id_int, [])
                        # 检查字段是否变更（包含手动修改的拼音）
                        if original and (
                                diag_name != original[1] or
                                pinyin != original[2]
                        ):
                            cursor.execute(
                                "UPDATE 诊断 SET 诊断=%s, 诊断拼音=%s WHERE 编号=%s",
                                (diag_name, pinyin, diag_id)
                            )

                self.conn.commit()
                self.load_data()  # 刷新数据
                QMessageBox.information(self, "成功", "保存成功")

        except pymysql.IntegrityError as e:
            self.conn.rollback()
            QMessageBox.warning(self, "错误", f"诊断名称已存在: {str(e)}")
        except Exception as e:
            self.conn.rollback()
            QMessageBox.warning(self, "错误", f"保存失败：{str(e)}")

    def on_delete_clicked(self):
        selected_rows = list({index.row() for index in self.m_tbl_ClinicalDiag.selectedIndexes()})
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
                selected_rows.sort(reverse=True)
                for row in selected_rows:
                    item_id = self.m_tbl_ClinicalDiag.item(row, 0).text()
                    if item_id:
                        cursor.execute("DELETE FROM 诊断 WHERE 编号=%s", (item_id,))
                    self.m_tbl_ClinicalDiag.removeRow(row)
                self.conn.commit()
                QMessageBox.information(self, "成功", "删除成功")
        except Exception as e:
            self.conn.rollback()
            QMessageBox.warning(self, "错误", f"删除失败：{str(e)}")

    def closeEvent(self, event):
        if self.conn:
            self.conn.close()
        event.accept()