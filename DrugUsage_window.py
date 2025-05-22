import sys
from PySide6 import QtWidgets, QtCore
from PySide6.QtWidgets import QDialog, QMessageBox
from ui_DrugUsage import Ui_Dialog
import pymysql
from Database_connection import load_db_config  # 导入数据库配置模块


class DrugUsageWindow(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.conn = None
        self.original_data = {}  # 使用字典保存原始数据，键为编号（整数）
        self.column_names = ['编号', '用法', '煎法']  # 根据实际数据库字段调整
        self.setup_connections()
        self.init_db()
        self.load_data()
        self.m_tbl_DrugUsage.setColumnHidden(0, True)  # 隐藏编号列

    def setup_connections(self):
        """连接按钮信号与槽函数"""
        self.m_bt_add.clicked.connect(self.on_add_clicked)
        self.m_bt_save.clicked.connect(self.on_save_clicked)
        self.m_bt_del.clicked.connect(self.on_delete_clicked)

    def init_db(self):
        """初始化数据库连接"""
        try:
            self.conn = pymysql.connect(**load_db_config())
        except Exception as e:
            QMessageBox.critical(self, "错误", f"数据库连接失败：{str(e)}")
            sys.exit(1)

    def load_data(self):
        """从数据库加载数据到表格"""
        try:
            with self.conn.cursor() as cursor:
                cursor.execute("SELECT 编号, 用法, 煎法 FROM 用法")  # 根据实际表名调整
                results = cursor.fetchall()
                self.m_tbl_DrugUsage.setRowCount(0)
                self.original_data.clear()

                for row_data in results:
                    row = self.m_tbl_DrugUsage.rowCount()
                    self.m_tbl_DrugUsage.insertRow(row)
                    drug_id = row_data[0]
                    # 保存原始数据（转换为字符串类型以便比较）
                    self.original_data[drug_id] = [str(item) if item is not None else '' for item in row_data]

                    for col, data in enumerate(row_data):
                        item = QtWidgets.QTableWidgetItem(str(data) if data is not None else "")
                        if col == 0:  # 编号列不可编辑
                            item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                        else:
                            # 启用自动换行
                            item.setFlags(item.flags() | QtCore.Qt.TextWordWrap)
                        self.m_tbl_DrugUsage.setItem(row, col, item)

                # 自动调整行高以匹配内容
                self.m_tbl_DrugUsage.resizeRowsToContents()

        except Exception as e:
            QMessageBox.warning(self, "错误", f"加载数据失败：{str(e)}")

    def on_add_clicked(self):
        """新增空行"""
        row = self.m_tbl_DrugUsage.rowCount()
        self.m_tbl_DrugUsage.insertRow(row)
        # 初始化新行的项目
        for col in range(self.m_tbl_DrugUsage.columnCount()):
            item = QtWidgets.QTableWidgetItem("")
            if col == 0:
                item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            else:
                # 启用自动换行
                item.setFlags(item.flags() | QtCore.Qt.TextWordWrap)
            self.m_tbl_DrugUsage.setItem(row, col, item)

        # 自动调整行高以匹配内容
        self.m_tbl_DrugUsage.resizeRowsToContents()

        # 自动聚焦到新行
        self.m_tbl_DrugUsage.setCurrentCell(row, 1)
        self.m_tbl_DrugUsage.edit(self.m_tbl_DrugUsage.currentIndex())

    def on_save_clicked(self):
        """保存所有修改到数据库"""
        try:
            with self.conn.cursor() as cursor:
                # 逐行校验并保存数据
                for row in range(self.m_tbl_DrugUsage.rowCount()):
                    row_data = []
                    for col in range(self.m_tbl_DrugUsage.columnCount()):
                        item = self.m_tbl_DrugUsage.item(row, col)
                        row_data.append(item.text().strip() if item else "")

                    # 获取数据项
                    usage_id = row_data[0]
                    usage_text = row_data[1]
                    decoction_text = row_data[2]  # 新增：获取煎法数据

                    # 特殊处理第一行
                    is_first_row = (row == 0)

                    # 新增记录逻辑
                    if not usage_id:
                        if not is_first_row and not usage_text:  # 非首行空值跳过
                            continue

                        # 执行插入（允许首行为空）
                        cursor.execute(
                            "INSERT INTO 用法 (用法, 煎法) VALUES (%s, %s)",
                            (usage_text if usage_text else None, decoction_text if decoction_text else None)
                        )

                    # 修改记录逻辑
                    else:
                        try:
                            usage_id_int = int(usage_id)
                        except ValueError:
                            QMessageBox.warning(self, "错误", f"第{row + 1}行编号无效")
                            self.conn.rollback()
                            return

                        # 不再检查usage_text是否为空，直接更新
                        new_values = [usage_id, usage_text, decoction_text]  # 包含煎法，允许为空
                        original_values = self.original_data.get(usage_id_int, None)

                        if original_values is not None:
                            # 如果原始数据存在，则检查是否需要更新
                            if new_values != original_values:
                                cursor.execute(
                                    "UPDATE 用法 SET 用法=%s, 煎法=%s WHERE 编号=%s",
                                    (usage_text, decoction_text, usage_id)
                                )
                        else:
                            QMessageBox.warning(self, "错误", f"第{row + 1}行记录不存在")
                            self.conn.rollback()
                            return

                # 提交事务并刷新数据
                self.conn.commit()
                self.load_data()
                QMessageBox.information(self, "成功", "保存成功")

        except pymysql.IntegrityError as e:
            self.conn.rollback()
            QMessageBox.warning(self, "错误", f"数据库约束错误: {str(e)}")
        except Exception as e:
            self.conn.rollback()
            QMessageBox.warning(self, "错误", f"保存失败：{str(e)}")

    def on_delete_clicked(self):
        """删除选中行"""
        selected_rows = list({index.row() for index in self.m_tbl_DrugUsage.selectedIndexes()})
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
                    item_id = self.m_tbl_DrugUsage.item(row, 0).text()
                    if item_id:
                        cursor.execute("DELETE FROM 用法 WHERE 编号=%s", (item_id,))
                    self.m_tbl_DrugUsage.removeRow(row)
                self.conn.commit()
                QMessageBox.information(self, "成功", "删除成功")
        except Exception as e:
            self.conn.rollback()
            QMessageBox.warning(self, "错误", f"删除失败：{str(e)}")

    def closeEvent(self, event):
        """关闭时释放数据库连接"""
        if self.conn:
            self.conn.close()
        event.accept()