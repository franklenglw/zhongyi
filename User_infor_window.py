import sys
from PySide6 import QtWidgets, QtCore
from PySide6.QtWidgets import QDialog, QMessageBox
from ui_UserInfor import Ui_Dialog
import pymysql
from DatabaseUtil import myDatabaseUtil
from Database_connection import load_db_config
from pypinyin import pinyin, Style


class AuthDialog(QtWidgets.QDialog):
    _empty_password_prompted = False

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("管理员授权")
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        layout = QtWidgets.QVBoxLayout(self)

        self.username_edit = QtWidgets.QLineEdit("Admin")
        self.username_edit.setEnabled(False)
        layout.addWidget(QtWidgets.QLabel("用户名:"))
        layout.addWidget(self.username_edit)

        self.password_edit = QtWidgets.QLineEdit()
        self.password_edit.setEchoMode(QtWidgets.QLineEdit.Password)
        layout.addWidget(QtWidgets.QLabel("密码:"))
        layout.addWidget(self.password_edit)

        self.confirm_btn = QtWidgets.QPushButton("确认")
        self.confirm_btn.clicked.connect(self.verify)
        layout.addWidget(self.confirm_btn)

        self.password_edit.returnPressed.connect(self.verify)

    def verify(self):
        try:
            # 使用专用数据库连接模块的配置（原硬编码配置已删除）
            db_config = load_db_config()
            conn = pymysql.connect(**db_config)

            with conn.cursor() as cursor:
                cursor.execute("SELECT 密码 FROM 基本设置 WHERE 账号=%s", ("Admin",))
                result = cursor.fetchone()

                if not result:
                    QtWidgets.QMessageBox.warning(self, "错误", "管理员账号不存在")
                    return

                valid_password = result[0] or ""
                input_password = self.password_edit.text()

                if valid_password == input_password:
                    if valid_password == "":
                        # 检查类变量状态
                        if not AuthDialog._empty_password_prompted:  # 直接通过类名访问
                            QtWidgets.QMessageBox.information(
                                self,
                                "提示",
                                "当前管理员密码为空，建议立即设置",
                                QtWidgets.QMessageBox.Ok
                            )
                            AuthDialog._empty_password_prompted = True  # 更新类变量
                    self.accept()
                else:
                    QtWidgets.QMessageBox.warning(self, "错误", "密码错误")
            conn.close()
        except Exception as e:
            QtWidgets.QMessageBox.warning(self, "错误", f"验证失败：{str(e)}")

class UserInfoWindow(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.conn = None
        self.original_data = {}
        # 修正列名顺序与数据库字段对应
        self.column_names = [
            '账号', '医生', '诊金', '诊所名称', '处方抬头',
            '配药', '诊所电话', '诊所地址', '密码', '密码提示', '医生拼音'
        ]
        self.m_databaseUtil = myDatabaseUtil()
        self.setup_connections()
        self.init_db()
        self.load_data()
        self.m_tbl_UserInfor.setColumnHidden(0, True)   # 隐藏user_id列
        self.m_tbl_UserInfor.setColumnHidden(11, True)  # 隐藏医生拼音列

    def setup_connections(self):
        self.m_bt_add.clicked.connect(self.on_add_clicked)
        self.m_bt_save.clicked.connect(self.on_save_clicked)
        self.m_bt_del.clicked.connect(self.on_delete_clicked)
        self.m_edt_searchfilterDoc.textChanged.connect(self.filter_data)

    def init_db(self):
        try:
            # 使用专用数据库连接模块的配置（原硬编码配置已删除）
            self.conn = pymysql.connect(**load_db_config())
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "错误", f"数据库连接失败：{str(e)}")
            sys.exit(1)

    def generate_pinyin_abbreviation(self, chinese_str):
        """生成拼音首字母缩写"""
        if not chinese_str:
            return ""
        pinyin_list = pinyin(chinese_str, style=Style.FIRST_LETTER)
        abbreviation = ''.join([p[0].upper() for p in pinyin_list if p])
        return abbreviation

    def filter_data(self):
        """优化后的过滤逻辑（修正列索引）"""
        keyword = self.m_edt_searchfilterDoc.text().lower()
        for row in range(self.m_tbl_UserInfor.rowCount()):
            # 医生列（索引2）和拼音列（索引11）
            doctor_item = self.m_tbl_UserInfor.item(row, 2)
            pinyin_item = self.m_tbl_UserInfor.item(row, 11)

            doctor_text = doctor_item.text().lower() if doctor_item else ""
            pinyin_text = pinyin_item.text().lower() if pinyin_item else ""

            match = keyword in doctor_text or keyword in pinyin_text
            self.m_tbl_UserInfor.setRowHidden(row, not match)

    def load_data(self):
        """从数据库加载数据（修正列索引处理）"""
        try:
            with self.conn.cursor() as cursor:
                sql = """SELECT user_id, 账号, 医生, 诊金, 诊所名称, 处方抬头, 
                        配药, 诊所电话, 诊所地址, 密码, 密码提示, 医生拼音 
                        FROM 基本设置"""
                cursor.execute(sql)
                results = cursor.fetchall()
                self.m_tbl_UserInfor.setRowCount(0)
                self.original_data.clear()

                # 设置表格列数匹配数据库字段数
                self.m_tbl_UserInfor.setColumnCount(len(results[0]) if results else 12)

                for row_data in results:
                    row = self.m_tbl_UserInfor.rowCount()
                    self.m_tbl_UserInfor.insertRow(row)
                    record_id = row_data[0]

                    # 转换所有字段为字符串并处理None
                    str_row = [str(item) if item is not None else '' for item in row_data]
                    self.original_data[record_id] = str_row

                    # 填充所有列数据
                    for col in range(len(row_data)):
                        item = QtWidgets.QTableWidgetItem(str_row[col])
                        if col == 0:  # user_id列不可编辑
                            item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                        self.m_tbl_UserInfor.setItem(row, col, item)
        except Exception as e:
            QMessageBox.warning(self, "错误", f"加载数据失败：{str(e)}")

    def on_add_clicked(self):
        """新增空行并自动聚焦"""
        row = self.m_tbl_UserInfor.rowCount()
        self.m_tbl_UserInfor.insertRow(row)

        # 创建并插入新行项目
        for col in range(self.m_tbl_UserInfor.columnCount()):
            item = QtWidgets.QTableWidgetItem("")
            if col == 0:  # user_id列不可编辑
                item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            self.m_tbl_UserInfor.setItem(row, col, item)

        # 自动聚焦配置
        if row >= 0:
            # 设置当前选中行
            self.m_tbl_UserInfor.setCurrentCell(row, 1)
            # 触发单元格编辑
            self.m_tbl_UserInfor.edit(self.m_tbl_UserInfor.currentIndex())
            # 滚动确保新行可见
            self.m_tbl_UserInfor.scrollToItem(
                self.m_tbl_UserInfor.item(row, 1),
                QtWidgets.QAbstractItemView.PositionAtTop
            )

    def on_save_clicked(self):
        """重构保存逻辑（修正类型转换和索引问题）"""
        try:
            # 第一阶段：生成拼音并更新界面
            for row in range(self.m_tbl_UserInfor.rowCount()):
                id_item = self.m_tbl_UserInfor.item(row, 0)
                doctor_item = self.m_tbl_UserInfor.item(row, 2)  # 医生列索引2
                pinyin_item = self.m_tbl_UserInfor.item(row, 11)  # 拼音列索引11

                id_str = id_item.text().strip() if id_item else ""
                doctor_name = doctor_item.text().strip() if doctor_item else ""
                current_pinyin = pinyin_item.text().strip() if pinyin_item else ""

                new_pinyin = None
                if not id_str:  # 新增记录
                    if doctor_name:
                        new_pinyin = self.generate_pinyin_abbreviation(doctor_name)
                else:  # 修改记录
                    try:
                        record_id = int(id_str)
                        original_data = self.original_data.get(record_id)
                        if original_data and doctor_name != original_data[2]:  # 原始数据医生列索引2
                            new_pinyin = self.generate_pinyin_abbreviation(doctor_name)
                    except ValueError:
                        QMessageBox.warning(self, "错误", f"无效的user_id：{id_str}")
                        continue

                # 更新拼音显示
                if new_pinyin is not None:
                    if not pinyin_item:
                        pinyin_item = QtWidgets.QTableWidgetItem(new_pinyin)
                        self.m_tbl_UserInfor.setItem(row, 11, pinyin_item)
                    else:
                        pinyin_item.setText(new_pinyin)

            # 第二阶段：数据库操作
            with self.conn.cursor() as cursor:
                # 验证必填字段
                for row in range(self.m_tbl_UserInfor.rowCount()):
                    account_item = self.m_tbl_UserInfor.item(row, 1)
                    if not account_item or not account_item.text().strip():
                        QMessageBox.warning(self, "错误", f"第{row + 1}行账号不能为空")
                        return

                # 保存数据
                for row in range(self.m_tbl_UserInfor.rowCount()):
                    row_data = [
                        self.m_tbl_UserInfor.item(row, col).text().strip()
                        if self.m_tbl_UserInfor.item(row, col) else ""
                        for col in range(self.m_tbl_UserInfor.columnCount())
                    ]
                    id_str = row_data[0]

                    # 处理新增记录
                    if not id_str:
                        try:
                            # 类型转换和验证
                            fee = float(row_data[3]) if row_data[3] else 0.0  # 诊金列索引3
                        except ValueError:
                            QMessageBox.warning(self, "错误", f"第{row + 1}行诊金格式错误")
                            continue

                        insert_data = [
                            row_data[1],  # 账号
                            row_data[2],  # 医生
                            fee,  # 诊金（已转换）
                            row_data[4],  # 诊所名称
                            row_data[5],  # 处方抬头
                            row_data[6],  # 配药
                            row_data[7],  # 诊所电话
                            row_data[8],  # 诊所地址
                            row_data[9],  # 密码
                            row_data[10],  # 密码提示
                            row_data[11]  # 医生拼音
                        ]
                        try:
                            sql = """INSERT INTO 基本设置 
                                (账号,医生,诊金,诊所名称,处方抬头,配药,
                                诊所电话,诊所地址,密码,密码提示,医生拼音)
                                VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
                            cursor.execute(sql, insert_data)
                        except pymysql.IntegrityError:
                            QMessageBox.warning(self, "错误", f"账号 {insert_data[0]} 已存在")
                            continue

                    # 处理修改记录
                    else:
                        try:
                            record_id = int(id_str)
                        except ValueError:
                            QMessageBox.warning(self, "错误", f"第{row + 1}行user_id无效：{id_str}")
                            continue

                        original_full = self.original_data.get(record_id)
                        if not original_full:
                            continue

                        # 获取当前数据和原始数据（排除user_id列）
                        current_data = row_data[1:]  # 账号到医生拼音（11列）
                        original_data = original_full[1:]  # 对应11列

                        # 构建更新字段
                        updates = []
                        params = []
                        for col_idx in range(len(current_data)):
                            current_val = current_data[col_idx]
                            original_val = original_data[col_idx] if col_idx < len(original_data) else ""

                            # 处理诊金字段转换
                            if col_idx == 2:  # 诊金在current_data索引2
                                try:
                                    current_val = float(current_val) if current_val else 0.0
                                    original_val = float(original_val) if original_val else 0.0
                                except ValueError:
                                    QMessageBox.warning(self, "错误", f"第{row + 1}行诊金格式错误")
                                    continue

                            # 跳过未修改的密码字段
                            #if self.column_names[col_idx] == '密码' and not current_val:
                            #    continue

                            if str(current_val) != str(original_val):
                                field = self.column_names[col_idx]
                                updates.append(f"`{field}`=%s")
                                params.append(current_val)

                        if updates:
                            params.append(record_id)
                            sql = f"UPDATE 基本设置 SET {','.join(updates)} WHERE user_id=%s"
                            cursor.execute(sql, tuple(params))

                self.conn.commit()
                self.load_data()
                QMessageBox.information(self, "成功", "保存成功")

        except Exception as e:
            self.conn.rollback()
            QMessageBox.warning(self, "错误", f"保存失败：{str(e)}")

    def on_delete_clicked(self):
        selected_rows = list({index.row() for index in self.m_tbl_UserInfor.selectedIndexes()})
        if not selected_rows:
            QtWidgets.QMessageBox.warning(self, "警告", "请选择要删除的行")
            return

        auth_dialog = AuthDialog(self)  # 使用独立类
        if auth_dialog.exec() != QtWidgets.QDialog.Accepted:
            return

        deletion_occurred = False  # 添加标志变量，用于跟踪是否发生了删除操作

        try:
            with self.conn.cursor() as cursor:
                selected_rows.sort(reverse=True)
                ids_to_delete = []
                rows_to_remove = []
                admin_deletion_attempted = False  # 跟踪是否尝试删除Admin

                for row in selected_rows:
                    # 检查账号列是否为Admin（列索引1），不区分大小写
                    account_item = self.m_tbl_UserInfor.item(row, 1)
                    if account_item and account_item.text().strip().lower() == "admin":
                        admin_deletion_attempted = True
                        continue  # 跳过Admin账号的删除

                    id_item = self.m_tbl_UserInfor.item(row, 0)
                    if id_item and id_item.text().strip():
                        ids_to_delete.append(id_item.text())
                    else:
                        rows_to_remove.append(row)

                # 如果有尝试删除Admin，显示提示
                if admin_deletion_attempted:
                    QtWidgets.QMessageBox.warning(
                        self,
                        "操作禁止",
                        "Admin账号不可删除，已自动跳过",
                        QtWidgets.QMessageBox.Ok
                    )

                # 执行删除操作
                if ids_to_delete:
                    placeholders = ','.join(['%s'] * len(ids_to_delete))
                    cursor.execute(f"DELETE FROM 基本设置 WHERE user_id IN ({placeholders})", tuple(ids_to_delete))
                    deletion_occurred = True  # 如果执行了删除操作，则设置标志变量为True

                for row in rows_to_remove:
                    self.m_tbl_UserInfor.removeRow(row)

                self.conn.commit()
                self.load_data()

                # 只有在实际删除了账号时才显示“删除成功”的提示
                if deletion_occurred:
                    QtWidgets.QMessageBox.information(self, "成功", "删除成功")
        except Exception as e:
            QtWidgets.QMessageBox.warning(self, "错误", f"删除失败：{str(e)}")
            self.conn.rollback()

