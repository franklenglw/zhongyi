# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DrugFormulas.ui'
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
        DialogDrugSelec.resize(1136, 785)
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
        self.m_tabWidget_FomulaSet = QTabWidget(self.groupBox_5)
        self.m_tabWidget_FomulaSet.setObjectName(u"m_tabWidget_FomulaSet")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.m_tabWidget_FomulaSet.setFont(font)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_6 = QVBoxLayout(self.tab)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.m_tle_ExpdFormulaSet = QTableWidget(self.tab)
        if (self.m_tle_ExpdFormulaSet.columnCount() < 2):
            self.m_tle_ExpdFormulaSet.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.m_tle_ExpdFormulaSet.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.m_tle_ExpdFormulaSet.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.m_tle_ExpdFormulaSet.setObjectName(u"m_tle_ExpdFormulaSet")
        self.m_tle_ExpdFormulaSet.setStyleSheet(u"QTableWidget{\n"
"background-color:rgba(248, 248, 248, 220);\n"
"} ")
        self.m_tle_ExpdFormulaSet.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_3.addWidget(self.m_tle_ExpdFormulaSet)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer_4 = QSpacerItem(88, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_4)

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
        self.m_edt_FormulaSearch.setStyleSheet(u"QLineEdit { font-size: 11pt; }")

        self.horizontalLayout_6.addWidget(self.m_edt_FormulaSearch)


        self.verticalLayout_3.addLayout(self.horizontalLayout_6)


        self.verticalLayout_6.addLayout(self.verticalLayout_3)

        self.m_tabWidget_FomulaSet.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_7 = QGridLayout(self.tab_2)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.m_tle_DisFormulaSet = QTableWidget(self.tab_2)
        if (self.m_tle_DisFormulaSet.columnCount() < 2):
            self.m_tle_DisFormulaSet.setColumnCount(2)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.m_tle_DisFormulaSet.setHorizontalHeaderItem(0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.m_tle_DisFormulaSet.setHorizontalHeaderItem(1, __qtablewidgetitem3)
        self.m_tle_DisFormulaSet.setObjectName(u"m_tle_DisFormulaSet")
        self.m_tle_DisFormulaSet.setStyleSheet(u"QTableWidget{\n"
"background-color:rgba(248, 248, 248, 220);\n"
"} ")
        self.m_tle_DisFormulaSet.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_4.addWidget(self.m_tle_DisFormulaSet)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_5 = QSpacerItem(88, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_5)

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
        self.m_edt_FormulaSearch_2.setStyleSheet(u"QLineEdit { font-size: 11pt; }")

        self.horizontalLayout_5.addWidget(self.m_edt_FormulaSearch_2)


        self.verticalLayout_4.addLayout(self.horizontalLayout_5)


        self.gridLayout_7.addLayout(self.verticalLayout_4, 0, 0, 1, 1)

        self.m_tabWidget_FomulaSet.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout_8 = QGridLayout(self.tab_3)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.m_tle_ClassicFormulaSet = QTableWidget(self.tab_3)
        if (self.m_tle_ClassicFormulaSet.columnCount() < 2):
            self.m_tle_ClassicFormulaSet.setColumnCount(2)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.m_tle_ClassicFormulaSet.setHorizontalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.m_tle_ClassicFormulaSet.setHorizontalHeaderItem(1, __qtablewidgetitem5)
        self.m_tle_ClassicFormulaSet.setObjectName(u"m_tle_ClassicFormulaSet")
        self.m_tle_ClassicFormulaSet.setStyleSheet(u"QTableWidget{\n"
"background-color:rgba(248, 248, 248, 220);\n"
"} ")
        self.m_tle_ClassicFormulaSet.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_5.addWidget(self.m_tle_ClassicFormulaSet)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_6 = QSpacerItem(88, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_6)

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
        self.m_edt_FormulaSearch_3.setStyleSheet(u"QLineEdit { font-size: 11pt; }")

        self.horizontalLayout_4.addWidget(self.m_edt_FormulaSearch_3)


        self.verticalLayout_5.addLayout(self.horizontalLayout_4)


        self.gridLayout_8.addLayout(self.verticalLayout_5, 0, 0, 1, 1)

        self.m_tabWidget_FomulaSet.addTab(self.tab_3, "")

        self.verticalLayout_7.addWidget(self.m_tabWidget_FomulaSet)

        self.line = QFrame(self.groupBox_5)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_7.addWidget(self.line)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.bt_title_3 = QPushButton(self.groupBox_5)
        self.bt_title_3.setObjectName(u"bt_title_3")
        self.bt_title_3.setFont(font1)
        self.bt_title_3.setStyleSheet(u"QPushButton{\n"
"font-size:11pt;\n"
"border: none;\n"
"color:white;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/Resources/icons/icon_note_grey.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_title_3.setIcon(icon2)
        self.bt_title_3.setIconSize(QSize(25, 23))

        self.horizontalLayout_7.addWidget(self.bt_title_3)

        self.label_5 = QLabel(self.groupBox_5)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_7.addWidget(self.label_5)

        self.horizontalSpacer_7 = QSpacerItem(118, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_7)

        self.horizontalSpacer_8 = QSpacerItem(138, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_8)


        self.verticalLayout_7.addLayout(self.horizontalLayout_7)

        self.m_edt_DrugDiscripSet = QTextEdit(self.groupBox_5)
        self.m_edt_DrugDiscripSet.setObjectName(u"m_edt_DrugDiscripSet")
        self.m_edt_DrugDiscripSet.setFont(font)
        self.m_edt_DrugDiscripSet.setStyleSheet(u"QTableWidget{\n"
"background-color:rgba(248, 248, 248, 220);\n"
"} ")

        self.verticalLayout_7.addWidget(self.m_edt_DrugDiscripSet)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_6 = QLabel(self.groupBox_5)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"QLabel { \n"
"color:grey;\n"
"font-size: 11pt; }\n"
"")

        self.horizontalLayout_2.addWidget(self.label_6)

        self.horizontalSpacer_2 = QSpacerItem(168, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.m_bt_add = QPushButton(self.groupBox_5)
        self.m_bt_add.setObjectName(u"m_bt_add")

        self.horizontalLayout_2.addWidget(self.m_bt_add)

        self.m_bt_save = QPushButton(self.groupBox_5)
        self.m_bt_save.setObjectName(u"m_bt_save")

        self.horizontalLayout_2.addWidget(self.m_bt_save)

        self.m_bt_del = QPushButton(self.groupBox_5)
        self.m_bt_del.setObjectName(u"m_bt_del")

        self.horizontalLayout_2.addWidget(self.m_bt_del)


        self.verticalLayout_7.addLayout(self.horizontalLayout_2)

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
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.m_tle_FormulaDrugCombSet = QTableWidget(self.groupBox_6)
        if (self.m_tle_FormulaDrugCombSet.columnCount() < 3):
            self.m_tle_FormulaDrugCombSet.setColumnCount(3)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.m_tle_FormulaDrugCombSet.setHorizontalHeaderItem(0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.m_tle_FormulaDrugCombSet.setHorizontalHeaderItem(1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.m_tle_FormulaDrugCombSet.setHorizontalHeaderItem(2, __qtablewidgetitem8)
        self.m_tle_FormulaDrugCombSet.setObjectName(u"m_tle_FormulaDrugCombSet")
        self.m_tle_FormulaDrugCombSet.setStyleSheet(u"QTableWidget{\n"
"background-color:rgba(248, 248, 248, 220);\n"
"} ")
        self.m_tle_FormulaDrugCombSet.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_2.addWidget(self.m_tle_FormulaDrugCombSet)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_3 = QSpacerItem(168, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.m_bt_del_drug = QPushButton(self.groupBox_6)
        self.m_bt_del_drug.setObjectName(u"m_bt_del_drug")

        self.horizontalLayout_3.addWidget(self.m_bt_del_drug)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

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
        self.m_tle_FormulaSelDruglistSet = QTableWidget(self.groupBox_7)
        if (self.m_tle_FormulaSelDruglistSet.columnCount() < 3):
            self.m_tle_FormulaSelDruglistSet.setColumnCount(3)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.m_tle_FormulaSelDruglistSet.setHorizontalHeaderItem(0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.m_tle_FormulaSelDruglistSet.setHorizontalHeaderItem(1, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.m_tle_FormulaSelDruglistSet.setHorizontalHeaderItem(2, __qtablewidgetitem11)
        self.m_tle_FormulaSelDruglistSet.setObjectName(u"m_tle_FormulaSelDruglistSet")
        font3 = QFont()
        font3.setBold(True)
        self.m_tle_FormulaSelDruglistSet.setFont(font3)
        self.m_tle_FormulaSelDruglistSet.setStyleSheet(u"QTableWidget{\n"
"background-color:rgba(248, 248, 248, 220);\n"
"} ")
        self.m_tle_FormulaSelDruglistSet.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout.addWidget(self.m_tle_FormulaSelDruglistSet)

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

        self.m_edt_FormulaSearchSet_4 = QLineEdit(self.groupBox_7)
        self.m_edt_FormulaSearchSet_4.setObjectName(u"m_edt_FormulaSearchSet_4")
        self.m_edt_FormulaSearchSet_4.setStyleSheet(u"QLineEdit { font-size: 11pt; }")

        self.horizontalLayout.addWidget(self.m_edt_FormulaSearchSet_4)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.gridLayout_4.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.splitter.addWidget(self.groupBox_7)

        self.horizontalLayout_8.addWidget(self.splitter)


        self.retranslateUi(DialogDrugSelec)

        self.m_tabWidget_FomulaSet.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(DialogDrugSelec)
    # setupUi

    def retranslateUi(self, DialogDrugSelec):
        DialogDrugSelec.setWindowTitle(QCoreApplication.translate("DialogDrugSelec", u"\u5904\u65b9\u8bbe\u7f6e", None))
        self.groupBox_5.setTitle("")
        ___qtablewidgetitem = self.m_tle_ExpdFormulaSet.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("DialogDrugSelec", u"\u7f16\u53f7", None));
        ___qtablewidgetitem1 = self.m_tle_ExpdFormulaSet.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("DialogDrugSelec", u"\u65b9\u540d", None));
        self.bt_searchicon_2.setText("")
        self.m_edt_FormulaSearch.setPlaceholderText(QCoreApplication.translate("DialogDrugSelec", u"\u8f93\u5165\u65b9\u5242\u62fc\u97f3\u7f29\u5199", None))
        self.m_tabWidget_FomulaSet.setTabText(self.m_tabWidget_FomulaSet.indexOf(self.tab), QCoreApplication.translate("DialogDrugSelec", u"\u7ecf\u9a8c\u9009\u65b9", None))
        ___qtablewidgetitem2 = self.m_tle_DisFormulaSet.horizontalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("DialogDrugSelec", u"\u7f16\u53f7", None));
        ___qtablewidgetitem3 = self.m_tle_DisFormulaSet.horizontalHeaderItem(1)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("DialogDrugSelec", u"\u65b9\u540d", None));
        self.bt_searchicon_3.setText("")
        self.m_edt_FormulaSearch_2.setPlaceholderText(QCoreApplication.translate("DialogDrugSelec", u"\u8f93\u5165\u65b9\u5242\u62fc\u97f3\u7f29\u5199", None))
        self.m_tabWidget_FomulaSet.setTabText(self.m_tabWidget_FomulaSet.indexOf(self.tab_2), QCoreApplication.translate("DialogDrugSelec", u"\u8fa8\u75c5\u9009\u65b9", None))
        ___qtablewidgetitem4 = self.m_tle_ClassicFormulaSet.horizontalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("DialogDrugSelec", u"\u7f16\u53f7", None));
        ___qtablewidgetitem5 = self.m_tle_ClassicFormulaSet.horizontalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("DialogDrugSelec", u"\u65b9\u540d", None));
        self.bt_searchicon_4.setText("")
        self.m_edt_FormulaSearch_3.setPlaceholderText(QCoreApplication.translate("DialogDrugSelec", u"\u8f93\u5165\u65b9\u5242\u62fc\u97f3\u7f29\u5199", None))
        self.m_tabWidget_FomulaSet.setTabText(self.m_tabWidget_FomulaSet.indexOf(self.tab_3), QCoreApplication.translate("DialogDrugSelec", u"\u65b9\u5242\u9009\u65b9", None))
        self.bt_title_3.setText("")
        self.label_5.setText(QCoreApplication.translate("DialogDrugSelec", u"\u65b9\u5242\u8bf4\u660e", None))
        self.label_6.setText(QCoreApplication.translate("DialogDrugSelec", u"\u6ce8\uff1a\u62fc\u97f3\u81ea\u52a8\u4fdd\u5b58", None))
        self.m_bt_add.setText(QCoreApplication.translate("DialogDrugSelec", u"\u6dfb\u52a0", None))
        self.m_bt_save.setText(QCoreApplication.translate("DialogDrugSelec", u"\u4fdd\u5b58", None))
        self.m_bt_del.setText(QCoreApplication.translate("DialogDrugSelec", u"\u5220\u9664", None))
        self.groupBox_6.setTitle("")
        ___qtablewidgetitem6 = self.m_tle_FormulaDrugCombSet.horizontalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("DialogDrugSelec", u"\u7f16\u53f7", None));
        ___qtablewidgetitem7 = self.m_tle_FormulaDrugCombSet.horizontalHeaderItem(1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("DialogDrugSelec", u"\u836f\u7269", None));
        ___qtablewidgetitem8 = self.m_tle_FormulaDrugCombSet.horizontalHeaderItem(2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("DialogDrugSelec", u"\u5242\u91cf", None));
        self.m_bt_del_drug.setText(QCoreApplication.translate("DialogDrugSelec", u"\u6e05\u7a7a\u9009\u4e2d\u5355\u5143\u683c", None))
        self.groupBox_7.setTitle("")
        ___qtablewidgetitem9 = self.m_tle_FormulaSelDruglistSet.horizontalHeaderItem(0)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("DialogDrugSelec", u"\u7f16\u53f7", None));
        ___qtablewidgetitem10 = self.m_tle_FormulaSelDruglistSet.horizontalHeaderItem(1)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("DialogDrugSelec", u"\u836f\u540d", None));
        ___qtablewidgetitem11 = self.m_tle_FormulaSelDruglistSet.horizontalHeaderItem(2)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("DialogDrugSelec", u"\u4ef7\u683c", None));
        self.bt_searchicon.setText("")
        self.m_edt_FormulaSearchSet_4.setPlaceholderText(QCoreApplication.translate("DialogDrugSelec", u"\u8f93\u5165\u836f\u7269\u62fc\u97f3\u7f29\u5199", None))
    # retranslateUi

