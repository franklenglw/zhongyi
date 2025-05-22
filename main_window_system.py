import os
import re
import pymysql
import shutil
import weakref
from PySide6 import QtWidgets
from PySide6.QtWidgets import QHeaderView, QCalendarWidget, QDialog, QApplication, QTableWidget, \
    QTableWidgetItem, QVBoxLayout, QAbstractItemView, QMessageBox, QMainWindow, QFileDialog
from PySide6.QtCore import QDate, QEvent, QPoint, QDateTime, Qt, QTimer
from PySide6.QtGui import QColor, QDoubleValidator, QScreen, QPixmap
from pymysql import Error

from ui_main_window import Ui_MainWindow  # 导入生成的界面类
import warnings
from functools import partial
from datetime import datetime
from DatabaseUtil import myDatabaseUtil
from PdfViewerDialog import PdfViewerDialog
from SearchableComboBox import mySearchableComboBox
from DrugSelect_mainwindow import MyDrugSelectWindow
from decimal import Decimal, InvalidOperation
import random
from ReportGenerator import myReporter
from pymysql.cursors import DictCursor
from ui_UserInfor import Ui_Dialog as UserInfo_Ui
from ui_DrugSetting import Ui_Dialog as DrugSetting_Ui
from User_infor_window import UserInfoWindow
from DrugSetting_window import DrugSettingWindow
from PySide6.QtGui import QAction
from DrugUsage_window import DrugUsageWindow
from DrugFormulas_window import MyDrugFormulasWindow
from ClinicalSymptoms_windows import ClinicalSymptomsWindow
from ClinicalAnylasis_windows import ClinicalAnylasisWindow
from ClinicalDiag_windows import ClinicalDiagWindow
from AcupSetting_window import AcupSettingWindow
from PatientList_window import PatientListWindow
from MedicalRecord_window import MedicalRecordWindow
from About import AboutDialog
warnings.filterwarnings("ignore", category=DeprecationWarning, message="sipPyTypeDict.*")

from Database_connection import load_db_config  # 导入数据库配置加载函数


# 用户信息对话框类
class UserInfoDialog(QDialog, UserInfo_Ui):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("用户信息设置")  # 设置对话框标题


# 中药设置对话框类
class DrugSettingDialog(QDialog, DrugSetting_Ui):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("中药设置管理")  # 设置对话框标题


class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, user_id):
        super().__init__()
        self.setupUi(self)  # 加载界面
        self.m_databaseUtil = myDatabaseUtil()
        self.current_image_path = None  # 初始化为None
        self.current_user_id = user_id

        #------------设置初始化窗口中groupbox默认占比 start----------------
        # 安装事件过滤器以监听groupBox_3的显示/隐藏事件
        self.groupBox_3.installEventFilter(self)
        # 初始调整splitter的尺寸
        self.adjust_splitter_sizes()
        # ------------设置初始化窗口中groupbox默认占比 end----------------
        # 强制初始化表头（即使无数据）
        self.display_patient_info(None)

        # 确保初始有选中行
        if self.m_tle_Basic_Filter.rowCount() > 0:
            self.m_tle_Basic_Filter.setCurrentCell(0, 1)
        else:
            # 插入空行防止操作异常
            self.m_tle_Basic_Filter.insertRow(0)
            for col in range(self.m_tle_Basic_Filter.columnCount()):
                self.m_tle_Basic_Filter.setItem(0, col, QTableWidgetItem(""))

        # 窗口初始化设置
        self.showMaximized()  # 窗口最大化
        # 添加以下行，禁用患者信息表格的编辑
        self.m_tle_PatientInfo.setEditTriggers(
            QAbstractItemView.DoubleClicked |
            QAbstractItemView.SelectedClicked
        )
        self.m_tle_PatientInfo.setSelectionMode(QAbstractItemView.SingleSelection)

        # 设置label_PatientPhoto的事件过滤
        self.label_PatientPhoto.installEventFilter(self)

        self.diagnosis_combo_config = {
            'column': 1,
            'data_source': self._get_all_diagnoses,
            'filter_logic': self._filter_diagnoses,
            'placeholder': "输入诊断拼音首字母"
        }

        # 年龄类型配置
        self.age_combo_config = {
            'column': 1,
            'data_source': self._generate_age_data,
            'filter_logic': self._filter_age,
            'placeholder': "输入年龄数字"
        }

        # 煎法类型配置
        self.decoction_combo_config = {
            'column': 3,
            'data_source': self._get_decoction_methods,
            'use_dialog': False  # 确保使用内联QComboBox而非对话框
        }

        self.m_edt_Diagnote_4.textChanged.connect(self.checkdiagnotetexteidtlenth)
        self.m_edt_acup.textChanged.connect(self.checkdacubtetexteidtlenth)
        self.m_edt_DiagConcl_2.textChanged.connect(self.checkdiagconcllenth)
        self.m_edt_DrugDiscrip.setReadOnly(True)
        self.m_edtDosesPrice.setReadOnly(True)
        self.m_edtAcubPrice.setReadOnly(True)
        self.m_edtTotalPrice.setReadOnly(True)

        # 设置浮点数验证器（允许范围：-9999.99~9999.99，两位小数）
        uint_validator = QDoubleValidator(0, 10, 0, self)
        uint_validator.setNotation(QDoubleValidator.StandardNotation)
        self.m_edtDosesNumber.setValidator(uint_validator)
        self.m_edtAcubNumber.setValidator(uint_validator)

        # self.m_tle_Basic_Filter = CustomTableWidget(10, 5, self)
        # self.m_tle_Basic_Filter.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        # self.m_tle_Basic_Filter.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)

        self.m_tle_Basic_Filter.setEditTriggers(QAbstractItemView.NoEditTriggers)  # 禁用直接编辑
        # self.m_tle_PatientInfo.setEditTriggers(QAbstractItemView.NoEditTriggers)  # 禁用直接编辑
        self.m_tle_ClinicalSymptom.setEditTriggers(QAbstractItemView.NoEditTriggers)  # 禁用直接编辑
        self.m_tle_Diagnosis.setEditTriggers(QAbstractItemView.NoEditTriggers)  # 禁用直接编辑
        self.m_tbl_DrugUsage.setEditTriggers(QTableWidget.NoEditTriggers)

        # 绑定菜单项点击事件
        #self.on_action_jingyanxuanfang.triggered.connect(self.on_action_jingyanxuanfang_key)
        #self.on_action_bianbingxuanfang.triggered.connect(self.on_action_bianbingxuanfang_key)
        self.m_bt_4_DateSearch.clicked.connect(self.handle_search_click)
        self.m_bt_DrugSelect_3.clicked.connect(self.handle_drugselect_click)
        self.m_pbWithDiagSyndrome.clicked.connect(self.handle_withdiagprint_click)
        self.m_pbWithoutDiagSyndrome.clicked.connect(self.handle_withoutdiagprint_click)
        self.m_bt_Visit_2.clicked.connect(self.handle_secondvisit_click)
        self.m_bt_Visit.clicked.connect(self.handle_firstvisit_click)
        self.m_bt_Save.clicked.connect(self.handle_savepatientinfo_click)
        self.m_bt_Del.clicked.connect(self.handle_deletepatientinfo_click)
        self.m_bt_menu_DrugList.clicked.connect(self.open_drug_setting)
        self.m_bt_menu_DrugUsage.clicked.connect(self.open_drug_usage)
        self.m_bt_menu_Userinfor.clicked.connect(self.open_Userinfor_window)
        self.m_bt_menu_Formulas.clicked.connect(self.open_menu_Formulas)
        self.m_bt_menu_symptoms.clicked.connect(self.show_symptoms_window)
        self.m_bt_menu_Anylasis.clicked.connect(self.show_analysis_window)
        self.m_bt_menu_Diagnosis.clicked.connect(self.show_clinical_diag)
        self.m_bt_menu_Acup.clicked.connect(self.show_acup_setting)
        self.m_bt_menu_Patients.clicked.connect(self.show_patient_list)
        self.m_bt_menu_MedicalRec.clicked.connect(self.open_medical_record_window)
        self.m_bt_About.clicked.connect(self.show_about)
        self.m_pbPreview.clicked.connect(self.handle_preview_click)

        currentdate = QDate.currentDate()
        threeyearsago = currentdate.addYears(-3)
        self.m_edt_searchfilter_DateStart.setText(threeyearsago.toString("yyyy-MM-dd"))
        self.m_edt_searchfilter_DateEnd.setText(currentdate.toString("yyyy-MM-dd"))
        self.m_edt_searchfilter_DateStart.installEventFilter(self)
        self.m_edt_searchfilter_DateEnd.installEventFilter(self)
        self.m_tle_Basic_Filter.installEventFilter(self)

        self.m_edt_searchfilter.textChanged.connect(
            partial(self.m_databaseUtil.load_tableWidget_data, self.m_tle_Basic_Filter,
                    columnLabels=['编号', '姓名', '性别', '年龄', '诊断', '日期时间'],
                    sqlstr="SELECT `编号`,`姓名`, `性别`, `年龄`, `诊断`, `日期时间` FROM 常规资料 WHERE 姓名拼音 LIKE %s ORDER BY 编号 DESC"))
        self.m_edt_searchfilter_DiagnosisP.textChanged.connect(
            partial(self.m_databaseUtil.load_tableWidget_data, self.m_tle_Basic_Filter,
                    columnLabels=['编号', '姓名', '性别', '年龄', '诊断', '日期时间'],
                    sqlstr="SELECT `编号`,`姓名`, `性别`, `年龄`, `诊断`, `日期时间` FROM 常规资料 WHERE 诊断拼音 LIKE %s ORDER BY 编号 DESC"))
        self.m_edt_SympConcl.textChanged.connect(self.handle_refresh_sympconcl_content)
        self.m_edt_searchfilter_ClinicalSymptom.textChanged.connect(
            partial(self.m_databaseUtil.load_tableWidget_data, self.m_tle_ClinicalSymptom,
                    columnLabels=['编号', '常见病证表现'], sqlstr="SELECT `编号`,`临床表现` FROM 病证 WHERE 病证拼音 LIKE %s"))
        self.m_edt_searchfilter_DiagnosisD.textChanged.connect(
            partial(self.m_databaseUtil.load_tableWidget_data, self.m_tle_Diagnosis, columnLabels=['编号', '常用辩证处方'],
                    sqlstr="SELECT `编号`,`辩证` FROM 辩证 WHERE 辩证拼音 LIKE %s"))

        self.m_tle_PatientInfo.setColumnCount(2)
        self.m_tle_PatientInfo.horizontalHeader().setVisible(False)  # 隐藏水平表头
        self.m_tle_PatientInfo.verticalHeader().setVisible(False)  # 隐藏垂直表头

        self.m_databaseUtil.load_tableWidget_data(self.m_tle_Basic_Filter, "",
                                                  ['编号', '姓名', '性别', '年龄', '诊断', '日期时间'],  # 新增诊断列
                                                  sqlstr="SELECT `编号`,`姓名`, `性别`, `年龄`, `诊断`, `日期时间` FROM 常规资料 WHERE 编号 LIKE %s ORDER BY 编号 DESC")
        self.m_databaseUtil.load_tableWidget_data(self.m_tle_ClinicalSymptom, "", ['编号', '常见病证表现'],
                                                  sqlstr="SELECT `编号`,`临床表现` FROM 病证 WHERE 编号 LIKE %s")
        self.m_databaseUtil.load_tableWidget_data(self.m_tle_Diagnosis, "", ['编号', '常用辩证处方'],
                                                  sqlstr="SELECT `编号`,`辩证` FROM 辩证 WHERE 辩证拼音 LIKE %s")
        self.load_druguse_data()

        # 连接双击信号
        self.m_tle_Basic_Filter.itemClicked.connect(self.on_row_basic_filter_click)
        self.m_tle_PatientInfo.cellClicked.connect(self.on_cell_patientInfo_click)
        self.m_tbl_DrugUsage.cellClicked.connect(self.on_cell_decoction_clicked)
        self.m_tle_ClinicalSymptom.itemDoubleClicked.connect(self.on_row_ClinicalSymptom_double_click)
        self.m_tle_Diagnosis.itemDoubleClicked.connect(self.on_row_diagnosis_double_click)
        self.m_tle_Diagnosis.itemClicked.connect(self.on_row_Diagnosis_click)
        # 新增：连接当前单元格变化的信号，处理键盘上下键选择行的情况
        self.m_tle_Basic_Filter.currentCellChanged.connect(self.handle_current_cell_changed)
        self.m_tle_Diagnosis.currentCellChanged.connect(self.handle_Diagnosis_cell_changed)

        self.m_tbl_DrugUsage.setColumnHidden(0, True)
        self.m_edtDosesNumber.textChanged.connect(self.calc_drug_total_price)
        self.m_edtAcubNumber.textChanged.connect(self.calc_acub_total_price)

        if self.m_tle_Basic_Filter.rowCount() > 0 and self.m_tle_Basic_Filter.columnCount() > 0:
            self.m_tle_Basic_Filter.setCurrentCell(0, 1)
            self.m_tle_Basic_Filter.setFocus()
            item = self.m_tle_Basic_Filter.item(0, 1)

            self.on_row_basic_filter_click(item)

    def get_max_case_number(self):
        """查询数据库中当前最大的病历号（安全版本），取消默认初始值"""
        try:
            # 确保传递空元组作为参数，并修正SQL语法
            result = self.m_databaseUtil.query_database_info(
                "SELECT MAX(CAST(病历号 AS UNSIGNED)) FROM 常规资料",  # 修正SQL语法错误
                ()  # 显式传递空参数
            )
            # 处理结果
            if result and result[0] and result[0][0] is not None:
                return int(result[0][0])
            else:
                # 当数据库为空或查询结果为空时，返回None
                return None
        except Exception as e:
            print(f"获取病历号失败: {str(e)}")
            # 异常时返回None，调用者需要根据此情况做进一步处理
            return None

    # ------------设置初始化窗口中groupbox默认占比 start----------------
    def adjust_splitter_sizes(self):
        # 计算可用宽度
        total_width = self.splitter.width()

        # 根据groupBox_3的可见性应用不同比例
        if self.groupBox_3.isVisible():
            # 36:270:create_decoction_combobox160:110 的比例
            ratios = [36, 260, 140, 140]
        else:
            # 当groupBox_3隐藏时调整为 36:330:210:0
            ratios = [36, 330, 210, 0]

        total_ratio = sum(ratios)
        if total_ratio == 0:
            return

        # 计算实际像素尺寸
        sizes = [int(total_width * ratio / total_ratio) for ratio in ratios]

        # 设置分割器尺寸
        self.splitter.setSizes(sizes)

    def resizeEvent(self, event):
        """窗口大小改变时自动调整比例"""
        super().resizeEvent(event)
        self.adjust_splitter_sizes()

    def showEvent(self, event):
        """窗口首次显示时初始化比例"""
        super().showEvent(event)
        # 使用单次定时器确保在窗口布局完成后执行
        QTimer.singleShot(0, self.adjust_splitter_sizes)

    # ------------设置初始化窗口中groupbox默认占比 end----------------

    def open_drug_setting(self):
        drug_setting_diag = DrugSettingWindow(self)  # 将主窗口作为父组件
        # 自定义窗口大小
        width = self.width() * 0.6
        height = width * 9 / 14
        drug_setting_diag.resize(width, height)
        drug_setting_diag.exec()

    def open_drug_usage(self):
        drug_usage_diag = DrugUsageWindow(self)  # 将主窗口作为父组件
        # 自定义窗口大小
        width = self.width() * 0.6
        height = width * 9 / 14
        drug_usage_diag.resize(width, height)
        drug_usage_diag.exec()

    def open_Userinfor_window(self):
        Userinfor_window_diag = UserInfoWindow(self) # 将主窗口作为父组件
        # 自定义窗口大小
        width = self.width() * 0.6
        height = width * 9 / 14
        Userinfor_window_diag.resize(width, height)
        Userinfor_window_diag.exec()

    def open_menu_Formulas(self):
        menu_Formulas_diag = MyDrugFormulasWindow(self) # 将主窗口作为父组件
        # 自定义窗口大小
        width = self.width() * 0.7
        height = width * 9 / 14
        menu_Formulas_diag.resize(width, height)
        menu_Formulas_diag.exec()


    def show_clinical_diag(self):
        clinical_diag = ClinicalDiagWindow(self)# 将主窗口作为父组件
        # 自定义窗口大小
        width = self.width() * 0.6
        height = width * 9 / 14
        clinical_diag.resize(width, height)
        clinical_diag.exec()


    def show_patient_list(self):
        patient_list_dialog = PatientListWindow(self)
        # 自定义窗口大小
        width = self.width() * 0.7
        height = width * 9 / 14
        patient_list_dialog.resize(width, height)
        patient_list_dialog.exec()


    def show_symptoms_window(self):
        symptoms_window_dialog = ClinicalSymptomsWindow(self)
        # 自定义窗口大小
        width = self.width() * 0.6
        height = width * 9 / 14
        symptoms_window_dialog.resize(width, height)
        symptoms_window_dialog.exec()

    def show_analysis_window(self):
        analysis_window_dialog = ClinicalAnylasisWindow(self)
        # 自定义窗口大小
        width = self.width() * 0.6
        height = width * 9 / 14
        analysis_window_dialog.resize(width, height)
        analysis_window_dialog.exec()

    def show_acup_setting(self):
        acup_setting_dialog = AcupSettingWindow(self)
        # 自定义窗口大小
        width = self.width() * 0.6
        height = width * 9 / 14
        acup_setting_dialog.resize(width, height)
        acup_setting_dialog.exec()

    def open_medical_record_window(self):
        medical_record_dialog = MedicalRecordWindow(self)
        width = self.width() * 0.6
        height = width * 9 / 14
        medical_record_dialog.resize(width, height)
        medical_record_dialog.exec()


    def show_about(self):
        about_dialog = AboutDialog(self)
        # 自定义窗口大小
        width = self.width() * 0.6
        height = width * 9 / 14
        about_dialog.resize(width, height)
        about_dialog.exec()

    # 新增处理函数：处理键盘导航时的行选择
    def handle_current_cell_changed(self, current_row, current_col, previous_row, previous_col):
        """当用户使用键盘上下键或鼠标改变当前行时，触发患者信息更新"""
        if current_row >= 0:
            # 获取当前行第一列的item（编号列）
            item = self.m_tle_Basic_Filter.item(current_row, 0)
            if item is not None:
                self.on_row_basic_filter_click(item)  # 调用原有的点击处理函数

    def handle_Diagnosis_cell_changed(self, current_row, current_col, previous_row, previous_col):
        """当用户使用键盘上下键或鼠标改变当前行时，触发患者信息更新"""
        if current_row >= 0:
            # 获取当前行第一列的item（编号列）
            item = self.m_tle_Diagnosis.item(current_row, 0)
            if item is not None:
                self.on_row_Diagnosis_click(item)  # 调用原有的点击处理函数

    def checkdiagnotetexteidtlenth(self):
        if len(self.m_edt_Diagnote_4.toPlainText()) > 100:
            text = self.m_edt_Diagnote_4.toPlainText()[:100]
            self.m_edt_Diagnote_4.setText(text)
            QMessageBox.warning(self, "警告", "输入的文字不得超过100字")

    def checkdacubtetexteidtlenth(self):
        if len(self.m_edt_acup.toPlainText()) > 200:
            text = self.m_edt_acup.toPlainText()[:200]
            self.m_edt_acup.setText(text)
            QMessageBox.warning(self, "警告", "输入的文字不得超过200字")

    def checkdiagconcllenth(self):
        if len(self.m_edt_DiagConcl_2.toPlainText()) > 50:
            text = self.m_edt_DiagConcl_2.toPlainText()[:50]
            self.m_edt_DiagConcl_2.setText(text)
            QMessageBox.warning(self, "警告", "输入的文字不得超过50字")

    def handle_refresh_sympconcl_content(self):
        current_text = self.m_edt_SympConcl.toPlainText()
        if len(current_text) > 200:
            self.m_edt_SympConcl.setPlainText(current_text[:200])
            QMessageBox.warning(self, "警告", "输入的文字不得超过200字")
        item = self.m_tle_PatientInfo.item(3, 1)
        if item is not None:
            item.setText(self.m_edt_SympConcl.toPlainText().strip() or "")

    def handle_firstvisit_click(self):
        # 清空所有字段前确保表格已初始化
        self.display_patient_info(None)



        for row in range(self.m_tle_PatientInfo.rowCount()):
            item = self.m_tle_PatientInfo.item(row, 1)
            if item is not None:
                item.setText("")

        self.m_edt_SympConcl.clear()

        self.m_edt_DiagConcl_2.setText("")
        self.m_edt_Diagnote_4.setText("")
        self.m_tbl_DrugUsage.clearContents()
        for i in range(self.m_tbl_DrugUsage.rowCount()):
            self.m_tbl_DrugUsage.removeRow(i)
        self.m_edt_acup.setText("")
        self.m_edtDosesNumber.setText("0")
        self.m_edtAcubNumber.setText("0")
        self.m_edtDosesPrice.setText("0")
        self.m_edtAcubPrice.setText("0")
        self.m_edtTotalPrice.setText("0")
        # 随机生成8位病历号
        item = self.m_tle_PatientInfo.item(8, 1)
        if item is not None:
            item.setText(str(random.randint(10_000_000, 99_999_999)))

        self.insert_or_update_patient_record(True, True)
        self.label_PatientPhoto.clear()
        self.current_image_path = None

    def handle_secondvisit_click(self):
        # 设置编辑触发器（如果被其他代码覆盖）
        for row in range(self.m_tle_PatientInfo.rowCount()):
            item = self.m_tle_PatientInfo.item(row, 1)
            if item is not None:
                if row == 3 or row == 4:  # 清空
                    item.setText("")

        self.m_edt_SympConcl.clear()

        self.m_edt_DiagConcl_2.setText("")
        self.m_edt_Diagnote_4.setText("")
        self.m_tbl_DrugUsage.clearContents()
        for i in range(self.m_tbl_DrugUsage.rowCount()):
            self.m_tbl_DrugUsage.removeRow(i)
        self.m_edt_acup.setText("")
        self.m_edtDosesNumber.setText("0")
        self.m_edtAcubNumber.setText("0")
        self.m_edtDosesPrice.setText("0")
        self.m_edtAcubPrice.setText("0")
        self.m_edtTotalPrice.setText("0")
        item = self.m_tle_PatientInfo.item(8, 1)
        if item is not None:
            self.m_casenumber = item.text()

        self.insert_or_update_patient_record(True, False)
        #self.label_PatientPhoto.clear()
        #self.current_image_path = None

    ############################################
    def validate_insert_data(self):
        """数据校验函数"""
        errors = []
        valid_data = {}

        # 姓名校验（非空）
        name_item = self.m_tle_PatientInfo.item(0, 1)
        name = name_item.text().strip() or ""
        if not name:
            errors.append(("姓名不能为空", 0))
        else:
            valid_data["name"] = name

        # 性别校验（男/女）
        gender_item = self.m_tle_PatientInfo.item(1, 1)
        gender = gender_item.text().strip()
        if not gender:  # 新增空值检查
            errors.append(("性别不能为空", 1))
        elif gender not in ["男", "女"]:
            errors.append(("性别必须为'男'或'女'", 1))
        else:
            valid_data["gender"] = gender

        # 年龄校验（1-150之间的整数）

        age = self.m_tle_PatientInfo.item(2, 1).text()
        valid_data["age"] = age

        # 病证
        disease = str(self.m_tle_PatientInfo.item(3, 1).text() or "")
        valid_data["disease"] = disease

        # 捕获针灸或其他内容
        acu = self.m_edt_acup.toPlainText().strip()  # ✅ 确保读取最新值
        valid_data["acu"] = acu

        # 捕获备注内容
        diagnote = self.m_edt_Diagnote_4.toPlainText().strip()  # ✅ 确保读取最新值
        valid_data["diagnote"] = diagnote

        # 诊断
        diagnosis = str(self.m_tle_PatientInfo.item(4, 1).text() or "")
        valid_data["diagnosis"] = diagnosis

        # 血压校验（格式：120/80）
        bp = self.m_tle_PatientInfo.item(5, 1).text().strip() or ""
        valid_data["blood_pressure"] = bp

        # 住址校验（非空）
        address = self.m_tle_PatientInfo.item(6, 1).text().strip() or ""
        valid_data["address"] = address

        # 病历号校验（确保存在且为有效整数）
        try:
            case_number_item = self.m_tle_PatientInfo.item(8, 1)
            if not case_number_item or not case_number_item.text().strip():
                errors.append(("病历号不能为空", 8))
            else:
                case_number = case_number_item.text().strip()
                valid_data["case_number"] = int(case_number)
                if valid_data["case_number"] <= 0:
                    errors.append(("病历号必须为正整数", 8))
        except ValueError:
            errors.append(("病历号必须为有效整数", 8))

        # 身份证号校验
        id_card_item = self.m_tle_PatientInfo.item(9, 1)
        id_card = id_card_item.text().strip() if id_card_item else ""
        valid_data["id_card"] = id_card

        # 身份证号校验（允许为空）
        id_card_item = self.m_tle_PatientInfo.item(9, 1)
        valid_data["id_card"] = id_card_item.text().strip() if id_card_item else ""


        # 电话校验（11位数字）
        phone_item = self.m_tle_PatientInfo.item(7, 1)
        phone = phone_item.text().strip() if phone_item else ""
        valid_data["phone"] = phone  # 允许空值和非数字

        # 诊金校验（正整数）
        try:
            case_number_item = self.m_tle_PatientInfo.item(8, 1)
            if not case_number_item or not case_number_item.text().strip():
                errors.append(("病历号不能为空", 8))

            case_number = int(case_number_item.text())
            if case_number <= 0:
                raise ValueError
            valid_data["case_number"] = case_number
        except:
            errors.append(("病历号必须为正整数", 3))

        drugnum = self.m_edtDosesNumber.text().strip() or "0"
        if drugnum != "":
            if not (drugnum.isdigit()):
                errors.append(("剂数必须为数字", 4))
            else:
                valid_data["drugnum"] = drugnum

        acubnum = self.m_edtAcubNumber.text().strip() or "0"
        valid_data["acubnum"] = acubnum

        drug_useage = self.m_cbUseage.currentText()
        valid_data["drug_useage"] = drug_useage

        for i in range(4):  # 按照列读取
            for j in range(20):
                item = self.m_tbl_DrugUsage.item(j, i)
                key_name = f"drugname{j + 1}"  # 动态生成键名
                key_num = f"drugnum{j + 1}"  # 动态生成键名
                key_decoction = f"drugdecoction{j + 1}"  # 动态生成键名
                if i == 0:  # 第一列是编号，不读取
                    continue
                elif i == 1:  # 第二列药名
                    if item is not None:
                        valid_data[key_name] = item.text()
                    else:
                        valid_data[key_name] = ""
                elif i == 2:  # 第二列剂量
                    if item is not None:
                        valid_data[key_num] = item.text()
                    else:
                        valid_data[key_num] = ""
                elif i == 3:  # 第二列煎法
                    if item is not None:
                        valid_data[key_decoction] = item.text()
                    else:
                        valid_data[key_decoction] = ""
            #
        if not self.current_user_id:
            QMessageBox.warning(self, "错误", "未获取到当前用户ID")
            errors.append(("用户未登录", -1))
            return valid_data, errors

        try:
            cf_data = self.m_databaseUtil.query_database_info(
                "SELECT 诊金 FROM 基本设置 WHERE user_id = %s",
                (self.current_user_id,)
            )

            if cf_data and cf_data[0] is not None:
                consultationfee = Decimal(str(cf_data[0]))
                valid_data["consultationfee"] = consultationfee
            else:
                errors.append(("当前用户未设置诊金", 5))
                QMessageBox.warning(self, "警告", "当前用户未设置诊金，默认使用0")

        except Exception as e:
            errors.append(("诊金查询失败", 5))
            print(f"诊金查询错误: {str(e)}")

        doseprice = self.m_edtDosesPrice.text().strip() or "0"
        valid_data["doseprice"] = doseprice

        acubprice = self.m_edtAcubPrice.text().strip() or "0"
        valid_data["acubprice"] = acubprice

        diagconcl = str(self.m_edt_DiagConcl_2.toPlainText() or "")
        valid_data["diagconcl"] = diagconcl

        totalprice = self.m_edtTotalPrice.text().strip() or "0"
        valid_data["totalprice"] = totalprice

        acu = str(self.m_edt_acup.toPlainText().strip() or "")
        valid_data["acu"] = acu

        diagnote = str(self.m_edt_Diagnote_4.toPlainText().strip() or "")
        valid_data["diagnote"] = diagnote

        return valid_data, errors

    def highlight_error(self, row):
        """高亮错误单元格"""
        for col in [1]:  # 只高亮值列
            item = self.m_tle_PatientInfo.item(row, col)
            if item:
                item.setBackground(QColor(255, 200, 200))  # 浅红色背景

    def clear_highlights(self):
        """清除所有高亮"""
        for row in range(self.m_tle_PatientInfo.rowCount()):
            for col in [1]:
                item = self.m_tle_PatientInfo.item(row, col)
                if item:
                    item.setBackground(QColor(255, 255, 255))

    # 插入或更新当前记录
    def insert_or_update_patient_record(self, newrecord: bool, newpatient: bool):
        """插入数据库记录"""
        try:
            newrecord_id = 0
            refreshdata_id = None

            db_config = load_db_config()
            connect = pymysql.connect(**db_config)
            if not connect:
                return
            cursor = connect.cursor()

            if newpatient:  # 新病人，只插入ID、病历号的记录
                # 获取诊金，若未设置则使用0
                consultation_fee = self.get_consultation_fee()
                # 提供必填字段的默认值
                query = """INSERT INTO 常规资料 (姓名, 性别, 年龄, 病证, 诊断, 血压, 住址, 电话, 病历号, 身份证号, 诊金) 
                                   VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

                item = self.m_tle_PatientInfo.item(8, 1)
                if item != None:
                    case_number = int(item.text())
                    case_number_data = ("", "", "", "", "", "", "", "", case_number, "", consultation_fee)
                    cursor.execute(query, case_number_data)
                    n = cursor.rowcount
                    connect.commit()
                    newrecord_id = cursor.lastrowid
            else:
                self.clear_highlights()
                valid_data, errors = self.validate_insert_data()

                if errors:
                    error_msg = "发现以下错误：\n\n" + "\n".join([f"• {msg}" for msg, row in errors])
                    QMessageBox.warning(self, "数据校验失败", error_msg)
                    # for msg, row in errors:
                    #    self.highlight_error(row)#需要根据控件调整高亮的位置
                    return

                current_data = QDateTime.currentDateTime()
                current_date_str = current_data.toString("yyyy-MM-dd HH:mm:ss")
                query = ""
                current_row = self.m_tle_Basic_Filter.currentRow()
                item = self.m_tle_Basic_Filter.item(current_row, 0)
                if item != None:
                    refreshdata_id = self.m_tle_Basic_Filter.item(current_row, 0).text()

                if newrecord:
                    query = """INSERT INTO 常规资料 
                                      (姓名, 性别, 年龄, 病证,诊断,血压, 住址, 电话, 病历号, 身份证号, 日期时间, 姓名拼音, 
                                      诊断拼音,剂数,针灸次数,用法,
                                      药物1, 药物2,药物3,药物4,药物5,药物6,药物7,药物8,药物9,药物10,
                                      药物11,药物12,药物13,药物14,药物15,药物16,药物17,药物18,药物19,药物20,
                                      用量1,用量2,用量3,用量4,用量5,用量6,用量7,用量8,用量9,用量10,
                                      用量11,用量12,用量13,用量14,用量15,用量16,用量17,用量18,用量19,用量20,
                                      先煎后下1,先煎后下2,先煎后下3,先煎后下4,先煎后下5,先煎后下6,先煎后下7,先煎后下8,先煎后下9,先煎后下10,
                                      先煎后下11,先煎后下12,先煎后下13,先煎后下14,先煎后下15,先煎后下16,先煎后下17,先煎后下18,先煎后下19,先煎后下20,
                                      诊金,药费,针灸费用,辨证,总费用,针灸或其他,备注, 患者照片)
                               VALUES (
                               %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                               %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                               %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                               %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                               %s, %s, %s, %s)"""
                else:
                    # 修改1：添加有效性检查
                    current_row = self.m_tle_Basic_Filter.currentRow()
                    if current_row < 0:
                        QMessageBox.warning(self, "操作错误", "请先选择要更新的记录")
                        return

                    item = self.m_tle_Basic_Filter.item(current_row, 0)
                    if not item or not item.text().strip():
                        QMessageBox.warning(self, "数据错误", "选中记录编号无效")
                        return

                    refreshdata_id = item.text()  # 确保赋值
                    query = """UPDATE 常规资料 
                                                   SET 姓名=%s, 性别=%s, 年龄=%s, 病证=%s, 诊断=%s, 血压=%s, 住址=%s, 电话=%s, 病历号=%s, 身份证号=%s, 日期时间=%s,
                                                       姓名拼音=%s, 诊断拼音=%s, 剂数=%s, 针灸次数=%s, 用法=%s,
                                                       药物1=%s, 药物2=%s, 药物3=%s, 药物4=%s, 药物5=%s, 药物6=%s, 药物7=%s, 药物8=%s, 药物9=%s, 药物10=%s,
                                                       药物11=%s, 药物12=%s, 药物13=%s, 药物14=%s, 药物15=%s, 药物16=%s, 药物17=%s, 药物18=%s, 药物19=%s, 药物20=%s,
                                                       用量1=%s, 用量2=%s, 用量3=%s, 用量4=%s, 用量5=%s, 用量6=%s, 用量7=%s, 用量8=%s, 用量9=%s, 用量10=%s,
                                                       用量11=%s, 用量12=%s, 用量13=%s, 用量14=%s, 用量15=%s, 用量16=%s, 用量17=%s, 用量18=%s, 用量19=%s, 用量20=%s,
                                                       先煎后下1=%s, 先煎后下2=%s, 先煎后下3=%s, 先煎后下4=%s, 先煎后下5=%s, 先煎后下6=%s, 先煎后下7=%s, 先煎后下8=%s, 先煎后下9=%s, 先煎后下10=%s,
                                                       先煎后下11=%s, 先煎后下12=%s, 先煎后下13=%s, 先煎后下14=%s, 先煎后下15=%s, 先煎后下16=%s, 先煎后下17=%s, 先煎后下18=%s, 先煎后下19=%s, 先煎后下20=%s,
                                                       诊金=%s, 药费=%s, 针灸费用=%s, 辨证=%s, 总费用=%s, 针灸或其他=%s, 备注=%s, 患者照片=%s
                                                   WHERE 编号=%s"""  # 最后使用编号作为WHERE条件

                    if current_row >= 0:  # 确保有选中行
                        item = self.m_tle_Basic_Filter.item(current_row, 0)  # 获取第 0 列数据
                        query = """UPDATE 常规资料 
                                   SET 姓名=%s, 性别=%s, 年龄=%s, 病证=%s, 诊断=%s, 血压=%s, 住址=%s, 电话=%s, 病历号=%s, 身份证号=%s, 日期时间=%s,
                                       姓名拼音=%s, 诊断拼音=%s, 剂数=%s, 针灸次数=%s, 用法=%s,
                                       药物1=%s, 药物2=%s, 药物3=%s, 药物4=%s, 药物5=%s, 药物6=%s, 药物7=%s, 药物8=%s, 药物9=%s, 药物10=%s,
                                       药物11=%s, 药物12=%s, 药物13=%s, 药物14=%s, 药物15=%s, 药物16=%s, 药物17=%s, 药物18=%s, 药物19=%s, 药物20=%s,
                                       用量1=%s, 用量2=%s, 用量3=%s, 用量4=%s, 用量5=%s, 用量6=%s, 用量7=%s, 用量8=%s, 用量9=%s, 用量10=%s,
                                       用量11=%s, 用量12=%s, 用量13=%s, 用量14=%s, 用量15=%s, 用量16=%s, 用量17=%s, 用量18=%s, 用量19=%s, 用量20=%s,
                                       先煎后下1=%s, 先煎后下2=%s, 先煎后下3=%s, 先煎后下4=%s, 先煎后下5=%s, 先煎后下6=%s, 先煎后下7=%s, 先煎后下8=%s, 先煎后下9=%s, 先煎后下10=%s,
                                       先煎后下11=%s, 先煎后下12=%s, 先煎后下13=%s, 先煎后下14=%s, 先煎后下15=%s, 先煎后下16=%s, 先煎后下17=%s, 先煎后下18=%s, 先煎后下19=%s, 先煎后下20=%s,
                                       诊金=%s, 药费=%s, 针灸费用=%s, 辨证=%s, 总费用=%s, 针灸或其他=%s, 备注=%s, 患者照片=%s
                                   WHERE 编号=%s"""  # 最后使用编号作为WHERE条件

                strnamepin = self.m_databaseUtil.get_name_initials(valid_data["name"])
                strndiagpin = self.m_databaseUtil.get_name_initials(valid_data["diagnosis"])
                # 新病人，需要生成一个病历号

                drugs = [valid_data.get(f"drugname{i}", None) for i in range(1, 21)]
                usages = [valid_data.get(f"drugnum{i}", None) for i in range(1, 21)]
                decoctions = [valid_data.get(f"drugdecoction{i}", None) for i in range(1, 21)]

                values = (
                    valid_data["name"],
                    valid_data["gender"],
                    valid_data["age"],
                    valid_data["disease"],
                    valid_data["diagnosis"],
                    valid_data["blood_pressure"],
                    valid_data["address"],
                    valid_data["phone"],
                    valid_data["case_number"],
                    valid_data.get("id_card", ""),  # 添加身份证号，使用 get 避免 KeyError
                    current_date_str,
                    strnamepin,
                    strndiagpin,
                    valid_data["drugnum"],
                    valid_data["acubnum"],
                    valid_data["drug_useage"],
                    *drugs,
                    *usages,
                    *decoctions,
                    valid_data["consultationfee"],
                    valid_data["doseprice"],
                    valid_data["acubprice"],
                    valid_data["diagconcl"],
                    valid_data["totalprice"],
                    valid_data["acu"],
                    valid_data["diagnote"],
                    self.current_image_path if self.current_image_path else None,  # 存储路径
                )
                if newrecord:
                    cursor.execute(query, values)
                    newrecord_id = cursor.lastrowid
                else:
                    if not refreshdata_id:
                        raise ValueError("更新操作需要有效的记录ID")
                    # 将current_row添加到values末尾，形成完整的参数元组
                    cursor.execute(query, values + (refreshdata_id,))
                connect.commit()

        except Exception as e:  # 扩大异常捕获范围
            if connect:
                connect.rollback()
            error_msg = f"数据库操作失败: {str(e)}"
            if "refreshdata_id" in str(e):  # 新增特定错误提示
                error_msg = "更新操作需要先选择有效记录"
            QMessageBox.critical(self, "错误", error_msg)
        finally:
            if connect:
                connect.close()

        # 如果是初诊或者复诊，需要更新basick_filter当前选中的行

        self.m_databaseUtil.load_tableWidget_data(
            self.m_tle_Basic_Filter, "",
            ['编号', '姓名', '性别', '年龄', '诊断', '日期时间'],
            sqlstr="SELECT `编号`,`姓名`, `性别`, `年龄`, `诊断`, `日期时间` FROM 常规资料 WHERE 编号 LIKE %s ORDER BY 编号 DESC")

        # 修复点：严格检查 item 是否存在且文本有效
        target_id = newrecord_id if newrecord else refreshdata_id
        if target_id is None:
            return

        for row in range(self.m_tle_Basic_Filter.rowCount()):
            item = self.m_tle_Basic_Filter.item(row, 0)
            # 关键修改：添加空值检查和异常处理
            if item is not None and item.text().strip():
                try:
                    current_id = int(item.text())
                    if current_id == target_id:
                        self.m_tle_Basic_Filter.setCurrentItem(item)
                        self.m_tle_Basic_Filter.setCurrentCell(row, 1)
                        self.m_tle_Basic_Filter.setFocus()
                        self.m_tle_Basic_Filter.selectRow(row)
                        self.on_row_basic_filter_click(item)
                        break
                except ValueError:
                    continue  # 忽略无效的编号

        for row in range(self.m_tle_Basic_Filter.rowCount()):
            item = self.m_tle_Basic_Filter.item(row, 0)
            if item is not None and item.text().strip():  # 添加有效性检查
                try:
                    current_id = int(item.text())
                    recID = newrecord_id if newrecord else int(refreshdata_id)
                    if current_id == recID:
                        self.m_tle_Basic_Filter.setCurrentItem(item)
                        self.m_tle_Basic_Filter.setCurrentCell(row, 1)
                        self.m_tle_Basic_Filter.setFocus()
                        self.m_tle_Basic_Filter.selectRow(row)
                        self.on_row_basic_filter_click(item)
                        break
                except ValueError:
                    continue  # 忽略无效的编号

    def handle_savepatientinfo_click(self):
        # 原有的保存逻辑
        self.insert_or_update_patient_record(False, False)

        # 获取当前登录用户的医生名字
        try:
            # 查询当前用户的医生名字
            db_config = load_db_config()
            connection = pymysql.connect(**db_config)
            with connection.cursor() as cursor:
                sql = "SELECT 医生 FROM 基本设置 WHERE user_id = %s"
                cursor.execute(sql, (self.current_user_id,))
                result = cursor.fetchone()
                if result and result[0]:
                    doctor_name = result[0]
                else:
                    QMessageBox.warning(self, "警告", "当前用户未设置医生名字")
                    return
        except Exception as e:
            QMessageBox.critical(self, "数据库错误", f"查询医生名字失败: {str(e)}")
            return
        finally:
            if connection:
                connection.close()

        # 获取当前选中的患者ID
        current_row = self.m_tle_Basic_Filter.currentRow()
        if current_row < 0:
            QMessageBox.warning(self, "操作错误", "请先选择患者记录")
            return

        patient_id_item = self.m_tle_Basic_Filter.item(current_row, 0)
        if not patient_id_item or not patient_id_item.text().strip():
            QMessageBox.warning(self, "数据错误", "选中的记录编号无效")
            return

        patient_id = patient_id_item.text()

        # 更新“常规资料”表中的“主治医生”字段
        try:
            db_config = load_db_config()
            connection = pymysql.connect(**db_config)
            with connection.cursor() as cursor:
                sql = "UPDATE 常规资料 SET 主治医生 = %s WHERE 编号 = %s"
                cursor.execute(sql, (doctor_name, patient_id))
                connection.commit()
        except Exception as e:
            QMessageBox.critical(self, "数据库错误", f"更新主治医生信息失败: {str(e)}")
            if connection:
                connection.rollback()
        finally:
            if connection:
                connection.close()

    def handle_deletepatientinfo_click(self):
        current_row = self.m_tle_Basic_Filter.currentRow()
        if current_row >= 0:  # 确保有选中行
            selected_item_idvalues = []
            for range_obj in self.m_tle_Basic_Filter.selectedRanges():
                for row in range(range_obj.rowCount()):
                    row_index = range_obj.topRow() + row
                    item = self.m_tle_Basic_Filter.item(row_index, 0)  # 获取第一列的值
                    if item:  # 确保该项非空
                        selected_item_idvalues.append(item.text())

            # 数据库配置（根据实际情况修改）
            try:
                # 连接数据库

                db_config = load_db_config()
                connection = pymysql.connect(**db_config)
                cursor = connection.cursor()

                # 用户确认对话框
                msg_box = QMessageBox(self)
                msg_box.setIcon(QMessageBox.Warning)
                msg_box.setText("你确定要删除这些条记录吗？")
                msg_box.setWindowTitle("确认")
                msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
                msg_box.button(QMessageBox.Yes).setText("是")
                msg_box.button(QMessageBox.No).setText("否")
                msg_box.setDefaultButton(QMessageBox.No)  # 设置默认按钮为"否"

                ret = msg_box.exec()

                if ret == QMessageBox.Yes:
                    placeholders = ','.join(['%s'] * len(selected_item_idvalues))
                    sql = f"DELETE FROM 常规资料 WHERE 编号 IN ({placeholders})"
                    cursor.execute(sql, tuple(selected_item_idvalues))
                    connection.commit()
                    informationstr = f"已成功删除{cursor.rowcount}条患者记录!"
                    QMessageBox.information(self, "成功", informationstr)
                else:  # 如果用户点击“Cancel”或关闭对话框，则不执行任何操作
                    pass
            except pymysql.Error as e:
                print(f"数据库操作失败: {e}")
                if connection:
                    connection.rollback()
            finally:
                # 关闭连接
                connection.close()
            self.m_databaseUtil.load_tableWidget_data(self.m_tle_Basic_Filter, "",
                                                      ['编号', '姓名', '性别', '年龄', '诊断', '日期时间'],  # 新增诊断列
                                                      sqlstr="SELECT `编号`,`姓名`, `性别`, `年龄`, `诊断`, `日期时间` FROM 常规资料 WHERE 编号 LIKE %s ORDER BY 编号 DESC")

            item = self.m_tle_Basic_Filter.item(0, 0)
            if item != None:
                self.m_tle_Basic_Filter.setCurrentItem(item)
                self.m_tle_Basic_Filter.setCurrentCell(0, 1)
                self.m_tle_Basic_Filter.setFocus()
                self.on_row_basic_filter_click(item)

    def handle_withdiagprint_click(self):
        self.handle_savepatientinfo_click()
        current_row = self.m_tle_Basic_Filter.currentRow()
        if current_row < 0:
            QMessageBox.warning(self, "操作错误", "请先选择患者记录")
            return

        patient_id_item = self.m_tle_Basic_Filter.item(current_row, 0)
        if not patient_id_item or not patient_id_item.text().strip():
            QMessageBox.warning(self, "数据错误", "选中的记录编号无效")
            return

        patient_id = patient_id_item.text()

        # ✅ 新增：检查患者数据是否存在
        if not self._patient_data_exists(patient_id):
            QMessageBox.warning(self, "数据错误", "该患者记录不存在或数据不完整")
            return

        # 获取诊断信息
        diagnosis_item = self.m_tle_Basic_Filter.item(current_row, 4)
        diagnosis = diagnosis_item.text() if diagnosis_item else ""

        # 创建报表生成器并传递参数
        reporter = myReporter(self.current_user_id)  # 传入当前用户ID
        pdf_content = reporter.generate(patient_id, False)  # 第二个参数控制是否隐藏诊断
        pdf_data = pdf_content.getvalue()

        # 显示 PDF 预览
        viewer = PdfViewerDialog(pdf_data, self)
        viewer.exec()

        # 更新患者记录（如果需要）
        self.insert_or_update_patient_record(False, False)

    def _patient_data_exists(self, patient_id):
        """检查患者数据是否存在"""
        try:
            db_config = load_db_config()
            conn = pymysql.connect(**db_config)
            cursor = conn.cursor()
            cursor.execute("SELECT COUNT(*) FROM 常规资料 WHERE 编号 = %s", (patient_id,))
            count = cursor.fetchone()[0]
            return count > 0
        except Exception as e:
            print(f"检查患者数据失败: {e}")
            return False
        finally:
            if conn:
                conn.close()

    def handle_withoutdiagprint_click(self):
        """处理‘不带诊断打印’点击事件"""
        # 前置检查：确保选中有效记录
        self.handle_savepatientinfo_click()
        current_row = self.m_tle_Basic_Filter.currentRow()
        if current_row < 0:
            QMessageBox.warning(self, "操作错误", "请先选择患者记录")
            return

        patient_id_item = self.m_tle_Basic_Filter.item(current_row, 0)
        if not patient_id_item or not patient_id_item.text().strip():
            QMessageBox.warning(self, "数据错误", "选中的记录编号无效")
            return

        patient_id = patient_id_item.text()
        if not self._patient_data_exists(patient_id):
            QMessageBox.warning(self, "数据错误", "该患者记录不存在或数据不完整")
            return

        # ✅ 所有检查通过后直接生成PDF，无需重复判断 current_row >= 0
        reporter = myReporter(self.current_user_id)
        pdf_content = reporter.generate(patient_id, True)
        pdf_data = pdf_content.getvalue()
        viewer = PdfViewerDialog(pdf_data, self)
        viewer.exec()

        # 更新患者记录（如果需要）
        self.insert_or_update_patient_record(False, False)

    def calc_acub_total_price(self):

        db_config = load_db_config()
        conn = pymysql.connect(**db_config)
        try:
            with conn.cursor() as cursor:
                sql = """SELECT `价格` FROM 针灸 """
                cursor.execute(sql)

                results = cursor.fetchall()
                conn.commit()

                if not results:
                    return
                else:
                    # 获取原始值，处理可能的None或无效数据
                    raw_value = results[0][0] if results[0][0] is not None else '0'
                    cleaned_value = str(raw_value).replace(',', '.')  # 替换逗号为点
                    # 移除非数字、点和负号之外的字符
                    cleaned_value = ''.join([c for c in cleaned_value if c in '0123456789.-'])

                    try:
                        dAcubPrice = Decimal(cleaned_value)
                    except InvalidOperation:
                        dAcubPrice = Decimal(0)

                    acub_num = Decimal(self.m_edtAcubNumber.text() or 0.0)
                    total_acub_price = acub_num * dAcubPrice
                    self.m_edtAcubPrice.setText(f"{total_acub_price:.2f}")

                    dDrugPrice = Decimal(self.m_edtDosesPrice.text() or '0')  # 确保此处输入有效
                    self.calcTotalPrice()  # 调用新的总费用计算方法

        except Exception as e:
            QMessageBox.warning(self, "查询错误", f"搜索失败: {str(e)}")
        except pymysql.Error as e:
            QMessageBox.critical(self, "数据库错误", f"数据库操作失败:\n{str(e)}")
        finally:
            conn.close()

    def calc_drug_total_price(self):
        # 初始化总金额
        drug_dosages = []  # 存储药品名称和剂量的元组列表

        if self.m_tbl_DrugUsage.rowCount() <= 0:
            return
        # 遍历表格，收集有效数据
        for row in range(self.m_tbl_DrugUsage.rowCount()):
            # 获取药品名称（第1列）
            drug_item = self.m_tbl_DrugUsage.item(row, 1)
            if not drug_item:
                continue
            drug_name = drug_item.text().strip()
            if not drug_name:
                continue

            # 获取剂量（第2列）
            dosage_item = self.m_tbl_DrugUsage.item(row, 2)
            if not dosage_item:
                continue
            try:
                # 使用Decimal解析剂量（而非float）
                dosage_str = dosage_item.text().strip().replace('g', '').replace('克', '')
                dosage = Decimal(dosage_str) if dosage_str else Decimal('0')
            except (ValueError, InvalidOperation):
                QMessageBox.warning(
                    self,
                    "输入错误",
                    f"第{row + 1}行剂量格式无效（示例：9 或 3.5）"
                )
                continue

            # 保存药品名称和剂量
            drug_dosages.append((drug_name, dosage))

        # 无有效数据时直接返回
        if not drug_dosages:
            return

        try:

            db_config = load_db_config()
            conn = pymysql.connect(**db_config)
            with conn.cursor() as cursor:
                # 提取药品名称列表
                # 执行查询
                cursor.execute("SELECT 药名,价格 FROM 中药")
                results = cursor.fetchall()
                conn.commit()
                price_dict = {row[0]: row[1] for row in results}

                # 计算总价
                missing_drugs = []  # 记录未找到的药品
                # 后续计算时，确保所有数值操作使用Decimal
                total = Decimal('0.0')  # 初始化Decimal类型的总价
                for drug, dosage in drug_dosages:
                    if drug in price_dict:
                        # 价格已经是Decimal（来自数据库），剂量也是Decimal
                        total += price_dict[drug] * dosage
                    else:
                        missing_drugs.append(drug)

                # 提示未找到的药品
                if missing_drugs:
                    QMessageBox.warning(
                        self,
                        "药品未找到",
                        f"以下药品未在数据库中找到：\n{', '.join(missing_drugs)}"
                    )

                # 计算总金额
                dose_num = Decimal(self.m_edtDosesNumber.text() or 0.0)
                total_drug_price = dose_num * total
                self.m_edtDosesPrice.setText(f"{total_drug_price:.2f}")
                dAcubPrice = Decimal(self.m_edtAcubPrice.text() or 0.0)
                self.calcTotalPrice()  # 调用新的总费用计算方法

        except pymysql.Error as e:
            QMessageBox.critical(self, "数据库错误", f"查询失败: {str(e)}")
        # except ValueError:
        #   QMessageBox.warning(self, "输入错误", "剂量次数必须为整数")
        except Exception as e:
            QMessageBox.critical(self, "未知错误", f"发生异常: {str(e)}")

        finally:
            conn.close()

    def calcTotalPrice(self):
        consultation_fee = self.get_consultation_fee()
        drug_price = Decimal(self.m_edtDosesPrice.text() or 0)
        acub_price = Decimal(self.m_edtAcubPrice.text() or 0)

        total = consultation_fee + drug_price + acub_price
        self.m_edtTotalPrice.setText(f"{total:.2f}")
        return total  # 返回计算结果用于保存

    def get_consultation_fee(self):
        try:
            if not self.current_user_id:
                QMessageBox.warning(self, "错误", "用户未登录")
                return Decimal(0)

            # 修改后的查询逻辑
            cf_data = self.m_databaseUtil.query_database_info(
                "SELECT 诊金 FROM 基本设置 WHERE user_id = %s",
                (self.current_user_id,)
            )

            # 正确处理查询结果
            if cf_data and cf_data[0] is not None:
                return Decimal(str(cf_data[0]))
            else:
                return Decimal(0)  # 明确返回0而非仅警告
        except Exception as e:
            print(f"获取诊金失败: {str(e)}")
            return Decimal(0)

    def on_cell_patientInfo_click(self, row, column):
        if row == 1 and column == 1:  # 性别单元格
            current_item = self.m_tle_PatientInfo.item(row, column)
            if current_item:
                current_value = current_item.text()
                new_value = "女" if current_value == "男" else "男"
                current_item.setText(new_value)
                # 立即提交数据变更
                self.m_tle_PatientInfo.itemChanged.emit(current_item)
        elif row == 4 and column == 1:
            self.create_diagnoses_combobox(row)
        elif row == 2 and column == 1:
            self.create_age_combobox(row)

    def on_row_basic_filter_click(self, item):
        """处理表格双击事件"""
        row = item.row()
        patient_id = self.m_tle_Basic_Filter.item(row, 0).text()

        data = self.m_databaseUtil.query_database_info(
            """SELECT 姓名,性别,年龄,病证,诊断, 血压,住址, 电话, 病历号, 身份证号 FROM 常规资料 WHERE 编号 = %s""", patient_id)
        self.display_patient_info(data)
        self.query_and_fill_data(patient_id)

    # 双击临床表现，将内容填充到m_edt_SympConcl控件中
    def on_row_ClinicalSymptom_double_click(self, item):
        """处理表格双击事件"""
        row = item.row()
        sympConclInfo = self.m_tle_ClinicalSymptom.item(row, 1).text()
        self.m_edt_SympConcl.append(sympConclInfo)

    def on_row_Diagnosis_click(self, item):
        """处理表格双击事件"""
        row = item.row()

        id = self.m_tle_Diagnosis.item(row, 0).text()
        data = self.m_databaseUtil.query_database_info("""SELECT 说明 FROM 辩证 WHERE 编号 = %s""", id)

        self.m_edt_DrugDiscrip.clear()
        for row, (value) in enumerate(data):
            # 添加字段名称（左列）
            self.m_edt_DrugDiscrip.append(value)

    def on_row_diagnosis_double_click(self, item):
        """处理表格双击事件"""
        row = item.row()
        diagnosisInfo = self.m_tle_Diagnosis.item(row, 1).text()
        self.m_edt_DiagConcl_2.append(diagnosisInfo)

    def display_patient_info(self, data):
        # 清空旧数据前断开所有信号
        self.m_tle_PatientInfo.clearContents()

        # 定义字段名称并初始化表头
        fields = [
            '姓名', '性别', '年龄', '病证', '诊断',
            '血压', '住址', '电话', '病历号', '身份证号'
        ]
        self.m_tle_PatientInfo.setRowCount(len(fields))
        self.m_tle_PatientInfo.setColumnCount(2)

        # 初始化所有单元格
        for row in range(len(fields)):
            # 字段名称列
            field_item = QTableWidgetItem(fields[row])
            field_item.setFlags(Qt.ItemIsEnabled)
            self.m_tle_PatientInfo.setItem(row, 0, field_item)

            # 值列（确保每个单元格都有QTableWidgetItem实例）
            value_item = QTableWidgetItem()
            value_item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsEditable)
            self.m_tle_PatientInfo.setItem(row, 1, value_item)

        # 如果有数据，填充数据
        if data:
            for row, value in enumerate(data):
                if row < self.m_tle_PatientInfo.rowCount():
                    self.m_tle_PatientInfo.item(row, 1).setText(str(value))

        # 调整列宽
        self.m_tle_PatientInfo.resizeColumnsToContents()
        self.m_tle_PatientInfo.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)

    def eventFilter(self, obj, event):
        # 处理 groupBox_3 的显示/隐藏事件，调整布局
        if obj == self.groupBox_3 and event.type() in (QEvent.Show, QEvent.Hide):
            self.adjust_splitter_sizes()
            return super().eventFilter(obj, event)

        # 处理焦点离开 QComboBox
        if isinstance(obj, QtWidgets.QComboBox) and event.type() == QEvent.FocusOut:
            row = self.parent_table.currentRow()
            column = self.parent_table.currentColumn()
            item = self.parent_table.item(row, column)
            if item:  # 根据具体情况处理
                self.close_sex_editor(item)  # 或 close_decoction_editor
            return True

        # 处理日期输入框的点击事件，弹出日历
        if event.type() == QEvent.MouseButtonRelease:
            if obj in [self.m_edt_searchfilter_DateStart, self.m_edt_searchfilter_DateEnd]:
                self.active_lineedit = obj  # 记录当前激活的输入框
                self.show_calendar_dialog()
                return True
        # 处理患者照片标签的双击事件，选择图片
        if event.type() == QEvent.MouseButtonDblClick:
            if obj == self.label_PatientPhoto:
                self.select_and_load_image()
                return True
        # 处理基础过滤表格的双击事件，加载数据
        if event.type() == QEvent.MouseButtonDblClick and obj == self.m_tle_Basic_Filter:
            # 获取当前选中行
            current_row = self.m_tle_Basic_Filter.currentRow()

            if current_row >= 0:
                # 获取编号
                item = self.m_tle_Basic_Filter.item(current_row, 0)
                self.m_tle_Basic_Filter.setCurrentItem(item)
                if item is not None:
                    number = item.text()
                    self.query_and_fill_data(number)
                return True  # 阻止默认滚动行为
        return super().eventFilter(obj, event)

    def query_and_fill_data(self, number):
        """查询数据库并填充控件"""
        try:
            # 执行SQL查询

            db_config = load_db_config()
            connection = pymysql.connect(**db_config)
            with connection.cursor() as cursor:
                query = """
                SELECT 病证,辨证,用法,针灸或其他,剂数,针灸次数,药费,针灸费用,总费用,
                       药物1,药物2,药物3,药物4,药物5,药物6,药物7,药物8,药物9,药物10,
                       药物11,药物12,药物13,药物14,药物15,药物16,药物17,药物18,药物19,药物20,
                       用量1,用量2,用量3,用量4,用量5,用量6,用量7,用量8,用量9,用量10,
                       用量11,用量12,用量13,用量14,用量15,用量16,用量17,用量18,用量19,用量20,
                       先煎后下1,先煎后下2,先煎后下3,先煎后下4,先煎后下5,先煎后下6,先煎后下7,先煎后下8,先煎后下9,先煎后下10,
                       先煎后下11,先煎后下12,先煎后下13,先煎后下14,先煎后下15,先煎后下16,先煎后下17,先煎后下18,先煎后下19,先煎后下20,
                       备注, 患者照片
                FROM 常规资料 WHERE 编号 = %s
                """
                cursor.execute(query, (number,))
                result = cursor.fetchall()
                connection.commit()

                if not result:
                    return

            row = result[0]  # 假设只处理查询结果的第一行

            # 填充QLineEdit控件，使用正确的字段索引
            self.m_edt_SympConcl.setText(row[0] or "")  # 病证是第一个字段
            self.m_edt_DiagConcl_2.setText(row[1] or "")  # 辨证是第二个字段
            index = self.m_cbUseage.findText(str(row[2] or ""), Qt.MatchExactly)
            if index != -1:
                self.m_cbUseage.setCurrentIndex(index)
            else:
                self.m_cbUseage.setCurrentIndex(0)

            self.m_edt_acup.setText(row[3] or "")  # 针灸或其他是第四个字段
            self.m_edtDosesNumber.setText(str(row[4] or "0"))  # 剂数是第五个字段
            self.m_edtAcubNumber.setText(str(row[5] or "0"))  # 针灸次数是第六个字段
            self.m_edtDosesPrice.setText(str(row[6] or "0"))  # 药费是第七个字段
            self.m_edtAcubPrice.setText(str(row[7] or "0"))  # 针灸费用是第八个字段
            self.m_edtTotalPrice.setText(str(row[8] or "0"))  # 总费用是第九个字段

            self.m_tbl_DrugUsage.setRowCount(20)
            self.m_tbl_DrugUsage.setColumnCount(4)

            nDrugRows = 0
            for i in range(20):
                drug = str(row[9 + i])  # 药物1~20（索引9到28）
                if row[9 + i] != None and row[9 + i] != "":
                    nDrugRows += 1

            self.m_tbl_DrugUsage.setRowCount(nDrugRows)

            for i in range(nDrugRows):
                drug = str(row[9 + i])  # 药物1~20（索引9到28）
                usage = row[29 + i]  # 用量1~20（索引29到48）
                decoction = row[49 + i]
                self.m_tbl_DrugUsage.setItem(i, 0, QtWidgets.QTableWidgetItem(number))
                # 设置药物和用量列
                self.m_tbl_DrugUsage.setItem(i, 1, QtWidgets.QTableWidgetItem(str(drug)))
                self.m_tbl_DrugUsage.setItem(i, 2, QtWidgets.QTableWidgetItem(str(usage)))
                self.m_tbl_DrugUsage.setItem(i, 3, QtWidgets.QTableWidgetItem(str(decoction)))
            # 隐藏编号列（此处原代码可能误写为m_lst_DrugUsage，应为m_tbl_DrugUsage）
            self.m_edt_Diagnote_4.setText(str(row[69] or " "))  # 备注
            self.m_tbl_DrugUsage.setColumnHidden(0, True)

            # 处理患者照片
            photo_path = row[70]  # 假设这是第70个字段
            if photo_path:
                try:
                    full_path = os.path.join(os.getcwd(), photo_path)
                    pixmap = QPixmap(full_path)
                    if not pixmap.isNull():
                        scaled_pixmap = pixmap.scaled(self.label_PatientPhoto.size(),
                                                      Qt.KeepAspectRatio,
                                                      Qt.SmoothTransformation)
                        self.label_PatientPhoto.setPixmap(scaled_pixmap)
                        self.current_image_path = photo_path  # 新增：设置当前图片路径
                    else:
                        self.label_PatientPhoto.clear()  # 图片为空时清除标签内容
                        self.current_image_path = None  # 加载失败时重置路径
                except Exception as e:
                    QMessageBox.warning(self, "图片加载失败", f"无法加载患者照片，请检查文件路径或文件是否损坏：{str(e)}")
                    self.label_PatientPhoto.clear()
                    self.current_image_path = None  # 加载失败时重置路径
            else:
                self.label_PatientPhoto.clear()
                self.current_image_path = None  # 无照片时设为None

        except pymysql.Error as e:
            QMessageBox.critical(self, '数据库错误', f'数据库操作失败: {str(e)}')
        finally:
            connection.close()

    def select_and_load_image(self):
        """选择并加载患者照片，保存到本地目录"""
        # 确保photos目录存在
        photo_dir = os.path.join(os.getcwd(), "photos")
        if not os.path.exists(photo_dir):
            os.makedirs(photo_dir)

        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(
            self,
            "选择患者照片",
            "",
            "图片文件 (*.png *.jpg *.jpeg *.bmp)",
            options=options
        )
        if file_name:
            try:
                # 获取当前患者的ID
                current_row = self.m_tle_Basic_Filter.currentRow()
                if current_row < 0:
                    QMessageBox.warning(self, "错误", "请先选择患者记录")
                    return

                patient_id_item = self.m_tle_Basic_Filter.item(current_row, 0)
                if not patient_id_item or not patient_id_item.text().strip():
                    QMessageBox.warning(self, "数据错误", "选中的记录编号无效")
                    return

                patient_id = patient_id_item.text()

                # 生成新的文件名
                new_filename = f"{patient_id}_photo_1.jpeg"
                save_path = os.path.join(photo_dir, new_filename)

                # 如果文件已存在，直接覆盖
                if os.path.exists(save_path):
                    os.remove(save_path)

                # 复制文件到目标目录
                shutil.copy(file_name, save_path)

                # 存储相对路径
                relative_path = os.path.join("photos", new_filename)
                self.current_image_path = relative_path

                # 显示图片
                pixmap = QPixmap(save_path)
                scaled_pixmap = pixmap.scaled(
                    self.label_PatientPhoto.size(),
                    Qt.KeepAspectRatio,
                    Qt.SmoothTransformation
                )
                self.label_PatientPhoto.setPixmap(scaled_pixmap)

            except Exception as e:
                QMessageBox.warning(self, "错误", f"图片保存失败: {str(e)}")
                self.current_image_path = None

    def show_calendar_dialog(self):
        dialog = QDialog(self)
        dialog.setWindowFlags(Qt.FramelessWindowHint | Qt.Popup)
        dialog.setAttribute(Qt.WA_DeleteOnClose)

        # 创建日历控件
        calendar = QCalendarWidget(dialog)
        calendar.setFixedSize(300, 200)
        layout = QVBoxLayout(dialog)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(calendar)

        # 设置初始日期
        current_date_str = self.active_lineedit.text()
        if current_date_str:
            current_date = QDate.fromString(current_date_str, "yyyy-MM-dd")
            if current_date.isValid():
                calendar.setSelectedDate(current_date)
        else:
            calendar.setSelectedDate(QDate.currentDate())

        # 定位对话框
        self.adjust_dialog_position(dialog, self.active_lineedit)

        # 连接日期选择信号
        calendar.clicked.connect(lambda date: self.update_date(date, dialog))
        dialog.exec()

    def adjust_dialog_position(self, dialog, target_widget):
        """智能定位对话框"""
        # 获取目标控件的位置
        target_pos = target_widget.mapToGlobal(QPoint(0, 0))
        dialog_size = dialog.sizeHint()
        screen_geo = QScreen.geometry(QApplication.primaryScreen())

        # 计算理想位置（优先显示在上方）
        x = target_pos.x()
        y = target_pos.y() - dialog_size.height()

        # 上方空间不足时显示在下方
        if y < screen_geo.top():
            y = target_pos.y() + target_widget.height()

        # 右侧边界检测
        if x + dialog_size.width() > screen_geo.right():
            x = screen_geo.right() - dialog_size.width()

        dialog.move(x, y)

    def update_date(self, date, dialog):
        self.active_lineedit.setText(date.toString("yyyy-MM-dd"))
        dialog.accept()

    def handle_drugselect_click(self):
        """ 处理搜索按钮点击事件 """
        drug_dialog = MyDrugSelectWindow(self)
        # 自定义窗口大小
        width = self.width() * 0.8
        height = width * 9 / 14
        drug_dialog.resize(width, height)
        drug_dialog.exec()

    def handle_search_click(self):
        """ 处理搜索按钮点击事件 """
        # 获取输入值
        start_str = self.m_edt_searchfilter_DateStart.text().strip()
        end_str = self.m_edt_searchfilter_DateEnd.text().strip()

        try:
            # 转换日期格式
            formatted_start = self.convert_to_datetime_str(start_str)
            formatted_end = self.convert_to_datetime_str(end_str, is_end=True)

            # 传递参数并触发数据加载
            self.load_basicinfo_data(formatted_start, formatted_end)

        except ValueError as e:
            QMessageBox.warning(self, "输入错误", str(e))

    def convert_to_datetime_str(self, input_str: str, is_end=False) -> str:
        """
        将输入字符串转换为标准日期时间格式
        :param input_str: 用户输入的日期字符串
        :param is_end: 是否为结束时间（自动补全23:59:59）
        :return: 格式化后的日期字符串
        """
        # 空值检查
        if not input_str:
            raise ValueError("日期不能为空")

        # 尝试解析不同格式
        for fmt in ("%Y-%m-%d %H:%M:%S", "%Y-%m-%d"):
            try:
                dt = datetime.strptime(input_str, fmt)
                # 自动补全时间
                if fmt == "%Y-%m-%d":
                    if is_end:
                        return dt.strftime("%Y-%m-%d 23:59:59")
                    else:
                        return dt.strftime("%Y-%m-%d 00:00:00")
                else:
                    return dt.strftime("%Y-%m-%d %H:%M:%S")
            except ValueError:
                continue

        raise ValueError("日期格式错误，请输入类似 '2023-10-01' 或 '2023-10-01 12:34:56'")

    # 处方设置
    def on_action_jingyanxuanfang_key(self):
        """基本设置菜单项点击事件"""
        print("经验选方设置设置被点击")

    def on_action_bianbingxuanfang_key(self):
        """处方设置菜单项点击事件"""
        print("辨病选方处方设置被点击")

    def load_basicinfo_data(self, keyword_first, keyword_second):
        """使用 PyMySQL 连接数据库并加载数据"""
        try:
            # 1. 连接数据库

            db_config = load_db_config()
            connection = pymysql.connect(**db_config)

            # 2. 执行查询
            self.m_tle_Basic_Filter.clearContents()  # 清空旧数据
            try:
                with connection.cursor() as cursor:
                    # 按照姓名检索

                    # 获取用户输入的日期（假设输入格式为 "YYYY-MM-DD"）
                    start_date = f"{keyword_first} 00:00:00"
                    end_date = f"{keyword_second} 23:59:59"

                    # 构建 SQL
                    sql = """
                    SELECT `编号`,`姓名`, `性别`, `年龄`, `诊断`, `日期时间`  # 新增诊断字段
                    FROM 常规资料 
                    WHERE 日期时间 BETWEEN %s AND %s
                    ORDER BY 编号 DESC
                    """
                    # 执行查询（注意参数格式）
                    cursor.execute(sql, (start_date, end_date))

                    results = cursor.fetchall()
                    connection.commit()

                    # 3. 初始化表格
                    self.m_tle_Basic_Filter.setColumnCount(6)
                    self.m_tle_Basic_Filter.setHorizontalHeaderLabels(['编号', '姓名', '性别', '年龄', '诊断', '日期时间'])  # 新增诊断列
                    self.m_tle_Basic_Filter.setRowCount(0)  # 清空旧数据

                    # 4. 填充数据
                    column_count = self.m_tle_Basic_Filter.columnCount()

                    total_width = self.m_tle_Basic_Filter.width()
                    ratios = [0, 1, 1, 1, 2, 3]  # 新增诊断列比例（编号0，姓名1，性别1，年龄1，诊断2，日期时间3）
                    total_ratio = sum(ratios)
                    current_widths = [int(total_width * ratio / total_ratio) for ratio in ratios]
                    for column, width in enumerate(current_widths):
                        self.m_tle_Basic_Filter.setColumnWidth(column, width)
                    self.m_tle_Basic_Filter.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed)
                    self.m_tle_Basic_Filter.setColumnHidden(0, True)
                    if not results:
                        # 插入一个空行
                        row_idx = 0
                        self.m_tle_Basic_Filter.insertRow(row_idx)
                        column_count = self.m_tle_Basic_Filter.columnCount()

                        for col_idx in range(column_count):
                            item = QTableWidgetItem(" ")
                            self.m_tle_Basic_Filter.setItem(row_idx, col_idx, item)

                    else:
                        # 正常插入数据
                        for row_idx, row_data in enumerate(results):
                            self.m_tle_Basic_Filter.insertRow(row_idx)
                            for col_idx, col_data in enumerate(row_data):
                                # 处理第五列诊断字段
                                if col_idx == 4:  # 诊断列索引
                                    item = QTableWidgetItem(str(col_data) if col_data is not None else "")
                                # 处理第六列日期时间字段
                                elif col_idx == 5 and col_data is not None:  # 日期时间列索引改为5
                                    item = QTableWidgetItem(col_data.strftime("%Y-%m-%d %H:%M:%S"))
                                else:
                                    item = QTableWidgetItem(str(col_data) if col_data is not None else "")
                                self.m_tle_Basic_Filter.setItem(row_idx, col_idx, item)
                    # 5. 自动调整列宽
                    self.m_tle_Basic_Filter.resizeColumnsToContents()
            except Exception as e:
                QMessageBox.warning(self, "查询错误", f"搜索失败: {str(e)}")
        except pymysql.Error as e:
            QMessageBox.critical(self, "数据库错误", f"数据库操作失败:\n{str(e)}")
        finally:
            # 6. 关闭连接
            connection.close()

    def load_druguse_data(self):
        """使用 PyMySQL 连接数据库并加载数据"""
        try:
            # 1. 连接数据库

            db_config = load_db_config()
            connection = pymysql.connect(**db_config)

            # 2. 执行查询
            self.m_cbUseage.clear()  # 清空旧数据
            try:
                with connection.cursor() as cursor:
                    # 构建 SQL
                    sql = """
                     SELECT `用法` FROM 用法 """
                    # 执行查询（注意参数格式）
                    cursor.execute(sql)

                    results = cursor.fetchall()
                    connection.commit()

                    if not results:
                        # 插入一个空行
                        return
                    else:
                        # 正常插入数据
                        for row_idx, row_data in enumerate(results):
                            self.m_cbUseage.insertItems(row_idx, row_data)

            except Exception as e:
                QMessageBox.warning(self, "查询错误", f"搜索失败: {str(e)}")
        except pymysql.Error as e:
            QMessageBox.critical(self, "数据库错误", f"数据库操作失败:\n{str(e)}")
        finally:
            connection.close()

    # 诊断相关方法
    def _get_all_diagnoses(self):
        return self._fetch_data("SELECT 诊断 FROM 诊断", cache_key='diagnoses')

    def _filter_diagnoses(self, table_widget, text):
        search_text = text.strip().lower()
        if not search_text:
            items = self._fetch_data("SELECT 诊断 FROM 诊断")
        else:
            items = self._fetch_data(
                "SELECT 诊断 FROM 诊断 WHERE 诊断拼音 LIKE %s",
                params=(f"{search_text}%",)
            )
        self._update_table_items(table_widget, items)

    # 年龄相关方法
    def _generate_age_data(self):
        months = [f"{i}个月" for i in range(1, 12)]
        ages = [f"{i}岁" for i in range(1, 151)]
        return months + ages

    def _generate_sex_data(self):
        sex = {"男", "女"}
        return sex

    def _filter_age(self, table_widget, text):
        search_text = text.strip()
        if not search_text:
            items = self._generate_age_data()
        else:
            items = [item for item in self._generate_age_data()
                     if re.match(f"^{search_text}", item)]
        self._update_table_items(table_widget, items)

    # 煎法相关方法
    def _get_decoction_methods(self):
        return self._fetch_data("SELECT 煎法 FROM 用法", cache_key='decoction')

    # 通用数据库方法
    def _fetch_data(self, query, params=None, cache_key=None):
        """通用数据库查询方法"""
        if cache_key and hasattr(self, f'_cached_{cache_key}'):
            return getattr(self, f'_cached_{cache_key}')

        try:
            # 从专用配置文件加载数据库配置（Database_connection.py）
            db_config = load_db_config()
            # 添加cursorclass配置
            db_config['cursorclass'] = DictCursor

            # 使用动态加载的配置连接数据库
            with pymysql.connect(**db_config) as conn:
                with conn.cursor() as cursor:
                    cursor.execute(query, params or ())
                    results = cursor.fetchall()
                    data = [result[list(result.keys())[0]] for result in results]

                    if cache_key:
                        setattr(self, f'_cached_{cache_key}', data)
                    return data
        except Exception as e:
            print(f"Database error: {e}")
            return []

    def _update_table_items(self, table_widget, items):
        """更新表格项"""
        table_widget.setRowCount(0)
        for text in items or ["未找到匹配项"]:
            row = table_widget.rowCount()
            table_widget.insertRow(row)
            table_widget.setItem(row, 0, QTableWidgetItem(text))

    def create_diagnoses_combobox(self, row):
        if self.m_tle_PatientInfo.cellWidget(1, 1):
            self.m_tle_PatientInfo.removeCellWidget(1, 1)
        mySearchableComboBox(
            self.m_tle_PatientInfo,
            self.diagnosis_combo_config
        ).create(row)

    def create_age_combobox(self, row):
        if self.m_tle_PatientInfo.cellWidget(1, 1):
            self.m_tle_PatientInfo.removeCellWidget(1, 1)
        mySearchableComboBox(
            self.m_tle_PatientInfo,
            self.age_combo_config
        ).create(row)


    def handle_sex_selection(self, row, combo):
        """处理性别选择"""
        selected = combo.currentText()
        self.m_tle_PatientInfo.setItem(row, 1, QTableWidgetItem(selected))
        self.m_tle_PatientInfo.removeCellWidget(row, 1)  # 移除下拉框

    def close_sex_editor(self, item):
        """安全关闭性别单元格编辑器"""
        try:
            if item is None or not hasattr(item, "text"):
                return

            # 强制关闭编辑器（即使已经关闭也不会报错）
            if self.m_tle_PatientInfo.isPersistentEditorOpen(item):
                self.m_tle_PatientInfo.closePersistentEditor(item)

            # 清除焦点
            self.m_tle_PatientInfo.clearFocus()
        except RuntimeError as e:
            if "Internal C++ object" not in str(e):
                raise e

    def create_decoction_combobox(self, row):
        """创建煎法下拉框并连接信号"""
        combo = mySearchableComboBox(
            self.m_tbl_DrugUsage,
            self.decoction_combo_config
        )
        combo.create(row)

        # 获取当前单元格项和下拉框控件
        current_item = self.m_tbl_DrugUsage.item(row, 3)
        decoction_combobox = self.m_tbl_DrugUsage.cellWidget(row, 3)

        # 连接信号：当下拉框选项被选中时更新单元格
        if decoction_combobox:
            decoction_combobox.activated.connect(
                lambda index, r=row: self.update_decoction_cell(r))

    def update_decoction_cell(self, row):
        """更新煎法单元格内容"""
        combo = self.m_tbl_DrugUsage.cellWidget(row, 3)
        if combo:
            selected_text = combo.currentText()  # 获取选中的文本
            self.m_tbl_DrugUsage.setItem(row, 3, QTableWidgetItem(selected_text))  # 更新单元格
            self.m_tbl_DrugUsage.removeCellWidget(row, 3)  # 移除下拉框

    def handle_preview_click(self):
        """处理预览按钮点击事件"""
        current_row = self.m_tle_Basic_Filter.currentRow()
        if current_row < 0:
            QMessageBox.warning(self, "操作错误", "请先选择患者记录")
            return

        patient_id_item = self.m_tle_Basic_Filter.item(current_row, 0)
        if not patient_id_item or not patient_id_item.text().strip():
            QMessageBox.warning(self, "数据错误", "选中的记录编号无效")
            return

        patient_id = patient_id_item.text()

        try:
            # 使用修改后的预览生成器
            from preview import PreviewGenerator
            generator = PreviewGenerator(patient_id, self.current_user_id)
            pdf_data = generator.generate().getvalue()

            # 显示预览
            from PdfViewerDialog import PdfViewerDialog
            viewer = PdfViewerDialog(pdf_data, self)
            viewer.exec()
        except Exception as e:
            QMessageBox.critical(self, "错误", f"生成预览失败: {str(e)}")

    def close_decoction_editor(self, item):
        """安全关闭煎法单元格编辑器"""
        try:
            if item is None:
                return

            # 获取单元格的行列索引
            row = item.row()
            col = item.column()

            # 如果是煎法列且有下拉框控件，则更新单元格
            if col == 3 and self.m_tbl_DrugUsage.cellWidget(row, col):
                self.update_decoction_cell(row)

        except RuntimeError as e:
            if "Internal C++ object" not in str(e):
                raise e

    def on_cell_decoction_clicked(self, row, column):
        if column == 3:  # 第3列（索引从0开始）
            self.create_decoction_combobox(row)