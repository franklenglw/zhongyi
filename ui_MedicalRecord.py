# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MedicalRecord.ui'
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
        Dialog.resize(884, 698)
        icon = QIcon()
        icon.addFile(u":/Resources/icons/logo.ico", QSize(), QIcon.Normal, QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet(u"")
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox = QGroupBox(Dialog)
        self.groupBox.setObjectName(u"groupBox")
        font = QFont()
        font.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font.setPointSize(12)
        self.groupBox.setFont(font)
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
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.m_tbl_Record = QTableWidget(self.groupBox)
        if (self.m_tbl_Record.columnCount() < 4):
            self.m_tbl_Record.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.m_tbl_Record.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.m_tbl_Record.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.m_tbl_Record.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.m_tbl_Record.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.m_tbl_Record.setObjectName(u"m_tbl_Record")
        self.m_tbl_Record.setStyleSheet(u"QTableWidget{\n"
"background-color:rgba(248, 248, 248, 220);\n"
"} \n"
"")
        self.m_tbl_Record.horizontalHeader().setDefaultSectionSize(400)
        self.m_tbl_Record.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout.addWidget(self.m_tbl_Record)

        self.line = QFrame(self.groupBox)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.bt_title_3 = QPushButton(self.groupBox)
        self.bt_title_3.setObjectName(u"bt_title_3")
        font1 = QFont()
        font1.setPointSize(11)
        font1.setBold(True)
        self.bt_title_3.setFont(font1)
        self.bt_title_3.setStyleSheet(u"QPushButton{\n"
"font-size:11pt;\n"
"border: none;\n"
"color:white;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/Resources/icons/icon_note_grey.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_title_3.setIcon(icon1)
        self.bt_title_3.setIconSize(QSize(25, 23))

        self.horizontalLayout_3.addWidget(self.bt_title_3)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        self.label_3.setFont(font2)
        self.label_3.setStyleSheet(u"QLabel { \n"
"font-size: 12pt; }\n"
"")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.horizontalSpacer_3 = QSpacerItem(278, 17, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.m_edt_MedicalRec = QTextEdit(self.groupBox)
        self.m_edt_MedicalRec.setObjectName(u"m_edt_MedicalRec")
        self.m_edt_MedicalRec.setStyleSheet(u"QTextEdit{\n"
"background-color:rgba(248, 248, 248, 220);\n"
"} ")

        self.verticalLayout.addWidget(self.m_edt_MedicalRec)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.bt_searchicon = QPushButton(self.groupBox)
        self.bt_searchicon.setObjectName(u"bt_searchicon")
        self.bt_searchicon.setFont(font1)
        self.bt_searchicon.setStyleSheet(u"QPushButton{\n"
"font-size:11pt;\n"
"border: none;\n"
"color:white;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/Resources/icons/icon_search.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_searchicon.setIcon(icon2)
        self.bt_searchicon.setIconSize(QSize(25, 25))

        self.horizontalLayout.addWidget(self.bt_searchicon)

        self.m_edt_searchfilterRec = QLineEdit(self.groupBox)
        self.m_edt_searchfilterRec.setObjectName(u"m_edt_searchfilterRec")
        self.m_edt_searchfilterRec.setMinimumSize(QSize(0, 24))
        self.m_edt_searchfilterRec.setStyleSheet(u"QLineEdit { font-size: 11pt; }")

        self.horizontalLayout.addWidget(self.m_edt_searchfilterRec)

        self.horizontalSpacer = QSpacerItem(200, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.m_bt_add = QPushButton(self.groupBox)
        self.m_bt_add.setObjectName(u"m_bt_add")
        self.m_bt_add.setFont(font2)
        self.m_bt_add.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.m_bt_add)

        self.m_bt_save = QPushButton(self.groupBox)
        self.m_bt_save.setObjectName(u"m_bt_save")
        self.m_bt_save.setFont(font2)
        self.m_bt_save.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.m_bt_save)

        self.m_bt_del = QPushButton(self.groupBox)
        self.m_bt_del.setObjectName(u"m_bt_del")
        self.m_bt_del.setFont(font2)

        self.horizontalLayout.addWidget(self.m_bt_del)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.horizontalLayout_2.addLayout(self.verticalLayout)


        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u533b\u6848\u5fc3\u5f97", None))
        self.groupBox.setTitle("")
        ___qtablewidgetitem = self.m_tbl_Record.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Dialog", u"\u7f16\u53f7", None));
        ___qtablewidgetitem1 = self.m_tbl_Record.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Dialog", u"\u6807\u9898", None));
        ___qtablewidgetitem2 = self.m_tbl_Record.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Dialog", u"\u5185\u5bb9", None));
        ___qtablewidgetitem3 = self.m_tbl_Record.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Dialog", u"\u5904\u7f6e\u65b9\u6cd5", None));
        self.bt_title_3.setText("")
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u5185\u5bb9", None))
        self.bt_searchicon.setText("")
        self.m_edt_searchfilterRec.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u8f93\u5165\u4efb\u610f\u5173\u952e\u5b57", None))
        self.m_bt_add.setText(QCoreApplication.translate("Dialog", u"\u6dfb\u52a0", None))
        self.m_bt_save.setText(QCoreApplication.translate("Dialog", u"\u4fdd\u5b58", None))
        self.m_bt_del.setText(QCoreApplication.translate("Dialog", u"\u5220\u9664", None))
    # retranslateUi

