import sys
from PySide6 import QtWidgets, QtCore
from PySide6.QtWidgets import QDialog, QMessageBox, QTableWidgetItem
from ui_ClinicalAnylasis import Ui_Dialog
import pymysql
from Database_connection import load_db_config
from pypinyin import pinyin, Style  # 新增导入

class ClinicalAnylasisWindow(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.conn = None
        self.original_data = {}
        self.last_selected_id = None
        self.setup_connections()
        self.init_db()
        self.load_data()
        self.m_tbl_Anylasis.setColumnHidden(0, True)  # 隐藏编号列
        self.m_tbl_Anylasis.setColumnHidden(3, True)  # 隐藏说明列
        self.m_tbl_Anylasis.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.m_tbl_Anylasis.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)

    def get_pinyin_initials(self, name):
        """根据辩证名称生成拼音首字母"""
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
        self.m_edt_searchfilterAnyl.textChanged.connect(self.on_filter_text_changed)
        self.m_tbl_Anylasis.itemSelectionChanged.connect(self.update_description_edit)
        self.m_edt_AnylDiscrip.textChanged.connect(self.update_current_row_description)

    def init_db(self):
        try:
            self.conn = pymysql.connect(**load_db_config())
        except Exception as e:
            QMessageBox.critical(self, "错误", f"数据库连接失败：{str(e)}")
            sys.exit(1)

    def load_data(self):
        try:
            with self.conn.cursor() as cursor:
                cursor.execute("SELECT 编号, 辩证, 辩证拼音, 说明 FROM 辩证")
                results = cursor.fetchall()
                self.m_tbl_Anylasis.setRowCount(0)
                self.original_data.clear()

                for row_data in results:
                    row = self.m_tbl_Anylasis.rowCount()
                    self.m_tbl_Anylasis.insertRow(row)
                    self.original_data[row_data[0]] = list(row_data)

                    for col, data in enumerate(row_data):
                        item = QtWidgets.QTableWidgetItem(str(data))
                        if col == 0:
                            item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                        self.m_tbl_Anylasis.setItem(row, col, item)

                # 数据加载完成后定位到上次选中的行
                if self.last_selected_id is not None:
                    self.select_row_by_id(self.last_selected_id)

        except Exception as e:
            QMessageBox.warning(self, "错误", f"加载数据失败：{str(e)}")

    def on_add_clicked(self):
        row = self.m_tbl_Anylasis.rowCount()
        self.m_tbl_Anylasis.insertRow(row)
        for col in range(self.m_tbl_Anylasis.columnCount()):
            item = QtWidgets.QTableWidgetItem("")
            if col == 0:
                item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            self.m_tbl_Anylasis.setItem(row, col, item)
        self.m_tbl_Anylasis.setCurrentCell(row, 1)
        self.m_tbl_Anylasis.edit(self.m_tbl_Anylasis.currentIndex())

    def on_save_clicked(self):
        current_row = self.m_tbl_Anylasis.currentRow()
        if current_row >= 0:
            current_id_item = self.m_tbl_Anylasis.item(current_row, 0)
            self.last_selected_id = current_id_item.text() if current_id_item else None

        try:
            # 第一阶段：智能生成拼音（仅名称变更时更新）
            for row in range(self.m_tbl_Anylasis.rowCount()):
                bianzheng_id_item = self.m_tbl_Anylasis.item(row, 0)
                bianzheng_item = self.m_tbl_Anylasis.item(row, 1)
                pinyin_item = self.m_tbl_Anylasis.item(row, 2)

                # 获取当前值
                bianzheng_id = bianzheng_id_item.text().strip() if bianzheng_id_item else ""
                bianzheng = bianzheng_item.text().strip() if bianzheng_item else ""
                current_pinyin = pinyin_item.text().strip() if pinyin_item else ""

                # 拼音生成策略调整（核心修改点）
                new_pinyin = None
                if not bianzheng_id:  # 新增记录
                    if bianzheng:
                        new_pinyin = self.get_pinyin_initials(bianzheng)
                else:  # 现有记录
                    original = self.original_data.get(int(bianzheng_id))
                    if original and bianzheng != original[1]:  # 名称发生变更
                        new_pinyin = self.get_pinyin_initials(bianzheng)

                # 更新界面显示（仅当需要生成新拼音时）
                if new_pinyin is not None:
                    if not pinyin_item:
                        pinyin_item = QTableWidgetItem(new_pinyin)
                        self.m_tbl_Anylasis.setItem(row, 2, pinyin_item)
                    else:
                        pinyin_item.setText(new_pinyin)

            # 第二阶段：数据库操作（保留手动修改的拼音）
            with self.conn.cursor() as cursor:
                # 先进行整体验证
                for row in range(self.m_tbl_Anylasis.rowCount()):
                    bianzheng = self.m_tbl_Anylasis.item(row, 1).text().strip()
                    if not bianzheng:
                        QMessageBox.warning(self, "错误", f"第{row + 1}行辩证不能为空")
                        return

                # 正式保存数据
                for row in range(self.m_tbl_Anylasis.rowCount()):
                    # 获取当前行数据（包含可能更新的拼音）
                    row_data = [
                        self.m_tbl_Anylasis.item(row, col).text().strip() if self.m_tbl_Anylasis.item(row, col) else ""
                        for col in range(self.m_tbl_Anylasis.columnCount())
                    ]
                    bianzheng_id = row_data[0]
                    bianzheng = row_data[1]
                    pinyin = row_data[2]
                    description = row_data[3]

                    # 新增记录
                    if not bianzheng_id:
                        if bianzheng:  # 确保辩证名称不为空
                            cursor.execute(
                                "INSERT INTO 辩证 (辩证, 辩证拼音, 说明) VALUES (%s, %s, %s)",
                                (bianzheng, pinyin, description)
                            )
                            new_id = cursor.lastrowid
                            self.last_selected_id = new_id
                    # 更新记录
                    else:
                        bianzheng_id_int = int(bianzheng_id)
                        original = self.original_data.get(bianzheng_id_int)
                        if original and (
                                bianzheng != original[1] or
                                pinyin != original[2] or
                                description != original[3]
                        ):
                            cursor.execute(
                                "UPDATE 辩证 SET 辩证=%s, 辩证拼音=%s, 说明=%s WHERE 编号=%s",
                                (bianzheng, pinyin, description, bianzheng_id)
                            )

                self.conn.commit()
                self.load_data()  # 重新加载数据以刷新原始数据缓存
                QMessageBox.information(self, "成功", "保存成功")

                if self.last_selected_id is not None:
                    self.select_row_by_id(self.last_selected_id)

        except pymysql.IntegrityError as e:
            self.conn.rollback()
            QMessageBox.warning(self, "错误", f"数据唯一性冲突：{str(e)}")
        except Exception as e:
            self.conn.rollback()
            QMessageBox.warning(self, "错误", f"保存失败：{str(e)}")

    def on_delete_clicked(self):
        # 获取所有选中的行号（去重）
        selected_rows = list({index.row() for index in self.m_tbl_Anylasis.selectedIndexes()})
        if not selected_rows:
            QMessageBox.warning(self, "警告", "请选择要删除的行")
            return

        reply = QMessageBox.question(
            self, "确认删除",
            f"确定要删除选中的 {len(selected_rows)} 条记录吗？",  # 提示删除数量
            QMessageBox.Yes | QMessageBox.No
        )
        if reply == QMessageBox.No:
            return

        try:
            with self.conn.cursor() as cursor:
                # 按逆序删除避免行号错乱
                selected_rows.sort(reverse=True)
                delete_ids = []  # 收集要删除的数据库ID

                # 先收集所有需要删除的ID
                for row in selected_rows:
                    item_id = self.m_tbl_Anylasis.item(row, 0)
                    if item_id and item_id.text().isdigit():
                        delete_ids.append(int(item_id.text()))

                # 批量数据库删除（提高效率）
                if delete_ids:
                    placeholders = ','.join(['%s'] * len(delete_ids))
                    cursor.execute(f"DELETE FROM 辩证 WHERE 编号 IN ({placeholders})", delete_ids)

                # 删除界面行
                for row in selected_rows:
                    self.m_tbl_Anylasis.removeRow(row)

                self.conn.commit()
                QMessageBox.information(self, "成功", f"已删除 {len(delete_ids)} 条记录")

        except Exception as e:
            self.conn.rollback()
            QMessageBox.warning(self, "错误", f"删除失败：{str(e)}")

    def on_filter_text_changed(self, text):
        filter_text = text.strip().lower()
        for row in range(self.m_tbl_Anylasis.rowCount()):
            bianzheng = self.m_tbl_Anylasis.item(row, 1).text().lower() if self.m_tbl_Anylasis.item(row, 1) else ""
            pinyin = self.m_tbl_Anylasis.item(row, 2).text().lower() if self.m_tbl_Anylasis.item(row, 2) else ""
            match = filter_text in bianzheng or filter_text in pinyin
            self.m_tbl_Anylasis.setRowHidden(row, not match)

    def update_description_edit(self):
        selected = self.m_tbl_Anylasis.selectedItems()
        if selected:
            row = selected[0].row()
            description_item = self.m_tbl_Anylasis.item(row, 3)
            self.m_edt_AnylDiscrip.blockSignals(True)
            self.m_edt_AnylDiscrip.setText(description_item.text() if description_item else "")
            self.m_edt_AnylDiscrip.blockSignals(False)
        else:
            self.m_edt_AnylDiscrip.clear()

    def update_current_row_description(self):
        selected = self.m_tbl_Anylasis.selectedItems()
        if selected:
            row = selected[0].row()
            description = self.m_edt_AnylDiscrip.toPlainText()
            item = self.m_tbl_Anylasis.item(row, 3)
            if item:
                item.setText(description)
            else:
                new_item = QtWidgets.QTableWidgetItem(description)
                self.m_tbl_Anylasis.setItem(row, 3, new_item)

    def select_row_by_id(self, target_id):
        """根据编号定位到指定行"""
        for row in range(self.m_tbl_Anylasis.rowCount()):
            item = self.m_tbl_Anylasis.item(row, 0)
            if item and item.text() == str(target_id):
                self.m_tbl_Anylasis.selectRow(row)
                self.m_tbl_Anylasis.setCurrentCell(row, 1)
                self.m_tbl_Anylasis.scrollToItem(
                    self.m_tbl_Anylasis.item(row, 1),
                    QtWidgets.QAbstractItemView.PositionAtTop
                )
                break

    def closeEvent(self, event):
        if self.conn:
            self.conn.close()
        event.accept()