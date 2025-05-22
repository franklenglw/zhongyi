"""
MySQL姓名转拼音首字母工具
作者：智能助手
版本：1.1
功能：自动将数据库中的中文姓名转换为拼音首字母
"""

import pymysql
from pypinyin import pinyin, Style
import logging
import re
from Database_connection import check_and_show_config, load_db_config  # 新增数据库连接模块导入

# ------------------ 配置区 ------------------
# DB_CONFIG = {
#     'host': 'localhost',  # 数据库地址
#   'user': 'root',  # 数据库用户名
#   'password': 'zhongyichufang2025',  # 数据库密码
#   'database': 'zy',  # 数据库名称
#   'port': 3306,  # 端口号
#   'charset': 'utf8',  # 字符编码
#   'cursorclass': pymysql.cursors.DictCursor
# }

# 配置日志记录
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# 假设 DB_CONFIG 和其他配置已经正确设置

def has_chinese_characters(text: str) -> bool:
    """检查字符串中是否包含中文字符"""
    return any('\u4e00' <= c <= '\u9fff' for c in text)

def get_initials(name: str) -> str:
    """
    将姓名转换为拼音首字母（中文）或首字母缩写（英文）
    示例：张三 -> ZS；John Doe -> JD
    """
    try:
        if has_chinese_characters(name):
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

def get_name_initials(name:str)->str:
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
    if has_chinese_characters(name):
        initials = get_pinyin_initials(name)
    else:
        # 处理英文名：分割并取首字母
        words = re.split(r"[^a-zA-Z']+", name.strip())
        initials = [word[0].upper() for word in words if word]
        initials = ''.join(initials) if initials else ''
def get_pinyin_initials(name: str) -> str:
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

if __name__ == "__main__":
    # ------------------ 数据库连接初始化 ------------------
    check_and_show_config()  # 检查数据库配置
    db_config = load_db_config()  # 加载加密配置
    db_config['cursorclass'] = pymysql.cursors.DictCursor  # 补充游标类型配置

    # ------------------ 环境检查 ------------------
    connection = None
    try:
        # ------------------ 连接数据库 ------------------
        connection = pymysql.connect(**DB_CONFIG)
        with connection:
            with connection.cursor() as cursor:
                # ------------------ 数据读取 ------------------
                read_sql = "SELECT 编号, 姓名 FROM 常规资料 WHERE 姓名 IS NOT NULL"
                cursor.execute(read_sql)
                records = cursor.fetchall()

                if not records:
                    logging.warning("未找到有效数据")
                    exit(0)

                # ------------------ 数据处理 ------------------
                update_count = 0
                for record in records:
                    record_id = record['编号']
                    name = record['姓名'].strip()  # 去除前后空格

                    if not name:
                        continue

                    # 生成拼音首字母
                    if has_chinese_characters(name):
                        initials = get_pinyin_initials(name)
                    else:
                        # 处理英文名：分割并取首字母
                        words = re.split(r"[^a-zA-Z']+", name.strip())
                        initials = [word[0].upper() for word in words if word]
                        initials = ''.join(initials) if initials else ''
                    # ------------------ 数据更新 ------------------
                    update_sql = "UPDATE 常规资料 SET 姓名拼音 = %s WHERE 编号 = %s"
                    affected = cursor.execute(update_sql, (initials, record_id))

                    if affected == 1:
                        update_count += 1
                        if update_count % 100 == 0:
                            logging.info(f"已处理 {update_count} 条记录")

                # ------------------ 提交事务 ------------------
                connection.commit()
                logging.info(f"成功更新 {update_count}/{len(records)} 条记录")

    except pymysql.MySQLError as e:
        logging.error(f"数据库操作失败：{str(e)}")
        if connection:
            connection.rollback()