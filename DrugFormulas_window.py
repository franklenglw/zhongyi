from functools import partial
from PySide6.QtCore import Qt
from PySide6 import QtWidgets
from PySide6.QtWidgets import QTableWidget, QDialog, QTableWidgetItem, QMessageBox
from PySide6.QtWidgets import QAbstractItemView
from ui_DrugFormulas import Ui_DialogDrugSelec
from DatabaseUtil import myDatabaseUtil
import pymysql
from Database_connection import load_db_config
import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning, message="sipPyTypeDict.*")


class MyDrugFormulasWindow(QDialog, Ui_DialogDrugSelec):
    m_databaseUtil = myDatabaseUtil()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.conn = None
        self.original_data = {
            '经验选方': {},
            '辨病选方': {},
            '方剂选方': {}
        }
        self.current_table_name = None  # 当前选中的处方表名
        self.current_formula_id = None  # 当前选中的处方ID
        self.original_drug_comb = None  # 当前处方的原始药物组合数据
        self.original_description = ""  # 当前处方的原始说明
        self.tab_tables = [  # 三个处方表的引用
            self.m_tle_ExpdFormulaSet,
            self.m_tle_DisFormulaSet,
            self.m_tle_ClassicFormulaSet
        ]

        # 初始化UI配置
        self.init_ui()
        # 初始化数据库
        self.init_db()
        # 加载初始数据
        self.load_initial_data()
        # 绑定事件
        self.setup_connections()

    def init_ui(self):
        """初始化界面配置"""
        self.m_tabWidget_FomulaSet.setCurrentIndex(0)
        # 设置表格属性
        self.m_tle_ExpdFormulaSet.setColumnHidden(0, True)
        self.m_tle_DisFormulaSet.setColumnHidden(0, True)
        self.m_tle_ClassicFormulaSet.setColumnHidden(0, True)
        self.m_tle_FormulaSelDruglistSet.setColumnHidden(0, True)
        self.m_tle_FormulaDrugCombSet.setColumnHidden(0, True)

        # 设置表格标题
        self.m_tle_FormulaDrugCombSet.setHorizontalHeaderLabels(['编号', '药物', '剂量'])
        self.m_tle_FormulaSelDruglistSet.setHorizontalHeaderLabels(['编号', '药名', '价格'])

        # 设置搜索框提示
        self.m_edt_FormulaSearch.setPlaceholderText("请输入拼音首字母")
        self.m_edt_FormulaSearch_2.setPlaceholderText("请输入拼音首字母")
        self.m_edt_FormulaSearch_3.setPlaceholderText("请输入拼音首字母")
        self.m_edt_FormulaSearchSet_4.setPlaceholderText("请输入拼音首字母")
        # +++ 新增：设置中药列表不可编辑（可选） +++
        self.m_tle_FormulaSelDruglistSet.setEditTriggers(QAbstractItemView.NoEditTriggers)  # 禁用直接编辑

    def init_db(self):
        """初始化数据库连接"""
        try:
            self.conn = pymysql.connect(**load_db_config())
        except Exception as e:
            QMessageBox.critical(self, "错误", f"数据库连接失败：{str(e)}")
            self.close()

    def load_initial_data(self):
        """加载初始数据到表格"""
        # 加载三个选方表
        self.m_databaseUtil.load_tableWidget_data(
            self.m_tle_ExpdFormulaSet, "", ['编号', '方名'],
            sqlstr="SELECT `编号`,`方名` FROM 经验选方 WHERE 经验选方拼音 LIKE %s"
        )
        self.original_data['经验选方'] = {}
        for row in range(self.m_tle_ExpdFormulaSet.rowCount()):
            id_item = self.m_tle_ExpdFormulaSet.item(row, 0)
            name_item = self.m_tle_ExpdFormulaSet.item(row, 1)
            if id_item and name_item:
                self.original_data['经验选方'][id_item.text()] = name_item.text()

        self.m_databaseUtil.load_tableWidget_data(
            self.m_tle_DisFormulaSet, "", ['编号', '方名'],
            sqlstr="SELECT `编号`,`方名` FROM 辨病选方 WHERE 辨病选方拼音 LIKE %s"
        )
        self.original_data['辨病选方'] = {}
        for row in range(self.m_tle_DisFormulaSet.rowCount()):
            id_item = self.m_tle_DisFormulaSet.item(row, 0)
            name_item = self.m_tle_DisFormulaSet.item(row, 1)
            if id_item and name_item:
                self.original_data['辨病选方'][id_item.text()] = name_item.text()

        self.m_databaseUtil.load_tableWidget_data(
            self.m_tle_ClassicFormulaSet, "", ['编号', '方名'],
            sqlstr="SELECT `编号`,`方名` FROM 方剂选方 WHERE 方剂选方拼音 LIKE %s"
        )
        self.original_data['方剂选方'] = {}
        for row in range(self.m_tle_ClassicFormulaSet.rowCount()):
            id_item = self.m_tle_ClassicFormulaSet.item(row, 0)
            name_item = self.m_tle_ClassicFormulaSet.item(row, 1)
            if id_item and name_item:
                self.original_data['方剂选方'][id_item.text()] = name_item.text()

        # 加载药物列表
        self.m_databaseUtil.load_tableWidget_data(
            self.m_tle_FormulaSelDruglistSet, "", ['编号', '药名', '价格'],
            sqlstr="SELECT `编号`,`药名`,`价格` FROM 中药 WHERE 中药拼音 LIKE %s"
        )

    def setup_connections(self):
        # 绑定标签页切换事件
        self.m_tabWidget_FomulaSet.currentChanged.connect(self.on_tab_changed)
        # 搜索框绑定
        self.m_edt_FormulaSearch.textChanged.connect(
            partial(self.m_databaseUtil.load_tableWidget_data,
                    self.m_tle_ExpdFormulaSet,
                    columnLabels=['编号', '方名'],
                    sqlstr="SELECT `编号`,`方名` FROM 经验选方 WHERE 经验选方拼音 LIKE %s"))

        self.m_edt_FormulaSearch_2.textChanged.connect(
            partial(self.m_databaseUtil.load_tableWidget_data,
                    self.m_tle_DisFormulaSet,
                    columnLabels=['编号', '方名'],
                    sqlstr="SELECT `编号`,`方名` FROM 辨病选方 WHERE 辨病选方拼音 LIKE %s"))

        self.m_edt_FormulaSearch_3.textChanged.connect(
            partial(self.m_databaseUtil.load_tableWidget_data,
                    self.m_tle_ClassicFormulaSet,
                    columnLabels=['编号', '方名'],
                    sqlstr="SELECT `编号`,`方名` FROM 方剂选方 WHERE 方剂选方拼音 LIKE %s"))

        self.m_edt_FormulaSearchSet_4.textChanged.connect(
            partial(self.m_databaseUtil.load_tableWidget_data,
                    self.m_tle_FormulaSelDruglistSet,
                    columnLabels=['编号', '药名', '价格'],
                    sqlstr="SELECT `编号`,`药名`,`价格` FROM 中药 WHERE 中药拼音 LIKE %s"))

        # 表格点击事件
        self.m_tle_ExpdFormulaSet.itemClicked.connect(self.on_formula_click)
        self.m_tle_DisFormulaSet.itemClicked.connect(self.on_formula_click)
        self.m_tle_ClassicFormulaSet.itemClicked.connect(self.on_formula_click)
        # +++ 新增：绑定中药列表点击事件 +++
        self.m_tle_FormulaSelDruglistSet.itemClicked.connect(self.on_row_FormulaSelDrugListSet_click)

        # 绑定currentCellChanged信号处理上下键事件
        self.m_tle_ExpdFormulaSet.currentCellChanged.connect(self.handle_expd_formula_cell_changed)
        self.m_tle_DisFormulaSet.currentCellChanged.connect(self.handle_dis_formula_cell_changed)
        self.m_tle_ClassicFormulaSet.currentCellChanged.connect(self.handle_classic_formula_cell_changed)

        # 按钮事件
        self.m_bt_add.clicked.connect(self.on_add_formula_clicked)
        self.m_bt_save.clicked.connect(self.on_save_clicked)
        self.m_bt_del.clicked.connect(self.on_delete_formula_clicked)
        self.m_bt_del_drug.clicked.connect(self.on_delete_drug_clicked)

        # +++ 新增：处理中药列表点击事件的函数 +++
    def on_row_FormulaSelDrugListSet_click(self, item):
        """处理中药列表点击事件，复制药名到药物组合表的当前行（药物列）"""
        row = item.row()
        drugnameStr = self.m_tle_FormulaSelDruglistSet.item(row, 1).text()  # 获取药名
        target_table = self.m_tle_FormulaDrugCombSet

        # 检查目标表格中是否已存在相同药名
        existing_row = -1
        for i in range(target_table.rowCount()):
            drug_item = target_table.item(i, 1)
            if drug_item and drug_item.text() == drugnameStr:
                existing_row = i
                break

        if existing_row != -1:
            # 存在重复，定位到该行剂量列
            target_table.setCurrentCell(existing_row, 2)
            target_table.setFocus()
        else:
            # 不存在重复，获取当前选中行
            current_row = target_table.currentRow()
            if current_row == -1:
                # 若未选中行，默认设置为第一行
                current_row = 0
                target_table.setCurrentCell(current_row, 1)
            # 将药名填入当前行的药物列
            target_table.setItem(current_row, 1, QtWidgets.QTableWidgetItem(drugnameStr))
            # 移动焦点到剂量列
            target_table.setCurrentCell(current_row, 2)
            target_table.setFocus()

    def on_tab_changed(self, index):
        """处理标签页切换事件"""
        table_map = {
            0: "经验选方",
            1: "辨病选方",
            2: "方剂选方"
        }
        self.current_table_name = table_map[index]

        # 获取当前处方表的选中行ID
        current_table = self.tab_tables[index]
        selected_items = current_table.selectedItems()
        if selected_items:
            row = selected_items[0].row()
            id_item = current_table.item(row, 0)
            self.current_formula_id = id_item.text() if id_item else None
        else:
            self.current_formula_id = None

    def handle_expd_formula_cell_changed(self, current_row, current_col, previous_row, previous_col):
        """经验选方表格键盘上下键切换时触发"""
        if current_row >= 0:
            item = self.m_tle_ExpdFormulaSet.item(current_row, 0)
            if item is not None:
                self.on_formula_click(item)

    def handle_dis_formula_cell_changed(self, current_row, current_col, previous_row, previous_col):
        """辨病选方表格键盘上下键切换时触发"""
        if current_row >= 0:
            item = self.m_tle_DisFormulaSet.item(current_row, 0)
            if item is not None:
                self.on_formula_click(item)

    def handle_classic_formula_cell_changed(self, current_row, current_col, previous_row, previous_col):
        """方剂选方表格键盘上下键切换时触发"""
        if current_row >= 0:
            item = self.m_tle_ClassicFormulaSet.item(current_row, 0)
            if item is not None:
                self.on_formula_click(item)

    def on_formula_click(self, item):
        """处理选方表点击事件"""
        table_map = {
            self.m_tle_ExpdFormulaSet: "经验选方",
            self.m_tle_DisFormulaSet: "辨病选方",
            self.m_tle_ClassicFormulaSet: "方剂选方"
        }

        current_table = self.sender()
        self.current_table_name = table_map[current_table]
        row = item.row()
        self.current_formula_id = current_table.item(row, 0).text()

        # 查询药物组合数据
        sql = f"""SELECT 药物1,药物2,药物3,药物4,药物5,药物6,药物7,药物8,药物9,药物10,
                药物11,药物12,药物13,药物14,药物15,药物16,药物17,药物18,药物19,药物20,
                剂量1,剂量2,剂量3,剂量4,剂量5,剂量6,剂量7,剂量8,剂量9,剂量10,
                剂量11,剂量12,剂量13,剂量14,剂量15,剂量16,剂量17,剂量18,剂量19,剂量20,说明 
                FROM {self.current_table_name} WHERE 编号 = %s"""

        data = self.m_databaseUtil.query_database_info(sql, self.current_formula_id)
        if data:
            self.display_drug_combination(data)
            # 保存原始药物组合和说明数据
            self.original_drug_comb = data
            self.original_description = data[40] if len(data) > 40 else ""
        else:
            self.original_drug_comb = None
            self.original_description = ""

    def display_drug_combination(self, data):
        """显示药物组合数据（严格对应数据库字段顺序）"""
        self.m_edt_DrugDiscripSet.clear()

        # 处理说明字段
        description = ""
        if data and len(data) > 40:
            desc_value = data[40]
            if desc_value is not None:
                # 将字段内容转换为字符串，并移除其中的空字符
                description = str(desc_value).replace('\x00', '')
        self.m_edt_DrugDiscripSet.setPlainText(description)

        # 固定设置为20行
        self.m_tle_FormulaDrugCombSet.setRowCount(20)

        # 分离药物和剂量数据（严格对应数据库字段）
        drugs = []
        doses = []
        if data:
            # 前20个是药物字段（药物1-药物20）
            drugs = [str(data[i]) if i < 20 and data[i] is not None else "" for i in range(20)]
            # 接下来20个是剂量字段（剂量1-剂量20）
            doses = [str(data[i]) if 20 <= i < 40 and data[i] is not None else "" for i in range(20, 40)]
        else:
            drugs = [""] * 20
            doses = [""] * 20

        # 按原始顺序填充表格
        for row in range(20):
            # 编号列（0-19对应药物1-20）
            self.m_tle_FormulaDrugCombSet.setItem(row, 0, QTableWidgetItem(str(row)))

            # 药物列（直接对应数据库字段顺序）
            drug = drugs[row].strip()
            drug_item = QTableWidgetItem(drug)
            self.m_tle_FormulaDrugCombSet.setItem(row, 1, drug_item)

            # 剂量列（直接对应数据库字段顺序）
            dose = doses[row].strip()
            dose_item = QTableWidgetItem(dose)
            self.m_tle_FormulaDrugCombSet.setItem(row, 2, dose_item)

        # 确保所有单元格都有Item对象
        for row in range(20):
            for col in range(3):
                if self.m_tle_FormulaDrugCombSet.item(row, col) is None:
                    self.m_tle_FormulaDrugCombSet.setItem(row, col, QTableWidgetItem(""))

        # 自动调整行高
        self.m_tle_FormulaDrugCombSet.resizeRowsToContents()

    def on_add_formula_clicked(self):
        """在当前选中的处方表中添加新行"""
        current_index = self.m_tabWidget_FomulaSet.currentIndex()
        current_table = self.tab_tables[current_index]
        row_count = current_table.rowCount()
        current_table.insertRow(row_count)
        current_table.setItem(row_count, 0, QTableWidgetItem(""))  # 编号列（数据库自动生成）
        current_table.setItem(row_count, 1, QTableWidgetItem(""))  # 方名列
        current_table.setCurrentCell(row_count, 1)  # 自动选中新行

        # 清空药物组合表和说明
        self.m_tle_FormulaDrugCombSet.clearContents()
        self.m_edt_DrugDiscripSet.clear()

        # 初始化药物组合表
        self.m_tle_FormulaDrugCombSet.setRowCount(20)
        for row in range(20):
            self.m_tle_FormulaDrugCombSet.setItem(row, 0, QTableWidgetItem(str(row)))
            self.m_tle_FormulaDrugCombSet.setItem(row, 1, QTableWidgetItem(""))
            self.m_tle_FormulaDrugCombSet.setItem(row, 2, QTableWidgetItem(""))

        # 更新当前处方ID（此时为空，保存后会生成新ID）
        self.current_formula_id = None
        # 重置原始药物组合和说明数据
        self.original_drug_comb = None
        self.original_description = ""

    def on_delete_formula_clicked(self):
        """删除当前选中的处方表的行（数据库级删除）"""
        current_index = self.m_tabWidget_FomulaSet.currentIndex()
        current_table = self.tab_tables[current_index]
        table_name_map = {
            0: "经验选方",
            1: "辨病选方",
            2: "方剂选方"
        }
        table_name = table_name_map[current_index]

        selected = current_table.selectedItems()
        if not selected:
            QMessageBox.warning(self, "警告", "请选择要删除的行")
            return

        # 获取所有选中的行号（去重）
        rows = {item.row() for item in selected}
        delete_ids = []

        # 收集要删除的数据库ID
        for row in rows:
            id_item = current_table.item(row, 0)  # 第0列是隐藏的编号列
            if id_item and id_item.text().isdigit():
                delete_ids.append(int(id_item.text()))

        # 执行数据库删除
        if delete_ids:
            try:
                with self.conn.cursor() as cursor:
                    # 使用IN语句批量删除
                    placeholders = ','.join(['%s'] * len(delete_ids))
                    sql = f"DELETE FROM {table_name} WHERE 编号 IN ({placeholders})"
                    cursor.execute(sql, delete_ids)
                    self.conn.commit()
            except Exception as e:
                self.conn.rollback()
                QMessageBox.critical(self, "错误", f"数据库删除失败：{str(e)}")
                return

        # 更新界面（反向删除避免索引错位）
        for row in sorted(rows, reverse=True):
            current_table.removeRow(row)

        # 刷新关联数据
        self.load_initial_data()
        QMessageBox.information(self, "成功", f"已删除{len(delete_ids)}条记录")

    def on_delete_drug_clicked(self):
        """清空药物组合表中的选中单元格"""
        selected = self.m_tle_FormulaDrugCombSet.selectedItems()
        if not selected:
            QMessageBox.warning(self, "警告", "请选择要清空的单元格")
            return
        for item in selected:
            item.setText("")

    def save_formula_table(self, cursor, table_widget, table_name):
        """辅助函数：保存单个处方表的数据（更新插入逻辑）"""
        existing_ids = set()
        table_pinyin_map = {
            "经验选方": "经验选方拼音",
            "辨病选方": "辨病选方拼音",
            "方剂选方": "方剂选方拼音"
        }
        pinyin_column = table_pinyin_map.get(table_name, "")
        original_table_data = self.original_data.get(table_name, {})

        for row in range(table_widget.rowCount()):
            id_item = table_widget.item(row, 0)
            name_item = table_widget.item(row, 1)

            if not name_item or not name_item.text().strip():
                continue  # 跳过空方名

            formula_id = id_item.text() if id_item else None
            formula_name = name_item.text().strip()
            pinyin = self.m_databaseUtil.get_name_initials(formula_name)

            try:
                if formula_id:
                    # 检查是否修改
                    original_name = original_table_data.get(formula_id)
                    if original_name == formula_name:
                        # 未修改，跳过
                        existing_ids.add(int(formula_id))
                        continue

                    # 执行更新
                    sql = f"UPDATE {table_name} SET 方名=%s, {pinyin_column}=%s WHERE 编号=%s"
                    cursor.execute(sql, (formula_name, pinyin, formula_id))
                    existing_ids.add(int(formula_id))
                    # 更新原始数据
                    self.original_data[table_name][formula_id] = formula_name
                else:
                    # 插入新记录
                    sql = f"INSERT INTO {table_name} (方名, {pinyin_column}) VALUES (%s, %s)"
                    cursor.execute(sql, (formula_name, pinyin))
                    new_id = cursor.lastrowid
                    table_widget.setItem(row, 0, QTableWidgetItem(str(new_id)))
                    existing_ids.add(new_id)
                    # 更新原始数据
                    self.original_data[table_name][str(new_id)] = formula_name
            except Exception as e:
                raise Exception(f"保存{table_name}失败: {str(e)}")

    def on_save_clicked(self):
        """保存所有数据到数据库"""
        if not self.conn:
            QMessageBox.warning(self, "错误", "数据库未连接")
            return

        try:
            with self.conn.cursor() as cursor:
                # 保存三个处方表
                self.save_formula_table(cursor, self.m_tle_ExpdFormulaSet, "经验选方")
                self.save_formula_table(cursor, self.m_tle_DisFormulaSet, "辨病选方")
                self.save_formula_table(cursor, self.m_tle_ClassicFormulaSet, "方剂选方")

                # 获取当前选中的标签页和对应处方表
                current_index = self.m_tabWidget_FomulaSet.currentIndex()
                current_table = self.tab_tables[current_index]
                table_name_map = {0: "经验选方", 1: "辨病选方", 2: "方剂选方"}
                current_table_name = table_name_map[current_index]

                # 获取当前选中的处方行
                selected_items = current_table.selectedItems()
                if not selected_items:
                    QMessageBox.warning(self, "警告", "请先选中要保存的处方行")
                    return

                row = selected_items[0].row()
                formula_id_item = current_table.item(row, 0)
                if not formula_id_item or not formula_id_item.text():
                    QMessageBox.warning(self, "警告", "处方编号无效，请先保存方名")
                    return

                current_formula_id = formula_id_item.text()

                # 保存药物组合数据
                drugs = []
                doses = []
                current_description = self.m_edt_DrugDiscripSet.toPlainText()

                # 检查药物组合或说明是否被修改
                drugs_modified = False
                doses_modified = False
                description_modified = current_description != self.original_description

                # 收集当前药物和剂量数据
                for row_idx in range(20):
                    drug_item = self.m_tle_FormulaDrugCombSet.item(row_idx, 1)
                    dose_item = self.m_tle_FormulaDrugCombSet.item(row_idx, 2)

                    current_drug = drug_item.text().strip() if drug_item else ""
                    current_dose = dose_item.text().strip() if dose_item else ""

                    # 获取原始数据中的药物和剂量
                    original_drug = ""
                    original_dose = ""
                    if self.original_drug_comb is not None:
                        if row_idx < 20:
                            original_drug = self.original_drug_comb[row_idx] if self.original_drug_comb[row_idx] is not None else ""
                        if (row_idx + 20) < 40:
                            original_dose = str(self.original_drug_comb[row_idx + 20]) if self.original_drug_comb[row_idx + 20] is not None else ""

                    # 比较是否修改
                    if current_drug != original_drug:
                        drugs_modified = True
                    if current_dose != original_dose:
                        doses_modified = True

                    drugs.append(current_drug)
                    # 处理剂量为整数或None
                    try:
                        processed_dose = int(current_dose) if current_dose else None
                    except ValueError:
                        processed_dose = None
                    doses.append(processed_dose)

                # 如果有任何修改，则执行更新
                if drugs_modified or doses_modified or description_modified:
                    sql = f"""UPDATE {current_table_name} SET 
                            药物1=%s,药物2=%s,药物3=%s,药物4=%s,药物5=%s,
                            药物6=%s,药物7=%s,药物8=%s,药物9=%s,药物10=%s,
                            药物11=%s,药物12=%s,药物13=%s,药物14=%s,药物15=%s,
                            药物16=%s,药物17=%s,药物18=%s,药物19=%s,药物20=%s,
                            剂量1=%s,剂量2=%s,剂量3=%s,剂量4=%s,剂量5=%s,
                            剂量6=%s,剂量7=%s,剂量8=%s,剂量9=%s,剂量10=%s,
                            剂量11=%s,剂量12=%s,剂量13=%s,剂量14=%s,剂量15=%s,
                            剂量16=%s,剂量17=%s,剂量18=%s,剂量19=%s,剂量20=%s,
                            说明=%s WHERE 编号=%s"""

                    params = drugs + doses + [current_description, current_formula_id]
                    cursor.execute(sql, params)
                    # 更新原始数据
                    sql_select = f"""SELECT 药物1,药物2,药物3,药物4,药物5,药物6,药物7,药物8,药物9,药物10,
                                    药物11,药物12,药物13,药物14,药物15,药物16,药物17,药物18,药物19,药物20,
                                    剂量1,剂量2,剂量3,剂量4,剂量5,剂量6,剂量7,剂量8,剂量9,剂量10,
                                    剂量11,剂量12,剂量13,剂量14,剂量15,剂量16,剂量17,剂量18,剂量19,剂量20,说明 
                                    FROM {current_table_name} WHERE 编号=%s"""
                    data = self.m_databaseUtil.query_database_info(sql_select, current_formula_id)
                    if data:
                        self.original_drug_comb = data
                        self.original_description = data[40] if len(data) > 40 else ""
                    else:
                        self.original_drug_comb = None
                        self.original_description = ""

                self.conn.commit()
                QMessageBox.information(self, "成功", "保存修改")
        except Exception as e:
            self.conn.rollback()
            error_msg = str(e)
            if "Incorrect integer" in error_msg:
                error_msg += "\n提示：剂量必须为整数，请检查剂量列输入"
            QMessageBox.critical(self, "错误", f"保存失败: {error_msg}")
        finally:
            self.load_initial_data()

    def closeEvent(self, event):
        """关闭时释放数据库连接"""
        if self.conn:
            self.conn.close()
        event.accept()