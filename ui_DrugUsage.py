# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DrugUsage.ui'
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
        Dialog.resize(800, 556)
        icon = QIcon()
        icon.addFile(u":/Resources/icons/logo.ico", QSize(), QIcon.Normal, QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet(u"")
        self.horizontalLayout_3 = QHBoxLayout(Dialog)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
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
"        font-size: 16px; /* \u8bbe\u7f6e\u5b50\u63a7\u4ef6\u7684\u5b57\u4f53\u5927\u5c0f */\n"
"        font-weight: bold; /* \u8bbe\u7f6e\u5b50\u63a7\u4ef6\u7684\u5b57\u4f53\u7c97\u7ec6 */\n"
"    }")
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.m_tbl_DrugUsage = QTableWidget(self.groupBox)
        if (self.m_tbl_DrugUsage.columnCount() < 3):
            self.m_tbl_DrugUsage.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.m_tbl_DrugUsage.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.m_tbl_DrugUsage.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.m_tbl_DrugUsage.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.m_tbl_DrugUsage.setObjectName(u"m_tbl_DrugUsage")
        self.m_tbl_DrugUsage.setStyleSheet(u"QTableWidget{\n"
"background-color:rgba(248, 248, 248, 220);\n"
"font-size: 16px; /* \u8bbe\u7f6e\u5b50\u63a7\u4ef6\u7684\u5b57\u4f53\u5927\u5c0f */\n"
"font-weight: bold; /* \u8bbe\u7f6e\u5b50\u63a7\u4ef6\u7684\u5b57\u4f53\u7c97\u7ec6 */\n"
"} ")
        self.m_tbl_DrugUsage.horizontalHeader().setDefaultSectionSize(400)
        self.m_tbl_DrugUsage.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout.addWidget(self.m_tbl_DrugUsage)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"QLabel { \n"
"color:grey;\n"
"font-size: 11pt; }\n"
"")

        self.horizontalLayout.addWidget(self.label_2)

        self.horizontalSpacer = QSpacerItem(200, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.m_bt_add = QPushButton(self.groupBox)
        self.m_bt_add.setObjectName(u"m_bt_add")
        font = QFont()
        font.setBold(True)
        self.m_bt_add.setFont(font)
        self.m_bt_add.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.m_bt_add)

        self.m_bt_save = QPushButton(self.groupBox)
        self.m_bt_save.setObjectName(u"m_bt_save")
        self.m_bt_save.setFont(font)
        self.m_bt_save.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.m_bt_save)

        self.m_bt_del = QPushButton(self.groupBox)
        self.m_bt_del.setObjectName(u"m_bt_del")
        self.m_bt_del.setFont(font)

        self.horizontalLayout.addWidget(self.m_bt_del)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.horizontalLayout_2.addLayout(self.verticalLayout)


        self.horizontalLayout_3.addWidget(self.groupBox)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u7528\u6cd5\u8bbe\u7f6e", None))
        self.groupBox.setTitle("")
        ___qtablewidgetitem = self.m_tbl_DrugUsage.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Dialog", u"\u7f16\u53f7", None));
        ___qtablewidgetitem1 = self.m_tbl_DrugUsage.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Dialog", u"\u7528\u6cd5", None));
        ___qtablewidgetitem2 = self.m_tbl_DrugUsage.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Dialog", u"\u714e\u6cd5", None));
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u6ce8\uff1a\u9996\u884c\u7559\u7a7a", None))
        self.m_bt_add.setText(QCoreApplication.translate("Dialog", u"\u6dfb\u52a0", None))
        self.m_bt_save.setText(QCoreApplication.translate("Dialog", u"\u4fdd\u5b58", None))
        self.m_bt_del.setText(QCoreApplication.translate("Dialog", u"\u5220\u9664", None))
    # retranslateUi

