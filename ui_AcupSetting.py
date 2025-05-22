# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AcupSetting.ui'
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
        Dialog.resize(768, 614)
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
        self.m_tbl_AcupSetting = QTableWidget(self.groupBox)
        if (self.m_tbl_AcupSetting.columnCount() < 4):
            self.m_tbl_AcupSetting.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.m_tbl_AcupSetting.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.m_tbl_AcupSetting.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.m_tbl_AcupSetting.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.m_tbl_AcupSetting.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.m_tbl_AcupSetting.setObjectName(u"m_tbl_AcupSetting")
        self.m_tbl_AcupSetting.setStyleSheet(u"QTableWidget{\n"
"background-color:rgba(248, 248, 248, 220);\n"
"font-size: 16px; /* \u8bbe\u7f6e\u5b50\u63a7\u4ef6\u7684\u5b57\u4f53\u5927\u5c0f */\n"
"font-weight: bold; /* \u8bbe\u7f6e\u5b50\u63a7\u4ef6\u7684\u5b57\u4f53\u7c97\u7ec6 */\n"
"} ")
        self.m_tbl_AcupSetting.horizontalHeader().setDefaultSectionSize(150)
        self.m_tbl_AcupSetting.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout.addWidget(self.m_tbl_AcupSetting)

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

        self.m_edt_searchfilter_Acup = QLineEdit(self.groupBox)
        self.m_edt_searchfilter_Acup.setObjectName(u"m_edt_searchfilter_Acup")
        self.m_edt_searchfilter_Acup.setMinimumSize(QSize(0, 29))
        self.m_edt_searchfilter_Acup.setStyleSheet(u"QLineEdit { font-size: 11pt; }")

        self.horizontalLayout.addWidget(self.m_edt_searchfilter_Acup)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"QLabel { \n"
"color:grey;\n"
"font-size: 11pt; }\n"
"")

        self.horizontalLayout.addWidget(self.label_3)

        self.horizontalSpacer = QSpacerItem(48, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"QLabel { \n"
"color:grey;\n"
"font-size: 11pt; }\n"
"")

        self.horizontalLayout.addWidget(self.label_2)

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
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u9488\u7078\u6216\u5176\u4ed6\u7597\u6cd5\u8bbe\u7f6e", None))
        self.groupBox.setTitle("")
        ___qtablewidgetitem = self.m_tbl_AcupSetting.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Dialog", u"\u7f16\u53f7", None));
        ___qtablewidgetitem1 = self.m_tbl_AcupSetting.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Dialog", u"\u9879\u76ee", None));
        ___qtablewidgetitem2 = self.m_tbl_AcupSetting.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Dialog", u"\u4ef7\u683c", None));
        ___qtablewidgetitem3 = self.m_tbl_AcupSetting.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Dialog", u"\u5907\u6ce8", None));
        self.bt_searchicon.setText("")
        self.m_edt_searchfilter_Acup.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u8f93\u5165\u9879\u76ee\u62fc\u97f3\u7f29\u5199\u6216\u6c49\u5b57", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u6ce8\uff1a\u62fc\u97f3\u81ea\u52a8\u4fdd\u5b58", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u9996\u884c\u8ba1\u4ef7\uff0c\u4ed6\u884c\u65e0\u6548", None))
        self.m_bt_add.setText(QCoreApplication.translate("Dialog", u"\u6dfb\u52a0", None))
        self.m_bt_save.setText(QCoreApplication.translate("Dialog", u"\u4fdd\u5b58", None))
        self.m_bt_del.setText(QCoreApplication.translate("Dialog", u"\u5220\u9664", None))
    # retranslateUi

