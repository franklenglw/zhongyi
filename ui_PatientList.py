# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PatientList.ui'
##
## Created by: Qt User Interface Compiler version 6.1.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

import resources_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1188, 704)
        icon = QIcon()
        icon.addFile(u":/Resources/icons/logo.ico", QSize(), QIcon.Normal, QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.horizontalLayout_12 = QHBoxLayout(Dialog)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.splitter = QSplitter(Dialog)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.widget = QWidget(self.splitter)
        self.widget.setObjectName(u"widget")
        self.widget.setMaximumSize(QSize(580, 16777215))
        self.verticalLayout_4 = QVBoxLayout(self.widget)
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.groupBox_1 = QGroupBox(self.widget)
        self.groupBox_1.setObjectName(u"groupBox_1")
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
        self.verticalLayout = QVBoxLayout(self.groupBox_1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.bt_title_3 = QPushButton(self.groupBox_1)
        self.bt_title_3.setObjectName(u"bt_title_3")
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.bt_title_3.setFont(font)
        self.bt_title_3.setStyleSheet(u"QPushButton{\n"
"font-size:11pt;\n"
"border: none;\n"
"color:white;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/Resources/icons/icon_compare.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_title_3.setIcon(icon1)
        self.bt_title_3.setIconSize(QSize(25, 25))

        self.horizontalLayout_4.addWidget(self.bt_title_3)

        self.label = QLabel(self.groupBox_1)
        self.label.setObjectName(u"label")

        self.horizontalLayout_4.addWidget(self.label)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.bt_title_5 = QPushButton(self.groupBox_1)
        self.bt_title_5.setObjectName(u"bt_title_5")
        self.bt_title_5.setFont(font)
        self.bt_title_5.setStyleSheet(u"QPushButton{\n"
"font-size:11pt;\n"
"border: none;\n"
"color:white;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/Resources/icons/icon_info_grey.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_title_5.setIcon(icon2)
        self.bt_title_5.setIconSize(QSize(25, 25))

        self.horizontalLayout_4.addWidget(self.bt_title_5)

        self.label_name_1 = QLabel(self.groupBox_1)
        self.label_name_1.setObjectName(u"label_name_1")

        self.horizontalLayout_4.addWidget(self.label_name_1)

        self.m_edt_CompareName_1 = QLineEdit(self.groupBox_1)
        self.m_edt_CompareName_1.setObjectName(u"m_edt_CompareName_1")
        self.m_edt_CompareName_1.setStyleSheet(u"QLineEdit{\n"
"background-color:rgba(248, 248, 248, 220);\n"
"} ")

        self.horizontalLayout_4.addWidget(self.m_edt_CompareName_1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_SyndromePic_1 = QLabel(self.groupBox_1)
        self.label_SyndromePic_1.setObjectName(u"label_SyndromePic_1")
        self.label_SyndromePic_1.setMinimumSize(QSize(100, 100))
        self.label_SyndromePic_1.setMaximumSize(QSize(100, 100))
        self.label_SyndromePic_1.setStyleSheet(u"QLabel{\n"
"background-color: rgba(255, 255, 255,120);\n"
"border:2px solid rgb(190, 190, 190); \n"
"} ")

        self.horizontalLayout.addWidget(self.label_SyndromePic_1)

        self.label_SyndromePic_2 = QLabel(self.groupBox_1)
        self.label_SyndromePic_2.setObjectName(u"label_SyndromePic_2")
        self.label_SyndromePic_2.setMinimumSize(QSize(100, 100))
        self.label_SyndromePic_2.setMaximumSize(QSize(100, 100))
        self.label_SyndromePic_2.setStyleSheet(u"QLabel{\n"
"background-color: rgba(255, 255, 255,120);\n"
"border:2px solid rgb(190, 190, 190); \n"
"} ")

        self.horizontalLayout.addWidget(self.label_SyndromePic_2)

        self.label_SyndromePic_3 = QLabel(self.groupBox_1)
        self.label_SyndromePic_3.setObjectName(u"label_SyndromePic_3")
        self.label_SyndromePic_3.setMinimumSize(QSize(100, 100))
        self.label_SyndromePic_3.setMaximumSize(QSize(100, 100))
        self.label_SyndromePic_3.setStyleSheet(u"QLabel{\n"
"background-color: rgba(255, 255, 255,120);\n"
"border:2px solid rgb(190, 190, 190); \n"
"} ")

        self.horizontalLayout.addWidget(self.label_SyndromePic_3)

        self.label_SyndromePic_4 = QLabel(self.groupBox_1)
        self.label_SyndromePic_4.setObjectName(u"label_SyndromePic_4")
        self.label_SyndromePic_4.setMinimumSize(QSize(100, 100))
        self.label_SyndromePic_4.setMaximumSize(QSize(100, 100))
        self.label_SyndromePic_4.setStyleSheet(u"QLabel{\n"
"background-color: rgba(255, 255, 255,120);\n"
"border:2px solid rgb(190, 190, 190); \n"
"} ")

        self.horizontalLayout.addWidget(self.label_SyndromePic_4)

        self.label_SyndromePic_5 = QLabel(self.groupBox_1)
        self.label_SyndromePic_5.setObjectName(u"label_SyndromePic_5")
        self.label_SyndromePic_5.setMinimumSize(QSize(100, 100))
        self.label_SyndromePic_5.setMaximumSize(QSize(100, 100))
        self.label_SyndromePic_5.setStyleSheet(u"QLabel{\n"
"background-color: rgba(255, 255, 255,120);\n"
"border:2px solid rgb(190, 190, 190); \n"
"} ")

        self.horizontalLayout.addWidget(self.label_SyndromePic_5)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_diagnosis_1 = QLabel(self.groupBox_1)
        self.label_diagnosis_1.setObjectName(u"label_diagnosis_1")

        self.horizontalLayout_3.addWidget(self.label_diagnosis_1)

        self.m_edt_diagnosis_1 = QTextEdit(self.groupBox_1)
        self.m_edt_diagnosis_1.setObjectName(u"m_edt_diagnosis_1")
        self.m_edt_diagnosis_1.setMaximumSize(QSize(16777215, 40))
        self.m_edt_diagnosis_1.setStyleSheet(u"QTextEdit{\n"
"background-color:rgba(248, 248, 248, 220);\n"
"} ")

        self.horizontalLayout_3.addWidget(self.m_edt_diagnosis_1)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_sympt_1 = QLabel(self.groupBox_1)
        self.label_sympt_1.setObjectName(u"label_sympt_1")

        self.horizontalLayout_2.addWidget(self.label_sympt_1)

        self.m_edt_sysmpt_1 = QTextEdit(self.groupBox_1)
        self.m_edt_sysmpt_1.setObjectName(u"m_edt_sysmpt_1")
        self.m_edt_sysmpt_1.setStyleSheet(u"QTextEdit{\n"
"background-color:rgba(248, 248, 248, 220);\n"
"} ")

        self.horizontalLayout_2.addWidget(self.m_edt_sysmpt_1)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_Analysis_1 = QLabel(self.groupBox_1)
        self.label_Analysis_1.setObjectName(u"label_Analysis_1")

        self.horizontalLayout_5.addWidget(self.label_Analysis_1)

        self.m_edt_Analysis_1 = QTextEdit(self.groupBox_1)
        self.m_edt_Analysis_1.setObjectName(u"m_edt_Analysis_1")
        self.m_edt_Analysis_1.setMaximumSize(QSize(16777215, 40))
        self.m_edt_Analysis_1.setStyleSheet(u"QTextEdit{\n"
"background-color:rgba(248, 248, 248, 220);\n"
"} ")

        self.horizontalLayout_5.addWidget(self.m_edt_Analysis_1)


        self.verticalLayout.addLayout(self.horizontalLayout_5)


        self.verticalLayout_4.addWidget(self.groupBox_1)

        self.groupBox_2 = QGroupBox(self.widget)
        self.groupBox_2.setObjectName(u"groupBox_2")
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
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.bt_title_4 = QPushButton(self.groupBox_2)
        self.bt_title_4.setObjectName(u"bt_title_4")
        self.bt_title_4.setFont(font)
        self.bt_title_4.setStyleSheet(u"QPushButton{\n"
"font-size:11pt;\n"
"border: none;\n"
"color:white;\n"
"}")
        self.bt_title_4.setIcon(icon1)
        self.bt_title_4.setIconSize(QSize(25, 25))

        self.horizontalLayout_6.addWidget(self.bt_title_4)

        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_6.addWidget(self.label_2)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_3)

        self.bt_title_6 = QPushButton(self.groupBox_2)
        self.bt_title_6.setObjectName(u"bt_title_6")
        self.bt_title_6.setFont(font)
        self.bt_title_6.setStyleSheet(u"QPushButton{\n"
"font-size:11pt;\n"
"border: none;\n"
"color:white;\n"
"}")
        self.bt_title_6.setIcon(icon2)
        self.bt_title_6.setIconSize(QSize(25, 25))

        self.horizontalLayout_6.addWidget(self.bt_title_6)

        self.label_name_2 = QLabel(self.groupBox_2)
        self.label_name_2.setObjectName(u"label_name_2")

        self.horizontalLayout_6.addWidget(self.label_name_2)

        self.m_edt_CompareName_2 = QLineEdit(self.groupBox_2)
        self.m_edt_CompareName_2.setObjectName(u"m_edt_CompareName_2")
        self.m_edt_CompareName_2.setStyleSheet(u"QLineEdit{\n"
"background-color:rgba(248, 248, 248, 220);\n"
"} ")

        self.horizontalLayout_6.addWidget(self.m_edt_CompareName_2)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_5)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_SyndromePic_6 = QLabel(self.groupBox_2)
        self.label_SyndromePic_6.setObjectName(u"label_SyndromePic_6")
        self.label_SyndromePic_6.setMinimumSize(QSize(100, 100))
        self.label_SyndromePic_6.setMaximumSize(QSize(100, 100))
        self.label_SyndromePic_6.setStyleSheet(u"QLabel{\n"
"background-color: rgba(255, 255, 255,120);\n"
"border:2px solid rgb(190, 190, 190); \n"
"} ")

        self.horizontalLayout_10.addWidget(self.label_SyndromePic_6)

        self.label_SyndromePic_7 = QLabel(self.groupBox_2)
        self.label_SyndromePic_7.setObjectName(u"label_SyndromePic_7")
        self.label_SyndromePic_7.setMinimumSize(QSize(100, 100))
        self.label_SyndromePic_7.setMaximumSize(QSize(100, 100))
        self.label_SyndromePic_7.setStyleSheet(u"QLabel{\n"
"background-color: rgba(255, 255, 255,120);\n"
"border:2px solid rgb(190, 190, 190); \n"
"} ")

        self.horizontalLayout_10.addWidget(self.label_SyndromePic_7)

        self.label_SyndromePic_8 = QLabel(self.groupBox_2)
        self.label_SyndromePic_8.setObjectName(u"label_SyndromePic_8")
        self.label_SyndromePic_8.setMinimumSize(QSize(100, 100))
        self.label_SyndromePic_8.setMaximumSize(QSize(100, 100))
        self.label_SyndromePic_8.setStyleSheet(u"QLabel{\n"
"background-color: rgba(255, 255, 255,120);\n"
"border:2px solid rgb(190, 190, 190); \n"
"} ")

        self.horizontalLayout_10.addWidget(self.label_SyndromePic_8)

        self.label_SyndromePic_9 = QLabel(self.groupBox_2)
        self.label_SyndromePic_9.setObjectName(u"label_SyndromePic_9")
        self.label_SyndromePic_9.setMinimumSize(QSize(100, 100))
        self.label_SyndromePic_9.setMaximumSize(QSize(100, 100))
        self.label_SyndromePic_9.setStyleSheet(u"QLabel{\n"
"background-color: rgba(255, 255, 255,120);\n"
"border:2px solid rgb(190, 190, 190); \n"
"} ")

        self.horizontalLayout_10.addWidget(self.label_SyndromePic_9)

        self.label_SyndromePic_10 = QLabel(self.groupBox_2)
        self.label_SyndromePic_10.setObjectName(u"label_SyndromePic_10")
        self.label_SyndromePic_10.setMinimumSize(QSize(100, 100))
        self.label_SyndromePic_10.setMaximumSize(QSize(100, 100))
        self.label_SyndromePic_10.setStyleSheet(u"QLabel{\n"
"background-color: rgba(255, 255, 255,120);\n"
"border:2px solid rgb(190, 190, 190); \n"
"} ")

        self.horizontalLayout_10.addWidget(self.label_SyndromePic_10)


        self.verticalLayout_2.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_diagnosis_2 = QLabel(self.groupBox_2)
        self.label_diagnosis_2.setObjectName(u"label_diagnosis_2")

        self.horizontalLayout_7.addWidget(self.label_diagnosis_2)

        self.m_edt_diagnosis_2 = QTextEdit(self.groupBox_2)
        self.m_edt_diagnosis_2.setObjectName(u"m_edt_diagnosis_2")
        self.m_edt_diagnosis_2.setMaximumSize(QSize(16777215, 40))
        self.m_edt_diagnosis_2.setStyleSheet(u"QTextEdit{\n"
"background-color:rgba(248, 248, 248, 220);\n"
"} ")

        self.horizontalLayout_7.addWidget(self.m_edt_diagnosis_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_sympt_2 = QLabel(self.groupBox_2)
        self.label_sympt_2.setObjectName(u"label_sympt_2")

        self.horizontalLayout_8.addWidget(self.label_sympt_2)

        self.m_edt_sysmpt_2 = QTextEdit(self.groupBox_2)
        self.m_edt_sysmpt_2.setObjectName(u"m_edt_sysmpt_2")
        self.m_edt_sysmpt_2.setStyleSheet(u"QTextEdit{\n"
"background-color:rgba(248, 248, 248, 220);\n"
"} ")

        self.horizontalLayout_8.addWidget(self.m_edt_sysmpt_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_Analysis_2 = QLabel(self.groupBox_2)
        self.label_Analysis_2.setObjectName(u"label_Analysis_2")

        self.horizontalLayout_11.addWidget(self.label_Analysis_2)

        self.m_edt_Analysis_2 = QTextEdit(self.groupBox_2)
        self.m_edt_Analysis_2.setObjectName(u"m_edt_Analysis_2")
        self.m_edt_Analysis_2.setMaximumSize(QSize(16777215, 40))
        self.m_edt_Analysis_2.setStyleSheet(u"QTextEdit{\n"
"background-color:rgba(248, 248, 248, 220);\n"
"} ")

        self.horizontalLayout_11.addWidget(self.m_edt_Analysis_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_11)


        self.verticalLayout_4.addWidget(self.groupBox_2)

        self.splitter.addWidget(self.widget)
        self.groupBox_3 = QGroupBox(self.splitter)
        self.groupBox_3.setObjectName(u"groupBox_3")
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
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.m_tle_PatientList = QTableWidget(self.groupBox_3)
        if (self.m_tle_PatientList.columnCount() < 60):
            self.m_tle_PatientList.setColumnCount(60)
        __qtablewidgetitem = QTableWidgetItem()
        self.m_tle_PatientList.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.m_tle_PatientList.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.m_tle_PatientList.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.m_tle_PatientList.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.m_tle_PatientList.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.m_tle_PatientList.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.m_tle_PatientList.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.m_tle_PatientList.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.m_tle_PatientList.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.m_tle_PatientList.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.m_tle_PatientList.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.m_tle_PatientList.setHorizontalHeaderItem(11, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.m_tle_PatientList.setHorizontalHeaderItem(12, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.m_tle_PatientList.setHorizontalHeaderItem(13, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.m_tle_PatientList.setHorizontalHeaderItem(14, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.m_tle_PatientList.setHorizontalHeaderItem(15, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.m_tle_PatientList.setHorizontalHeaderItem(16, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.m_tle_PatientList.setHorizontalHeaderItem(17, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.m_tle_PatientList.setHorizontalHeaderItem(18, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.m_tle_PatientList.setHorizontalHeaderItem(19, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.m_tle_PatientList.setHorizontalHeaderItem(20, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.m_tle_PatientList.setHorizontalHeaderItem(21, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.m_tle_PatientList.setHorizontalHeaderItem(22, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.m_tle_PatientList.setHorizontalHeaderItem(23, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.m_tle_PatientList.setHorizontalHeaderItem(24, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.m_tle_PatientList.setHorizontalHeaderItem(25, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.m_tle_PatientList.setHorizontalHeaderItem(26, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.m_tle_PatientList.setHorizontalHeaderItem(27, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.m_tle_PatientList.setHorizontalHeaderItem(28, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.m_tle_PatientList.setHorizontalHeaderItem(29, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.m_tle_PatientList.setHorizontalHeaderItem(30, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.m_tle_PatientList.setHorizontalHeaderItem(31, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.m_tle_PatientList.setHorizontalHeaderItem(32, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.m_tle_PatientList.setHorizontalHeaderItem(33, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.m_tle_PatientList.setHorizontalHeaderItem(34, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.m_tle_PatientList.setHorizontalHeaderItem(35, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.m_tle_PatientList.setHorizontalHeaderItem(36, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.m_tle_PatientList.setHorizontalHeaderItem(37, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.m_tle_PatientList.setHorizontalHeaderItem(38, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.m_tle_PatientList.setHorizontalHeaderItem(39, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.m_tle_PatientList.setHorizontalHeaderItem(40, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.m_tle_PatientList.setHorizontalHeaderItem(41, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        self.m_tle_PatientList.setHorizontalHeaderItem(42, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        self.m_tle_PatientList.setHorizontalHeaderItem(43, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        self.m_tle_PatientList.setHorizontalHeaderItem(44, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        self.m_tle_PatientList.setHorizontalHeaderItem(45, __qtablewidgetitem45)
        __qtablewidgetitem46 = QTableWidgetItem()
        self.m_tle_PatientList.setHorizontalHeaderItem(46, __qtablewidgetitem46)
        __qtablewidgetitem47 = QTableWidgetItem()
        self.m_tle_PatientList.setHorizontalHeaderItem(47, __qtablewidgetitem47)
        __qtablewidgetitem48 = QTableWidgetItem()
        self.m_tle_PatientList.setHorizontalHeaderItem(48, __qtablewidgetitem48)
        __qtablewidgetitem49 = QTableWidgetItem()
        self.m_tle_PatientList.setHorizontalHeaderItem(49, __qtablewidgetitem49)
        __qtablewidgetitem50 = QTableWidgetItem()
        self.m_tle_PatientList.setHorizontalHeaderItem(50, __qtablewidgetitem50)
        __qtablewidgetitem51 = QTableWidgetItem()
        self.m_tle_PatientList.setHorizontalHeaderItem(51, __qtablewidgetitem51)
        __qtablewidgetitem52 = QTableWidgetItem()
        self.m_tle_PatientList.setHorizontalHeaderItem(52, __qtablewidgetitem52)
        __qtablewidgetitem53 = QTableWidgetItem()
        self.m_tle_PatientList.setHorizontalHeaderItem(53, __qtablewidgetitem53)
        __qtablewidgetitem54 = QTableWidgetItem()
        self.m_tle_PatientList.setHorizontalHeaderItem(54, __qtablewidgetitem54)
        __qtablewidgetitem55 = QTableWidgetItem()
        self.m_tle_PatientList.setHorizontalHeaderItem(55, __qtablewidgetitem55)
        __qtablewidgetitem56 = QTableWidgetItem()
        self.m_tle_PatientList.setHorizontalHeaderItem(56, __qtablewidgetitem56)
        __qtablewidgetitem57 = QTableWidgetItem()
        self.m_tle_PatientList.setHorizontalHeaderItem(57, __qtablewidgetitem57)
        __qtablewidgetitem58 = QTableWidgetItem()
        self.m_tle_PatientList.setHorizontalHeaderItem(58, __qtablewidgetitem58)
        __qtablewidgetitem59 = QTableWidgetItem()
        self.m_tle_PatientList.setHorizontalHeaderItem(59, __qtablewidgetitem59)
        self.m_tle_PatientList.setObjectName(u"m_tle_PatientList")
        self.m_tle_PatientList.setStyleSheet(u"QTableWidget{\n"
"background-color:rgba(248, 248, 248, 220);\n"
"} ")

        self.verticalLayout_3.addWidget(self.m_tle_PatientList)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.bt_searchicon = QPushButton(self.groupBox_3)
        self.bt_searchicon.setObjectName(u"bt_searchicon")
        self.bt_searchicon.setFont(font)
        self.bt_searchicon.setStyleSheet(u"QPushButton{\n"
"font-size:11pt;\n"
"border: none;\n"
"color:white;\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/Resources/icons/icon_search.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_searchicon.setIcon(icon3)
        self.bt_searchicon.setIconSize(QSize(25, 25))

        self.horizontalLayout_9.addWidget(self.bt_searchicon)

        self.m_edt_searchpatient = QLineEdit(self.groupBox_3)
        self.m_edt_searchpatient.setObjectName(u"m_edt_searchpatient")
        self.m_edt_searchpatient.setStyleSheet(u"QLineEdit { \n"
"background-color:rgba(248, 248, 248, 220);\n"
"font-size: 11pt; }\n"
"")

        self.horizontalLayout_9.addWidget(self.m_edt_searchpatient)

        self.label_3 = QLabel(self.groupBox_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"QLabel { \n"
"color: grey;\n"
"font-size: 11pt; }\n"
"")

        self.horizontalLayout_9.addWidget(self.label_3)

        self.m_bt_compare = QPushButton(self.groupBox_3)
        self.m_bt_compare.setObjectName(u"m_bt_compare")

        self.horizontalLayout_9.addWidget(self.m_bt_compare)


        self.verticalLayout_3.addLayout(self.horizontalLayout_9)

        self.splitter.addWidget(self.groupBox_3)

        self.horizontalLayout_12.addWidget(self.splitter)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u60a3\u8005\u8d44\u6599\u53ca\u75c5\u5386\u6bd4\u8f83", None))
        self.groupBox_1.setTitle("")
        self.bt_title_3.setText("")
        self.label.setText(QCoreApplication.translate("Dialog", u"\u6bd4\u8f83\u5bf9\u8c61\uff1a\u7532", None))
        self.bt_title_5.setText("")
        self.label_name_1.setText(QCoreApplication.translate("Dialog", u"\u59d3\u540d", None))
        self.label_SyndromePic_1.setText("")
        self.label_SyndromePic_2.setText("")
        self.label_SyndromePic_3.setText("")
        self.label_SyndromePic_4.setText("")
        self.label_SyndromePic_5.setText("")
        self.label_diagnosis_1.setText(QCoreApplication.translate("Dialog", u"\u8bca\n"
"\u65ad", None))
        self.label_sympt_1.setText(QCoreApplication.translate("Dialog", u"\u75c5\n"
"\u8bc1", None))
        self.label_Analysis_1.setText(QCoreApplication.translate("Dialog", u"\u8fa8\n"
"\u8bc1", None))
        self.groupBox_2.setTitle("")
        self.bt_title_4.setText("")
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u6bd4\u8f83\u5bf9\u8c61\uff1a\u4e59", None))
        self.bt_title_6.setText("")
        self.label_name_2.setText(QCoreApplication.translate("Dialog", u"\u59d3\u540d", None))
        self.label_SyndromePic_6.setText("")
        self.label_SyndromePic_7.setText("")
        self.label_SyndromePic_8.setText("")
        self.label_SyndromePic_9.setText("")
        self.label_SyndromePic_10.setText("")
        self.label_diagnosis_2.setText(QCoreApplication.translate("Dialog", u"\u8bca\n"
"\u65ad", None))
        self.label_sympt_2.setText(QCoreApplication.translate("Dialog", u"\u75c5\n"
"\u8bc1", None))
        self.label_Analysis_2.setText(QCoreApplication.translate("Dialog", u"\u8fa8\n"
"\u8bc1", None))
        self.groupBox_3.setTitle("")
        ___qtablewidgetitem = self.m_tle_PatientList.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Dialog", u"\u7f16\u53f7", None));
        ___qtablewidgetitem1 = self.m_tle_PatientList.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Dialog", u"\u59d3\u540d", None));
        ___qtablewidgetitem2 = self.m_tle_PatientList.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Dialog", u"\u65e5\u671f\u65f6\u95f4", None));
        ___qtablewidgetitem3 = self.m_tle_PatientList.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Dialog", u"\u8bca\u65ad", None));
        ___qtablewidgetitem4 = self.m_tle_PatientList.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Dialog", u"\u75c5\u8bc1", None));
        ___qtablewidgetitem5 = self.m_tle_PatientList.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Dialog", u"\u8840\u538b", None));
        ___qtablewidgetitem6 = self.m_tle_PatientList.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Dialog", u"\u8fa9\u8bc1", None));
        ___qtablewidgetitem7 = self.m_tle_PatientList.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Dialog", u"\u9488\u7078\u6216\u5176\u4ed6", None));
        ___qtablewidgetitem8 = self.m_tle_PatientList.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Dialog", u"\u836f\u72691", None));
        ___qtablewidgetitem9 = self.m_tle_PatientList.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Dialog", u"\u836f\u72692", None));
        ___qtablewidgetitem10 = self.m_tle_PatientList.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("Dialog", u"\u836f\u72693", None));
        ___qtablewidgetitem11 = self.m_tle_PatientList.horizontalHeaderItem(11)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("Dialog", u"\u836f\u72694", None));
        ___qtablewidgetitem12 = self.m_tle_PatientList.horizontalHeaderItem(12)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("Dialog", u"\u836f\u72695", None));
        ___qtablewidgetitem13 = self.m_tle_PatientList.horizontalHeaderItem(13)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("Dialog", u"\u836f\u72696", None));
        ___qtablewidgetitem14 = self.m_tle_PatientList.horizontalHeaderItem(14)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("Dialog", u"\u836f\u72697", None));
        ___qtablewidgetitem15 = self.m_tle_PatientList.horizontalHeaderItem(15)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("Dialog", u"\u836f\u72698", None));
        ___qtablewidgetitem16 = self.m_tle_PatientList.horizontalHeaderItem(16)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("Dialog", u"\u836f\u72699", None));
        ___qtablewidgetitem17 = self.m_tle_PatientList.horizontalHeaderItem(17)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("Dialog", u"\u836f\u726910", None));
        ___qtablewidgetitem18 = self.m_tle_PatientList.horizontalHeaderItem(18)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("Dialog", u"\u836f\u726911", None));
        ___qtablewidgetitem19 = self.m_tle_PatientList.horizontalHeaderItem(19)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("Dialog", u"\u836f\u726912", None));
        ___qtablewidgetitem20 = self.m_tle_PatientList.horizontalHeaderItem(20)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("Dialog", u"\u836f\u726913", None));
        ___qtablewidgetitem21 = self.m_tle_PatientList.horizontalHeaderItem(21)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("Dialog", u"\u836f\u726914", None));
        ___qtablewidgetitem22 = self.m_tle_PatientList.horizontalHeaderItem(22)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("Dialog", u"\u836f\u726915", None));
        ___qtablewidgetitem23 = self.m_tle_PatientList.horizontalHeaderItem(23)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("Dialog", u"\u836f\u726916", None));
        ___qtablewidgetitem24 = self.m_tle_PatientList.horizontalHeaderItem(24)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("Dialog", u"\u836f\u726917", None));
        ___qtablewidgetitem25 = self.m_tle_PatientList.horizontalHeaderItem(25)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("Dialog", u"\u836f\u726918", None));
        ___qtablewidgetitem26 = self.m_tle_PatientList.horizontalHeaderItem(26)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("Dialog", u"\u836f\u726919", None));
        ___qtablewidgetitem27 = self.m_tle_PatientList.horizontalHeaderItem(27)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("Dialog", u"\u836f\u726920", None));
        ___qtablewidgetitem28 = self.m_tle_PatientList.horizontalHeaderItem(28)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("Dialog", u"\u7528\u91cf1", None));
        ___qtablewidgetitem29 = self.m_tle_PatientList.horizontalHeaderItem(29)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("Dialog", u"\u7528\u91cf2", None));
        ___qtablewidgetitem30 = self.m_tle_PatientList.horizontalHeaderItem(30)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("Dialog", u"\u7528\u91cf3", None));
        ___qtablewidgetitem31 = self.m_tle_PatientList.horizontalHeaderItem(31)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("Dialog", u"\u7528\u91cf4", None));
        ___qtablewidgetitem32 = self.m_tle_PatientList.horizontalHeaderItem(32)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("Dialog", u"\u7528\u91cf5", None));
        ___qtablewidgetitem33 = self.m_tle_PatientList.horizontalHeaderItem(33)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("Dialog", u"\u7528\u91cf6", None));
        ___qtablewidgetitem34 = self.m_tle_PatientList.horizontalHeaderItem(34)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("Dialog", u"\u7528\u91cf7", None));
        ___qtablewidgetitem35 = self.m_tle_PatientList.horizontalHeaderItem(35)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("Dialog", u"\u7528\u91cf8", None));
        ___qtablewidgetitem36 = self.m_tle_PatientList.horizontalHeaderItem(36)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("Dialog", u"\u7528\u91cf9", None));
        ___qtablewidgetitem37 = self.m_tle_PatientList.horizontalHeaderItem(37)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("Dialog", u"\u7528\u91cf10", None));
        ___qtablewidgetitem38 = self.m_tle_PatientList.horizontalHeaderItem(38)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("Dialog", u"\u7528\u91cf11", None));
        ___qtablewidgetitem39 = self.m_tle_PatientList.horizontalHeaderItem(39)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("Dialog", u"\u7528\u91cf12", None));
        ___qtablewidgetitem40 = self.m_tle_PatientList.horizontalHeaderItem(40)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("Dialog", u"\u7528\u91cf13", None));
        ___qtablewidgetitem41 = self.m_tle_PatientList.horizontalHeaderItem(41)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("Dialog", u"\u7528\u91cf14", None));
        ___qtablewidgetitem42 = self.m_tle_PatientList.horizontalHeaderItem(42)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("Dialog", u"\u7528\u91cf15", None));
        ___qtablewidgetitem43 = self.m_tle_PatientList.horizontalHeaderItem(43)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("Dialog", u"\u7528\u91cf16", None));
        ___qtablewidgetitem44 = self.m_tle_PatientList.horizontalHeaderItem(44)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("Dialog", u"\u7528\u91cf17", None));
        ___qtablewidgetitem45 = self.m_tle_PatientList.horizontalHeaderItem(45)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("Dialog", u"\u7528\u91cf18", None));
        ___qtablewidgetitem46 = self.m_tle_PatientList.horizontalHeaderItem(46)
        ___qtablewidgetitem46.setText(QCoreApplication.translate("Dialog", u"\u7528\u91cf19", None));
        ___qtablewidgetitem47 = self.m_tle_PatientList.horizontalHeaderItem(47)
        ___qtablewidgetitem47.setText(QCoreApplication.translate("Dialog", u"\u7528\u91cf20", None));
        ___qtablewidgetitem48 = self.m_tle_PatientList.horizontalHeaderItem(48)
        ___qtablewidgetitem48.setText(QCoreApplication.translate("Dialog", u"\u8bca\u91d1", None));
        ___qtablewidgetitem49 = self.m_tle_PatientList.horizontalHeaderItem(49)
        ___qtablewidgetitem49.setText(QCoreApplication.translate("Dialog", u"\u836f\u8d39", None));
        ___qtablewidgetitem50 = self.m_tle_PatientList.horizontalHeaderItem(50)
        ___qtablewidgetitem50.setText(QCoreApplication.translate("Dialog", u"\u9488\u7078\u8d39\u7528", None));
        ___qtablewidgetitem51 = self.m_tle_PatientList.horizontalHeaderItem(51)
        ___qtablewidgetitem51.setText(QCoreApplication.translate("Dialog", u"\u8fa9\u8bc1", None));
        ___qtablewidgetitem52 = self.m_tle_PatientList.horizontalHeaderItem(52)
        ___qtablewidgetitem52.setText(QCoreApplication.translate("Dialog", u"\u603b\u8d39\u7528", None));
        ___qtablewidgetitem53 = self.m_tle_PatientList.horizontalHeaderItem(53)
        ___qtablewidgetitem53.setText(QCoreApplication.translate("Dialog", u"\u9488\u7078\u6216\u5176\u4ed6", None));
        ___qtablewidgetitem54 = self.m_tle_PatientList.horizontalHeaderItem(54)
        ___qtablewidgetitem54.setText(QCoreApplication.translate("Dialog", u"\u5907\u6ce8", None));
        ___qtablewidgetitem55 = self.m_tle_PatientList.horizontalHeaderItem(55)
        ___qtablewidgetitem55.setText(QCoreApplication.translate("Dialog", u"\u75c5\u8bc1\u7167\u72471", None));
        ___qtablewidgetitem56 = self.m_tle_PatientList.horizontalHeaderItem(56)
        ___qtablewidgetitem56.setText(QCoreApplication.translate("Dialog", u"\u75c5\u8bc1\u7167\u72472", None));
        ___qtablewidgetitem57 = self.m_tle_PatientList.horizontalHeaderItem(57)
        ___qtablewidgetitem57.setText(QCoreApplication.translate("Dialog", u"\u75c5\u8bc1\u7167\u72473", None));
        ___qtablewidgetitem58 = self.m_tle_PatientList.horizontalHeaderItem(58)
        ___qtablewidgetitem58.setText(QCoreApplication.translate("Dialog", u"\u75c5\u8bc1\u7167\u72475", None));
        ___qtablewidgetitem59 = self.m_tle_PatientList.horizontalHeaderItem(59)
        ___qtablewidgetitem59.setText(QCoreApplication.translate("Dialog", u"\u4e3b\u6cbb\u533b\u751f", None));
        self.bt_searchicon.setText("")
        self.m_edt_searchpatient.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u8f93\u5165\u4efb\u610f\u5173\u952e\u5b57", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u6ce8\uff1a\u9009\u4e2d\u4e24\u884c\u6bd4\u8f83", None))
        self.m_bt_compare.setText(QCoreApplication.translate("Dialog", u"\u75c5\u5386\u6bd4\u8f83", None))
    # retranslateUi

