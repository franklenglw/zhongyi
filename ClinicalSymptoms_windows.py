import sys
from PySide6 import QtWidgets, QtCore
from PySide6.QtWidgets import QDialog, QMessageBox
from ui_ClinicalSymptoms import Ui_Dialog
import pymysql
from Database_connection import load_db_config  # 导入数据库配置模块
# 添加pypinyin导入
from pypinyin import pinyin, Style


class ClinicalSymptomsWindow(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.conn = None
        self.original_data = {}  # 使用字典存储原始数据，键为编号（整数）
        self.column_names = ['编号', '临床表现', '病证拼音']
        self.setup_connections()
        self.init_db()
        self.load_data()
        self.m_tbl_ClinicalSymps.setColumnHidden(0, True)  # 隐藏编号列

    def setup_connections(self):
        """连接按钮信号与槽函数"""
        self.m_bt_add.clicked.connect(self.on_add_clicked)
        self.m_bt_save.clicked.connect(self.on_save_clicked)
        self.m_bt_del.clicked.connect(self.on_delete_clicked)
        self.m_edt_searchfilterSymp.textChanged.connect(self.filter_table)

    def init_db(self):
        """初始化数据库连接"""
        try:
            self.conn = pymysql.connect(**load_db_config())
        except Exception as e:
            QMessageBox.critical(self, "错误", f"数据库连接失败：{str(e)}")
            sys.exit(1)

    def generate_pinyin_abbreviation(self, chinese_str):
        """生成拼音首字母缩写"""
        if not chinese_str:
            return ""
        # 获取每个汉字的拼音首字母
        pinyin_list = pinyin(chinese_str, style=Style.FIRST_LETTER)
        # 拼接成字符串，如"头痛" -> "TT"
        abbreviation = ''.join([p[0].upper() for p in pinyin_list if p])
        return abbreviation

    def load_data(self):
        """从数据库加载数据到表格（带字符串转换）"""
        try:
            with self.conn.cursor() as cursor:
                cursor.execute("SELECT 编号, 临床表现, 病证拼音 FROM 病证")
                results = cursor.fetchall()
                self.m_tbl_ClinicalSymps.setRowCount(0)
                self.original_data.clear()

                for row_data in results:
                    row = self.m_tbl_ClinicalSymps.rowCount()
                    self.m_tbl_ClinicalSymps.insertRow(row)
                    symptom_id = row_data[0]
                    # 转换为字符串并处理None值
                    str_row = [str(item) if item is not None else '' for item in row_data]
                    self.original_data[symptom_id] = str_row

                    for col, data in enumerate(row_data):
                        item = QtWidgets.QTableWidgetItem(str(data) if data is not None else "")
                        if col == 0:  # 编号列不可编辑
                            item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                        self.m_tbl_ClinicalSymps.setItem(row, col, item)
        except Exception as e:
            QMessageBox.warning(self, "错误", f"加载数据失败：{str(e)}")

    def on_add_clicked(self):
        """新增空行（逻辑保持不变）"""
        row = self.m_tbl_ClinicalSymps.rowCount()
        self.m_tbl_ClinicalSymps.insertRow(row)
        for col in range(self.m_tbl_ClinicalSymps.columnCount()):
            item = QtWidgets.QTableWidgetItem("")
            if col == 0:
                item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            self.m_tbl_ClinicalSymps.setItem(row, col, item)
        self.m_tbl_ClinicalSymps.setCurrentCell(row, 1)
        self.m_tbl_ClinicalSymps.edit(self.m_tbl_ClinicalSymps.currentIndex())

    def on_save_clicked(self):
        """重构后的保存逻辑（遵循DrugSetting的更新策略）"""
        try:
            # 第一阶段：生成拼音并更新界面
            for row in range(self.m_tbl_ClinicalSymps.rowCount()):
                symptom_id_item = self.m_tbl_ClinicalSymps.item(row, 0)
                symptom_name_item = self.m_tbl_ClinicalSymps.item(row, 1)
                pinyin_item = self.m_tbl_ClinicalSymps.item(row, 2)

                # 获取当前值
                symptom_id = symptom_id_item.text().strip() if symptom_id_item else ""
                symptom_name = symptom_name_item.text().strip() if symptom_name_item else ""
                current_pinyin = pinyin_item.text().strip() if pinyin_item else ""

                # 逻辑核心修改：智能生成拼音策略
                new_pinyin = None
                if not symptom_id:  # 新增记录
                    if symptom_name:
                        new_pinyin = self.generate_pinyin_abbreviation(symptom_name)
                else:  # 现有记录
                    original = self.original_data.get(int(symptom_id))
                    if original and symptom_name != original[1]:  # 名称发生变更
                        new_pinyin = self.generate_pinyin_abbreviation(symptom_name)

                # 更新拼音显示
                if new_pinyin is not None:
                    if not pinyin_item:
                        pinyin_item = QtWidgets.QTableWidgetItem(new_pinyin)
                        self.m_tbl_ClinicalSymps.setItem(row, 2, pinyin_item)
                    else:
                        pinyin_item.setText(new_pinyin)

            # 第二阶段：数据库操作
            with self.conn.cursor() as cursor:
                # 先进行整体验证
                for row in range(self.m_tbl_ClinicalSymps.rowCount()):
                    clinical_manifestation = self.m_tbl_ClinicalSymps.item(row, 1).text().strip()
                    if not clinical_manifestation:
                        QMessageBox.warning(self, "错误", f"第{row + 1}行临床表现不能为空")
                        return

                # 正式保存数据
                for row in range(self.m_tbl_ClinicalSymps.rowCount()):
                    # 获取当前行数据（包含可能更新的拼音）
                    row_data = [
                        self.m_tbl_ClinicalSymps.item(row, col).text().strip() if self.m_tbl_ClinicalSymps.item(row,
                                                                                                                col) else ""
                        for col in range(self.m_tbl_ClinicalSymps.columnCount())
                    ]
                    symptom_id = row_data[0]
                    clinical_manifestation = row_data[1]
                    pinyin = row_data[2]

                    # 新增记录
                    if not symptom_id:
                        cursor.execute(
                            "INSERT INTO 病证 (临床表现, 病证拼音) VALUES (%s, %s)",
                            (clinical_manifestation, pinyin)
                        )
                    # 修改记录
                    else:
                        symptom_id_int = int(symptom_id)
                        original_data = self.original_data.get(symptom_id_int, [])
                        # 检查字段是否变更（包含手动修改的拼音）
                        if original_data and (
                                clinical_manifestation != original_data[1] or
                                pinyin != original_data[2]
                        ):
                            cursor.execute(
                                "UPDATE 病证 SET 临床表现=%s, 病证拼音=%s WHERE 编号=%s",
                                (clinical_manifestation, pinyin, symptom_id)
                            )

                self.conn.commit()
                self.load_data()  # 重新加载数据以刷新界面
                QMessageBox.information(self, "成功", "保存成功")

        except pymysql.IntegrityError as e:
            self.conn.rollback()
            QMessageBox.warning(self, "错误", f"数据唯一性冲突：{str(e)}")
        except ValueError as e:
            self.conn.rollback()
            QMessageBox.warning(self, "错误", f"数据类型错误：{str(e)}")
        except Exception as e:
            self.conn.rollback()
            QMessageBox.warning(self, "错误", f"保存失败：{str(e)}")

    def on_delete_clicked(self):
        """优化后的删除逻辑（保持与DrugSetting一致）"""
        selected_rows = list({index.row() for index in self.m_tbl_ClinicalSymps.selectedIndexes()})
        if not selected_rows:
            QMessageBox.warning(self, "警告", "请选择要删除的行")
            return

        reply = QMessageBox.question(
            self, "确认删除", "确定要删除选中的记录吗？", QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.No:
            return

        try:
            with self.conn.cursor() as cursor:
                # 按倒序删除避免行号变化
                for row in sorted(selected_rows, reverse=True):
                    item_id = self.m_tbl_ClinicalSymps.item(row, 0).text()
                    if item_id:
                        cursor.execute("DELETE FROM 病证 WHERE 编号=%s", (item_id,))
                    self.m_tbl_ClinicalSymps.removeRow(row)
                self.conn.commit()
                QMessageBox.information(self, "成功", "删除成功")
        except Exception as e:
            self.conn.rollback()
            QMessageBox.warning(self, "错误", f"删除失败：{str(e)}")

    def filter_table(self, text):
        """优化过滤逻辑（保持大小写不敏感）"""
        search_text = text.strip().lower()
        for row in range(self.m_tbl_ClinicalSymps.rowCount()):
            match = False
            # 同时匹配临床表现和拼音
            for col in [1, 2]:
                item = self.m_tbl_ClinicalSymps.item(row, col)
                if item and search_text in item.text().lower():
                    match = True
                    break
            self.m_tbl_ClinicalSymps.setRowHidden(row, not match)

    def closeEvent(self, event):
        """关闭时确保释放连接"""
        if self.conn:
            self.conn.close()
        event.accept()
