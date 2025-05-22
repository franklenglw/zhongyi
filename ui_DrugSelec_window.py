# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DrugSelec_window.ui'
##
## Created by: Qt User Interface Compiler version 6.1.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

import resources_rc

class Ui_DialogDrugSelec(object):
    def setupUi(self, DialogDrugSelec):
        if not DialogDrugSelec.objectName():
            DialogDrugSelec.setObjectName(u"DialogDrugSelec")
        DialogDrugSelec.resize(1017, 866)
        DialogDrugSelec.setMinimumSize(QSize(0, 600))
        DialogDrugSelec.setMaximumSize(QSize(1440, 1200))
        icon = QIcon()
        icon.addFile(u":/Resources/icons/logo.ico", QSize(), QIcon.Normal, QIcon.Off)
        DialogDrugSelec.setWindowIcon(icon)
        self.horizontalLayout_8 = QHBoxLayout(DialogDrugSelec)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.splitter = QSplitter(DialogDrugSelec)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.groupBox_5 = QGroupBox(self.splitter)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setMinimumSize(QSize(0, 0))
        self.groupBox_5.setStyleSheet(u"    QGroupBox {\n"
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
        self.verticalLayout_7 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.m_tabWidget_Fomula = QTabWidget(self.groupBox_5)
        self.m_tabWidget_Fomula.setObjectName(u"m_tabWidget_Fomula")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.m_tabWidget_Fomula.setFont(font)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_6 = QVBoxLayout(self.tab)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.m_tle_ExpdFormula = QTableWidget(self.tab)
        if (self.m_tle_ExpdFormula.columnCount() < 2):
            self.m_tle_ExpdFormula.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.m_tle_ExpdFormula.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.m_tle_ExpdFormula.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.m_tle_ExpdFormula.setObjectName(u"m_tle_ExpdFormula")
        self.m_tle_ExpdFormula.setStyleSheet(u"QTableWidget{\n"
"background-color:rgba(248, 248, 248, 220);\n"
"} ")
        self.m_tle_ExpdFormula.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_3.addWidget(self.m_tle_ExpdFormula)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.bt_searchicon_2 = QPushButton(self.tab)
        self.bt_searchicon_2.setObjectName(u"bt_searchicon_2")
        font1 = QFont()
        font1.setPointSize(11)
        font1.setBold(True)
        self.bt_searchicon_2.setFont(font1)
        self.bt_searchicon_2.setStyleSheet(u"QPushButton{\n"
"font-size:11pt;\n"
"border: none;\n"
"color:white;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/Resources/icons/icon_search.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_searchicon_2.setIcon(icon1)
        self.bt_searchicon_2.setIconSize(QSize(25, 25))

        self.horizontalLayout_6.addWidget(self.bt_searchicon_2)

        self.m_edt_FormulaSearch = QLineEdit(self.tab)
        self.m_edt_FormulaSearch.setObjectName(u"m_edt_FormulaSearch")

        self.horizontalLayout_6.addWidget(self.m_edt_FormulaSearch)


        self.verticalLayout_3.addLayout(self.horizontalLayout_6)


        self.verticalLayout_6.addLayout(self.verticalLayout_3)

        self.m_tabWidget_Fomula.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_7 = QGridLayout(self.tab_2)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.m_tle_DisFormula = QTableWidget(self.tab_2)
        if (self.m_tle_DisFormula.columnCount() < 2):
            self.m_tle_DisFormula.setColumnCount(2)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.m_tle_DisFormula.setHorizontalHeaderItem(0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.m_tle_DisFormula.setHorizontalHeaderItem(1, __qtablewidgetitem3)
        self.m_tle_DisFormula.setObjectName(u"m_tle_DisFormula")
        self.m_tle_DisFormula.setStyleSheet(u"QTableWidget{\n"
"background-color:rgba(248, 248, 248, 220);\n"
"} ")
        self.m_tle_DisFormula.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_4.addWidget(self.m_tle_DisFormula)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.bt_searchicon_3 = QPushButton(self.tab_2)
        self.bt_searchicon_3.setObjectName(u"bt_searchicon_3")
        self.bt_searchicon_3.setFont(font1)
        self.bt_searchicon_3.setStyleSheet(u"QPushButton{\n"
"font-size:11pt;\n"
"border: none;\n"
"color:white;\n"
"}")
        self.bt_searchicon_3.setIcon(icon1)
        self.bt_searchicon_3.setIconSize(QSize(25, 25))

        self.horizontalLayout_5.addWidget(self.bt_searchicon_3)

        self.m_edt_FormulaSearch_2 = QLineEdit(self.tab_2)
        self.m_edt_FormulaSearch_2.setObjectName(u"m_edt_FormulaSearch_2")

        self.horizontalLayout_5.addWidget(self.m_edt_FormulaSearch_2)


        self.verticalLayout_4.addLayout(self.horizontalLayout_5)


        self.gridLayout_7.addLayout(self.verticalLayout_4, 0, 0, 1, 1)

        self.m_tabWidget_Fomula.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout_8 = QGridLayout(self.tab_3)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.m_tle_ClassicFormula = QTableWidget(self.tab_3)
        if (self.m_tle_ClassicFormula.columnCount() < 2):
            self.m_tle_ClassicFormula.setColumnCount(2)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.m_tle_ClassicFormula.setHorizontalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.m_tle_ClassicFormula.setHorizontalHeaderItem(1, __qtablewidgetitem5)
        self.m_tle_ClassicFormula.setObjectName(u"m_tle_ClassicFormula")
        self.m_tle_ClassicFormula.setStyleSheet(u"QTableWidget{\n"
"background-color:rgba(248, 248, 248, 220);\n"
"} ")
        self.m_tle_ClassicFormula.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_5.addWidget(self.m_tle_ClassicFormula)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.bt_searchicon_4 = QPushButton(self.tab_3)
        self.bt_searchicon_4.setObjectName(u"bt_searchicon_4")
        self.bt_searchicon_4.setFont(font1)
        self.bt_searchicon_4.setStyleSheet(u"QPushButton{\n"
"font-size:11pt;\n"
"border: none;\n"
"color:white;\n"
"}")
        self.bt_searchicon_4.setIcon(icon1)
        self.bt_searchicon_4.setIconSize(QSize(25, 25))

        self.horizontalLayout_4.addWidget(self.bt_searchicon_4)

        self.m_edt_FormulaSearch_3 = QLineEdit(self.tab_3)
        self.m_edt_FormulaSearch_3.setObjectName(u"m_edt_FormulaSearch_3")

        self.horizontalLayout_4.addWidget(self.m_edt_FormulaSearch_3)


        self.verticalLayout_5.addLayout(self.horizontalLayout_4)


        self.gridLayout_8.addLayout(self.verticalLayout_5, 0, 0, 1, 1)

        self.m_tabWidget_Fomula.addTab(self.tab_3, "")

        self.verticalLayout_7.addWidget(self.m_tabWidget_Fomula)

        self.line = QFrame(self.groupBox_5)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_7.addWidget(self.line)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer_7 = QSpacerItem(118, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_7)

        self.label_5 = QLabel(self.groupBox_5)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_7.addWidget(self.label_5)

        self.horizontalSpacer_8 = QSpacerItem(138, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_8)


        self.verticalLayout_7.addLayout(self.horizontalLayout_7)

        self.m_edt_DrugDiscrip = QTextEdit(self.groupBox_5)
        self.m_edt_DrugDiscrip.setObjectName(u"m_edt_DrugDiscrip")
        self.m_edt_DrugDiscrip.setFont(font)
        self.m_edt_DrugDiscrip.setStyleSheet(u"QTextEdit{\n"
"background-color:rgba(248, 248, 248, 220);\n"
"} ")

        self.verticalLayout_7.addWidget(self.m_edt_DrugDiscrip)

        self.splitter.addWidget(self.groupBox_5)
        self.groupBox_6 = QGroupBox(self.splitter)
        self.groupBox_6.setObjectName(u"groupBox_6")
        font2 = QFont()
        font2.setPointSize(12)
        self.groupBox_6.setFont(font2)
        self.groupBox_6.setStyleSheet(u"    QGroupBox {\n"
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
        self.gridLayout_2 = QGridLayout(self.groupBox_6)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.m_tle_FormulaDrugComb = QTableWidget(self.groupBox_6)
        if (self.m_tle_FormulaDrugComb.columnCount() < 3):
            self.m_tle_FormulaDrugComb.setColumnCount(3)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.m_tle_FormulaDrugComb.setHorizontalHeaderItem(0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.m_tle_FormulaDrugComb.setHorizontalHeaderItem(1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.m_tle_FormulaDrugComb.setHorizontalHeaderItem(2, __qtablewidgetitem8)
        self.m_tle_FormulaDrugComb.setObjectName(u"m_tle_FormulaDrugComb")
        self.m_tle_FormulaDrugComb.setStyleSheet(u"QTableWidget{\n"
"background-color:rgba(248, 248, 248, 220);\n"
"} ")
        self.m_tle_FormulaDrugComb.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_2.addWidget(self.m_tle_FormulaDrugComb)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.DownArrow = QPushButton(self.groupBox_6)
        self.DownArrow.setObjectName(u"DownArrow")
        self.DownArrow.setFont(font)
        self.DownArrow.setStyleSheet(u"QPushButton{\n"
"border: none;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/Resources/icons/icon_downarrow.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.DownArrow.setIcon(icon2)
        self.DownArrow.setIconSize(QSize(30, 30))

        self.horizontalLayout_3.addWidget(self.DownArrow)

        self.m_bt_AddtoBt = QPushButton(self.groupBox_6)
        self.m_bt_AddtoBt.setObjectName(u"m_bt_AddtoBt")
        self.m_bt_AddtoBt.setStyleSheet(u"QPushButton {\n"
"                /* \u57fa\u7840\u53c2\u6570 */\n"
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
"                    stop:0 rgba(255, 255, 255, 0.95),\n"
"         "
                        "           stop:0.4 rgba(201, 237, 58, 0.86),\n"
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
"            }")

        self.horizontalLayout_3.addWidget(self.m_bt_AddtoBt)

        self.horizontalSpacer_3 = QSpacerItem(58, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.m_bt_AddtoBt_2 = QPushButton(self.groupBox_6)
        self.m_bt_AddtoBt_2.setObjectName(u"m_bt_AddtoBt_2")
        self.m_bt_AddtoBt_2.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout_3.addWidget(self.m_bt_AddtoBt_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.m_tle_FormulaDrugComb_2 = QTableWidget(self.groupBox_6)
        if (self.m_tle_FormulaDrugComb_2.columnCount() < 3):
            self.m_tle_FormulaDrugComb_2.setColumnCount(3)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.m_tle_FormulaDrugComb_2.setHorizontalHeaderItem(0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.m_tle_FormulaDrugComb_2.setHorizontalHeaderItem(1, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.m_tle_FormulaDrugComb_2.setHorizontalHeaderItem(2, __qtablewidgetitem11)
        self.m_tle_FormulaDrugComb_2.setObjectName(u"m_tle_FormulaDrugComb_2")
        self.m_tle_FormulaDrugComb_2.setStyleSheet(u"QTableWidget{\n"
"background-color:rgba(248, 248, 248, 220);\n"
"} ")

        self.verticalLayout_2.addWidget(self.m_tle_FormulaDrugComb_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(168, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.m_bt_AddtoBt_3 = QPushButton(self.groupBox_6)
        self.m_bt_AddtoBt_3.setObjectName(u"m_bt_AddtoBt_3")
        self.m_bt_AddtoBt_3.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout_2.addWidget(self.m_bt_AddtoBt_3)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 0, 1, 1)

        self.splitter.addWidget(self.groupBox_6)
        self.groupBox_7 = QGroupBox(self.splitter)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.groupBox_7.setFont(font2)
        self.groupBox_7.setStyleSheet(u"    QGroupBox {\n"
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
        self.gridLayout_4 = QGridLayout(self.groupBox_7)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.m_tle_FormulaSelDruglist = QTableWidget(self.groupBox_7)
        if (self.m_tle_FormulaSelDruglist.columnCount() < 3):
            self.m_tle_FormulaSelDruglist.setColumnCount(3)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.m_tle_FormulaSelDruglist.setHorizontalHeaderItem(0, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.m_tle_FormulaSelDruglist.setHorizontalHeaderItem(1, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.m_tle_FormulaSelDruglist.setHorizontalHeaderItem(2, __qtablewidgetitem14)
        self.m_tle_FormulaSelDruglist.setObjectName(u"m_tle_FormulaSelDruglist")
        font3 = QFont()
        font3.setBold(True)
        self.m_tle_FormulaSelDruglist.setFont(font3)
        self.m_tle_FormulaSelDruglist.setStyleSheet(u"QTableWidget{\n"
"background-color:rgba(248, 248, 248, 220);\n"
"} ")
        self.m_tle_FormulaSelDruglist.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout.addWidget(self.m_tle_FormulaSelDruglist)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.bt_searchicon = QPushButton(self.groupBox_7)
        self.bt_searchicon.setObjectName(u"bt_searchicon")
        self.bt_searchicon.setFont(font1)
        self.bt_searchicon.setStyleSheet(u"QPushButton{\n"
"font-size:11pt;\n"
"border: none;\n"
"color:white;\n"
"}")
        self.bt_searchicon.setIcon(icon1)
        self.bt_searchicon.setIconSize(QSize(25, 25))

        self.horizontalLayout.addWidget(self.bt_searchicon)

        self.m_edt_FormulaSearch_4 = QLineEdit(self.groupBox_7)
        self.m_edt_FormulaSearch_4.setObjectName(u"m_edt_FormulaSearch_4")
        self.m_edt_FormulaSearch_4.setStyleSheet(u"QLineEdit{\n"
"background-color:rgba(248, 248, 248, 220);\n"
"} ")

        self.horizontalLayout.addWidget(self.m_edt_FormulaSearch_4)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.gridLayout_4.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.splitter.addWidget(self.groupBox_7)

        self.horizontalLayout_8.addWidget(self.splitter)


        self.retranslateUi(DialogDrugSelec)

        self.m_tabWidget_Fomula.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(DialogDrugSelec)
    # setupUi

    def retranslateUi(self, DialogDrugSelec):
        DialogDrugSelec.setWindowTitle(QCoreApplication.translate("DialogDrugSelec", u"\u5904\u65b9\u9009\u62e9", None))
        self.groupBox_5.setTitle("")
        ___qtablewidgetitem = self.m_tle_ExpdFormula.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("DialogDrugSelec", u"\u7f16\u53f7", None));
        ___qtablewidgetitem1 = self.m_tle_ExpdFormula.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("DialogDrugSelec", u"\u65b9\u540d", None));
        self.bt_searchicon_2.setText("")
        self.m_edt_FormulaSearch.setPlaceholderText(QCoreApplication.translate("DialogDrugSelec", u"\u8f93\u5165\u62fc\u97f3\u7f29\u5199", None))
        self.m_tabWidget_Fomula.setTabText(self.m_tabWidget_Fomula.indexOf(self.tab), QCoreApplication.translate("DialogDrugSelec", u"\u7ecf\u9a8c\u9009\u65b9", None))
        ___qtablewidgetitem2 = self.m_tle_DisFormula.horizontalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("DialogDrugSelec", u"\u7f16\u53f7", None));
        ___qtablewidgetitem3 = self.m_tle_DisFormula.horizontalHeaderItem(1)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("DialogDrugSelec", u"\u65b9\u540d", None));
        self.bt_searchicon_3.setText("")
        self.m_edt_FormulaSearch_2.setPlaceholderText(QCoreApplication.translate("DialogDrugSelec", u"\u8f93\u5165\u62fc\u97f3\u7f29\u5199", None))
        self.m_tabWidget_Fomula.setTabText(self.m_tabWidget_Fomula.indexOf(self.tab_2), QCoreApplication.translate("DialogDrugSelec", u"\u8fa8\u75c5\u9009\u65b9", None))
        ___qtablewidgetitem4 = self.m_tle_ClassicFormula.horizontalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("DialogDrugSelec", u"\u7f16\u53f7", None));
        ___qtablewidgetitem5 = self.m_tle_ClassicFormula.horizontalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("DialogDrugSelec", u"\u65b9\u540d", None));
        self.bt_searchicon_4.setText("")
        self.m_edt_FormulaSearch_3.setPlaceholderText(QCoreApplication.translate("DialogDrugSelec", u"\u8f93\u5165\u62fc\u97f3\u7f29\u5199", None))
        self.m_tabWidget_Fomula.setTabText(self.m_tabWidget_Fomula.indexOf(self.tab_3), QCoreApplication.translate("DialogDrugSelec", u"\u65b9\u5242\u9009\u65b9", None))
        self.label_5.setText(QCoreApplication.translate("DialogDrugSelec", u"\u65b9\u5242\u8bf4\u660e", None))
        self.groupBox_6.setTitle("")
        ___qtablewidgetitem6 = self.m_tle_FormulaDrugComb.horizontalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("DialogDrugSelec", u"\u7f16\u53f7", None));
        ___qtablewidgetitem7 = self.m_tle_FormulaDrugComb.horizontalHeaderItem(1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("DialogDrugSelec", u"\u836f\u7269", None));
        ___qtablewidgetitem8 = self.m_tle_FormulaDrugComb.horizontalHeaderItem(2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("DialogDrugSelec", u"\u5242\u91cf", None));
        self.DownArrow.setText("")
        self.m_bt_AddtoBt.setText(QCoreApplication.translate("DialogDrugSelec", u"\u5728\u4e0b\u65b9\u5bf9\u6b64\u65b9\u5242\u52a0\u51cf", None))
        self.m_bt_AddtoBt_2.setText(QCoreApplication.translate("DialogDrugSelec", u"\u4f7f\u7528\u6b64\u65b9\u5242", None))
        ___qtablewidgetitem9 = self.m_tle_FormulaDrugComb_2.horizontalHeaderItem(0)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("DialogDrugSelec", u"\u7f16\u53f7", None));
        ___qtablewidgetitem10 = self.m_tle_FormulaDrugComb_2.horizontalHeaderItem(1)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("DialogDrugSelec", u"\u836f\u7269", None));
        ___qtablewidgetitem11 = self.m_tle_FormulaDrugComb_2.horizontalHeaderItem(2)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("DialogDrugSelec", u"\u5242\u91cf", None));
        self.m_bt_AddtoBt_3.setText(QCoreApplication.translate("DialogDrugSelec", u"\u4f7f\u7528\u6b64\u52a0\u51cf\u540e\u7684\u65b9\u5242", None))
        self.groupBox_7.setTitle("")
        ___qtablewidgetitem12 = self.m_tle_FormulaSelDruglist.horizontalHeaderItem(0)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("DialogDrugSelec", u"\u7f16\u53f7", None));
        ___qtablewidgetitem13 = self.m_tle_FormulaSelDruglist.horizontalHeaderItem(1)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("DialogDrugSelec", u"\u836f\u540d", None));
        ___qtablewidgetitem14 = self.m_tle_FormulaSelDruglist.horizontalHeaderItem(2)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("DialogDrugSelec", u"\u4ef7\u683c", None));
        self.bt_searchicon.setText("")
        self.m_edt_FormulaSearch_4.setPlaceholderText(QCoreApplication.translate("DialogDrugSelec", u"\u8f93\u5165\u62fc\u97f3\u7f29\u5199", None))
    # retranslateUi

