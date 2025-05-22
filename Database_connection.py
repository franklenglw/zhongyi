import sys
import os
import json
from PySide6.QtWidgets import (
    QApplication,
    QDialog,
    QVBoxLayout,
    QLineEdit,
    QPushButton,
    QFormLayout,
    QMessageBox
)
from PySide6.QtCore import Qt
import pymysql
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Hash import SHA256
from Crypto.Random import get_random_bytes


class DatabaseConnectionDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("数据库连接配置")
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()
        form = QFormLayout()

        self.host_edit = QLineEdit()
        self.port_edit = QLineEdit("3306")
        self.user_edit = QLineEdit()
        self.password_edit = QLineEdit()
        self.password_edit.setEchoMode(QLineEdit.Password)
        self.database_edit = QLineEdit()
        self.charset_edit = QLineEdit("utf8mb4")

        form.addRow("主机地址:", self.host_edit)
        form.addRow("端口:", self.port_edit)
        form.addRow("用户名:", self.user_edit)
        form.addRow("密码:", self.password_edit)
        form.addRow("数据库名:", self.database_edit)
        form.addRow("字符集:", self.charset_edit)

        self.test_btn = QPushButton("测试连接")
        self.test_btn.clicked.connect(self.test_connection)

        layout.addLayout(form)
        layout.addWidget(self.test_btn)
        self.setLayout(layout)

    def get_config(self):
        return {
            "host": self.host_edit.text().strip(),
            "port": self.port_edit.text().strip(),
            "user": self.user_edit.text().strip(),
            "password": self.password_edit.text().strip(),
            "database": self.database_edit.text().strip(),
            "charset": self.charset_edit.text().strip() or "utf8mb4"
        }

    def validate_config(self, config):
        errors = []
        if not config["host"]:
            errors.append("主机地址不能为空")
        if not config["user"]:
            errors.append("用户名不能为空")
        if not config["password"]:
            errors.append("密码不能为空")
        if not config["database"]:
            errors.append("数据库名不能为空")

        try:
            port = int(config["port"])
            if not (0 < port <= 65535):
                errors.append("端口号必须为1-65535之间的整数")
        except ValueError:
            errors.append("端口号必须为数字")

        return errors

    def test_connection(self):
        config = self.get_config()
        errors = self.validate_config(config)

        if errors:
            QMessageBox.critical(self, "输入错误", "\n".join(errors))
            return

        try:
            # 强制转换为整数
            port = int(config["port"])
            conn = pymysql.connect(
                host=config["host"],
                port=port,
                user=config["user"],
                password=config["password"],
                database=config["database"],
                charset=config["charset"]
            )
            conn.close()

            # 更新配置中的端口为整数
            config["port"] = port
            self.save_encrypted_config(config)

            QMessageBox.information(self, "成功", "数据库连接成功！")
            self.accept()
        except pymysql.Error as e:
            QMessageBox.critical(self, "连接失败", f"数据库连接失败: {e}")

    def save_encrypted_config(self, config):
        password = "secure_key_2023".encode("utf-8")
        key = SHA256.new(password).digest()
        data = json.dumps(config).encode("utf-8")

        iv = get_random_bytes(AES.block_size)
        cipher = AES.new(key, AES.MODE_CBC, iv)
        ct_bytes = cipher.encrypt(pad(data, AES.block_size))

        with open("Link_loop.enc", "wb") as f:
            f.write(iv)
            f.write(ct_bytes)

def load_db_config(self=None):
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

def check_and_show_config():
    if not os.path.exists("Link_loop.enc"):
        app = QApplication.instance()
        if not app:
            app = QApplication(sys.argv)

        dialog = DatabaseConnectionDialog()
        if dialog.exec() == QDialog.Accepted:
            return True
        else:
            sys.exit()
    return True
