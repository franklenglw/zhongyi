from functools import partial
from PySide6.QtCore import Qt
from PySide6 import QtWidgets
from PySide6.QtWidgets import QTableWidget, QDialog, QTableWidgetItem
from PySide6.QtWidgets import QAbstractItemView
from ui_DrugSelec_window import Ui_DialogDrugSelec  # 导入生成的对话框界面类
from DatabaseUtil import myDatabaseUtil
import warnings

# 过滤特定 SIP 警告

warnings.filterwarnings("ignore", category=DeprecationWarning, message="sipPyTypeDict.*")

class MyDrugSelectWindow(QDialog, Ui_DialogDrugSelec):


    def __init__(self, parent=None):
        super().__init__(parent)
        self.m_parentWindow = parent
        self.m_databaseUtil = myDatabaseUtil()  # 改为实例变量

        self.setWindowFlags(self.windowFlags()
                            & ~Qt.WindowContextHelpButtonHint
                            | Qt.WindowMinimizeButtonHint
                            | Qt.WindowMaximizeButtonHint)

        self.setupUi(self)  # 加载界面
        self.m_tabWidget_Fomula.setCurrentIndex(0)


        self.m_tle_FormulaDrugComb_2.setColumnCount(3)
        self.m_tle_FormulaDrugComb_2.setHorizontalHeaderLabels(['编号','药物', '剂量'])
        self.m_tle_FormulaDrugComb_2.setColumnHidden(0,True)

        self.m_tle_FormulaDrugComb.setColumnCount(3)
        self.m_tle_FormulaDrugComb.setHorizontalHeaderLabels(['编号','药物', '剂量'])
        self.m_tle_FormulaDrugComb.setColumnHidden(0,True)

        self.m_edt_FormulaSearch.textChanged.connect(
            partial(self.m_databaseUtil.load_tableWidget_data, self.m_tle_ExpdFormula, columnLabels=['编号', '方名'],
                    sqlstr="SELECT `编号`,`方名` FROM 经验选方 WHERE 经验选方拼音 LIKE %s"))
        self.m_edt_FormulaSearch_2.textChanged.connect(
            partial(self.m_databaseUtil.load_tableWidget_data, self.m_tle_DisFormula, columnLabels=['编号', '方名'],
                    sqlstr="SELECT `编号`,`方名` FROM 辨病选方 WHERE 辨病选方拼音 LIKE %s"))

        self.m_edt_FormulaSearch_3.textChanged.connect(
            partial(self.m_databaseUtil.load_tableWidget_data, self.m_tle_ClassicFormula, columnLabels=['编号', '方名'],
                    sqlstr="SELECT `编号`,`方名` FROM 方剂选方 WHERE 方剂选方拼音 LIKE %s"))

        self.m_edt_FormulaSearch_4.textChanged.connect(
            partial(self.m_databaseUtil.load_tableWidget_data, self.m_tle_FormulaSelDruglist, columnLabels=['编号', '药名', '价格'],
                    sqlstr="SELECT `编号`,`药名`,`价格` FROM 中药 WHERE 中药拼音 LIKE %s"))


        self.m_databaseUtil.load_tableWidget_data(self.m_tle_ExpdFormula,"",['编号','方名'],sqlstr="SELECT `编号`,`方名` FROM 经验选方 WHERE 经验选方拼音 LIKE %s")
        self.m_databaseUtil.load_tableWidget_data(self.m_tle_DisFormula, "", ['编号', '方名'],sqlstr="SELECT `编号`,`方名` FROM 辨病选方 WHERE 辨病选方拼音 LIKE %s")
        self.m_databaseUtil.load_tableWidget_data(self.m_tle_ClassicFormula, "", ['编号', '方名'],sqlstr="SELECT `编号`,`方名` FROM 方剂选方 WHERE 方剂选方拼音 LIKE %s")
        self.m_databaseUtil.load_tableWidget_data(self.m_tle_FormulaSelDruglist, "", ['编号', '药名', '价格'],
                                                  sqlstr="SELECT `编号`,`药名`,`价格` FROM 中药 WHERE 中药拼音 LIKE %s")
        self.m_tle_ExpdFormula.setEditTriggers(QAbstractItemView.NoEditTriggers)  # 禁用直接编辑
        self.m_tle_DisFormula.setEditTriggers(QAbstractItemView.NoEditTriggers)  # 禁用直接编辑
        self.m_tle_ClassicFormula.setEditTriggers(QAbstractItemView.NoEditTriggers)  # 禁用直接编辑
        self.m_tle_FormulaSelDruglist.setEditTriggers(QAbstractItemView.NoEditTriggers)  # 禁用直接编辑
        self.m_tle_FormulaDrugComb.setEditTriggers(QAbstractItemView.NoEditTriggers)  # 禁用直接编辑


        self.m_tle_ExpdFormula.itemClicked.connect(self.on_row_ExpdFormula_click)
        self.m_tle_ExpdFormula.currentCellChanged.connect(self.handle_ExpdFormula_cell_changed)

        self.m_tle_DisFormula.itemClicked.connect(self.on_row_DisFormula_click)
        self.m_tle_DisFormula.currentCellChanged.connect(self.handle_DisFormula_cell_changed)

        self.m_tle_ClassicFormula.itemClicked.connect(self.on_row_ClassicFormula_click)
        self.m_tle_ClassicFormula.currentCellChanged.connect(self.handle_ClassicFormula_cell_changed)

        self.m_tle_FormulaSelDruglist.itemClicked.connect(self.on_row_FormulaSelDrugList_click)


        self.m_bt_AddtoBt.clicked.connect(self.handle_AddtoBt_click)
        self.m_bt_AddtoBt_2.clicked.connect(self.handle_AddtoBt2_click)
        self.m_bt_AddtoBt_3.clicked.connect(self.handle_AddtoBt3_click)
        if self.m_tle_ExpdFormula.rowCount() > 0 and self.m_tle_ExpdFormula.columnCount() > 0:
            self.m_tle_ExpdFormula.setCurrentCell(0, 1)
            self.m_tle_ExpdFormula.setFocus()
            item = self.m_tle_ExpdFormula.item(0,1)
            self.on_row_ExpdFormula_click(item)


    def handle_AddtoBt2_click(self):
        self.copy_extend_formuladrug_content(self.m_tle_FormulaDrugComb)
        self.close()

    def copy_extend_formuladrug_content(self,tabelwidget:QTableWidget):

        dest_table: QTableWidget = self.m_parentWindow.m_tbl_DrugUsage
        src_table = tabelwidget

        dest_table.clearContents()
        # 1. 复制表格结构
        rows = src_table.rowCount()
        cols = src_table.columnCount()
        dest_table.setRowCount(rows)
        dest_table.setColumnCount(cols+1)

        ##
        # 2. 复制表头
        # 水平表头
        for col in range(cols+1):
            if col == cols:#拓展一列
                dest_table.setHorizontalHeaderItem(col, QTableWidgetItem(str("煎法")))
            else:
                header = src_table.horizontalHeaderItem(col)
                if header:
                    dest_table.setHorizontalHeaderItem(col, QTableWidgetItem(header.text()))
            # 复制列宽
            #dest_table.setColumnWidth(col, src_table.columnWidth(col)+1)
        ##
       # 3. 复制单元格数据
        for row in range(rows):
            for col in range(cols+1):
                if col == cols:
                    dest_table.setItem(row, col, QTableWidgetItem())
                else:
                    src_item = src_table.item(row, col)
                    if src_item:
                            # 深度复制单元格内容
                        dest_item = QTableWidgetItem(src_item.text())
                        dest_table.setItem(row, col, dest_item)
                    else:
                        dest_table.setItem(row, col, QTableWidgetItem())

    def is_good_data(a, b):
        """判断A列和B列的数据是否是好数据

        参数:
        a (any): A列的值
        b (any): B列的值

        返回:
        bool: 如果是好数据返回True，否则返回False
        """
        a_empty = a is None or a == ''  # 判断A列是否为空
        b_empty = b is None or b == ''  # 判断B列是否为空
        return not (a_empty ^ b_empty)  # 两列同时为空或同时非空时返回True

    def handle_AddtoBt3_click(self):
        nSum = 0
        row_count = self.m_tle_FormulaDrugComb_2.rowCount()

        # 逆序遍历所有行
        for i in range(row_count - 1, -1, -1):
            # 防御性获取文本
            def safe_text(item):
                return item.text().strip() if item and hasattr(item, 'text') else ""

            item_drug = self.m_tle_FormulaDrugComb_2.item(i, 1)
            strItemDrug = safe_text(item_drug)

            item_quantity = self.m_tle_FormulaDrugComb_2.item(i, 2)
            strItemQuantity = safe_text(item_quantity)

            # 判断逻辑
            if strItemDrug != "" and strItemQuantity == "":
                # 确保操作的行未被删除
                if i < self.m_tle_FormulaDrugComb_2.rowCount():
                    self.m_tle_FormulaDrugComb_2.setCurrentCell(i, 2)
                    self.m_tle_FormulaDrugComb_2.setFocus()
                    nSum += 0.001
            elif strItemQuantity != "" and strItemDrug == "":
                if i < self.m_tle_FormulaDrugComb_2.rowCount():
                    self.m_tle_FormulaDrugComb_2.setCurrentCell(i, 1)
                    self.m_tle_FormulaDrugComb_2.setFocus()
                    nSum += 0.001
            elif strItemDrug == "" and strItemQuantity == "":
                self.m_tle_FormulaDrugComb_2.removeRow(i)  # 删除空行
            else:
                nSum += 0

        # 处理结果
        if nSum % 2 == 0:
            tleParent = self.m_parentWindow.m_tbl_DrugUsage
            self.copy_extend_formuladrug_content(self.m_tle_FormulaDrugComb_2)
            self.close()

    def handle_AddtoBt_click(self):
        self.m_databaseUtil.copy_tablewidget_content(self.m_tle_FormulaDrugComb_2,self.m_tle_FormulaDrugComb)
        nRowCount = self.m_tle_FormulaDrugComb_2.rowCount()
        if nRowCount <= 20:
            self.m_tle_FormulaDrugComb_2.setRowCount(20)
            for i in range(20-nRowCount):
                self.m_tle_FormulaDrugComb_2.setItem(i+nRowCount, 0, QtWidgets.QTableWidgetItem(i+nRowCount))
                self.m_tle_FormulaDrugComb_2.setItem(i+nRowCount, 1, QtWidgets.QTableWidgetItem(""))
                self.m_tle_FormulaDrugComb_2.setItem(i+nRowCount, 2, QtWidgets.QTableWidgetItem(""))


    def on_row_FormulaSelDrugList_click(self,item):
        """处理表格双击事件"""
        row = item.row()
        drugnameStr = self.m_tle_FormulaSelDruglist.item(row, 1).text()
        nIndex:int = 0
        bFindStr:bool = False
        for i in range(20):

            item = self.m_tle_FormulaDrugComb_2.item(i,1)
            if item is None:
                continue
            else:
                strItemDrug = item.text()
            if strItemDrug != drugnameStr:
                bFindStr = False
                continue
            else:
                nIndex = i
                bFindStr = True
                self.m_tle_FormulaDrugComb_2.setCurrentCell(nIndex,2)
                break
        if bFindStr == False:
            self.m_tle_FormulaDrugComb_2.setItem(self.m_tle_FormulaDrugComb_2.currentRow(),1,QtWidgets.QTableWidgetItem(drugnameStr))

    #经验选方控件双击时触发
    def on_row_ExpdFormula_click(self, item):
        """处理表格双击事件"""
        row = item.row()
        id = self.m_tle_ExpdFormula.item(row, 0).text()

        data = self.m_databaseUtil.query_database_info(
            """SELECT 药物1,药物2,药物3,药物4,药物5,药物6,药物7,药物8,药物9,药物10,药物11,药物12,药物13,药物14,药物15,药物16,药物17,药物18,药物19,药物20,
            剂量1,剂量2,剂量3,剂量4,剂量5,剂量6,剂量7,剂量8,剂量9,剂量10,剂量11,剂量12,剂量13,剂量14,剂量15,剂量16,剂量17,剂量18,剂量19,剂量20,说明 FROM 经验选方 WHERE 编号 = %s""",
            id)
        if data:
            self.display_drug_info(data)

    #经验选方控件上下键触发
    def handle_ExpdFormula_cell_changed(self, current_row, current_col, previous_row, previous_col):
        """当用户使用键盘上下键或鼠标改变当前行时，触发患者信息更新"""
        if current_row >= 0:
            # 获取当前行第一列的item（编号列）
            item = self.m_tle_ExpdFormula.item(current_row, 0)
            if item is not None:
                self.on_row_ExpdFormula_click(item)  # 调用原有的点击处理函数

    # 辩证选方控件双击时触发
    def on_row_DisFormula_click(self, item):
        """处理表格双击事件"""
        row = item.row()
        id = self.m_tle_DisFormula.item(row, 0).text()

        data = self.m_databaseUtil.query_database_info(
            """SELECT 药物1,药物2,药物3,药物4,药物5,药物6,药物7,药物8,药物9,药物10,药物11,药物12,药物13,药物14,药物15,药物16,药物17,药物18,药物19,药物20,
            剂量1,剂量2,剂量3,剂量4,剂量5,剂量6,剂量7,剂量8,剂量9,剂量10,剂量11,剂量12,剂量13,剂量14,剂量15,剂量16,剂量17,剂量18,剂量19,剂量20,说明 FROM 辨病选方 WHERE 编号 = %s""",
            id)
        if data:
            self.display_drug_info(data)

    #辩证选方控件上下键触发
    def handle_DisFormula_cell_changed(self, current_row, current_col, previous_row, previous_col):
        """当用户使用键盘上下键或鼠标改变当前行时，触发患者信息更新"""
        if current_row >= 0:
            # 获取当前行第一列的item（编号列）
            item = self.m_tle_DisFormula.item(current_row, 0)
            if item is not None:
                self.on_row_DisFormula_click(item)  # 调用原有的点击处理函数

    # 方剂选方控件双击时触发
    def on_row_ClassicFormula_click(self, item):
        """处理表格双击事件"""
        row = item.row()
        id = self.m_tle_ClassicFormula.item(row, 0).text()

        data = self.m_databaseUtil.query_database_info(
            """SELECT 药物1,药物2,药物3,药物4,药物5,药物6,药物7,药物8,药物9,药物10,药物11,药物12,药物13,药物14,药物15,药物16,药物17,药物18,药物19,药物20,
            剂量1,剂量2,剂量3,剂量4,剂量5,剂量6,剂量7,剂量8,剂量9,剂量10,剂量11,剂量12,剂量13,剂量14,剂量15,剂量16,剂量17,剂量18,剂量19,剂量20,说明 FROM 方剂选方 WHERE 编号 = %s""",
            id)
        if data:
            self.display_drug_info(data)

    #方剂选方控件上下键触发
    def handle_ClassicFormula_cell_changed(self, current_row, current_col, previous_row, previous_col):
        """当用户使用键盘上下键或鼠标改变当前行时，触发患者信息更新"""
        if current_row >= 0:
            # 获取当前行第一列的item（编号列）
            item = self.m_tle_ClassicFormula.item(current_row, 0)
            if item is not None:
                self.on_row_ClassicFormula_click(item)  # 调用原有的点击处理函数

    def display_drug_info(self,  data):
        """显示药物详细信息"""
        # 配置表格
        if not data:
            return


        if(len(data[len(data)-1])>0):
            self.m_edt_DrugDiscrip.clear()
            self.m_edt_DrugDiscrip.append(str(data[len(data)-1]))
        nDataLen:int = 0
        for i in range(20):
            if len(str(data[i])) >0 and data[i] != None:
                nDataLen += 1

        self.m_tle_FormulaDrugComb.setRowCount(nDataLen)
        # 填充数据
        nIndex:int = 0
        for i in range(20):
            drug:str = str(data[i])  # 药物1~20（索引0到19）
            dose:str = str(data[20 + i])  # 用量1~20（索引20到39）
            if(len(drug)<= 0 or data[i] is None):
                continue

            self.m_tle_FormulaDrugComb.setItem(nIndex, 0, QtWidgets.QTableWidgetItem(nIndex))
            self.m_tle_FormulaDrugComb.setItem(nIndex, 1, QtWidgets.QTableWidgetItem(drug))
            self.m_tle_FormulaDrugComb.setItem(nIndex, 2, QtWidgets.QTableWidgetItem(dose))
            nIndex += 1

        # 优化显示
        #self.m_tle_FormulaDrugComb.resizeColumnsToContents()
        #self.m_tle_FormulaDrugComb.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)


    def closeEvent(self, event):
        """重写关闭事件处理数据库连接释放"""
        if hasattr(self.m_databaseUtil, 'close_connection'):
            self.m_databaseUtil.close_connection()
        super().closeEvent(event)