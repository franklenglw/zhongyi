import sys
import os
import json
import pymysql
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QDialog,
    QApplication,
    QLineEdit,
    QMessageBox,
    QInputDialog, QVBoxLayout, QLabel, QDialogButtonBox
)
from PySide6.QtCore import Qt
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from Crypto.Hash import SHA256
from PySide6.QtCore import QTranslator, QLocale, QLibraryInfo
from ui_Login_interface import Ui_Login_Dialog


class PasswordResetDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("密码重置")
        self.setWindowFlags(Qt.Dialog | Qt.WindowTitleHint | Qt.WindowCloseButtonHint)

        self.setStyleSheet("""
            QLabel, QLineEdit {
                font-size: 11pt;
                font-weight: bold;
            }
        """)
        layout = QVBoxLayout()

        self.username_edit = QLineEdit()
        layout.addWidget(QLabel("账号："))
        layout.addWidget(self.username_edit)

        self.hint_edit = QLineEdit()
        layout.addWidget(QLabel("密码提示词："))
        layout.addWidget(self.hint_edit)

        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        layout.addWidget(buttons)

        self.setLayout(layout)


class LoginDialog(QDialog, Ui_Login_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.attempts = 0
        self.setup_connections()
        self.m_edt_InputPass.setFocus()
        self.m_edt_InputUser.setText("Admin")
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)
        self.setWindowTitle("登录界面")

        self.db_config = self.load_db_config()

    def load_db_config(self):
        try:
            with open("Link_loop.enc", "rb") as f:
                iv = f.read(16)
                ciphertext = f.read()

            password = "secure_key_2023".encode("utf-8")
            key = SHA256.new(password).digest()

            cipher = AES.new(key, AES.MODE_CBC, iv=iv)
            decrypted_data = unpad(cipher.decrypt(ciphertext), AES.block_size)
            config = json.loads(decrypted_data.decode("utf-8"))

            # 确保端口是整数类型
            config["port"] = int(config["port"])
            return config
        except Exception as e:
            QMessageBox.critical(self, "配置错误", f"加载配置失败：{str(e)}")
            sys.exit(1)

    def setup_connections(self):
        self.m_bt_loginConfirm.clicked.connect(self.login)
        self.m_edt_InputUser.returnPressed.connect(self.login)  # 新增回车事件
        self.m_edt_InputPass.returnPressed.connect(self.login)
        self.m_bt_Register.clicked.connect(self.register_user)
        self.m_bt_PassReset.clicked.connect(self.reset_password)

    def get_db_connection(self):
        return pymysql.connect(**self.db_config)

    def keyPressEvent(self, event):
            super().keyPressEvent(event)

    def login(self):
        username = self.m_edt_InputUser.text().strip()
        password = self.m_edt_InputPass.text().strip()

        conn = None  # 显式初始化
        try:
            conn = self.get_db_connection()
            with conn.cursor() as cursor:
                # 修改 SQL 查询以获取 user_id
                sql = "SELECT `user_id`, `密码` FROM `基本设置` WHERE `账号`=%s"  # 假设用户表中有 user_id 字段
                cursor.execute(sql, (username,))
                result = cursor.fetchone()

            if result:
                user_id, db_password = result
                if password == db_password:
                    self.on_login_success(user_id)  # 调用 on_login_success 并传递 user_id
                    return

            self.attempts += 1
            if self.attempts >= 5:
                self.m_edt_InputPass.setEnabled(False)
                QMessageBox.warning(self, "警告", "密码错误次数过多，已锁定！")
                return

            QMessageBox.warning(self, "错误", f"密码错误，还剩{5 - self.attempts}次尝试机会")

        except Exception as e:
            QMessageBox.critical(self, "错误", f"数据库错误: {str(e)}")
        finally:
            if conn:  # 安全关闭连接
                conn.close()

    def on_login_success(self, user_id):
        from main_window_system import MyMainWindow
        self.main_window = MyMainWindow(user_id)  # ✅ 通过构造函数传递
        self.main_window.show()
        self.close()

    def resizeEvent(self, event):
        self.Backgroup_img.setGeometry(0, 0, self.width(), self.height())

        super().resizeEvent(event)

    # 删除以下代码
    # def open_main_window(self):
    #     from main_window_system import MyMainWindow
    #     self.main_window = MyMainWindow()
    #     self.main_window.show()
    #     self.close()

    class RegisterDialog(QDialog):
        def __init__(self, parent=None):
            super().__init__(parent)
            self.setWindowTitle("用户注册")
            self.setWindowFlags(Qt.Dialog | Qt.WindowTitleHint | Qt.WindowCloseButtonHint)

            self.setStyleSheet("""
                QLabel, QLineEdit {
                    font-size: 11pt;
                    font-weight: bold;
                }
            """)

            layout = QVBoxLayout()

            self.username_edit = QLineEdit()
            layout.addWidget(QLabel("账号："))
            layout.addWidget(self.username_edit)

            self.password_edit = QLineEdit()
            self.password_edit.setEchoMode(QLineEdit.Password)
            layout.addWidget(QLabel("密码："))
            layout.addWidget(self.password_edit)

            self.confirm_password_edit = QLineEdit()
            self.confirm_password_edit.setEchoMode(QLineEdit.Password)
            layout.addWidget(QLabel("重新输入密码："))
            layout.addWidget(self.confirm_password_edit)

            self.password_error_label = QLabel()
            self.password_error_label.setStyleSheet("color: red;")
            layout.addWidget(self.password_error_label)

            self.hint_edit = QLineEdit()
            layout.addWidget(QLabel("密码提示："))
            layout.addWidget(self.hint_edit)

            buttons = QDialogButtonBox(
                QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
            buttons.accepted.connect(self.accept)
            buttons.rejected.connect(self.reject)
            layout.addWidget(buttons)

            self.setLayout(layout)

            self.password_edit.textChanged.connect(self.validate_password)
            self.confirm_password_edit.textChanged.connect(self.validate_password)

        def validate_password(self):
            password = self.password_edit.text()
            confirm = self.confirm_password_edit.text()

            if not password and not confirm:
                self.password_error_label.clear()
                return

            if password == confirm:
                self.password_error_label.setText("✓ 密码匹配")
                self.password_error_label.setStyleSheet("color: green;")
            else:
                self.password_error_label.setText("✗ 密码不一致！")
                self.password_error_label.setStyleSheet("color: red;")

    def register_user(self):
        dialog = self.RegisterDialog(self)
        if dialog.exec() != QDialog.Accepted:
            return

        username = dialog.username_edit.text().strip()
        password = dialog.password_edit.text().strip()
        confirm = dialog.confirm_password_edit.text().strip()
        hint = dialog.hint_edit.text().strip()

        if password != confirm:
            QMessageBox.warning(self, "错误", "两次输入的密码不一致！")
            return

        if not username:
            QMessageBox.warning(self, "错误", "账号不能为空！")
            return

        try:
            conn = self.get_db_connection()
            with conn.cursor() as cursor:
                check_sql = "SELECT COUNT(*) FROM `基本设置` WHERE `账号`=%s"
                cursor.execute(check_sql, (username,))
                if cursor.fetchone()[0] > 0:
                    QMessageBox.warning(self, "错误", "该用户名已存在！")
                    return

                insert_sql = """INSERT INTO `基本设置` 
                              (`账号`, `密码`, `密码提示`, `诊金`) 
                              VALUES (%s, %s, %s, %s)"""
                cursor.execute(insert_sql, (username, password, hint, 0))
                conn.commit()
                QMessageBox.information(self, "成功", "用户注册成功！")

        except Exception as e:
            QMessageBox.critical(self, "错误", f"注册失败: {str(e)}")
            conn.rollback()
        finally:
            conn.close()

    def reset_password(self):
        dialog = PasswordResetDialog(self)
        if dialog.exec() != QDialog.Accepted:
            return

        username = dialog.username_edit.text().strip()
        hint_input = dialog.hint_edit.text().strip()

        if not username:
            QMessageBox.warning(self, "错误", "账号不能为空！")
            return

        conn = None
        try:
            conn = self.get_db_connection()
            with conn.cursor() as cursor:
                sql = "SELECT `密码提示` FROM `基本设置` WHERE `账号`=%s"
                cursor.execute(sql, (username,))
                result = cursor.fetchone()

            if not result:
                QMessageBox.warning(self, "错误", "该用户不存在！")
                return

            correct_hint = result[0] or ""
            if hint_input != correct_hint:
                QMessageBox.warning(self, "错误", "密码提示验证失败！")
                return

            new_password, ok = QInputDialog.getText(
                self, "重置密码", "请输入新密码:", QLineEdit.Password
            )
            # 允许新密码为空，因此移除对新密码的非空验证
            # if not ok or not new_password:
            #     return

            # 仅当用户点击了确定按钮时才继续
            if not ok:
                return

            # 将新密码（可能为空）设置为 None 或空字符串，具体取决于你的数据库设计
            # 如果你的数据库密码字段不允许 NULL，则使用空字符串 ""
            # 如果允许 NULL，则可以使用 None 或适当的空值表示
            if new_password.strip() == "":
                new_password_db = ""  # 或者 None，取决于你的数据库设计
            else:
                new_password_db = new_password

            try:
                with conn.cursor() as cursor:
                    update_sql = "UPDATE `基本设置` SET `密码`=%s WHERE `账号`=%s"
                    cursor.execute(update_sql, (new_password_db, username))
                    conn.commit()
                QMessageBox.information(self, "成功", "密码重置成功！")
            except Exception as e:
                conn.rollback()
                raise e

        except Exception as e:
            QMessageBox.critical(self, "错误", f"操作失败: {str(e)}")
        finally:
            if conn:
                conn.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # 设置默认区域为中文
    locale = QLocale(QLocale.Chinese, QLocale.China)
    QLocale.setDefault(locale)

    # 加载Qt基础模块的翻译
    translator = QTranslator()
    # 显式指定翻译文件的路径
    translations_path = os.path.join(os.path.dirname(__file__), "PySide6", "translations")
    if translator.load(locale, 'qtbase', '_', translations_path):
        app.installTranslator(translator)

    # 设置应用程序字体
    system_font = QFont()
    system_font.setFamilies(["Microsoft YaHei", "STSong", "FangSong"])
    system_font.setPointSize(10)
    system_font.setStyleStrategy(QFont.StyleStrategy.PreferAntialias)
    app.setFont(system_font)

    if not os.path.exists("Link_loop.enc"):
        from Database_connection import check_and_show_config
        if not check_and_show_config():
            sys.exit()
    # 创建并显示界面
    login_dialog = LoginDialog()

    # 设置窗口尺寸
    screen = app.primaryScreen()
    size = screen.size()
    width = size.width()*0.72
    height = width*16/9
    login_dialog.resize(width, height)
    login_dialog.show()

    sys.exit(app.exec())