from decimal import Decimal, InvalidOperation
import pymysql
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QTableWidget, QTableWidgetItem, QMessageBox
from pypinyin import pinyin, Style
import logging
import re
# 导入数据库连接配置模块
from Database_connection import load_db_config

# 加载数据库配置
db_config = load_db_config()

# 全局连接池（线程安全，可多线程共享）
# 使用Database_connection.py中的配置信息

# 配置日志记录
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class myDatabaseUtil(object):
    def __init__(self):
        self.connection = None  # 新增实例变量跟踪当前连接
    # 加载TableWidget信息，load_tableWidget_data
    def load_tableWidget_data(self, tlb_widget: QTableWidget, keyword, columnLabels: list, sqlstr: str):
        connection = None  # 改为局部变量
        try:
            db_config = load_db_config()
            connection = pymysql.connect(**db_config)  # 创建新连接
            self.connection = connection  # 跟踪当前连接（可选）
            try:
                with connection.cursor() as cursor:
                    # 按照姓名检索
                    cursor.execute(sqlstr, (f"%{keyword}%",))  # 模糊查询

                    results = cursor.fetchall()
                    connection.commit()

                    # 3. 初始化表格
                    tlb_widget.setHorizontalHeaderLabels(columnLabels)
                    tlb_widget.setRowCount(0)  # 清空旧数据

                    # 4. 填充数据
                    column_count = tlb_widget.columnCount()
                    tlb_widget.setColumnHidden(0, True)
                    if not results:
                        # 插入一个空行
                        row_idx = 0
                        tlb_widget.insertRow(row_idx)
                        column_count = tlb_widget.columnCount()

                        for col_idx in range(column_count):
                            item = QTableWidgetItem(" ")
                            tlb_widget.setItem(row_idx, col_idx, item)

                    else:
                        # 正常插入数据
                        for row_idx, row_data in enumerate(results):
                            tlb_widget.insertRow(row_idx)
                            for col_idx, col_data in enumerate(row_data):
                                item = QTableWidgetItem(str(col_data) if col_data is not None else "")
                                tlb_widget.setItem(row_idx, col_idx, item)
                    # 5. 自动调整列宽
                    tlb_widget.resizeColumnsToContents()
            except Exception as e:
                QMessageBox.warning(self, "查询错误", f"搜索失败: {str(e)}")
        except pymysql.Error as e:
           QMessageBox.critical(None, "数据库错误", f"数据库操作失败:\n{str(e)}")  # 修复self参数问题

        finally:
            if connection and connection.open:  # 安全关闭连接
                connection.close()
            self.connection = None  # 重置连接状态


    def query_database_info(self, sqlstr, parameter)->tuple:
        connection = None  # 局部变量
        """查询患者详细信息"""
        try:
            db_config = load_db_config()
            connection = pymysql.connect(**db_config)
            self.connection = connection  # 跟踪当前连接（可选）
            with connection.cursor() as cursor:
                cursor.execute(sqlstr, (parameter,))
                result = cursor.fetchone()
                connection.commit()

                if result!=0:
                    return result
                else:
                    QMessageBox.warning(self, '提示', '未找到该患者的记录')
                    return None
        except pymysql.Error as e:
            # 检查错误码（表不存在的错误码通常是 1146）
            if e.args[0] == 1146:
                print("错误：数据库表不存在！")
                QMessageBox.critical(self, '数据库错误', f'错误：数据库表不存在！: {str(e)}')
            else:
                QMessageBox.critical(self, '数据库错误', f'数据库错误: {str(e)}')
        except pymysql.Error as e:
            QMessageBox.critical(self, '数据库错误', f'数据库操作失败: {str(e)}')
        finally:
            if connection and connection.open:
                connection.close()
            self.connection = None

    def close_connection(self):  # 新增方法
        """显式关闭当前连接（如果存在）"""
        if self.connection and self.connection.open:
            self.connection.close()
            self.connection = None

    def copy_tablewidget_content(self,dest_table:QTableWidget,src_table:QTableWidget):
        """执行表格复制操作"""
        # 清空目标表格
        """执行表格复制操作"""
        # 清空目标表格
        dest_table.clearContents()
        # 1. 复制表格结构
        rows = src_table.rowCount()
        cols = src_table.columnCount()
        dest_table.setRowCount(rows)
        dest_table.setColumnCount(cols)

        ##
        # 2. 复制表头
        # 水平表头
        for col in range(cols):
            header = src_table.horizontalHeaderItem(col)
            if header:
                dest_table.setHorizontalHeaderItem(col, QTableWidgetItem(header.text()))
            # 复制列宽
            dest_table.setColumnWidth(col, src_table.columnWidth(col))
        ##
       # 3. 复制单元格数据
        for row in range(rows):
            for col in range(cols):
                src_item = src_table.item(row, col)
                if src_item:
                    # 深度复制单元格内容
                    dest_item = QTableWidgetItem(src_item.text())
                    dest_table.setItem(row, col, dest_item)
                else:
                    dest_table.setItem(row, col, QTableWidgetItem())

    def set_column_read_only(self, table_widget:QTableWidget, column_index, read_only):
        """
        设置指定列的编辑权限。

        :param column_index: 要设置的列的索引。
        :param read_only: 是否为只读（不可编辑）。
        """
        for row in range(table_widget.rowCount()):
            item = table_widget.item(row, column_index)
            if item is not None:
                if read_only:
                    item.setFlags(item.flags() & ~Qt.ItemIsEditable)
                else:
                    item.setFlags(item.flags() | Qt.ItemIsEditable)


    # 假设 DB_CONFIG 和其他配置已经正确设置

    def has_chinese_characters(self,text: str) -> bool:
        """检查字符串中是否包含中文字符"""
        return any('\u4e00' <= c <= '\u9fff' for c in text)

    def get_initials(self,name: str) -> str:
        """
        将姓名转换为拼音首字母（中文）或首字母缩写（英文）
        示例：张三 -> ZS；John Doe -> JD
        """
        try:
            if self.has_chinese_characters(name):
                # 处理中文名：过滤非中文和·符号
                cleaned_name = ''.join([c for c in name if ('\u4e00' <= c <= '\u9fff') or c == '·'])
                initials = [
                    p[0][0].upper()
                    for p in pinyin(
                        cleaned_name,
                        style=Style.FIRST_LETTER,
                        errors='ignore'
                    )
                ]
                return ''.join(initials) if initials else ''
            else:
                # 处理英文名：分割并取首字母
                words = re.split(r"[^a-zA-Z']+", name.strip())

                initials = [word[0].upper() for word in words if word]
                return ''.join(initials) if initials else ''
        except Exception as e:
            logging.error(f"Initials conversion failed: {name} | Error: {str(e)}")
            return ''

    def get_name_initials(self,name: str) -> str:
        # 获取拼音首字母并大写
        cleaned_name = ''.join([c for c in name if '\u4e00' <= c <= '\u9fff' or c == '·'])
        initials = [
            p[0][0].upper()
            for p in pinyin(
                cleaned_name,
                style=Style.FIRST_LETTER,
                errors='ignore'  # 忽略无法转换的字符
            )
        ]
        if self.has_chinese_characters(name):
            initials = self.get_pinyin_initials(name)
        else:
            # 处理英文名：分割并取首字母
            words = re.split(r"[^a-zA-Z']+", name.strip())
            initials = [word[0].upper() for word in words if word]
            initials = ''.join(initials) if initials else ''
        return initials

    def get_pinyin_initials(self,name: str) -> str:
        """
        将中文姓名转换为拼音首字母
        示例：张三 -> ZS
        """
        try:
            # 过滤非中文字符（保留中文和·符号）
            cleaned_name = ''.join([c for c in name if '\u4e00' <= c <= '\u9fff' or c == '·'])

            # 获取拼音首字母并大写
            initials = [
                p[0][0].upper()
                for p in pinyin(
                    cleaned_name,
                    style=Style.FIRST_LETTER,
                    errors='ignore'  # 忽略无法转换的字符
                )
            ]
            return ''.join(initials) if initials else ''
        except Exception as e:
            logging.error(f"拼音转换失败：{name} | 错误：{str(e)}")
            return ''

    def is_float(self, str):
        try:
            Decimal(str.replace(',', ''))  # 移除可能的逗号，例如在欧洲数字格式中
            return True
        except InvalidOperation:
            return False

    def clean_decimal_input(self,input_str: str) -> Decimal:
        # 处理空值或None
        cleaned = (input_str or "0").strip()
        # 替换逗号为小数点（适应不同地区格式）
        cleaned = cleaned.replace(",", ".")
        # 移除非数字字符（保留数字、负号和小数点）
        cleaned = "".join([c for c in cleaned if c in "0123456789.-"])
        # 处理空字符串或无效格式（如 "--"）
        if not cleaned or cleaned in (".", "-"):
            cleaned = "0"
        # 转换并返回Decimal
        try:
            return Decimal(cleaned)
        except InvalidOperation:
            return Decimal(0)