# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DrugSetting.ui'
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
        Dialog.resize(842, 680)
        icon = QIcon()
        icon.addFile(u":/Resources/icons/logo.ico", QSize(), QIcon.Normal, QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet(u"")
        self.horizontalLayout_2 = QHBoxLayout(Dialog)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.groupBox = QGroupBox(Dialog)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setStyleSheet(u"    QGroupBox {\n"
"        background-color: rgba(169,208,107,235); /* \u53ea\u8bbe\u7f6e\u80cc\u666f\u8272 */\n"
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
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.m_tbl_DrugSetting = QTableWidget(self.groupBox)
        if (self.m_tbl_DrugSetting.columnCount() < 6):
            self.m_tbl_DrugSetting.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.m_tbl_DrugSetting.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.m_tbl_DrugSetting.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.m_tbl_DrugSetting.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.m_tbl_DrugSetting.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.m_tbl_DrugSetting.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.m_tbl_DrugSetting.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.m_tbl_DrugSetting.setObjectName(u"m_tbl_DrugSetting")
        self.m_tbl_DrugSetting.setStyleSheet(u"QTableWidget{\n"
"background-color:rgba(248, 248, 248, 220);\n"
"} ")
        self.m_tbl_DrugSetting.horizontalHeader().setDefaultSectionSize(120)
        self.m_tbl_DrugSetting.horizontalHeader().setStretchLastSection(True)

        self.gridLayout.addWidget(self.m_tbl_DrugSetting, 0, 0, 1, 3)

        self.line = QFrame(self.groupBox)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line, 1, 0, 1, 3)

        self.m_edt_DrugDiscrip = QTextEdit(self.groupBox)
        self.m_edt_DrugDiscrip.setObjectName(u"m_edt_DrugDiscrip")
        self.m_edt_DrugDiscrip.setStyleSheet(u"QTextEdit{\n"
"background-color:rgba(248, 248, 248, 220);\n"
"} ")

        self.gridLayout.addWidget(self.m_edt_DrugDiscrip, 3, 0, 2, 1)

        self.label_HerbPic_1 = QLabel(self.groupBox)
        self.label_HerbPic_1.setObjectName(u"label_HerbPic_1")
        self.label_HerbPic_1.setMinimumSize(QSize(140, 140))
        self.label_HerbPic_1.setMaximumSize(QSize(140, 140))
        self.label_HerbPic_1.setStyleSheet(u"QLabel{\n"
"background-color: rgba(255, 255, 255,120);\n"
"border:2px solid rgb(190, 190, 190); \n"
"} ")

        self.gridLayout.addWidget(self.label_HerbPic_1, 3, 1, 1, 1)

        self.label_HerbPic_3 = QLabel(self.groupBox)
        self.label_HerbPic_3.setObjectName(u"label_HerbPic_3")
        self.label_HerbPic_3.setMinimumSize(QSize(140, 140))
        self.label_HerbPic_3.setMaximumSize(QSize(140, 140))
        self.label_HerbPic_3.setStyleSheet(u"QLabel{\n"
"background-color: rgba(255, 255, 255,120);\n"
"border:2px solid rgb(190, 190, 190); \n"
"} ")

        self.gridLayout.addWidget(self.label_HerbPic_3, 3, 2, 1, 1)

        self.label_HerbPic_2 = QLabel(self.groupBox)
        self.label_HerbPic_2.setObjectName(u"label_HerbPic_2")
        self.label_HerbPic_2.setMinimumSize(QSize(140, 140))
        self.label_HerbPic_2.setMaximumSize(QSize(140, 140))
        self.label_HerbPic_2.setStyleSheet(u"QLabel{\n"
"background-color: rgba(255, 255, 255,120);\n"
"border:2px solid rgb(190, 190, 190); \n"
"} ")

        self.gridLayout.addWidget(self.label_HerbPic_2, 4, 1, 1, 1)

        self.label_HerbPic_4 = QLabel(self.groupBox)
        self.label_HerbPic_4.setObjectName(u"label_HerbPic_4")
        self.label_HerbPic_4.setMinimumSize(QSize(140, 140))
        self.label_HerbPic_4.setMaximumSize(QSize(140, 140))
        self.label_HerbPic_4.setStyleSheet(u"QLabel{\n"
"background-color: rgba(255, 255, 255,120);\n"
"border:2px solid rgb(190, 190, 190); \n"
"} ")

        self.gridLayout.addWidget(self.label_HerbPic_4, 4, 2, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.bt_searchicon = QPushButton(self.groupBox)
        self.bt_searchicon.setObjectName(u"bt_searchicon")
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.bt_searchicon.setFont(font)
        self.bt_searchicon.setStyleSheet(u"QPushButton{\n"
"font-size:11pt;\n"
"border: none;\n"
"color:white;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/Resources/icons/icon_search.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_searchicon.setIcon(icon1)
        self.bt_searchicon.setIconSize(QSize(25, 25))

        self.horizontalLayout.addWidget(self.bt_searchicon)

        self.m_edt_searchfilter_Drug = QLineEdit(self.groupBox)
        self.m_edt_searchfilter_Drug.setObjectName(u"m_edt_searchfilter_Drug")
        self.m_edt_searchfilter_Drug.setMinimumSize(QSize(0, 29))
        self.m_edt_searchfilter_Drug.setStyleSheet(u"QLineEdit { font-size: 11pt; }")

        self.horizontalLayout.addWidget(self.m_edt_searchfilter_Drug)

        self.horizontalSpacer = QSpacerItem(48, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"QLabel { \n"
"color:grey;\n"
"font-size: 11pt; }\n"
"")

        self.horizontalLayout.addWidget(self.label_2)

        self.m_bt_add = QPushButton(self.groupBox)
        self.m_bt_add.setObjectName(u"m_bt_add")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.m_bt_add.setFont(font1)
        self.m_bt_add.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.m_bt_add)

        self.m_bt_save = QPushButton(self.groupBox)
        self.m_bt_save.setObjectName(u"m_bt_save")
        self.m_bt_save.setFont(font1)
        self.m_bt_save.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.m_bt_save)

        self.m_bt_del = QPushButton(self.groupBox)
        self.m_bt_del.setObjectName(u"m_bt_del")
        self.m_bt_del.setFont(font1)

        self.horizontalLayout.addWidget(self.m_bt_del)


        self.gridLayout.addLayout(self.horizontalLayout, 5, 0, 1, 3)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.bt_title_3 = QPushButton(self.groupBox)
        self.bt_title_3.setObjectName(u"bt_title_3")
        self.bt_title_3.setFont(font)
        self.bt_title_3.setStyleSheet(u"QPushButton{\n"
"font-size:11pt;\n"
"border: none;\n"
"color:white;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/Resources/icons/icon_note_grey.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_title_3.setIcon(icon2)
        self.bt_title_3.setIconSize(QSize(25, 23))

        self.horizontalLayout_3.addWidget(self.bt_title_3)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"QLabel { \n"
"font-size: 12pt; }\n"
"")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.horizontalSpacer_3 = QSpacerItem(278, 17, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)


        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 0, 1, 3)


        self.horizontalLayout_2.addWidget(self.groupBox)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u4e2d\u836f\u8bbe\u7f6e", None))
        self.groupBox.setTitle("")
        ___qtablewidgetitem = self.m_tbl_DrugSetting.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Dialog", u"\u7f16\u53f7", None));
        ___qtablewidgetitem1 = self.m_tbl_DrugSetting.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Dialog", u"\u836f\u540d", None));
        ___qtablewidgetitem2 = self.m_tbl_DrugSetting.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Dialog", u"\u4ef7\u683c", None));
        ___qtablewidgetitem3 = self.m_tbl_DrugSetting.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Dialog", u"\u5e38\u7528\u91cf", None));
        ___qtablewidgetitem4 = self.m_tbl_DrugSetting.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Dialog", u"\u4e2d\u836f\u62fc\u97f3", None));
        ___qtablewidgetitem5 = self.m_tbl_DrugSetting.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Dialog", u"\u5907\u6ce8", None));
        self.label_HerbPic_1.setText("")
        self.label_HerbPic_3.setText("")
        self.label_HerbPic_2.setText("")
        self.label_HerbPic_4.setText("")
        self.bt_searchicon.setText("")
        self.m_edt_searchfilter_Drug.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u8f93\u5165\u836f\u540d\u62fc\u97f3\u7f29\u5199\u6216\u6c49\u5b57", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u6ce8\uff1a\u62fc\u97f3\u81ea\u52a8\u4fdd\u5b58", None))
        self.m_bt_add.setText(QCoreApplication.translate("Dialog", u"\u6dfb\u52a0", None))
        self.m_bt_save.setText(QCoreApplication.translate("Dialog", u"\u4fdd\u5b58", None))
        self.m_bt_del.setText(QCoreApplication.translate("Dialog", u"\u5220\u9664", None))
        self.bt_title_3.setText("")
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u5907\u6ce8", None))
    # retranslateUi

