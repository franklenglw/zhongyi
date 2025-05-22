# preview.py
import os
import sys
import pymysql
from io import BytesIO
from reportlab.lib.enums import TA_LEFT
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus.para import Paragraph
from Database_connection import load_db_config
from PySide6.QtWidgets import QMessageBox

# ================== 字体注册配置 ==================
FONT_DEFINITIONS = [
    {'name': 'Microsoft YaHei', 'path': 'msyh.ttf'},  # 微软雅黑
    {'name': 'STSong', 'path': 'STSONG.TTF'},  # 宋体
    {'name': 'SimHei', 'path': 'simhei.ttf'},  # 黑体
    {'name': 'FangSong', 'path': 'simfang.ttf'},  # 仿宋
    {'name': 'KaiTi', 'path': 'simkai.ttf'},  # 楷体
]

# 尝试注册字体，选择第一个可用的
registered_font_name = None
for font in FONT_DEFINITIONS:
    try:
        pdfmetrics.registerFont(TTFont(font['name'], font['path']))
        registered_font_name = font['name']
        break
    except Exception as e:
        print(f"字体注册失败 {font['name']}: {str(e)}")

if not registered_font_name:
    raise RuntimeError("无法注册任何中文字体，请检查字体文件是否存在")


class PreviewGenerator:
    def __init__(self, patient_id, user_id):
        self.patient_id = patient_id
        self.user_id = user_id
        self.page_width, self.page_height = A4
        self.margin = 1.5 * cm
        self.y_position = self.page_height - self.margin
        self.line_height = 0.8 * cm
        self.data = None
        self.withoutdiagprint = False
        self.footer_height = 3 * cm  # 预估页脚高度
        self.font_name = registered_font_name  # 使用注册的字体名称

    def add_newlines_by_width(self, text, max_width, font_name, font_size, canvas):
        """
        根据文本宽度自动插入换行符 \n
        规则：
        1. 使用 canvas.stringWidth 计算文本宽度
        2. 当文本宽度超过 max_width 时，插入换行符
        3. 确保标点符号不会出现在行首
        4. 对特殊字符（如 < 和 >）进行转义处理
        5. 保留段落间的换行符
        """
        if not text:
            return text

        # 定义中英文标点符号集合
        punctuations = {
            # 中文标点符号
            '，', '。', '！', '？', '；', '：', '“', '”', '‘', '’', '）', '】', '…', '、', '—', '》', '』',
            '〕', '〉', '·',
            # 英文标点符号
            ',', '.', '!', '?', ';', ':', '"', "'", ')', ']', '}', '…', '-', '>', '”', '’'
        }
        # 转义特殊字符
        text = text.replace("<", "&lt;").replace(">", "&gt;")

        # 按段落分割文本
        paragraphs = text.split('\n')
        result = []

        for paragraph in paragraphs:
            if not paragraph:
                result.append("")  # 保留空行
                continue

            lines = []
            current_line = ""
            for word in paragraph:
                # 检查当前行宽度是否超过最大宽度
                if canvas.stringWidth(current_line + word, font_name, font_size) > max_width:
                    # 如果当前字符是标点符号，将其移到上一行的末尾
                    if word in punctuations and current_line:
                        # 将标点符号移到上一行的末尾
                        lines.append(current_line)
                        current_line = word  # 开始新的一行
                    else:
                        # 否则，插入换行符并开始新的一行
                        lines.append(current_line)
                        current_line = word
                else:
                    current_line += word  # 继续添加到当前行

            # 添加最后一行
            if current_line:
                lines.append(current_line)

            # 合并行并确保标点符号不在行首
            paragraph_result = []
            for line in lines:
                if line and line[0] in punctuations:
                    # 如果行首是标点符号，将其移到上一行的末尾
                    if paragraph_result:
                        paragraph_result[-1] += line[0]  # 将标点符号移到上一行的末尾
                        line = line[1:]  # 移除行首的标点符号
                paragraph_result.append(line)

            # 将段落结果添加到最终结果中
            result.append("\n".join(paragraph_result))

        # 合并段落，保留段落间的换行符
        return "\n".join(result)

    def _fetch_data(self):
        """从数据库获取所有需要的数据"""
        db_config = load_db_config()
        conn = pymysql.connect(**db_config)
        cursor = conn.cursor(pymysql.cursors.DictCursor)

        # 获取基本设置（只获取诊所名称和处方抬头）
        cursor.execute("""
            SELECT 诊所名称, 处方抬头
            FROM 基本设置 
            WHERE user_id = %s
        """, (self.user_id,))
        base_data = cursor.fetchone() or {"诊所名称": "", "处方抬头": ""}

        # 获取常规资料
        cursor.execute("""
            SELECT 
                主治医生, 病历号, 诊金,
                住址 AS 地址, 电话,
                姓名, 性别, 年龄, 诊断, 日期时间, 辨证, 用法, 剂数, 
                针灸或其他, 针灸次数, 药费, 针灸费用, 总费用, 备注,
                病证, 药物1, 药物2, 药物3, 药物4, 药物5, 药物6, 药物7, 药物8, 药物9, 药物10,
                药物11, 药物12, 药物13, 药物14, 药物15, 药物16, 药物17, 药物18, 药物19, 药物20,
                用量1, 用量2, 用量3, 用量4, 用量5, 用量6, 用量7, 用量8, 用量9, 用量10,
                用量11, 用量12, 用量13, 用量14, 用量15, 用量16, 用量17, 用量18, 用量19, 用量20,
                先煎后下1, 先煎后下2, 先煎后下3, 先煎后下4, 先煎后下5, 先煎后下6, 先煎后下7, 先煎后下8, 先煎后下9, 先煎后下10,
                先煎后下11, 先煎后下12, 先煎后下13, 先煎后下14, 先煎后下15, 先煎后下16, 先煎后下17, 先煎后下18, 先煎后下19, 先煎后下20
            FROM 常规资料 
            WHERE 编号 = %s
        """, (self.patient_id,))
        medical_data = cursor.fetchone() or {}

        conn.commit()
        cursor.close()
        conn.close()

        # 合并数据
        merged_data = {
            **base_data,
            **medical_data
        }
        return merged_data

    def _draw_page_header(self, c):
        """绘制每页固定表头"""
        # 绘制外框
        c.setLineWidth(1.2)
        c.rect(self.margin, self.margin,
               self.page_width - 2 * self.margin,
               self.page_height - 2 * self.margin)

        # 诊所名称（恢复原来的显示方式）
        self.y_position -= 0.5 * cm
        c.setFont(self.font_name, 12)
        clinic_name = self.data.get("诊所名称", "")
        # 手动插入空格加宽字间距
        spaced_clinic_name = " ".join(list(clinic_name)) if clinic_name else ""
        c.drawCentredString(self.page_width / 2, self.y_position, spaced_clinic_name)
        self.y_position -= 0.7 * cm

        # 主标题改为"病历"
        c.setFont(self.font_name, 18)
        c.drawCentredString(self.page_width / 2, self.y_position, "病历记录")
        self.y_position -= 1.0 * cm

        # 患者信息 - 姓名、性别、年龄左对齐，病历号右对齐
        c.setFont(self.font_name, 13)

        # 左对齐部分
        left_part = f"姓名：{self.data.get('姓名', '')}                  " \
                    f"性别：{self.data.get('性别', '')}                  " \
                    f"年龄：{self.data.get('年龄', '')}"
        c.drawString(2 * cm, self.y_position, left_part)

        # 右对齐部分（病历号）
        record_label = "病历号："
        record_number = str(self.data.get('病历号', ''))

        # 计算标签和号码的总宽度
        label_width = c.stringWidth(record_label, self.font_name, 13)
        number_width = c.stringWidth(record_number, self.font_name, 13)
        total_width = label_width + number_width

        # 确保不超过右边距
        max_right = self.page_width - 2 * cm  # 右边距位置
        start_x = max_right - total_width

        # 分别绘制标签和号码，确保右对齐
        c.drawString(start_x, self.y_position, record_label)
        c.drawString(start_x + label_width, self.y_position, record_number)

        self._draw_underline(c)
        self.y_position -= 1.0 * cm

        line4 = f"地址：{self.data.get('地址', '')}"
        c.drawString(2 * cm, self.y_position, line4)
        linephone = f"电话：{self.data.get('电话', '')}"
        phonestring_width = c.stringWidth(linephone, self.font_name, 13)
        c.drawRightString(self.page_width - 2 * cm, self.y_position, linephone)
        self._draw_underline(c)
        self.y_position -= 1.0 * cm

        line5 = f"诊断：{self.data.get('诊断', '')}"
        c.drawString(2 * cm, self.y_position, line5)
        datestring = f"日期：{self.data.get('日期时间', '')}"
        datestring_width = c.stringWidth(datestring, self.font_name, 13)
        c.drawRightString(self.page_width - 2 * cm, self.y_position, datestring)
        self._draw_underline(c)
        self.y_position -= 0.5 * cm

    def _draw_footer(self, c):
        """绘制每页固定页脚"""
        current_y = self.margin + self.footer_height

        # 只显示主治医生（居中）
        if self.data.get('主治医生'):
            doctor_text = f"主治医生：{self.data['主治医生']}"
            c.setFont(self.font_name, 12)
            c.drawCentredString(self.page_width / 2, current_y, doctor_text)
            current_y -= 0.8 * cm

        # 费用信息（药费、针灸费用、合计）
        fee_line = []
        if self.data.get('诊金') not in (None, "", "0"):
            fee_line.append(f"诊金：{float(self.data['诊金']):.2f}元")
        if self.data.get('药费') not in (None, "", "0"):
            fee_line.append(f"药费：{self.data['药费']}元")
        if self.data.get('针灸费用') not in (None, "", "0"):
            fee_line.append(f"针灸等费用：{self.data['针灸费用']}元")
        if self.data.get('总费用') not in (None, "", "0"):
            fee_line.append(f"合计：{self.data['总费用']}元")

        if fee_line:
            fee_line_text = '   '.join(fee_line)  # 用三个空格分隔
            c.setFont(self.font_name, 14)
            c.drawCentredString(self.page_width / 2, current_y, fee_line_text)
            # 绘制费用框
            c.rect(2 * cm, current_y - 0.5 * cm, self.page_width - 4 * cm, 1.2 * cm)
            current_y -= 1.2 * cm

        # 单位说明（左下角）
        c.setFont(self.font_name, 10)
        c.drawString(2 * cm, current_y, "（针灸等费用是指针灸或其他疗法的费用）")

    def _draw_prescription_content(self, c):
        """完善的药品表格打印"""
        page_top = self.y_position
        min_y = self.margin + self.footer_height
        col_margin = 0.5 * cm  # 列间距

        # 1. 打印辩证（需要分页保护）
        if '辨证' in self.data and self.data['辨证']:
            bianzheng_text = f"辩证：{self.data['辨证']}"
            wrapped_bz = self.add_newlines_by_width(bianzheng_text, self.page_width - 4 * cm, self.font_name, 12, c)
            bz_height = self._draw_content_block(c, wrapped_bz, self.font_name, 12)
            self.y_position -= bz_height + 0.1 * cm

        # 2. 打印证候（即病证表现，需要分页保护）
        if not self.withoutdiagprint and self.data.get('病证'):
            # 在辩证上方添加空行
            self.y_position -= 0.3 * cm  # ✅ 添加空行间距
            zhenghou_text = f"病证：{self.data['病证']}"
            wrapped_zh = self.add_newlines_by_width(zhenghou_text, self.page_width - 4 * cm, self.font_name, 12, c)
            zh_height = self._draw_content_block(c, wrapped_zh, self.font_name, 12)
            if self.y_position - zh_height < min_y:
                return False
            self.y_position -= zh_height + 0.1 * cm

        # 3. 打印针灸信息及次数（成对显示）
        has_acupuncture = False
        if self.data.get('针灸或其他'):
            self.y_position -= 0.5 * cm
            acu_text = f"针灸或其他：{self.data['针灸或其他']}"
            wrapped_acu = self.add_newlines_by_width(acu_text, self.page_width - 4 * cm, self.font_name, 12, c)
            acu_height = self._draw_content_block(c, wrapped_acu, self.font_name, 12)
            if self.y_position - acu_height < min_y:
                return False
            self.y_position -= acu_height + 0.1 * cm

            # 针灸次数（紧跟针灸信息）
            if self.data.get('针灸次数'):
                self.y_position -= 0.5 * cm
                zhenjiu_text = f"{self.data['针灸次数']}次"
                c.setFont(self.font_name, 12)
                c.drawRightString(self.page_width - 2 * cm, self.y_position, zhenjiu_text)
                self.y_position -= 0.1 * cm

        # 4. 打印药品信息（成对显示剂数）
        drug_data = []
        for i in range(1, 21):
            if self.data.get(f"药物{i}", "") and self.data.get(f"用量{i}", ""):
                drug = self.data.get(f"药物{i}", "").strip()
                dosage = self.data.get(f"用量{i}", "").strip() + "克"
                decoction = self.data.get(f"先煎后下{i}", "").strip()
                if drug:
                    drug_data.append((drug, dosage, f"({decoction})" if decoction else ""))

        if drug_data:
            # 处理间距：当没有针灸信息时，与上方内容保持一个空行
            if not has_acupuncture:
                self.y_position -= 0.4 * cm  # 空行间距

            # 添加中药标签（间距减少到0.5cm）
            c.setFont(self.font_name, 12)
            zhongyao_text = "中药："
            c.drawString(2 * cm, self.y_position, zhongyao_text)
            self.y_position -= 0.5 * cm  # 原为0.8cm

            # 打印药品表格
            drug_printed = self._draw_drug_table(c, min_y, self.font_name, 12, drug_data)
            if not drug_printed:
                return False

            # 剂数（紧跟药品表格）
            if self.data.get('剂数'):
                self.y_position -= 0.3 * cm  # 原为0.2cm
                ji_shu_text = f"{self.data['剂数']}付"
                c.drawRightString(self.page_width - 2 * cm, self.y_position, ji_shu_text)
                self.y_position -= 0.2 * cm

        # 5. 打印用法（带分页保护）
        if self.data.get('用法'):
            usage_text = f"用法：{self.data['用法']}"
            wrapped_usage = self.add_newlines_by_width(usage_text, self.page_width - 4 * cm, self.font_name, 12, c)
            usage_height = self._draw_content_block(c, wrapped_usage, self.font_name, 12)
            if self.y_position - usage_height < min_y:
                return False
            self.y_position -= usage_height + 0.5 * cm

        # 6. 打印备注（带分页保护）
        if self.data.get('备注'):
            note_text = f"备注：{self.data['备注']}"
            wrapped_note = self.add_newlines_by_width(note_text, self.page_width - 4 * cm, self.font_name, 12, c)
            note_height = self._draw_content_block(c, wrapped_note, self.font_name, 12)
            if self.y_position - note_height < min_y:
                return False
            self.y_position -= note_height

        return True

    def _draw_underline(self, c):
        """绘制单下划线"""
        c.line(2 * cm, self.y_position - 0.3 * cm,
               self.page_width - 2 * cm, self.y_position - 0.3 * cm)

    def _draw_content_block(self, c, text, fontname, fontsize):
        """通用内容块绘制方法"""
        try:
            return self._draw_wrapped_text(c, 2 * cm, self.y_position,
                                           self.page_width - 4 * cm, text, fontname, fontsize)
        except Exception as e:
            print(f"绘制内容块时出错：{str(e)}")
            return 0  # 容错处理

    def _draw_drug_table(self, c, min_y, fontname, fontsize, drug_data):
        """增强的药品表格打印（带自动分页）"""
        # 初始化表格参数
        col_width = (self.page_width - 4 * cm - 0.5 * cm) / 2
        line_spacing = 0.1 * cm

        # 分页打印逻辑
        while drug_data:
            current_page_drugs = []
            # 计算本页可打印药品数量
            while drug_data:
                temp = drug_data[:2]  # 每次取两个药品
                max_h = 0
                for drug_info in temp:
                    text = f"{drug_info[0]} {drug_info[1]}{drug_info[2]}"
                    wrapped = self.add_newlines_by_width(text, col_width, fontname, fontsize, c)
                    h = self._calculate_text_height(wrapped, col_width, fontname, fontsize)
                    max_h = max(max_h, h)

                if (self.y_position - (max_h + line_spacing)) < min_y:
                    break

                current_page_drugs.extend(temp)
                drug_data = drug_data[2:]

            # 绘制本页药品
            x_left = 2 * cm
            x_right = x_left + col_width + 0.5 * cm
            current_y = self.y_position + line_spacing  # 起始位置

            # 绘制表格线
            c.setLineWidth(0.3)
            c.line(x_left, current_y, x_left + 2 * col_width + 0.5 * cm, current_y)

            # 打印药品内容
            for i in range(0, len(current_page_drugs), 2):
                row_data = current_page_drugs[i:i + 2]
                row_height = 0

                # 左列
                if len(row_data) >= 1:
                    drug_info = row_data[0]
                    text = f"{drug_info[0]} {drug_info[1]}{drug_info[2]}"
                    wrapped = self.add_newlines_by_width(text, col_width, fontname, fontsize, c)
                    h = self._draw_wrapped_text(c, x_left, current_y, col_width, wrapped, fontname, fontsize)
                    row_height = max(row_height, h)

                # 右列
                if len(row_data) >= 2:
                    drug_info = row_data[1]
                    text = f"{drug_info[0]} {drug_info[1]}{drug_info[2]}"
                    wrapped = self.add_newlines_by_width(text, col_width, fontname, fontsize, c)
                    h = self._draw_wrapped_text(c, x_right, current_y, col_width, wrapped, fontname, fontsize)
                    row_height = max(row_height, h)

                # 更新位置
                current_y -= row_height + line_spacing
                c.line(x_left, current_y, x_left + 2 * col_width + 0.5 * cm, current_y)

            # 绘制列分隔线
            c.line(x_left + col_width, self.y_position + line_spacing,
                   x_left + col_width, current_y)

            # 更新当前页位置
            self.y_position = current_y - 0.3 * cm

        return True

    def _draw_wrapped_text(self, c, x, y, max_width, text, font_name, font_size):
        """确保始终返回数值型高度"""
        if not text.strip():  # 空内容直接返回0高度
            return 0

        # 使用改进后的换行逻辑
        wrapped_text = self.add_newlines_by_width(text, max_width, font_name, font_size, c)

        style = ParagraphStyle(
            name='CustomCN',
            fontName=font_name,
            fontSize=font_size,
            leading=font_size * 1.2,
            alignment=TA_LEFT,
            wordWrap='CJK',
            splitLongWords=True,  # 确保开启强制分割长词
            allowOrphans=0,  # 禁止孤行
            allowWidows=0  # 禁止寡行
        )

        try:
            p = Paragraph(wrapped_text, style)
            width, height = p.wrap(max_width, 1000)
            if height > 0:
                p.drawOn(c, x, y - height)
                return height
            return 0
        except:
            return 0

    def _calculate_text_height(self, text, max_width, font_name, font_size):
        style = ParagraphStyle(
            name='temp',
            fontName=font_name,
            fontSize=font_size,
            leading=font_size * 1.2,
            wordWrap='CJK',
            splitLongWords=True,  # 添加与绘制时相同的参数
            allowOrphans=0,
            allowWidows=0
        )
        p = Paragraph(text, style)
        return p.wrap(max_width, 1000)[1]

    def generate(self):
        """生成PDF预览"""
        self.data = self._fetch_data()
        buffer = BytesIO()
        c = canvas.Canvas(buffer, pagesize=A4)

        # 绘制页眉
        self.y_position = self.page_height - self.margin
        self._draw_page_header(c)

        # 绘制正文内容
        self._draw_prescription_content(c)

        # 绘制页脚
        self._draw_footer(c)

        c.save()
        buffer.seek(0)
        return buffer


def main(patient_id, user_id):
    try:
        generator = PreviewGenerator(patient_id, user_id)
        pdf_data = generator.generate()
        return pdf_data
    except Exception as e:
        QMessageBox.critical(None, "错误", f"生成预览失败: {str(e)}")
        return None


if __name__ == "__main__":
    # For testing
    if len(sys.argv) != 3:
        print("Usage: python preview.py <patient_id> <user_id>")
        sys.exit(1)

    patient_id = sys.argv[1]
    user_id = sys.argv[2]
    pdf_data = main(patient_id, user_id)

    if pdf_data:
        with open("preview.pdf", "wb") as f:
            f.write(pdf_data.getvalue())
        print("PDF generated successfully as preview.pdf")