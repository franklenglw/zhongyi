# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UserInfor.ui'
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
        Dialog.resize(833, 573)
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
        self.m_tbl_UserInfor = QTableWidget(self.groupBox)
        if (self.m_tbl_UserInfor.columnCount() < 11):
            self.m_tbl_UserInfor.setColumnCount(11)
        __qtablewidgetitem = QTableWidgetItem()
        self.m_tbl_UserInfor.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.m_tbl_UserInfor.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.m_tbl_UserInfor.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.m_tbl_UserInfor.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.m_tbl_UserInfor.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.m_tbl_UserInfor.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.m_tbl_UserInfor.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.m_tbl_UserInfor.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.m_tbl_UserInfor.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.m_tbl_UserInfor.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.m_tbl_UserInfor.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        self.m_tbl_UserInfor.setObjectName(u"m_tbl_UserInfor")
        self.m_tbl_UserInfor.setStyleSheet(u"QTableWidget{\n"
"background-color:rgba(248, 248, 248, 220);\n"
"font-size: 16px; /* \u8bbe\u7f6e\u5b50\u63a7\u4ef6\u7684\u5b57\u4f53\u5927\u5c0f */\n"
"font-weight: bold; /* \u8bbe\u7f6e\u5b50\u63a7\u4ef6\u7684\u5b57\u4f53\u7c97\u7ec6 */\n"
"} ")
        self.m_tbl_UserInfor.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout.addWidget(self.m_tbl_UserInfor)

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

        self.m_edt_searchfilterDoc = QLineEdit(self.groupBox)
        self.m_edt_searchfilterDoc.setObjectName(u"m_edt_searchfilterDoc")
        self.m_edt_searchfilterDoc.setMinimumSize(QSize(0, 24))
        self.m_edt_searchfilterDoc.setFont(font)
        self.m_edt_searchfilterDoc.setStyleSheet(u"QLineEdit { font-size: 11pt; }")

        self.horizontalLayout.addWidget(self.m_edt_searchfilterDoc)

        self.horizontalSpacer = QSpacerItem(200, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.m_bt_add = QPushButton(self.groupBox)
        self.m_bt_add.setObjectName(u"m_bt_add")
        font1 = QFont()
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


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.horizontalLayout_2.addLayout(self.verticalLayout)


        self.horizontalLayout_3.addWidget(self.groupBox)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u7528\u6237\u8bbe\u7f6e", None))
        self.groupBox.setTitle("")
        ___qtablewidgetitem = self.m_tbl_UserInfor.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Dialog", u"user_id", None));
        ___qtablewidgetitem1 = self.m_tbl_UserInfor.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Dialog", u"\u8d26\u53f7", None));
        ___qtablewidgetitem2 = self.m_tbl_UserInfor.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Dialog", u"\u533b\u751f", None));
        ___qtablewidgetitem3 = self.m_tbl_UserInfor.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Dialog", u"\u8bca\u91d1", None));
        ___qtablewidgetitem4 = self.m_tbl_UserInfor.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Dialog", u"\u8bca\u6240\u540d\u79f0", None));
        ___qtablewidgetitem5 = self.m_tbl_UserInfor.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Dialog", u"\u5904\u65b9\u62ac\u5934", None));
        ___qtablewidgetitem6 = self.m_tbl_UserInfor.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Dialog", u"\u914d\u836f", None));
        ___qtablewidgetitem7 = self.m_tbl_UserInfor.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Dialog", u"\u8bca\u6240\u7535\u8bdd", None));
        ___qtablewidgetitem8 = self.m_tbl_UserInfor.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Dialog", u"\u8bca\u6240\u5730\u5740", None));
        ___qtablewidgetitem9 = self.m_tbl_UserInfor.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Dialog", u"\u5bc6\u7801", None));
        ___qtablewidgetitem10 = self.m_tbl_UserInfor.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("Dialog", u"\u5bc6\u7801\u63d0\u793a", None));
        self.bt_searchicon.setText("")
        self.m_edt_searchfilterDoc.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u8f93\u5165\u59d3\u540d\u62fc\u97f3\u7f29\u5199\u6216\u6c49\u5b57", None))
        self.m_bt_add.setText(QCoreApplication.translate("Dialog", u"\u6dfb\u52a0", None))
        self.m_bt_save.setText(QCoreApplication.translate("Dialog", u"\u4fdd\u5b58", None))
        self.m_bt_del.setText(QCoreApplication.translate("Dialog", u"\u5220\u9664", None))
    # retranslateUi

