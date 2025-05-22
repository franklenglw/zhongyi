# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Login_interface.ui'
##
## Created by: Qt User Interface Compiler version 6.1.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

import resources_rc

class Ui_Login_Dialog(object):
    def setupUi(self, Login_Dialog):
        if not Login_Dialog.objectName():
            Login_Dialog.setObjectName(u"Login_Dialog")
        Login_Dialog.resize(1280, 720)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Login_Dialog.sizePolicy().hasHeightForWidth())
        Login_Dialog.setSizePolicy(sizePolicy)
        Login_Dialog.setMinimumSize(QSize(420, 360))
        Login_Dialog.setMaximumSize(QSize(1280, 720))
        font = QFont()
        font.setPointSize(12)
        Login_Dialog.setFont(font)
        icon = QIcon()
        icon.addFile(u":/Resources/icons/logo.ico", QSize(), QIcon.Normal, QIcon.Off)
        Login_Dialog.setWindowIcon(icon)
        self.gridLayout_2 = QGridLayout(Login_Dialog)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.Backgroup_img = QWidget(Login_Dialog)
        self.Backgroup_img.setObjectName(u"Backgroup_img")
        self.Backgroup_img.setMaximumSize(QSize(1280, 720))
        self.Backgroup_img.setFont(font)
        self.Backgroup_img.setStyleSheet(u"#Backgroup_img {\n"
"             background-image: url(:/Resources/images/login.jpg);\n"
"             background-position: center;\n"
"             background-repeat: no-repeat;\n"
"             background-clip: content;  /* \u9650\u5236\u80cc\u666f\u7ed8\u5236\u8303\u56f4 */\n"
"         }")
        self.gridLayout = QGridLayout(self.Backgroup_img)
        self.gridLayout.setObjectName(u"gridLayout")
        self.InputSection = QVBoxLayout()
        self.InputSection.setObjectName(u"InputSection")
        self.horizontalLayout_1 = QHBoxLayout()
        self.horizontalLayout_1.setSpacing(6)
        self.horizontalLayout_1.setObjectName(u"horizontalLayout_1")
        self.horizontalLayout_1.setContentsMargins(0, 0, -1, -1)
        self.label = QLabel(self.Backgroup_img)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(55, 30))
        self.label.setMaximumSize(QSize(55, 30))
        font1 = QFont()
        font1.setPointSize(13)
        font1.setBold(True)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"    QLabel {\n"
"        font-size: 13pt;\n"
"        color: black;\n"
"        background-color:rgba(54, 164, 225,100);\n"
"        border-radius: 5px;\n"
"        border: 2px solid #8f8f91;\n"
"        font-weight: bold; /* \u8bbe\u7f6e\u5b50\u63a7\u4ef6\u7684\u5b57\u4f53\u7c97\u7ec6 */\n"
"        padding: 3px;\n"
"    }\n"
"")
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_1.addWidget(self.label)

        self.m_edt_InputUser = QLineEdit(self.Backgroup_img)
        self.m_edt_InputUser.setObjectName(u"m_edt_InputUser")
        self.m_edt_InputUser.setMinimumSize(QSize(154, 30))
        self.m_edt_InputUser.setMaximumSize(QSize(154, 30))
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        self.m_edt_InputUser.setFont(font2)
        self.m_edt_InputUser.setStyleSheet(u"            QLineEdit {\n"
"                border: 2px solid #8f8f91;\n"
"                border-radius: 5px;\n"
"                padding: 0 8px;\n"
"                selection-background-color: #007BFF;\n"
"                background-color:  rgba(0,0,0,0.1);\n"
"                box-shadow: 5px 5px 10px rgba(0,0,0,0.3); /* \u6dfb\u52a0\u9634\u5f71 */\n"
"            }\n"
"            QLineEdit:hover {\n"
"                border-color: #1e90ff; /* \u9f20\u6807\u60ac\u505c\u65f6\u6539\u53d8\u8fb9\u6846\u989c\u8272 */\n"
"            }\n"
"            QLineEdit:focus {\n"
"                border-color: #4682b4; /* \u83b7\u5f97\u7126\u70b9\u65f6\u6539\u53d8\u8fb9\u6846\u989c\u8272 */\n"
"            }\n"
"    QLineEdit:focus {\n"
"        background-color: rgba(0, 170, 255, 20);    /* \u7126\u70b9\u72b6\u6001\u52a0\u6df1\u989c\u8272  */ \n"
"    }")
        self.m_edt_InputUser.setEchoMode(QLineEdit.Normal)

        self.horizontalLayout_1.addWidget(self.m_edt_InputUser)


        self.InputSection.addLayout(self.horizontalLayout_1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.Backgroup_img)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(55, 30))
        self.label_2.setMaximumSize(QSize(55, 30))
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"    QLabel {\n"
"        font-size: 13pt;\n"
"        color: black;\n"
"        background-color:rgba(54, 164, 225,100);\n"
"        border-radius: 5px;\n"
"        border: 2px solid #8f8f91;\n"
"        font-weight: bold; /* \u8bbe\u7f6e\u5b50\u63a7\u4ef6\u7684\u5b57\u4f53\u7c97\u7ec6 */\n"
"        padding: 3px;\n"
"    }\n"
"")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.m_edt_InputPass = QLineEdit(self.Backgroup_img)
        self.m_edt_InputPass.setObjectName(u"m_edt_InputPass")
        self.m_edt_InputPass.setMinimumSize(QSize(154, 30))
        self.m_edt_InputPass.setMaximumSize(QSize(154, 30))
        self.m_edt_InputPass.setFont(font2)
        self.m_edt_InputPass.setStyleSheet(u"            QLineEdit {\n"
"                border: 2px solid #8f8f91;\n"
"                border-radius: 5px;\n"
"                padding: 0 8px;\n"
"                selection-background-color: #007BFF;\n"
"                background-color:  rgba(0,0,0,0.1);\n"
"                box-shadow: 5px 5px 10px rgba(0,0,0,0.3); /* \u6dfb\u52a0\u9634\u5f71 */\n"
"            }\n"
"            QLineEdit:hover {\n"
"                border-color: #1e90ff; /* \u9f20\u6807\u60ac\u505c\u65f6\u6539\u53d8\u8fb9\u6846\u989c\u8272 */\n"
"            }\n"
"            QLineEdit:focus {\n"
"                border-color: #4682b4; /* \u83b7\u5f97\u7126\u70b9\u65f6\u6539\u53d8\u8fb9\u6846\u989c\u8272 */\n"
"            }\n"
"    QLineEdit:focus {\n"
"        background-color: rgba(0, 170, 255, 20);    /* \u7126\u70b9\u72b6\u6001\u52a0\u6df1\u989c\u8272  */ \n"
"    }")
        self.m_edt_InputPass.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_2.addWidget(self.m_edt_InputPass)


        self.InputSection.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.m_bt_loginConfirm = QPushButton(self.Backgroup_img)
        self.m_bt_loginConfirm.setObjectName(u"m_bt_loginConfirm")
        self.m_bt_loginConfirm.setEnabled(True)
        self.m_bt_loginConfirm.setMinimumSize(QSize(62, 30))
        self.m_bt_loginConfirm.setMaximumSize(QSize(65, 30))
        self.m_bt_loginConfirm.setFont(font1)
        self.m_bt_loginConfirm.setAutoFillBackground(False)
        self.m_bt_loginConfirm.setStyleSheet(u"QPushButton {\n"
"                /* \u57fa\u7840\u53c2\u6570 */\n"
"				letter-spacing: 2px;\n"
"                border-radius: 3px;\n"
"                border: 1px solid rgba(140, 170, 30, 0.78);\n"
"                padding: 3px 10px;\n"
"                color: black;\n"
"\n"
"                /* \u4e3b\u6e10\u53d8 (\u767d \u2192 \u7070 \u2192 \u6df1\u7070) */\n"
"                background-color: rgba(162, 255, 188,160);\n"
"\n"
"                /* \u5916\u90e8\u9634\u5f71 */\n"
"                box-shadow: 0 2px 4px rgba(140, 170, 30, 0.3);\n"
"            }\n"
"\n"
"            QPushButton:hover {\n"
"                /* \u60ac\u505c\u9ad8\u4eae */\n"
"                background-color:rgba(54, 164, 225,100);\n"
"                border-color: rgba(150, 180, 35, 0.86);\n"
"                box-shadow: 0 3px 5px rgba(140, 170, 30, 0.4);\n"
"            }\n"
"\n"
"            QPushButton:pressed {\n"
"                /* \u6309\u4e0b\u6548\u679c */\n"
"               background-color: rgb(149, 227, 132);\n"
"    "
                        "            box-shadow: inset 1px 2px 3px rgba(100, 130, 20, 0.3),\n"
"                           inset -1px -1px 2px rgba(255, 255, 255, 0.2);\n"
"                border-color: rgba(120, 150, 25, 0.86);\n"
"                padding: 5px 10px 3px 10px;\n"
"            }")
        self.m_bt_loginConfirm.setCheckable(False)

        self.horizontalLayout_3.addWidget(self.m_bt_loginConfirm)

        self.m_bt_Register = QPushButton(self.Backgroup_img)
        self.m_bt_Register.setObjectName(u"m_bt_Register")
        self.m_bt_Register.setEnabled(True)
        self.m_bt_Register.setMinimumSize(QSize(62, 30))
        self.m_bt_Register.setMaximumSize(QSize(65, 30))
        self.m_bt_Register.setFont(font1)
        self.m_bt_Register.setAutoFillBackground(False)
        self.m_bt_Register.setStyleSheet(u"QPushButton {\n"
"                /* \u57fa\u7840\u53c2\u6570 */\n"
"				letter-spacing: 2px;\n"
"                border-radius: 3px;\n"
"                border: 1px solid rgba(140, 170, 30, 0.78);\n"
"                padding: 3px 10px;\n"
"                color: black;\n"
"\n"
"                /* \u4e3b\u6e10\u53d8 (\u767d \u2192 \u7070 \u2192 \u6df1\u7070) */\n"
"                background-color: rgba(162, 255, 188,160);\n"
"\n"
"                /* \u5916\u90e8\u9634\u5f71 */\n"
"                box-shadow: 0 2px 4px rgba(140, 170, 30, 0.3);\n"
"            }\n"
"\n"
"            QPushButton:hover {\n"
"                /* \u60ac\u505c\u9ad8\u4eae */\n"
"                background-color:rgba(54, 164, 225,100);\n"
"                border-color: rgba(150, 180, 35, 0.86);\n"
"                box-shadow: 0 3px 5px rgba(140, 170, 30, 0.4);\n"
"            }\n"
"\n"
"            QPushButton:pressed {\n"
"                /* \u6309\u4e0b\u6548\u679c */\n"
"               background-color: rgb(149, 227, 132);\n"
"    "
                        "            box-shadow: inset 1px 2px 3px rgba(100, 130, 20, 0.3),\n"
"                           inset -1px -1px 2px rgba(255, 255, 255, 0.2);\n"
"                border-color: rgba(120, 150, 25, 0.86);\n"
"                padding: 5px 10px 3px 10px;\n"
"            }")
        self.m_bt_Register.setCheckable(False)

        self.horizontalLayout_3.addWidget(self.m_bt_Register)

        self.m_bt_PassReset = QPushButton(self.Backgroup_img)
        self.m_bt_PassReset.setObjectName(u"m_bt_PassReset")
        self.m_bt_PassReset.setEnabled(True)
        self.m_bt_PassReset.setMinimumSize(QSize(80, 30))
        self.m_bt_PassReset.setMaximumSize(QSize(82, 30))
        self.m_bt_PassReset.setFont(font1)
        self.m_bt_PassReset.setAutoFillBackground(False)
        self.m_bt_PassReset.setStyleSheet(u"QPushButton {\n"
"                /* \u57fa\u7840\u53c2\u6570 */\n"
"				letter-spacing:1px;\n"
"                border-radius: 3px;\n"
"                border: 1px solid rgba(140, 170, 30, 0.78);\n"
"                padding: 3px 3px;\n"
"                color: black;\n"
"\n"
"                /* \u4e3b\u6e10\u53d8 (\u767d \u2192 \u7070 \u2192 \u6df1\u7070) */\n"
"                background-color: rgba(162, 255, 188,160);\n"
"\n"
"                /* \u5916\u90e8\u9634\u5f71 */\n"
"                box-shadow: 0 2px 4px rgba(140, 170, 30, 0.3);\n"
"            }\n"
"\n"
"            QPushButton:hover {\n"
"                /* \u60ac\u505c\u9ad8\u4eae */\n"
"                background-color:rgba(54, 164, 225,100);\n"
"                border-color: rgba(150, 180, 35, 0.86);\n"
"                box-shadow: 0 3px 5px rgba(140, 170, 30, 0.4);\n"
"            }\n"
"\n"
"            QPushButton:pressed {\n"
"                /* \u6309\u4e0b\u6548\u679c */\n"
"               background-color: rgb(149, 227, 132);\n"
"      "
                        "          box-shadow: inset 1px 2px 3px rgba(100, 130, 20, 0.3),\n"
"                           inset -1px -1px 2px rgba(255, 255, 255, 0.2);\n"
"                border-color: rgba(120, 150, 25, 0.86);\n"
"                padding: 7px 3px 4px 3px;\n"
"            }")
        self.m_bt_PassReset.setCheckable(False)

        self.horizontalLayout_3.addWidget(self.m_bt_PassReset)


        self.InputSection.addLayout(self.horizontalLayout_3)


        self.gridLayout.addLayout(self.InputSection, 1, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(14, 381, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 0, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(788, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 0, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(310, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_5, 1, 2, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(17, 182, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_3, 2, 1, 1, 1)


        self.gridLayout_2.addWidget(self.Backgroup_img, 0, 0, 1, 1)


        self.retranslateUi(Login_Dialog)

        self.m_bt_loginConfirm.setDefault(True)
        self.m_bt_Register.setDefault(True)
        self.m_bt_PassReset.setDefault(True)


        QMetaObject.connectSlotsByName(Login_Dialog)
    # setupUi

    def retranslateUi(self, Login_Dialog):
        Login_Dialog.setWindowTitle(QCoreApplication.translate("Login_Dialog", u"\u7cfb\u7edf\u767b\u5f55", None))
        self.label.setText(QCoreApplication.translate("Login_Dialog", u"\u8d26\u53f7", None))
        self.m_edt_InputUser.setPlaceholderText(QCoreApplication.translate("Login_Dialog", u"\u8bf7\u8f93\u5165\u7528\u6237\u540d", None))
        self.label_2.setText(QCoreApplication.translate("Login_Dialog", u"\u5bc6\u7801", None))
        self.m_edt_InputPass.setPlaceholderText(QCoreApplication.translate("Login_Dialog", u"\u8bf7\u8f93\u5165\u5bc6\u7801", None))
        self.m_bt_loginConfirm.setText(QCoreApplication.translate("Login_Dialog", u"\u767b\u5f55", None))
        self.m_bt_Register.setText(QCoreApplication.translate("Login_Dialog", u"\u6ce8\u518c", None))
        self.m_bt_PassReset.setText(QCoreApplication.translate("Login_Dialog", u"\u91cd\u8bbe\u5bc6\u7801", None))
    # retranslateUi

