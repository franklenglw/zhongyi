import sys
from PySide6 import QtWidgets, QtCore, QtGui
from PySide6.QtWidgets import QDialog, QMessageBox, QTableWidgetItem
from ui_MedicalRecord import Ui_Dialog
import pymysql
from Database_connection import load_db_config

class MedicalRecordWindow(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.conn = None
        self.original_data = {}
        self.last_selected_id = None
        self.setup_connections()
        self.init_db()
        self.load_data()
        self.m_tbl_Record.setColumnHidden(0, True)  # 隐藏编号列
        self.m_tbl_Record.setColumnHidden(2, True)  # 隐藏内容列
        self.m_tbl_Record.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.m_tbl_Record.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)

    def setup_connections(self):
        self.m_bt_add.clicked.connect(self.on_add_clicked)
        self.m_bt_save.clicked.connect(self.on_save_clicked)
        self.m_bt_del.clicked.connect(self.on_delete_clicked)
        self.m_edt_searchfilterRec.textChanged.connect(self.on_filter_text_changed)
        self.m_tbl_Record.itemSelectionChanged.connect(self.update_content_edit)
        self.m_edt_MedicalRec.textChanged.connect(self.update_current_row_content)

        # 连接文本变化信号到高亮关键字函数
        self.m_edt_searchfilterRec.textChanged.connect(self.highlight_keyword)

    def highlight_keyword(self):
        """
        高亮显示 m_edt_searchfilterRec 中的关键字
        """
        # 获取 m_edt_searchfilterRec 中的关键字
        keyword = self.m_edt_searchfilterRec.text().strip()

        # 获取 m_edt_MedicalRec 的文本
        text = self.m_edt_MedicalRec.toPlainText()

        # 清除之前的高亮
        cursor = self.m_edt_MedicalRec.textCursor()
        cursor.select(QtGui.QTextCursor.Document)
        cursor.setCharFormat(QtGui.QTextCharFormat())

        if keyword:
            # 设置高亮格式
            format = QtGui.QTextCharFormat()
            format.setBackground(QtGui.QBrush(QtGui.QColor("yellow")))

            # 查找并高亮所有匹配的关键字
            index = 0
            while index < len(text):
                index = text.find(keyword, index)
                if index == -1:
                    break

                # 设置高亮
                cursor.setPosition(index)
                cursor.movePosition(QtGui.QTextCursor.Right, QtGui.QTextCursor.KeepAnchor, len(keyword))
                cursor.mergeCharFormat(format)

                index += len(keyword)

    def init_db(self):
        try:
            self.conn = pymysql.connect(**load_db_config())
        except Exception as e:
            QMessageBox.critical(self, "错误", f"数据库连接失败：{str(e)}")
            sys.exit(1)

    def load_data(self):
        try:
            with self.conn.cursor() as cursor:
                cursor.execute("SELECT 编号, 标题, 内容, 处置方法 FROM 医案")
                results = cursor.fetchall()
                self.m_tbl_Record.setRowCount(0)
                self.original_data.clear()

                for row_data in results:
                    row = self.m_tbl_Record.rowCount()
                    self.m_tbl_Record.insertRow(row)
                    self.original_data[row_data[0]] = list(row_data)

                    for col, data in enumerate(row_data):
                        # 处理 NULL 值，将其转换为空字符串
                        display_text = "" if data is None else str(data)
                        item = QtWidgets.QTableWidgetItem(display_text)
                        if col == 0:
                            item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                        self.m_tbl_Record.setItem(row, col, item)

                # 数据加载完成后定位到上次选中的行
                if self.last_selected_id is not None:
                    self.select_row_by_id(self.last_selected_id)

        except Exception as e:
            QMessageBox.warning(self, "错误", f"加载数据失败：{str(e)}")

    def on_add_clicked(self):
        row = self.m_tbl_Record.rowCount()
        self.m_tbl_Record.insertRow(row)
        for col in range(self.m_tbl_Record.columnCount()):
            item = QtWidgets.QTableWidgetItem("")
            if col == 0:
                item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            self.m_tbl_Record.setItem(row, col, item)
        self.m_tbl_Record.setCurrentCell(row, 1)
        self.m_tbl_Record.edit(self.m_tbl_Record.currentIndex())
        self.update_current_row_content()

    def on_save_clicked(self):
        # 确保内容更新到表格中
        self.update_current_row_content()
        try:
            with self.conn.cursor() as cursor:
                # 先进行整体验证
                for row in range(self.m_tbl_Record.rowCount()):
                    title = self.m_tbl_Record.item(row, 1).text().strip()
                    if not title:
                        QMessageBox.warning(self, "错误", f"第{row + 1}行标题不能为空")
                        return

                # 正式保存数据
                for row in range(self.m_tbl_Record.rowCount()):
                    # 获取当前行数据
                    row_data = [
                        self.m_tbl_Record.item(row, col).text().strip() if self.m_tbl_Record.item(row, col) else ""
                        for col in range(self.m_tbl_Record.columnCount())
                    ]
                    record_id = row_data[0]
                    title = row_data[1]
                    content = row_data[2]
                    treatment_method = row_data[3]  # 获取“处置方法”字段的值

                    # 新增记录
                    if not record_id:
                        if title:  # 确保标题不为空
                            cursor.execute(
                                "INSERT INTO 医案 (标题, 内容, 处置方法) VALUES (%s, %s, %s)",
                                (title, content, treatment_method)  # 添加“处置方法”字段
                            )
                            new_id = cursor.lastrowid
                            self.last_selected_id = new_id
                            # 更新表格中的编号
                            self.m_tbl_Record.item(row, 0).setText(str(new_id))

                    # 更新记录
                    else:
                        record_id_int = int(record_id)
                        original = self.original_data.get(record_id_int)
                        if original and (
                                title != original[1] or
                                content != original[2] or
                                treatment_method != original[3]  # 检查“处置方法”是否变化
                        ):
                            cursor.execute(
                                "UPDATE 医案 SET 标题=%s, 内容=%s, 处置方法=%s WHERE 编号=%s",
                                (title, content, treatment_method, record_id)  # 添加“处置方法”字段
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
            print(f"保存失败：{str(e)}")  # 打印错误信息
            QMessageBox.warning(self, "错误", f"保存失败：{str(e)}")

    def on_delete_clicked(self):
        # 获取所有选中的行号（去重）
        selected_rows = list({index.row() for index in self.m_tbl_Record.selectedIndexes()})
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
                    item_id = self.m_tbl_Record.item(row, 0)
                    if item_id and item_id.text().isdigit():
                        delete_ids.append(int(item_id.text()))

                # 批量数据库删除（提高效率）
                if delete_ids:
                    placeholders = ','.join(['%s'] * len(delete_ids))
                    cursor.execute(f"DELETE FROM 医案 WHERE 编号 IN ({placeholders})", delete_ids)

                # 删除界面行
                for row in selected_rows:
                    self.m_tbl_Record.removeRow(row)

                self.conn.commit()
                QMessageBox.information(self, "成功", f"已删除 {len(delete_ids)} 条记录")

        except Exception as e:
            self.conn.rollback()
            QMessageBox.warning(self, "错误", f"删除失败：{str(e)}")

    def on_filter_text_changed(self, text):
        filter_text = text.strip().lower()  # 获取搜索关键字并转换为小写
        for row in range(self.m_tbl_Record.rowCount()):
            # 获取标题和内容
            title_item = self.m_tbl_Record.item(row, 1)
            content_item = self.m_tbl_Record.item(row, 2)

            # 获取标题和内容的文本（如果存在）
            title = title_item.text().lower() if title_item else ""
            content = content_item.text().lower() if content_item else ""

            # 检查关键字是否匹配标题或内容
            match = filter_text in title or filter_text in content
            self.m_tbl_Record.setRowHidden(row, not match)  # 隐藏不匹配的行

    def update_content_edit(self):
        """
        当表格中的行选择发生变化时，更新 m_edt_MedicalRec 的内容
        """
        selected = self.m_tbl_Record.selectedItems()
        if selected:
            row = selected[0].row()
            content_item = self.m_tbl_Record.item(row, 2)
            self.m_edt_MedicalRec.blockSignals(True)  # 阻止信号，避免触发 textChanged
            try:
                self.m_edt_MedicalRec.setText(content_item.text() if content_item else "")
            finally:
                self.m_edt_MedicalRec.blockSignals(False)  # 恢复信号
            # 更新内容后，触发高亮关键字
            self.highlight_keyword()

    def update_current_row_content(self):
        selected = self.m_tbl_Record.selectedItems()
        if selected:
            row = selected[0].row()
            content = self.m_edt_MedicalRec.toPlainText()
            item = self.m_tbl_Record.item(row, 2)
            if item:
                item.setText(content if content else "")  # 确保空内容也能正确保存
            else:
                new_item = QtWidgets.QTableWidgetItem(content if content else "")
                self.m_tbl_Record.setItem(row, 2, new_item)

    def select_row_by_id(self, target_id):
        """根据编号定位到指定行"""
        for row in range(self.m_tbl_Record.rowCount()):
            item = self.m_tbl_Record.item(row, 0)
            if item and item.text() == str(target_id):
                self.m_tbl_Record.selectRow(row)
                self.m_tbl_Record.setCurrentCell(row, 1)
                self.m_tbl_Record.scrollToItem(
                    self.m_tbl_Record.item(row, 1),
                    QtWidgets.QAbstractItemView.PositionAtTop
                )
                break

    def closeEvent(self, event):
        if self.conn:
            self.conn.close()
        event.accept()