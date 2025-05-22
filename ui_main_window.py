# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.1.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1170, 815)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(800, 600))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        MainWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u":/Resources/icons/logo.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        self.on_action_jingyanxuanfang = QAction(MainWindow)
        self.on_action_jingyanxuanfang.setObjectName(u"on_action_jingyanxuanfang")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(False)
        self.on_action_jingyanxuanfang.setFont(font1)
        self.on_action_bianbingxuanfang = QAction(MainWindow)
        self.on_action_bianbingxuanfang.setObjectName(u"on_action_bianbingxuanfang")
        font2 = QFont()
        font2.setPointSize(12)
        self.on_action_bianbingxuanfang.setFont(font2)
        self.on_action_fangjixuanfang = QAction(MainWindow)
        self.on_action_fangjixuanfang.setObjectName(u"on_action_fangjixuanfang")
        self.on_action_fangjixuanfang.setFont(font2)
        self.on_action_DrugSetting = QAction(MainWindow)
        self.on_action_DrugSetting.setObjectName(u"on_action_DrugSetting")
        self.on_action_DrugSetting.setFont(font2)
        self.on_action_usage = QAction(MainWindow)
        self.on_action_usage.setObjectName(u"on_action_usage")
        self.on_action_usage.setFont(font2)
        self.on_action_DrugList = QAction(MainWindow)
        self.on_action_DrugList.setObjectName(u"on_action_DrugList")
        self.on_action_DrugList.setFont(font2)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_9 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.Sidebar = QWidget(self.splitter)
        self.Sidebar.setObjectName(u"Sidebar")
        self.Sidebar.setMinimumSize(QSize(100, 0))
        self.Sidebar.setMaximumSize(QSize(100, 16777215))
        self.Sidebar.setStyleSheet(u"    QWidget {\n"
"        background-color: rgb(5, 117, 230); /* \u53ea\u8bbe\u7f6e\u80cc\u666f\u8272 */\n"
"        border:1px solid rgb(190, 190, 190);   /*\u8fb9\u6846\u7684\u7c97\u7ec6\uff0c\u989c\u8272*/\n"
"        border-radius:10px;    /*\u8bbe\u7f6e\u5706\u89d2\u534a\u5f84 */\n"
"    }")
        self.verticalLayout_4 = QVBoxLayout(self.Sidebar)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalSpacer_9 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_9)

        self.m_bt_menu_Userinfor = QPushButton(self.Sidebar)
        self.m_bt_menu_Userinfor.setObjectName(u"m_bt_menu_Userinfor")
        self.m_bt_menu_Userinfor.setFont(font)
        self.m_bt_menu_Userinfor.setStyleSheet(u"QPushButton{\n"
"letter-spacing: 1px;\n"
"font-size:12pt;\n"
"border: none;\n"
"color:white;\n"
"border-radius:5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color:rgba(54, 164, 225,100);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(149, 227, 132, 152);\n"
"border-top:5px;\n"
"border-left:5px;\n"
"border-radius:5px;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/Resources/icons/icon_add_user.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.m_bt_menu_Userinfor.setIcon(icon1)
        self.m_bt_menu_Userinfor.setIconSize(QSize(30, 30))

        self.verticalLayout_4.addWidget(self.m_bt_menu_Userinfor)

        self.verticalSpacer = QSpacerItem(20, 3, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.m_bt_menu_Patients = QPushButton(self.Sidebar)
        self.m_bt_menu_Patients.setObjectName(u"m_bt_menu_Patients")
        self.m_bt_menu_Patients.setFont(font)
        self.m_bt_menu_Patients.setStyleSheet(u"QPushButton{\n"
"letter-spacing: 1px;\n"
"font-size:12pt;\n"
"border: none;\n"
"color:white;\n"
"border-radius:5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color:rgba(54, 164, 225,100);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(149, 227, 132, 152);\n"
"border-top:5px;\n"
"border-left:5px;\n"
"border-radius:5px;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/Resources/icons/icon_patient.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.m_bt_menu_Patients.setIcon(icon2)
        self.m_bt_menu_Patients.setIconSize(QSize(30, 30))

        self.verticalLayout_4.addWidget(self.m_bt_menu_Patients)

        self.verticalSpacer_2 = QSpacerItem(20, 3, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.m_bt_menu_symptoms = QPushButton(self.Sidebar)
        self.m_bt_menu_symptoms.setObjectName(u"m_bt_menu_symptoms")
        self.m_bt_menu_symptoms.setFont(font)
        self.m_bt_menu_symptoms.setStyleSheet(u"QPushButton{\n"
"letter-spacing: 1px;\n"
"font-size:12pt;\n"
"border: none;\n"
"color:white;\n"
"border-radius:5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color:rgba(54, 164, 225,100);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(149, 227, 132, 152);\n"
"border-top:5px;\n"
"border-left:5px;\n"
"border-radius:5px;\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/Resources/icons/icon_diseases.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.m_bt_menu_symptoms.setIcon(icon3)
        self.m_bt_menu_symptoms.setIconSize(QSize(30, 30))

        self.verticalLayout_4.addWidget(self.m_bt_menu_symptoms)

        self.verticalSpacer_3 = QSpacerItem(20, 3, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_3)

        self.m_bt_menu_Anylasis = QPushButton(self.Sidebar)
        self.m_bt_menu_Anylasis.setObjectName(u"m_bt_menu_Anylasis")
        self.m_bt_menu_Anylasis.setFont(font)
        self.m_bt_menu_Anylasis.setStyleSheet(u"QPushButton{\n"
"letter-spacing: 1px;\n"
"font-size:12pt;\n"
"border: none;\n"
"color:white;\n"
"border-radius:5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color:rgba(54, 164, 225,100);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(149, 227, 132, 152);\n"
"border-top:5px;\n"
"border-left:5px;\n"
"border-radius:5px;\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/Resources/icons/icon_analysis.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.m_bt_menu_Anylasis.setIcon(icon4)
        self.m_bt_menu_Anylasis.setIconSize(QSize(30, 30))

        self.verticalLayout_4.addWidget(self.m_bt_menu_Anylasis)

        self.verticalSpacer_4 = QSpacerItem(20, 3, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_4)

        self.m_bt_menu_Diagnosis = QPushButton(self.Sidebar)
        self.m_bt_menu_Diagnosis.setObjectName(u"m_bt_menu_Diagnosis")
        self.m_bt_menu_Diagnosis.setFont(font)
        self.m_bt_menu_Diagnosis.setStyleSheet(u"QPushButton{\n"
"letter-spacing: 1px;\n"
"font-size:12pt;\n"
"border: none;\n"
"color:white;\n"
"border-radius:5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color:rgba(54, 164, 225,100);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(149, 227, 132, 152);\n"
"border-top:5px;\n"
"border-left:5px;\n"
"border-radius:5px;\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/Resources/icons/icon_diagnosis.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.m_bt_menu_Diagnosis.setIcon(icon5)
        self.m_bt_menu_Diagnosis.setIconSize(QSize(30, 30))

        self.verticalLayout_4.addWidget(self.m_bt_menu_Diagnosis)

        self.verticalSpacer_5 = QSpacerItem(20, 3, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_5)

        self.m_bt_menu_Acup = QPushButton(self.Sidebar)
        self.m_bt_menu_Acup.setObjectName(u"m_bt_menu_Acup")
        self.m_bt_menu_Acup.setFont(font)
        self.m_bt_menu_Acup.setStyleSheet(u"QPushButton{\n"
"letter-spacing: 1px;\n"
"font-size:12pt;\n"
"border: none;\n"
"color:white;\n"
"border-radius:5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color:rgba(54, 164, 225,100);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(149, 227, 132, 152);\n"
"border-top:5px;\n"
"border-left:5px;\n"
"border-radius:5px;\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u":/Resources/icons/icon_acup.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.m_bt_menu_Acup.setIcon(icon6)
        self.m_bt_menu_Acup.setIconSize(QSize(30, 30))

        self.verticalLayout_4.addWidget(self.m_bt_menu_Acup)

        self.verticalSpacer_6 = QSpacerItem(20, 3, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_6)

        self.m_bt_menu_Formulas = QPushButton(self.Sidebar)
        self.m_bt_menu_Formulas.setObjectName(u"m_bt_menu_Formulas")
        self.m_bt_menu_Formulas.setFont(font)
        self.m_bt_menu_Formulas.setStyleSheet(u"QPushButton{\n"
"letter-spacing: 1px;\n"
"font-size:12pt;\n"
"border: none;\n"
"color:white;\n"
"border-radius:5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color:rgba(54, 164, 225,100);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(149, 227, 132, 152);\n"
"border-top:5px;\n"
"border-left:5px;\n"
"border-radius:5px;\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u":/Resources/icons/icon_pres.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.m_bt_menu_Formulas.setIcon(icon7)
        self.m_bt_menu_Formulas.setIconSize(QSize(30, 30))

        self.verticalLayout_4.addWidget(self.m_bt_menu_Formulas)

        self.verticalSpacer_7 = QSpacerItem(20, 3, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_7)

        self.m_bt_menu_DrugList = QPushButton(self.Sidebar)
        self.m_bt_menu_DrugList.setObjectName(u"m_bt_menu_DrugList")
        self.m_bt_menu_DrugList.setFont(font)
        self.m_bt_menu_DrugList.setStyleSheet(u"QPushButton{\n"
"letter-spacing: 1px;\n"
"font-size:12pt;\n"
"border: none;\n"
"color:white;\n"
"border-radius:5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color:rgba(54, 164, 225,100);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(149, 227, 132, 152);\n"
"border-top:5px;\n"
"border-left:5px;\n"
"border-radius:5px;\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u":/Resources/icons/icon_druglist.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.m_bt_menu_DrugList.setIcon(icon8)
        self.m_bt_menu_DrugList.setIconSize(QSize(30, 30))

        self.verticalLayout_4.addWidget(self.m_bt_menu_DrugList)

        self.verticalSpacer_8 = QSpacerItem(20, 3, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_8)

        self.m_bt_menu_DrugUsage = QPushButton(self.Sidebar)
        self.m_bt_menu_DrugUsage.setObjectName(u"m_bt_menu_DrugUsage")
        self.m_bt_menu_DrugUsage.setFont(font)
        self.m_bt_menu_DrugUsage.setStyleSheet(u"QPushButton{\n"
"letter-spacing: 1px;\n"
"font-size:12pt;\n"
"border: none;\n"
"color:white;\n"
"border-radius:5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color:rgba(54, 164, 225,100);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(149, 227, 132, 152);\n"
"border-top:5px;\n"
"border-left:5px;\n"
"border-radius:5px;\n"
"}")
        icon9 = QIcon()
        icon9.addFile(u":/Resources/icons/icon_usage.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.m_bt_menu_DrugUsage.setIcon(icon9)
        self.m_bt_menu_DrugUsage.setIconSize(QSize(30, 30))

        self.verticalLayout_4.addWidget(self.m_bt_menu_DrugUsage)

        self.verticalSpacer_10 = QSpacerItem(20, 3, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_10)

        self.m_bt_menu_MedicalRec = QPushButton(self.Sidebar)
        self.m_bt_menu_MedicalRec.setObjectName(u"m_bt_menu_MedicalRec")
        self.m_bt_menu_MedicalRec.setFont(font)
        self.m_bt_menu_MedicalRec.setStyleSheet(u"QPushButton{\n"
"letter-spacing: 1px;\n"
"font-size:12pt;\n"
"border: none;\n"
"color:white;\n"
"border-radius:5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color:rgba(54, 164, 225,100);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(149, 227, 132, 152);\n"
"border-top:5px;\n"
"border-left:5px;\n"
"border-radius:5px;\n"
"}")
        icon10 = QIcon()
        icon10.addFile(u":/Resources/icons/icon_record.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.m_bt_menu_MedicalRec.setIcon(icon10)
        self.m_bt_menu_MedicalRec.setIconSize(QSize(30, 30))

        self.verticalLayout_4.addWidget(self.m_bt_menu_MedicalRec)

        self.verticalSpacer_11 = QSpacerItem(20, 250, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_11)

        self.sutra_image = QPushButton(self.Sidebar)
        self.sutra_image.setObjectName(u"sutra_image")
        font3 = QFont()
        font3.setPointSize(11)
        font3.setBold(True)
        self.sutra_image.setFont(font3)
        self.sutra_image.setStyleSheet(u"QPushButton{\n"
"font-size:11pt;\n"
"border: none;\n"
"color:white;\n"
"}")
        icon11 = QIcon()
        icon11.addFile(u":/Resources/icons/icon_sutra.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.sutra_image.setIcon(icon11)
        self.sutra_image.setIconSize(QSize(110, 110))

        self.verticalLayout_4.addWidget(self.sutra_image)

        self.m_bt_About = QPushButton(self.Sidebar)
        self.m_bt_About.setObjectName(u"m_bt_About")
        self.m_bt_About.setFont(font)
        self.m_bt_About.setStyleSheet(u"QPushButton{\n"
"font-size:12pt;\n"
"border: none;\n"
"color:white;\n"
"border-radius:5px;\n"
"}")
        icon12 = QIcon()
        icon12.addFile(u":/Resources/icons/icon_settings.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.m_bt_About.setIcon(icon12)
        self.m_bt_About.setIconSize(QSize(100, 85))

        self.verticalLayout_4.addWidget(self.m_bt_About)

        self.verticalSpacer_12 = QSpacerItem(20, 19, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_12)

        self.splitter.addWidget(self.Sidebar)
        self.groupBox_1 = QGroupBox(self.splitter)
        self.groupBox_1.setObjectName(u"groupBox_1")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupBox_1.sizePolicy().hasHeightForWidth())
        self.groupBox_1.setSizePolicy(sizePolicy1)
        self.groupBox_1.setFont(font)
        self.groupBox_1.setStyleSheet(u"    QGroupBox {\n"
"        background-color: rgba(169,208,107,155); /* \u53ea\u8bbe\u7f6e\u80cc\u666f\u8272 */\n"
"        border:1px solid rgb(190, 190, 190);   /*\u8fb9\u6846\u7684\u7c97\u7ec6\uff0c\u989c\u8272*/\n"
"        border-radius:10px;    /*\u8bbe\u7f6e\u5706\u89d2\u534a\u5f84 */\n"
"    }\n"
"\n"
"\n"
"    /* \u786e\u4fdd\u5b50\u63a7\u4ef6\u7684\u5b57\u4f53\u5927\u5c0f\u548c\u7c97\u7ec6\u4e0d\u53d7\u5f71\u54cd */\n"
"    QGroupBox QWidget {\n"
"        font-size: 12pt; /* \u8bbe\u7f6e\u5b50\u63a7\u4ef6\u7684\u5b57\u4f53\u5927\u5c0f */\n"
"        font-weight: bold; /* \u8bbe\u7f6e\u5b50\u63a7\u4ef6\u7684\u5b57\u4f53\u7c97\u7ec6 */\n"
"    }")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.bt_title_3 = QPushButton(self.groupBox_1)
        self.bt_title_3.setObjectName(u"bt_title_3")
        self.bt_title_3.setFont(font3)
        self.bt_title_3.setStyleSheet(u"QPushButton{\n"
"font-size:11pt;\n"
"border: none;\n"
"color:white;\n"
"}")
        icon13 = QIcon()
        icon13.addFile(u":/Resources/icons/icon_info_grey.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_title_3.setIcon(icon13)
        self.bt_title_3.setIconSize(QSize(25, 25))

        self.horizontalLayout_17.addWidget(self.bt_title_3)

        self.label_19 = QLabel(self.groupBox_1)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font)
        self.label_19.setStyleSheet(u"QLabel{\n"
"letter-spacing: 3px;\n"
"}")
        self.label_19.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_17.addWidget(self.label_19)

        self.horizontalSpacer_13 = QSpacerItem(72, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_13)


        self.verticalLayout_2.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_PatientPhoto = QLabel(self.groupBox_1)
        self.label_PatientPhoto.setObjectName(u"label_PatientPhoto")
        self.label_PatientPhoto.setMinimumSize(QSize(120, 150))
        self.label_PatientPhoto.setMaximumSize(QSize(120, 150))
        self.label_PatientPhoto.setStyleSheet(u"QLabel{\n"
"background-color: rgba(255, 255, 255,120);\n"
"border:2px solid rgb(190, 190, 190); \n"
"} ")

        self.horizontalLayout_21.addWidget(self.label_PatientPhoto)

        self.m_tle_PatientInfo = QTableWidget(self.groupBox_1)
        if (self.m_tle_PatientInfo.columnCount() < 11):
            self.m_tle_PatientInfo.setColumnCount(11)
        __qtablewidgetitem = QTableWidgetItem()
        self.m_tle_PatientInfo.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.m_tle_PatientInfo.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.m_tle_PatientInfo.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.m_tle_PatientInfo.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.m_tle_PatientInfo.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.m_tle_PatientInfo.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.m_tle_PatientInfo.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.m_tle_PatientInfo.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.m_tle_PatientInfo.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.m_tle_PatientInfo.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.m_tle_PatientInfo.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        self.m_tle_PatientInfo.setObjectName(u"m_tle_PatientInfo")
        self.m_tle_PatientInfo.setMaximumSize(QSize(16777215, 150))
        self.m_tle_PatientInfo.setFont(font)
        self.m_tle_PatientInfo.setStyleSheet(u"background-color:rgba(248, 248, 248, 220);")

        self.horizontalLayout_21.addWidget(self.m_tle_PatientInfo)


        self.verticalLayout_2.addLayout(self.horizontalLayout_21)

        self.line_10 = QFrame(self.groupBox_1)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setFrameShape(QFrame.HLine)
        self.line_10.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line_10)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.bt_title_4 = QPushButton(self.groupBox_1)
        self.bt_title_4.setObjectName(u"bt_title_4")
        self.bt_title_4.setFont(font3)
        self.bt_title_4.setStyleSheet(u"QPushButton{\n"
"font-size:11pt;\n"
"border: none;\n"
"color:white;\n"
"}")
        icon14 = QIcon()
        icon14.addFile(u":/Resources/icons/icon_acup_grey.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_title_4.setIcon(icon14)
        self.bt_title_4.setIconSize(QSize(25, 25))

        self.horizontalLayout_23.addWidget(self.bt_title_4)

        self.label_20 = QLabel(self.groupBox_1)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font)
        self.label_20.setStyleSheet(u"QLabel{\n"
"letter-spacing: 1px;\n"
"}")
        self.label_20.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_23.addWidget(self.label_20)

        self.horizontalSpacer_17 = QSpacerItem(72, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_17)


        self.verticalLayout_2.addLayout(self.horizontalLayout_23)

        self.m_edt_acup = QTextEdit(self.groupBox_1)
        self.m_edt_acup.setObjectName(u"m_edt_acup")
        self.m_edt_acup.setMaximumSize(QSize(16777215, 150))
        self.m_edt_acup.setStyleSheet(u"QTextEdit{\n"
"background-color:rgba(248, 248, 248, 220);\n"
"} ")

        self.verticalLayout_2.addWidget(self.m_edt_acup)

        self.line_7 = QFrame(self.groupBox_1)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.HLine)
        self.line_7.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line_7)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.bt_title_5 = QPushButton(self.groupBox_1)
        self.bt_title_5.setObjectName(u"bt_title_5")
        self.bt_title_5.setFont(font3)
        self.bt_title_5.setStyleSheet(u"QPushButton{\n"
"font-size:11pt;\n"
"border: none;\n"
"color:white;\n"
"}")
        icon15 = QIcon()
        icon15.addFile(u":/Resources/icons/icon_druglist_grey.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_title_5.setIcon(icon15)
        self.bt_title_5.setIconSize(QSize(25, 25))

        self.horizontalLayout_24.addWidget(self.bt_title_5)

        self.label_22 = QLabel(self.groupBox_1)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font)
        self.label_22.setStyleSheet(u"QLabel{\n"
"letter-spacing: 3px;\n"
"}")
        self.label_22.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_24.addWidget(self.label_22)

        self.horizontalSpacer_19 = QSpacerItem(72, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_19)


        self.verticalLayout_2.addLayout(self.horizontalLayout_24)

        self.m_tbl_DrugUsage = QTableWidget(self.groupBox_1)
        if (self.m_tbl_DrugUsage.columnCount() < 4):
            self.m_tbl_DrugUsage.setColumnCount(4)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.m_tbl_DrugUsage.setHorizontalHeaderItem(0, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.m_tbl_DrugUsage.setHorizontalHeaderItem(1, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.m_tbl_DrugUsage.setHorizontalHeaderItem(2, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.m_tbl_DrugUsage.setHorizontalHeaderItem(3, __qtablewidgetitem14)
        self.m_tbl_DrugUsage.setObjectName(u"m_tbl_DrugUsage")
        self.m_tbl_DrugUsage.setFont(font)
        self.m_tbl_DrugUsage.setStyleSheet(u"QTableWidget{\n"
"background-color:rgba(248, 248, 248, 220);\n"
"} ")
        self.m_tbl_DrugUsage.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_2.addWidget(self.m_tbl_DrugUsage)

        self.line_12 = QFrame(self.groupBox_1)
        self.line_12.setObjectName(u"line_12")
        self.line_12.setFrameShape(QFrame.HLine)
        self.line_12.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line_12)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_9 = QLabel(self.groupBox_1)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_3.addWidget(self.label_9)


        self.horizontalLayout_10.addLayout(self.verticalLayout_3)

        self.m_cbUseage = QComboBox(self.groupBox_1)
        self.m_cbUseage.setObjectName(u"m_cbUseage")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.m_cbUseage.sizePolicy().hasHeightForWidth())
        self.m_cbUseage.setSizePolicy(sizePolicy2)
        self.m_cbUseage.setMaximumSize(QSize(16777215, 35))

        self.horizontalLayout_10.addWidget(self.m_cbUseage)


        self.verticalLayout_2.addLayout(self.horizontalLayout_10)

        self.line_8 = QFrame(self.groupBox_1)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShape(QFrame.HLine)
        self.line_8.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line_8)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.bt_title_6 = QPushButton(self.groupBox_1)
        self.bt_title_6.setObjectName(u"bt_title_6")
        self.bt_title_6.setFont(font3)
        self.bt_title_6.setStyleSheet(u"QPushButton{\n"
"font-size:11pt;\n"
"border: none;\n"
"color:white;\n"
"}")
        icon16 = QIcon()
        icon16.addFile(u":/Resources/icons/icon_note_grey.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_title_6.setIcon(icon16)
        self.bt_title_6.setIconSize(QSize(25, 25))

        self.horizontalLayout_16.addWidget(self.bt_title_6)

        self.label_12 = QLabel(self.groupBox_1)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setStyleSheet(u"QLabel{\n"
"letter-spacing: 3px;\n"
"}")

        self.horizontalLayout_16.addWidget(self.label_12)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_8)


        self.verticalLayout_2.addLayout(self.horizontalLayout_16)

        self.m_edt_Diagnote_4 = QTextEdit(self.groupBox_1)
        self.m_edt_Diagnote_4.setObjectName(u"m_edt_Diagnote_4")
        self.m_edt_Diagnote_4.setMaximumSize(QSize(16777215, 80))
        self.m_edt_Diagnote_4.setFont(font)
        self.m_edt_Diagnote_4.setStyleSheet(u"QTextEdit{\n"
"background-color:rgba(248, 248, 248, 220);\n"
"} ")

        self.verticalLayout_2.addWidget(self.m_edt_Diagnote_4)

        self.splitter.addWidget(self.groupBox_1)
        self.groupBox_2 = QGroupBox(self.splitter)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy3 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy3)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setStyleSheet(u"    QGroupBox {\n"
"        background-color: rgba(169,208,107,155); /* \u53ea\u8bbe\u7f6e\u80cc\u666f\u8272 */\n"
"        border:1px solid rgb(190, 190, 190);   /*\u8fb9\u6846\u7684\u7c97\u7ec6\uff0c\u989c\u8272*/\n"
"        border-radius:10px;    /*\u8bbe\u7f6e\u5706\u89d2\u534a\u5f84 */\n"
"    }\n"
"\n"
"\n"
"    /* \u786e\u4fdd\u5b50\u63a7\u4ef6\u7684\u5b57\u4f53\u5927\u5c0f\u548c\u7c97\u7ec6\u4e0d\u53d7\u5f71\u54cd */\n"
"    QGroupBox QWidget {\n"
"        font-size: 12pt; /* \u8bbe\u7f6e\u5b50\u63a7\u4ef6\u7684\u5b57\u4f53\u5927\u5c0f */\n"
"        font-weight: bold; /* \u8bbe\u7f6e\u5b50\u63a7\u4ef6\u7684\u5b57\u4f53\u7c97\u7ec6 */\n"
"    }")
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.bt_title = QPushButton(self.groupBox_2)
        self.bt_title.setObjectName(u"bt_title")
        self.bt_title.setFont(font3)
        self.bt_title.setStyleSheet(u"QPushButton{\n"
"font-size:11pt;\n"
"border: none;\n"
"color:white;\n"
"}")
        icon17 = QIcon()
        icon17.addFile(u":/Resources/icons/icon_diseases_grey.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_title.setIcon(icon17)
        self.bt_title.setIconSize(QSize(25, 25))

        self.horizontalLayout_14.addWidget(self.bt_title)

        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"QLabel{\n"
"letter-spacing: 3px;\n"
"}")

        self.horizontalLayout_14.addWidget(self.label_4)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_3)


        self.verticalLayout_5.addLayout(self.horizontalLayout_14)

        self.m_edt_SympConcl = QTextEdit(self.groupBox_2)
        self.m_edt_SympConcl.setObjectName(u"m_edt_SympConcl")
        self.m_edt_SympConcl.setStyleSheet(u"QTextEdit{\n"
"background-color:rgba(248, 248, 248, 220);\n"
"} ")

        self.verticalLayout_5.addWidget(self.m_edt_SympConcl)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.bt_title_2 = QPushButton(self.groupBox_2)
        self.bt_title_2.setObjectName(u"bt_title_2")
        self.bt_title_2.setFont(font3)
        self.bt_title_2.setStyleSheet(u"QPushButton{\n"
"font-size:11pt;\n"
"border: none;\n"
"color:white;\n"
"}")
        icon18 = QIcon()
        icon18.addFile(u":/Resources/icons/icon_analysis_grey.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_title_2.setIcon(icon18)
        self.bt_title_2.setIconSize(QSize(25, 25))

        self.horizontalLayout_15.addWidget(self.bt_title_2)

        self.label_5 = QLabel(self.groupBox_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"QLabel{\n"
"letter-spacing: 3px;\n"
"}")

        self.horizontalLayout_15.addWidget(self.label_5)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_5)


        self.verticalLayout_5.addLayout(self.horizontalLayout_15)

        self.m_edt_DiagConcl_2 = QTextEdit(self.groupBox_2)
        self.m_edt_DiagConcl_2.setObjectName(u"m_edt_DiagConcl_2")
        self.m_edt_DiagConcl_2.setMaximumSize(QSize(16777215, 150))
        self.m_edt_DiagConcl_2.setFont(font)
        self.m_edt_DiagConcl_2.setStyleSheet(u"QTextEdit{\n"
"background-color:rgba(248, 248, 248, 220);\n"
"} ")

        self.verticalLayout_5.addWidget(self.m_edt_DiagConcl_2)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.m_bt_DrugSelect_3 = QPushButton(self.groupBox_2)
        self.m_bt_DrugSelect_3.setObjectName(u"m_bt_DrugSelect_3")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.m_bt_DrugSelect_3.sizePolicy().hasHeightForWidth())
        self.m_bt_DrugSelect_3.setSizePolicy(sizePolicy4)
        self.m_bt_DrugSelect_3.setStyleSheet(u"QPushButton {\n"
"                /* \u57fa\u7840\u53c2\u6570 */\n"
"				letter-spacing: 2px;\n"
"                border-radius: 3px;\n"
"                border: 1px solid rgba(140, 170, 30, 0.78);\n"
"                padding: 3px 12px;\n"
"                color: black;\n"
"\n"
"                /* \u4e3b\u6e10\u53d8 (\u767d \u2192 \u7070 \u2192 \u6df1\u7070) */\n"
"                background: qlineargradient(\n"
"                    x1:0, y1:0, x2:0, y2:1,\n"
"                    stop:0 rgba(249, 249, 249,255),\n"
"                    stop:0.5 rgba(220, 220, 220,255),\n"
"                    stop:1 rgba(150, 150, 150,0.9)\n"
"                );\n"
"\n"
"                /* \u5916\u90e8\u9634\u5f71 */\n"
"                box-shadow: 0 2px 4px rgba(140, 170, 30, 0.3);\n"
"            }\n"
"\n"
"            QPushButton:hover {\n"
"                /* \u60ac\u505c\u9ad8\u4eae */\n"
"                background: qlineargradient(\n"
"                    x1:0, y1:0, x2:0, y2:1,\n"
"                    stop:0 rgba(255, 2"
                        "55, 255, 0.95),\n"
"                    stop:0.4 rgba(201, 237, 58, 0.86),\n"
"                    stop:1 rgba(201, 237, 58, 0.7)\n"
"                );\n"
"                border-color: rgba(150, 180, 35, 0.86);\n"
"                box-shadow: 0 3px 5px rgba(140, 170, 30, 0.4);\n"
"            }\n"
"\n"
"            QPushButton:pressed {\n"
"                /* \u6309\u4e0b\u6548\u679c */\n"
"                background: qlineargradient(\n"
"                    x1:0, y1:1,  /* \u53cd\u8f6c\u6e10\u53d8\u65b9\u5411 */\n"
"                    x2:0, y2:0,\n"
"                    stop:0 rgba(255, 255, 255, 0.7),\n"
"                    stop:0.6 rgba(161, 197, 28, 0.86),\n"
"                    stop:1 rgba(161, 197, 28, 0.9)\n"
"                );\n"
"                box-shadow: inset 1px 2px 3px rgba(100, 130, 20, 0.3),\n"
"                           inset -1px -1px 2px rgba(255, 255, 255, 0.2);\n"
"                border-color: rgba(120, 150, 25, 0.86);\n"
"                padding: 7px 12px 5px 12px;\n"
"          "
                        "  }")

        self.horizontalLayout_8.addWidget(self.m_bt_DrugSelect_3)


        self.verticalLayout_5.addLayout(self.horizontalLayout_8)

        self.line_5 = QFrame(self.groupBox_2)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_5.addWidget(self.line_5)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.bt_title_1 = QPushButton(self.groupBox_2)
        self.bt_title_1.setObjectName(u"bt_title_1")
        self.bt_title_1.setFont(font3)
        self.bt_title_1.setStyleSheet(u"QPushButton{\n"
"font-size:11pt;\n"
"border: none;\n"
"color:white;\n"
"}")
        icon19 = QIcon()
        icon19.addFile(u":/Resources/icons/icon_recordsearch_grey.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_title_1.setIcon(icon19)
        self.bt_title_1.setIconSize(QSize(25, 25))

        self.horizontalLayout_19.addWidget(self.bt_title_1)

        self.label_21 = QLabel(self.groupBox_2)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font)
        self.label_21.setStyleSheet(u"QLabel{\n"
"letter-spacing: 3px;\n"
"}")
        self.label_21.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_19.addWidget(self.label_21)

        self.horizontalSpacer_15 = QSpacerItem(72, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_15)


        self.verticalLayout_5.addLayout(self.horizontalLayout_19)

        self.m_tle_Basic_Filter = QTableWidget(self.groupBox_2)
        if (self.m_tle_Basic_Filter.columnCount() < 6):
            self.m_tle_Basic_Filter.setColumnCount(6)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.m_tle_Basic_Filter.setHorizontalHeaderItem(0, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.m_tle_Basic_Filter.setHorizontalHeaderItem(1, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.m_tle_Basic_Filter.setHorizontalHeaderItem(2, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.m_tle_Basic_Filter.setHorizontalHeaderItem(3, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.m_tle_Basic_Filter.setHorizontalHeaderItem(4, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.m_tle_Basic_Filter.setHorizontalHeaderItem(5, __qtablewidgetitem20)
        self.m_tle_Basic_Filter.setObjectName(u"m_tle_Basic_Filter")
        sizePolicy.setHeightForWidth(self.m_tle_Basic_Filter.sizePolicy().hasHeightForWidth())
        self.m_tle_Basic_Filter.setSizePolicy(sizePolicy)
        self.m_tle_Basic_Filter.setMinimumSize(QSize(0, 0))
        self.m_tle_Basic_Filter.setFont(font)
        self.m_tle_Basic_Filter.setStyleSheet(u"background-color:rgba(248, 248, 248, 220);")
        self.m_tle_Basic_Filter.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_5.addWidget(self.m_tle_Basic_Filter)

        self.line_3 = QFrame(self.groupBox_2)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_5.addWidget(self.line_3)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.groupBox_2)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"QLabel{\n"
"letter-spacing: 3px;\n"
"}")

        self.horizontalLayout_3.addWidget(self.label)

        self.m_edt_searchfilter = QLineEdit(self.groupBox_2)
        self.m_edt_searchfilter.setObjectName(u"m_edt_searchfilter")
        self.m_edt_searchfilter.setMaximumSize(QSize(16777215, 16777215))
        self.m_edt_searchfilter.setStyleSheet(u"QLineEdit { \n"
"background-color:rgba(248, 248, 248, 220);\n"
"font-size: 11pt; }\n"
"")

        self.horizontalLayout_3.addWidget(self.m_edt_searchfilter)


        self.horizontalLayout_22.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"QLabel{\n"
"letter-spacing: 3px;\n"
"}")

        self.horizontalLayout_4.addWidget(self.label_2)

        self.m_edt_searchfilter_DiagnosisP = QLineEdit(self.groupBox_2)
        self.m_edt_searchfilter_DiagnosisP.setObjectName(u"m_edt_searchfilter_DiagnosisP")
        self.m_edt_searchfilter_DiagnosisP.setMaximumSize(QSize(16777215, 16777215))
        self.m_edt_searchfilter_DiagnosisP.setStyleSheet(u"QLineEdit { \n"
"background-color:rgba(248, 248, 248, 220);\n"
"font-size: 11pt; }\n"
"")

        self.horizontalLayout_4.addWidget(self.m_edt_searchfilter_DiagnosisP)


        self.horizontalLayout_22.addLayout(self.horizontalLayout_4)


        self.verticalLayout_5.addLayout(self.horizontalLayout_22)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.m_edt_searchfilter_DateStart = QLineEdit(self.groupBox_2)
        self.m_edt_searchfilter_DateStart.setObjectName(u"m_edt_searchfilter_DateStart")
        self.m_edt_searchfilter_DateStart.setStyleSheet(u"background-color:rgba(248, 248, 248, 220);")

        self.horizontalLayout_5.addWidget(self.m_edt_searchfilter_DateStart)

        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_5.addWidget(self.label_3)

        self.m_edt_searchfilter_DateEnd = QLineEdit(self.groupBox_2)
        self.m_edt_searchfilter_DateEnd.setObjectName(u"m_edt_searchfilter_DateEnd")
        self.m_edt_searchfilter_DateEnd.setStyleSheet(u"background-color:rgba(248, 248, 248, 220);")

        self.horizontalLayout_5.addWidget(self.m_edt_searchfilter_DateEnd)

        self.m_bt_4_DateSearch = QPushButton(self.groupBox_2)
        self.m_bt_4_DateSearch.setObjectName(u"m_bt_4_DateSearch")
        self.m_bt_4_DateSearch.setMinimumSize(QSize(50, 30))
        icon20 = QIcon()
        icon20.addFile(u":/Resources/icons/icon_search_grey.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.m_bt_4_DateSearch.setIcon(icon20)
        self.m_bt_4_DateSearch.setIconSize(QSize(25, 25))

        self.horizontalLayout_5.addWidget(self.m_bt_4_DateSearch)


        self.verticalLayout_5.addLayout(self.horizontalLayout_5)

        self.line_9 = QFrame(self.groupBox_2)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setFrameShape(QFrame.HLine)
        self.line_9.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_5.addWidget(self.line_9)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.m_bt_Visit = QPushButton(self.groupBox_2)
        self.m_bt_Visit.setObjectName(u"m_bt_Visit")
        self.m_bt_Visit.setMinimumSize(QSize(0, 0))
        self.m_bt_Visit.setStyleSheet(u"QPushButton {\n"
"                /* \u57fa\u7840\u53c2\u6570 */\n"
"				letter-spacing: 2px;\n"
"                border-radius: 3px;\n"
"                border: 1px solid rgba(140, 170, 30, 0.78);\n"
"                padding: 3px 12px;\n"
"                color: black;\n"
"\n"
"                /* \u4e3b\u6e10\u53d8 (\u767d \u2192 \u7070 \u2192 \u6df1\u7070) */\n"
"                background: qlineargradient(\n"
"                    x1:0, y1:0, x2:0, y2:1,\n"
"                    stop:0 rgba(249, 249, 249,255),\n"
"                    stop:0.5 rgba(220, 220, 220,255),\n"
"                    stop:1 rgba(150, 150, 150,0.9)\n"
"                );\n"
"\n"
"                /* \u5916\u90e8\u9634\u5f71 */\n"
"                box-shadow: 0 2px 4px rgba(140, 170, 30, 0.3);\n"
"            }\n"
"\n"
"            QPushButton:hover {\n"
"                /* \u60ac\u505c\u9ad8\u4eae */\n"
"                background: qlineargradient(\n"
"                    x1:0, y1:0, x2:0, y2:1,\n"
"                    stop:0 rgba(255, 2"
                        "55, 255, 0.95),\n"
"                    stop:0.4 rgba(201, 237, 58, 0.86),\n"
"                    stop:1 rgba(201, 237, 58, 0.7)\n"
"                );\n"
"                border-color: rgba(150, 180, 35, 0.86);\n"
"                box-shadow: 0 3px 5px rgba(140, 170, 30, 0.4);\n"
"            }\n"
"\n"
"            QPushButton:pressed {\n"
"                /* \u6309\u4e0b\u6548\u679c */\n"
"                background: qlineargradient(\n"
"                    x1:0, y1:1,  /* \u53cd\u8f6c\u6e10\u53d8\u65b9\u5411 */\n"
"                    x2:0, y2:0,\n"
"                    stop:0 rgba(255, 255, 255, 0.7),\n"
"                    stop:0.6 rgba(161, 197, 28, 0.86),\n"
"                    stop:1 rgba(161, 197, 28, 0.9)\n"
"                );\n"
"                box-shadow: inset 1px 2px 3px rgba(100, 130, 20, 0.3),\n"
"                           inset -1px -1px 2px rgba(255, 255, 255, 0.2);\n"
"                border-color: rgba(120, 150, 25, 0.86);\n"
"                padding: 7px 12px 5px 12px;\n"
"          "
                        "  }")

        self.horizontalLayout_7.addWidget(self.m_bt_Visit)

        self.m_bt_Visit_2 = QPushButton(self.groupBox_2)
        self.m_bt_Visit_2.setObjectName(u"m_bt_Visit_2")
        self.m_bt_Visit_2.setStyleSheet(u"QPushButton {\n"
"                /* \u57fa\u7840\u53c2\u6570 */\n"
"				letter-spacing: 2px;\n"
"                border-radius: 3px;\n"
"                border: 1px solid rgba(140, 170, 30, 0.78);\n"
"                padding: 3px 12px;\n"
"                color: black;\n"
"\n"
"                /* \u4e3b\u6e10\u53d8 (\u767d \u2192 \u7070 \u2192 \u6df1\u7070) */\n"
"                background: qlineargradient(\n"
"                    x1:0, y1:0, x2:0, y2:1,\n"
"                    stop:0 rgba(249, 249, 249,255),\n"
"                    stop:0.5 rgba(220, 220, 220,255),\n"
"                    stop:1 rgba(150, 150, 150,0.9)\n"
"                );\n"
"\n"
"                /* \u5916\u90e8\u9634\u5f71 */\n"
"                box-shadow: 0 2px 4px rgba(140, 170, 30, 0.3);\n"
"            }\n"
"\n"
"            QPushButton:hover {\n"
"                /* \u60ac\u505c\u9ad8\u4eae */\n"
"                background: qlineargradient(\n"
"                    x1:0, y1:0, x2:0, y2:1,\n"
"                    stop:0 rgba(255, 2"
                        "55, 255, 0.95),\n"
"                    stop:0.4 rgba(201, 237, 58, 0.86),\n"
"                    stop:1 rgba(201, 237, 58, 0.7)\n"
"                );\n"
"                border-color: rgba(150, 180, 35, 0.86);\n"
"                box-shadow: 0 3px 5px rgba(140, 170, 30, 0.4);\n"
"            }\n"
"\n"
"            QPushButton:pressed {\n"
"                /* \u6309\u4e0b\u6548\u679c */\n"
"                background: qlineargradient(\n"
"                    x1:0, y1:1,  /* \u53cd\u8f6c\u6e10\u53d8\u65b9\u5411 */\n"
"                    x2:0, y2:0,\n"
"                    stop:0 rgba(255, 255, 255, 0.7),\n"
"                    stop:0.6 rgba(161, 197, 28, 0.86),\n"
"                    stop:1 rgba(161, 197, 28, 0.9)\n"
"                );\n"
"                box-shadow: inset 1px 2px 3px rgba(100, 130, 20, 0.3),\n"
"                           inset -1px -1px 2px rgba(255, 255, 255, 0.2);\n"
"                border-color: rgba(120, 150, 25, 0.86);\n"
"                padding: 7px 12px 5px 12px;\n"
"          "
                        "  }")

        self.horizontalLayout_7.addWidget(self.m_bt_Visit_2)


        self.verticalLayout_5.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.m_bt_Save = QPushButton(self.groupBox_2)
        self.m_bt_Save.setObjectName(u"m_bt_Save")
        self.m_bt_Save.setStyleSheet(u"QPushButton {\n"
"                /* \u57fa\u7840\u53c2\u6570 */\n"
"				letter-spacing: 2px;\n"
"                border-radius: 3px;\n"
"                border: 1px solid rgba(140, 170, 30, 0.78);\n"
"                padding: 3px 12px;\n"
"                color: black;\n"
"\n"
"                /* \u4e3b\u6e10\u53d8 (\u767d \u2192 \u7070 \u2192 \u6df1\u7070) */\n"
"                background: qlineargradient(\n"
"                    x1:0, y1:0, x2:0, y2:1,\n"
"                    stop:0 rgba(249, 249, 249,255),\n"
"                    stop:0.5 rgba(220, 220, 220,255),\n"
"                    stop:1 rgba(150, 150, 150,0.9)\n"
"                );\n"
"\n"
"                /* \u5916\u90e8\u9634\u5f71 */\n"
"                box-shadow: 0 2px 4px rgba(140, 170, 30, 0.3);\n"
"            }\n"
"\n"
"            QPushButton:hover {\n"
"                /* \u60ac\u505c\u9ad8\u4eae */\n"
"                background: qlineargradient(\n"
"                    x1:0, y1:0, x2:0, y2:1,\n"
"                    stop:0 rgba(255, 2"
                        "55, 255, 0.95),\n"
"                    stop:0.4 rgba(201, 237, 58, 0.86),\n"
"                    stop:1 rgba(201, 237, 58, 0.7)\n"
"                );\n"
"                border-color: rgba(150, 180, 35, 0.86);\n"
"                box-shadow: 0 3px 5px rgba(140, 170, 30, 0.4);\n"
"            }\n"
"\n"
"            QPushButton:pressed {\n"
"                /* \u6309\u4e0b\u6548\u679c */\n"
"                background: qlineargradient(\n"
"                    x1:0, y1:1,  /* \u53cd\u8f6c\u6e10\u53d8\u65b9\u5411 */\n"
"                    x2:0, y2:0,\n"
"                    stop:0 rgba(255, 255, 255, 0.7),\n"
"                    stop:0.6 rgba(161, 197, 28, 0.86),\n"
"                    stop:1 rgba(161, 197, 28, 0.9)\n"
"                );\n"
"                box-shadow: inset 1px 2px 3px rgba(100, 130, 20, 0.3),\n"
"                           inset -1px -1px 2px rgba(255, 255, 255, 0.2);\n"
"                border-color: rgba(120, 150, 25, 0.86);\n"
"                padding: 7px 12px 5px 12px;\n"
"          "
                        "  }")

        self.horizontalLayout_6.addWidget(self.m_bt_Save)

        self.m_bt_Del = QPushButton(self.groupBox_2)
        self.m_bt_Del.setObjectName(u"m_bt_Del")
        self.m_bt_Del.setStyleSheet(u"QPushButton {\n"
"                /* \u57fa\u7840\u53c2\u6570 */\n"
"				letter-spacing: 2px;\n"
"                border-radius: 3px;\n"
"                border: 1px solid rgba(140, 170, 30, 0.78);\n"
"                padding: 3px 12px;\n"
"                color: black;\n"
"\n"
"                /* \u4e3b\u6e10\u53d8 (\u767d \u2192 \u7070 \u2192 \u6df1\u7070) */\n"
"                background: qlineargradient(\n"
"                    x1:0, y1:0, x2:0, y2:1,\n"
"                    stop:0 rgba(249, 249, 249,255),\n"
"                    stop:0.5 rgba(220, 220, 220,255),\n"
"                    stop:1 rgba(150, 150, 150,0.9)\n"
"                );\n"
"\n"
"                /* \u5916\u90e8\u9634\u5f71 */\n"
"                box-shadow: 0 2px 4px rgba(140, 170, 30, 0.3);\n"
"            }\n"
"\n"
"            QPushButton:hover {\n"
"                /* \u60ac\u505c\u9ad8\u4eae */\n"
"                background: qlineargradient(\n"
"                    x1:0, y1:0, x2:0, y2:1,\n"
"                    stop:0 rgba(255, 2"
                        "55, 255, 0.95),\n"
"                    stop:0.4 rgba(201, 237, 58, 0.86),\n"
"                    stop:1 rgba(201, 237, 58, 0.7)\n"
"                );\n"
"                border-color: rgba(150, 180, 35, 0.86);\n"
"                box-shadow: 0 3px 5px rgba(140, 170, 30, 0.4);\n"
"            }\n"
"\n"
"            QPushButton:pressed {\n"
"                /* \u6309\u4e0b\u6548\u679c */\n"
"                background: qlineargradient(\n"
"                    x1:0, y1:1,  /* \u53cd\u8f6c\u6e10\u53d8\u65b9\u5411 */\n"
"                    x2:0, y2:0,\n"
"                    stop:0 rgba(255, 255, 255, 0.7),\n"
"                    stop:0.6 rgba(161, 197, 28, 0.86),\n"
"                    stop:1 rgba(161, 197, 28, 0.9)\n"
"                );\n"
"                box-shadow: inset 1px 2px 3px rgba(100, 130, 20, 0.3),\n"
"                           inset -1px -1px 2px rgba(255, 255, 255, 0.2);\n"
"                border-color: rgba(120, 150, 25, 0.86);\n"
"                padding: 7px 12px 5px 12px;\n"
"          "
                        "  }")

        self.horizontalLayout_6.addWidget(self.m_bt_Del)


        self.verticalLayout_5.addLayout(self.horizontalLayout_6)

        self.splitter.addWidget(self.groupBox_2)
        self.groupBox_3 = QGroupBox(self.splitter)
        self.groupBox_3.setObjectName(u"groupBox_3")
        sizePolicy1.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy1)
        self.groupBox_3.setStyleSheet(u"    QGroupBox {\n"
"        background-color: rgba(181, 217, 38, 205); /* \u53ea\u8bbe\u7f6e\u80cc\u666f\u8272 */\n"
"        border:1px solid rgb(190, 190, 190);   /*\u8fb9\u6846\u7684\u7c97\u7ec6\uff0c\u989c\u8272*/\n"
"        border-radius:10px;    /*\u8bbe\u7f6e\u5706\u89d2\u534a\u5f84 */\n"
"    }\n"
"\n"
"\n"
"    /* \u786e\u4fdd\u5b50\u63a7\u4ef6\u7684\u5b57\u4f53\u5927\u5c0f\u548c\u7c97\u7ec6\u4e0d\u53d7\u5f71\u54cd */\n"
"    QGroupBox QWidget {\n"
"        font-size: 16px; /* \u8bbe\u7f6e\u5b50\u63a7\u4ef6\u7684\u5b57\u4f53\u5927\u5c0f */\n"
"        font-weight: bold; /* \u8bbe\u7f6e\u5b50\u63a7\u4ef6\u7684\u5b57\u4f53\u7c97\u7ec6 */\n"
"    }")
        self.verticalLayout = QVBoxLayout(self.groupBox_3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.m_tle_ClinicalSymptom = QTableWidget(self.groupBox_3)
        if (self.m_tle_ClinicalSymptom.columnCount() < 2):
            self.m_tle_ClinicalSymptom.setColumnCount(2)
        font4 = QFont()
        __qtablewidgetitem21 = QTableWidgetItem()
        __qtablewidgetitem21.setFont(font4);
        self.m_tle_ClinicalSymptom.setHorizontalHeaderItem(0, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        __qtablewidgetitem22.setFont(font4);
        self.m_tle_ClinicalSymptom.setHorizontalHeaderItem(1, __qtablewidgetitem22)
        self.m_tle_ClinicalSymptom.setObjectName(u"m_tle_ClinicalSymptom")
        sizePolicy.setHeightForWidth(self.m_tle_ClinicalSymptom.sizePolicy().hasHeightForWidth())
        self.m_tle_ClinicalSymptom.setSizePolicy(sizePolicy)
        self.m_tle_ClinicalSymptom.setMinimumSize(QSize(0, 0))
        self.m_tle_ClinicalSymptom.setMaximumSize(QSize(16777215, 16777215))
        font5 = QFont()
        font5.setBold(True)
        self.m_tle_ClinicalSymptom.setFont(font5)
        self.m_tle_ClinicalSymptom.setStyleSheet(u"QTableWidget{\n"
"background-color:rgba(248, 248, 248, 220);\n"
"} ")
        self.m_tle_ClinicalSymptom.setColumnCount(2)
        self.m_tle_ClinicalSymptom.horizontalHeader().setDefaultSectionSize(100)
        self.m_tle_ClinicalSymptom.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout.addWidget(self.m_tle_ClinicalSymptom)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.m_edt_searchfilter_ClinicalSymptom = QLineEdit(self.groupBox_3)
        self.m_edt_searchfilter_ClinicalSymptom.setObjectName(u"m_edt_searchfilter_ClinicalSymptom")
        self.m_edt_searchfilter_ClinicalSymptom.setStyleSheet(u"QLineEdit { \n"
"background-color:rgba(248, 248, 248, 220);\n"
"font-size: 11pt; }\n"
"")

        self.horizontalLayout_2.addWidget(self.m_edt_searchfilter_ClinicalSymptom)

        self.bt_searchicon = QPushButton(self.groupBox_3)
        self.bt_searchicon.setObjectName(u"bt_searchicon")
        self.bt_searchicon.setFont(font3)
        self.bt_searchicon.setStyleSheet(u"QPushButton{\n"
"font-size:11pt;\n"
"border: none;\n"
"color:white;\n"
"}")
        icon21 = QIcon()
        icon21.addFile(u":/Resources/icons/icon_search.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_searchicon.setIcon(icon21)
        self.bt_searchicon.setIconSize(QSize(25, 25))

        self.horizontalLayout_2.addWidget(self.bt_searchicon)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.line_6 = QFrame(self.groupBox_3)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_6)

        self.m_tle_Diagnosis = QTableWidget(self.groupBox_3)
        if (self.m_tle_Diagnosis.columnCount() < 2):
            self.m_tle_Diagnosis.setColumnCount(2)
        __qtablewidgetitem23 = QTableWidgetItem()
        __qtablewidgetitem23.setFont(font);
        self.m_tle_Diagnosis.setHorizontalHeaderItem(0, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        __qtablewidgetitem24.setFont(font);
        self.m_tle_Diagnosis.setHorizontalHeaderItem(1, __qtablewidgetitem24)
        self.m_tle_Diagnosis.setObjectName(u"m_tle_Diagnosis")
        sizePolicy.setHeightForWidth(self.m_tle_Diagnosis.sizePolicy().hasHeightForWidth())
        self.m_tle_Diagnosis.setSizePolicy(sizePolicy)
        self.m_tle_Diagnosis.setFont(font5)
        self.m_tle_Diagnosis.setStyleSheet(u"QTableWidget{\n"
"background-color:rgba(248, 248, 248, 220);\n"
"} ")
        self.m_tle_Diagnosis.horizontalHeader().setDefaultSectionSize(100)
        self.m_tle_Diagnosis.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout.addWidget(self.m_tle_Diagnosis)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.m_edt_searchfilter_DiagnosisD = QLineEdit(self.groupBox_3)
        self.m_edt_searchfilter_DiagnosisD.setObjectName(u"m_edt_searchfilter_DiagnosisD")
        self.m_edt_searchfilter_DiagnosisD.setStyleSheet(u"QLineEdit { \n"
"background-color:rgba(248, 248, 248, 220);\n"
"font-size: 11pt; }\n"
"")

        self.horizontalLayout.addWidget(self.m_edt_searchfilter_DiagnosisD)

        self.bt_searchicon_2 = QPushButton(self.groupBox_3)
        self.bt_searchicon_2.setObjectName(u"bt_searchicon_2")
        self.bt_searchicon_2.setFont(font3)
        self.bt_searchicon_2.setStyleSheet(u"QPushButton{\n"
"font-size:11pt;\n"
"border: none;\n"
"color:white;\n"
"}")
        self.bt_searchicon_2.setIcon(icon21)
        self.bt_searchicon_2.setIconSize(QSize(25, 25))

        self.horizontalLayout.addWidget(self.bt_searchicon_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.m_edt_DrugDiscrip = QTextEdit(self.groupBox_3)
        self.m_edt_DrugDiscrip.setObjectName(u"m_edt_DrugDiscrip")
        self.m_edt_DrugDiscrip.setFont(font5)
        self.m_edt_DrugDiscrip.setStyleSheet(u"QTextEdit{\n"
"background-color:rgba(248, 248, 248, 220);\n"
"} ")

        self.verticalLayout.addWidget(self.m_edt_DrugDiscrip)

        self.line_11 = QFrame(self.groupBox_3)
        self.line_11.setObjectName(u"line_11")
        self.line_11.setFrameShape(QFrame.HLine)
        self.line_11.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_11)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalSpacer_9 = QSpacerItem(18, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_9)

        self.label_15 = QLabel(self.groupBox_3)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMaximumSize(QSize(60, 30))
        self.label_15.setFont(font5)

        self.horizontalLayout_18.addWidget(self.label_15)

        self.m_edtAcubNumber = QLineEdit(self.groupBox_3)
        self.m_edtAcubNumber.setObjectName(u"m_edtAcubNumber")
        sizePolicy5 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.m_edtAcubNumber.sizePolicy().hasHeightForWidth())
        self.m_edtAcubNumber.setSizePolicy(sizePolicy5)
        self.m_edtAcubNumber.setMinimumSize(QSize(40, 30))
        self.m_edtAcubNumber.setMaximumSize(QSize(40, 16777215))
        self.m_edtAcubNumber.setFont(font5)
        self.m_edtAcubNumber.setStyleSheet(u"background-color:rgba(248, 248, 248, 220);")

        self.horizontalLayout_18.addWidget(self.m_edtAcubNumber)

        self.label_14 = QLabel(self.groupBox_3)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMaximumSize(QSize(30, 30))
        self.label_14.setFont(font5)

        self.horizontalLayout_18.addWidget(self.label_14)

        self.line_2 = QFrame(self.groupBox_3)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_18.addWidget(self.line_2)

        self.label_17 = QLabel(self.groupBox_3)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMaximumSize(QSize(50, 30))
        self.label_17.setFont(font5)

        self.horizontalLayout_18.addWidget(self.label_17)

        self.m_edtAcubPrice = QLineEdit(self.groupBox_3)
        self.m_edtAcubPrice.setObjectName(u"m_edtAcubPrice")
        self.m_edtAcubPrice.setMinimumSize(QSize(0, 30))
        self.m_edtAcubPrice.setMaximumSize(QSize(160, 16777215))
        self.m_edtAcubPrice.setFont(font5)
        self.m_edtAcubPrice.setStyleSheet(u"background-color:rgba(248, 248, 248, 220);")

        self.horizontalLayout_18.addWidget(self.m_edtAcubPrice)


        self.verticalLayout.addLayout(self.horizontalLayout_18)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalSpacer_6 = QSpacerItem(28, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_6)

        self.label_13 = QLabel(self.groupBox_3)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMaximumSize(QSize(60, 30))
        self.label_13.setFont(font5)
        self.label_13.setStyleSheet(u"QLabel{\n"
"letter-spacing: 3px;\n"
"}")

        self.horizontalLayout_12.addWidget(self.label_13)

        self.m_edtDosesNumber = QLineEdit(self.groupBox_3)
        self.m_edtDosesNumber.setObjectName(u"m_edtDosesNumber")
        sizePolicy5.setHeightForWidth(self.m_edtDosesNumber.sizePolicy().hasHeightForWidth())
        self.m_edtDosesNumber.setSizePolicy(sizePolicy5)
        self.m_edtDosesNumber.setMinimumSize(QSize(40, 30))
        self.m_edtDosesNumber.setMaximumSize(QSize(40, 16777215))
        self.m_edtDosesNumber.setFont(font5)
        self.m_edtDosesNumber.setStyleSheet(u"background-color:rgba(248, 248, 248, 220);")

        self.horizontalLayout_12.addWidget(self.m_edtDosesNumber)

        self.label_11 = QLabel(self.groupBox_3)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMaximumSize(QSize(30, 30))
        self.label_11.setFont(font5)

        self.horizontalLayout_12.addWidget(self.label_11)

        self.line = QFrame(self.groupBox_3)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_12.addWidget(self.line)

        self.label_16 = QLabel(self.groupBox_3)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMaximumSize(QSize(50, 30))
        self.label_16.setFont(font5)

        self.horizontalLayout_12.addWidget(self.label_16)

        self.m_edtDosesPrice = QLineEdit(self.groupBox_3)
        self.m_edtDosesPrice.setObjectName(u"m_edtDosesPrice")
        self.m_edtDosesPrice.setMinimumSize(QSize(0, 30))
        self.m_edtDosesPrice.setMaximumSize(QSize(160, 16777215))
        self.m_edtDosesPrice.setFont(font5)
        self.m_edtDosesPrice.setStyleSheet(u"background-color:rgba(248, 248, 248, 220);")

        self.horizontalLayout_12.addWidget(self.m_edtDosesPrice)


        self.verticalLayout.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalSpacer_10 = QSpacerItem(36, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_10)

        self.label_6 = QLabel(self.groupBox_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"QLabel { \n"
"font-size: 11pt; }\n"
"")

        self.horizontalLayout_20.addWidget(self.label_6)

        self.line_13 = QFrame(self.groupBox_3)
        self.line_13.setObjectName(u"line_13")
        self.line_13.setFrameShape(QFrame.VLine)
        self.line_13.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_20.addWidget(self.line_13)

        self.label_18 = QLabel(self.groupBox_3)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMinimumSize(QSize(0, 0))
        self.label_18.setFont(font5)

        self.horizontalLayout_20.addWidget(self.label_18)

        self.m_edtTotalPrice = QLineEdit(self.groupBox_3)
        self.m_edtTotalPrice.setObjectName(u"m_edtTotalPrice")
        self.m_edtTotalPrice.setMinimumSize(QSize(0, 30))
        self.m_edtTotalPrice.setMaximumSize(QSize(160, 16777215))
        font6 = QFont()
        font6.setPointSize(12)
        font6.setBold(True)
        font6.setItalic(False)
        self.m_edtTotalPrice.setFont(font6)
        self.m_edtTotalPrice.setStyleSheet(u"    QLineEdit {\n"
"        background-color:rgba(248, 248, 248, 220);\n"
"        font-size: 12pt;\n"
"        color: black;\n"
"    }\n"
"")

        self.horizontalLayout_20.addWidget(self.m_edtTotalPrice)


        self.verticalLayout.addLayout(self.horizontalLayout_20)

        self.line_4 = QFrame(self.groupBox_3)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_4)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer)

        self.m_pbPreview = QPushButton(self.groupBox_3)
        self.m_pbPreview.setObjectName(u"m_pbPreview")
        self.m_pbPreview.setMinimumSize(QSize(0, 40))
        self.m_pbPreview.setMaximumSize(QSize(200, 16777215))
        self.m_pbPreview.setStyleSheet(u"QPushButton {\n"
"                /* \u57fa\u7840\u53c2\u6570 */\n"
"				letter-spacing: 1px;\n"
"                border-radius: 3px;\n"
"                border: 1px solid rgba(140, 170, 30, 0.78);\n"
"                padding: 3px 12px;\n"
"                color: black;\n"
"\n"
"                /* \u4e3b\u6e10\u53d8 (\u767d \u2192 \u7070 \u2192 \u6df1\u7070) */\n"
"                background: qlineargradient(\n"
"                    x1:0, y1:0, x2:0, y2:1,\n"
"                    stop:0 rgba(249, 249, 249,255),\n"
"                    stop:0.5 rgba(220, 220, 220,255),\n"
"                    stop:1 rgba(150, 150, 150,0.9)\n"
"                );\n"
"\n"
"                /* \u5916\u90e8\u9634\u5f71 */\n"
"                box-shadow: 0 2px 4px rgba(140, 170, 30, 0.3);\n"
"            }\n"
"\n"
"            QPushButton:hover {\n"
"                /* \u60ac\u505c\u9ad8\u4eae */\n"
"                background: qlineargradient(\n"
"                    x1:0, y1:0, x2:0, y2:1,\n"
"                    stop:0 rgba(255, 2"
                        "55, 255, 0.95),\n"
"                    stop:0.4 rgba(201, 237, 58, 0.86),\n"
"                    stop:1 rgba(201, 237, 58, 0.7)\n"
"                );\n"
"                border-color: rgba(150, 180, 35, 0.86);\n"
"                box-shadow: 0 3px 5px rgba(140, 170, 30, 0.4);\n"
"            }\n"
"\n"
"            QPushButton:pressed {\n"
"                /* \u6309\u4e0b\u6548\u679c */\n"
"                background: qlineargradient(\n"
"                    x1:0, y1:1,  /* \u53cd\u8f6c\u6e10\u53d8\u65b9\u5411 */\n"
"                    x2:0, y2:0,\n"
"                    stop:0 rgba(255, 255, 255, 0.7),\n"
"                    stop:0.6 rgba(161, 197, 28, 0.86),\n"
"                    stop:1 rgba(161, 197, 28, 0.9)\n"
"                );\n"
"                box-shadow: inset 1px 2px 3px rgba(100, 130, 20, 0.3),\n"
"                           inset -1px -1px 2px rgba(255, 255, 255, 0.2);\n"
"                border-color: rgba(120, 150, 25, 0.86);\n"
"                padding: 7px 12px 5px 12px;\n"
"          "
                        "  }")

        self.horizontalLayout_13.addWidget(self.m_pbPreview)

        self.horizontalSpacer_4 = QSpacerItem(10, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_4)

        self.m_pbWithDiagSyndrome = QPushButton(self.groupBox_3)
        self.m_pbWithDiagSyndrome.setObjectName(u"m_pbWithDiagSyndrome")
        self.m_pbWithDiagSyndrome.setMinimumSize(QSize(0, 40))
        self.m_pbWithDiagSyndrome.setMaximumSize(QSize(200, 16777215))
        self.m_pbWithDiagSyndrome.setStyleSheet(u"QPushButton {\n"
"                /* \u57fa\u7840\u53c2\u6570 */\n"
"				letter-spacing: 1px;\n"
"                border-radius: 3px;\n"
"                border: 1px solid rgba(140, 170, 30, 0.78);\n"
"                padding: 3px 12px;\n"
"                color: black;\n"
"\n"
"                /* \u4e3b\u6e10\u53d8 (\u767d \u2192 \u7070 \u2192 \u6df1\u7070) */\n"
"                background: qlineargradient(\n"
"                    x1:0, y1:0, x2:0, y2:1,\n"
"                    stop:0 rgba(249, 249, 249,255),\n"
"                    stop:0.5 rgba(220, 220, 220,255),\n"
"                    stop:1 rgba(150, 150, 150,0.9)\n"
"                );\n"
"\n"
"                /* \u5916\u90e8\u9634\u5f71 */\n"
"                box-shadow: 0 2px 4px rgba(140, 170, 30, 0.3);\n"
"            }\n"
"\n"
"            QPushButton:hover {\n"
"                /* \u60ac\u505c\u9ad8\u4eae */\n"
"                background: qlineargradient(\n"
"                    x1:0, y1:0, x2:0, y2:1,\n"
"                    stop:0 rgba(255, 2"
                        "55, 255, 0.95),\n"
"                    stop:0.4 rgba(201, 237, 58, 0.86),\n"
"                    stop:1 rgba(201, 237, 58, 0.7)\n"
"                );\n"
"                border-color: rgba(150, 180, 35, 0.86);\n"
"                box-shadow: 0 3px 5px rgba(140, 170, 30, 0.4);\n"
"            }\n"
"\n"
"            QPushButton:pressed {\n"
"                /* \u6309\u4e0b\u6548\u679c */\n"
"                background: qlineargradient(\n"
"                    x1:0, y1:1,  /* \u53cd\u8f6c\u6e10\u53d8\u65b9\u5411 */\n"
"                    x2:0, y2:0,\n"
"                    stop:0 rgba(255, 255, 255, 0.7),\n"
"                    stop:0.6 rgba(161, 197, 28, 0.86),\n"
"                    stop:1 rgba(161, 197, 28, 0.9)\n"
"                );\n"
"                box-shadow: inset 1px 2px 3px rgba(100, 130, 20, 0.3),\n"
"                           inset -1px -1px 2px rgba(255, 255, 255, 0.2);\n"
"                border-color: rgba(120, 150, 25, 0.86);\n"
"                padding: 7px 12px 5px 12px;\n"
"          "
                        "  }")

        self.horizontalLayout_13.addWidget(self.m_pbWithDiagSyndrome)

        self.horizontalSpacer_2 = QSpacerItem(10, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_2)

        self.m_pbWithoutDiagSyndrome = QPushButton(self.groupBox_3)
        self.m_pbWithoutDiagSyndrome.setObjectName(u"m_pbWithoutDiagSyndrome")
        self.m_pbWithoutDiagSyndrome.setMinimumSize(QSize(0, 40))
        self.m_pbWithoutDiagSyndrome.setMaximumSize(QSize(200, 16777215))
        self.m_pbWithoutDiagSyndrome.setFont(font5)
        self.m_pbWithoutDiagSyndrome.setLayoutDirection(Qt.LeftToRight)
        self.m_pbWithoutDiagSyndrome.setStyleSheet(u"QPushButton {\n"
"                /* \u57fa\u7840\u53c2\u6570 */\n"
"				letter-spacing: 1px;\n"
"                border-radius: 3px;\n"
"                border: 1px solid rgba(140, 170, 30, 0.78);\n"
"                padding: 3px 12px;\n"
"                color: black;\n"
"\n"
"                /* \u4e3b\u6e10\u53d8 (\u767d \u2192 \u7070 \u2192 \u6df1\u7070) */\n"
"                background: qlineargradient(\n"
"                    x1:0, y1:0, x2:0, y2:1,\n"
"                    stop:0 rgba(249, 249, 249,255),\n"
"                    stop:0.5 rgba(220, 220, 220,255),\n"
"                    stop:1 rgba(150, 150, 150,0.9)\n"
"                );\n"
"\n"
"                /* \u5916\u90e8\u9634\u5f71 */\n"
"                box-shadow: 0 2px 4px rgba(140, 170, 30, 0.3);\n"
"            }\n"
"\n"
"            QPushButton:hover {\n"
"                /* \u60ac\u505c\u9ad8\u4eae */\n"
"                background: qlineargradient(\n"
"                    x1:0, y1:0, x2:0, y2:1,\n"
"                    stop:0 rgba(255, 2"
                        "55, 255, 0.95),\n"
"                    stop:0.4 rgba(201, 237, 58, 0.86),\n"
"                    stop:1 rgba(201, 237, 58, 0.7)\n"
"                );\n"
"                border-color: rgba(150, 180, 35, 0.86);\n"
"                box-shadow: 0 3px 5px rgba(140, 170, 30, 0.4);\n"
"            }\n"
"\n"
"            QPushButton:pressed {\n"
"                /* \u6309\u4e0b\u6548\u679c */\n"
"                background: qlineargradient(\n"
"                    x1:0, y1:1,  /* \u53cd\u8f6c\u6e10\u53d8\u65b9\u5411 */\n"
"                    x2:0, y2:0,\n"
"                    stop:0 rgba(255, 255, 255, 0.7),\n"
"                    stop:0.6 rgba(161, 197, 28, 0.86),\n"
"                    stop:1 rgba(161, 197, 28, 0.9)\n"
"                );\n"
"                box-shadow: inset 1px 2px 3px rgba(100, 130, 20, 0.3),\n"
"                           inset -1px -1px 2px rgba(255, 255, 255, 0.2);\n"
"                border-color: rgba(120, 150, 25, 0.86);\n"
"                padding: 7px 12px 5px 12px;\n"
"          "
                        "  }")

        self.horizontalLayout_13.addWidget(self.m_pbWithoutDiagSyndrome)

        self.bt_title_7 = QPushButton(self.groupBox_3)
        self.bt_title_7.setObjectName(u"bt_title_7")
        self.bt_title_7.setFont(font3)
        self.bt_title_7.setStyleSheet(u"QPushButton{\n"
"font-size:11pt;\n"
"border: none;\n"
"color:white;\n"
"}")
        icon22 = QIcon()
        icon22.addFile(u":/Resources/icons/icon_print.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_title_7.setIcon(icon22)
        self.bt_title_7.setIconSize(QSize(25, 25))

        self.horizontalLayout_13.addWidget(self.bt_title_7)


        self.verticalLayout.addLayout(self.horizontalLayout_13)

        self.splitter.addWidget(self.groupBox_3)

        self.horizontalLayout_9.addWidget(self.splitter)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u6e05\u865a\u5185\u5b88\u4e2d\u533b\u5904\u65b9", None))
        self.on_action_jingyanxuanfang.setText(QCoreApplication.translate("MainWindow", u"\u7ecf\u9a8c\u9009\u65b9\u8bbe\u7f6e", None))
        self.on_action_bianbingxuanfang.setText(QCoreApplication.translate("MainWindow", u"\u8fa8\u75c5\u9009\u65b9\u8bbe\u7f6e", None))
        self.on_action_fangjixuanfang.setText(QCoreApplication.translate("MainWindow", u"\u65b9\u5242\u9009\u65b9\u8bbe\u7f6e", None))
#if QT_CONFIG(tooltip)
        self.on_action_fangjixuanfang.setToolTip(QCoreApplication.translate("MainWindow", u"\u65b9\u5242\u9009\u65b9\u8bbe\u7f6e", None))
#endif // QT_CONFIG(tooltip)
        self.on_action_DrugSetting.setText(QCoreApplication.translate("MainWindow", u"\u4e2d\u836f\u8bbe\u7f6e", None))
        self.on_action_usage.setText(QCoreApplication.translate("MainWindow", u"\u4e2d\u836f\u7528\u6cd5", None))
        self.on_action_DrugList.setText(QCoreApplication.translate("MainWindow", u"\u4e2d\u836f\u8bbe\u7f6e", None))
        self.m_bt_menu_Userinfor.setText(QCoreApplication.translate("MainWindow", u" \u7528\u6237", None))
        self.m_bt_menu_Patients.setText(QCoreApplication.translate("MainWindow", u" \u60a3\u8005", None))
        self.m_bt_menu_symptoms.setText(QCoreApplication.translate("MainWindow", u" \u75c5\u8bc1", None))
        self.m_bt_menu_Anylasis.setText(QCoreApplication.translate("MainWindow", u" \u8fa9\u8bc1", None))
        self.m_bt_menu_Diagnosis.setText(QCoreApplication.translate("MainWindow", u" \u8bca\u65ad", None))
        self.m_bt_menu_Acup.setText(QCoreApplication.translate("MainWindow", u" \u9488\u7078", None))
        self.m_bt_menu_Formulas.setText(QCoreApplication.translate("MainWindow", u" \u5904\u65b9", None))
        self.m_bt_menu_DrugList.setText(QCoreApplication.translate("MainWindow", u" \u4e2d\u836f", None))
        self.m_bt_menu_DrugUsage.setText(QCoreApplication.translate("MainWindow", u" \u7528\u6cd5", None))
        self.m_bt_menu_MedicalRec.setText(QCoreApplication.translate("MainWindow", u" \u533b\u6848", None))
        self.sutra_image.setText("")
        self.m_bt_About.setText("")
        self.groupBox_1.setTitle("")
        self.bt_title_3.setText("")
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"\u60a3\u8005\u8d44\u6599", None))
        self.label_PatientPhoto.setText("")
        ___qtablewidgetitem = self.m_tle_PatientInfo.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u7f16\u53f7", None));
        ___qtablewidgetitem1 = self.m_tle_PatientInfo.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u59d3\u540d", None));
        ___qtablewidgetitem2 = self.m_tle_PatientInfo.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u6027\u522b", None));
        ___qtablewidgetitem3 = self.m_tle_PatientInfo.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u5e74\u9f84", None));
        ___qtablewidgetitem4 = self.m_tle_PatientInfo.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"\u75c5\u8bc1", None));
        ___qtablewidgetitem5 = self.m_tle_PatientInfo.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"\u8bca\u65ad", None));
        ___qtablewidgetitem6 = self.m_tle_PatientInfo.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"\u8840\u538b", None));
        ___qtablewidgetitem7 = self.m_tle_PatientInfo.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"\u4f4f\u5740", None));
        ___qtablewidgetitem8 = self.m_tle_PatientInfo.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"\u7535\u8bdd", None));
        ___qtablewidgetitem9 = self.m_tle_PatientInfo.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"\u75c5\u5386\u53f7", None));
        ___qtablewidgetitem10 = self.m_tle_PatientInfo.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"\u8eab\u4efd\u8bc1\u53f7", None));
        self.bt_title_4.setText("")
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"\u9488\u7078\u6216\u5176\u4ed6\u7597\u6cd5", None))
        self.bt_title_5.setText("")
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"\u4e2d\u836f\u6cbb\u7597", None))
        ___qtablewidgetitem11 = self.m_tbl_DrugUsage.horizontalHeaderItem(0)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"\u7f16\u53f7", None));
        ___qtablewidgetitem12 = self.m_tbl_DrugUsage.horizontalHeaderItem(1)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"\u836f\u7269", None));
        ___qtablewidgetitem13 = self.m_tbl_DrugUsage.horizontalHeaderItem(2)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"\u5242\u91cf", None));
        ___qtablewidgetitem14 = self.m_tbl_DrugUsage.horizontalHeaderItem(3)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"\u714e\u6cd5", None));
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u7528\n"
"\u6cd5", None))
        self.bt_title_6.setText("")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"\u5907\u6ce8", None))
        self.groupBox_2.setTitle("")
        self.bt_title.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u75c5\u8bc1\u8868\u73b0", None))
        self.bt_title_2.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u4e00\u65f6\u8fa9\u8bc1", None))
        self.m_bt_DrugSelect_3.setText(QCoreApplication.translate("MainWindow", u"\u8fa9\u8bc1\u9009\u65b9", None))
        self.bt_title_1.setText("")
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"\u75c5\u5386\u67e5\u8be2", None))
        ___qtablewidgetitem15 = self.m_tle_Basic_Filter.horizontalHeaderItem(0)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"\u7f16\u53f7", None));
        ___qtablewidgetitem16 = self.m_tle_Basic_Filter.horizontalHeaderItem(1)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"\u59d3\u540d", None));
        ___qtablewidgetitem17 = self.m_tle_Basic_Filter.horizontalHeaderItem(2)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"\u6027\u522b", None));
        ___qtablewidgetitem18 = self.m_tle_Basic_Filter.horizontalHeaderItem(3)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"\u5e74\u9f84", None));
        ___qtablewidgetitem19 = self.m_tle_Basic_Filter.horizontalHeaderItem(4)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"\u8bca\u65ad", None));
        ___qtablewidgetitem20 = self.m_tle_Basic_Filter.horizontalHeaderItem(5)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"\u65e5\u671f\u65f6\u95f4", None));
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u59d3\u540d", None))
        self.m_edt_searchfilter.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u59d3\u540d\u62fc\u97f3\u7f29\u5199", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u8bca\u65ad", None))
        self.m_edt_searchfilter_DiagnosisP.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8bca\u65ad\u62fc\u97f3\u7f29\u5199", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u81f3", None))
        self.m_bt_4_DateSearch.setText("")
        self.m_bt_Visit.setText(QCoreApplication.translate("MainWindow", u"\u521d\u8bca", None))
        self.m_bt_Visit_2.setText(QCoreApplication.translate("MainWindow", u"\u590d\u8bca", None))
        self.m_bt_Save.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58", None))
        self.m_bt_Del.setText(QCoreApplication.translate("MainWindow", u"\u5220\u9664", None))
        self.groupBox_3.setTitle("")
        ___qtablewidgetitem21 = self.m_tle_ClinicalSymptom.horizontalHeaderItem(0)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"\u7f16\u53f7", None));
        ___qtablewidgetitem22 = self.m_tle_ClinicalSymptom.horizontalHeaderItem(1)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"\u5e38\u89c1\u75c5\u75c7\u8868\u73b0", None));
#if QT_CONFIG(tooltip)
        self.m_edt_searchfilter_ClinicalSymptom.setToolTip(QCoreApplication.translate("MainWindow", u"\u4e3a\u65e0\u4e3a", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.m_edt_searchfilter_ClinicalSymptom.setStatusTip(QCoreApplication.translate("MainWindow", u"www", u"5555"))
#endif // QT_CONFIG(statustip)
        self.m_edt_searchfilter_ClinicalSymptom.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u75c5\u8bc1\u62fc\u97f3\u7f29\u5199", None))
        self.bt_searchicon.setText("")
        ___qtablewidgetitem23 = self.m_tle_Diagnosis.horizontalHeaderItem(0)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"\u7f16\u53f7", None));
        ___qtablewidgetitem24 = self.m_tle_Diagnosis.horizontalHeaderItem(1)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"\u5e38\u7528\u8fa9\u8bc1\u5904\u65b9", None));
        self.m_edt_searchfilter_DiagnosisD.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8fa9\u8bc1\u62fc\u97f3\u7f29\u5199", None))
        self.bt_searchicon_2.setText("")
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"\u9488\u7078\u7b49", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"\u6b21", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"\u8ba1\u4ef7", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"\u4e2d\u836f", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u4ed8", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"\u8ba1\u4ef7", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\uff08\u542b\u8bca\u91d1\uff09", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"\u5408\u8ba1", None))
        self.m_pbPreview.setText(QCoreApplication.translate("MainWindow", u"\u67e5\u770b\u75c5\u5386", None))
        self.m_pbWithDiagSyndrome.setText(QCoreApplication.translate("MainWindow", u"\u5e26\u8bc1\u5019\u6253\u5370", None))
        self.m_pbWithoutDiagSyndrome.setText(QCoreApplication.translate("MainWindow", u"\u65e0\u8bc1\u5019\u6253\u5370", None))
        self.bt_title_7.setText("")
    # retranslateUi

