import sys
from PySide6.QtWidgets import (
    QApplication, QDialog, QVBoxLayout, QScrollArea, QLabel, QWidget
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont


class AboutDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("关于 清虚内守中医处方")
        self.resize(800, 600)

        # 创建基础字体
        self.base_font = QFont()
        self.base_font.setPointSize(13)  # 设置全局基础字号

        # 应用基础字体到整个对话框
        self.setFont(self.base_font)

        # 创建滚动区域
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)

        # 主容器
        container = QWidget()
        layout = QVBoxLayout(container)
        layout.setContentsMargins(20, 20, 20, 20)

        # 标题字体（基于基础字体修改）
        title_font = QFont(self.base_font)
        title_font.setBold(True)
        title_font.setPointSize(14)

        # 添加内容部件
        components = [
            self.create_title_label("清虚内守中医处方", title_font),
            self.create_content_label(f"版本: 5.25.0511<br>发行日期：2025-2-27<br>更新日期：2025-5-11<br>版权所有: X.L&Frank L"),
            self.create_section_title("设计", title_font),
            self.create_content_label("主要功能由X.L设计，软件界面和少部分功能由Frank L设计。"),
            self.create_section_title("维护", title_font),
            self.create_content_label("后期开发和维护由Frank L实现。对bug的反馈以及功能优化上的要求，可在github上提交，本人会在个人能力范围内酌情处理。"),
            self.create_section_title("特别声明", title_font),
            self.create_content_label(
                "本软件为免费开源软件，专为中医师设计，无任何功能限制，支持win7/win10 64位系统，"
                "其他系统暂未测试。待通过beta测试后，将免费开源在github上（"
                "<a href='https://github.com/franklenglw/zhongyi/'>https://github.com/franklenglw/zhongyi/</a>）"
                "以抛砖引玉，有缘之人可自取之。"
            ),
            self.create_section_title("软件说明", title_font),
            self.create_content_label(self.generate_software_description()),
            self.create_section_title("声明", title_font),
            self.create_content_label("本软件按「原样」提供，不承担任何使用风险。您可免费使用、修改和分发本软件。不得利用本软件从事非法活动。")
        ]

        for component in components:
            layout.addWidget(component)

        layout.addStretch()
        scroll.setWidget(container)

        main_layout = QVBoxLayout(self)
        main_layout.addWidget(scroll)

    def create_title_label(self, text, font):
        label = QLabel(text)
        label.setFont(font)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        return label

    def create_section_title(self, text, font):
        label = QLabel(text)
        label.setFont(font)
        label.setStyleSheet("margin-top: 15px; color: #2c3e50;")
        return label

    def create_content_label(self, text):
        label = QLabel()
        label.setFont(self.base_font)  # 关键修改：显式设置基础字体
        label.setTextFormat(Qt.TextFormat.RichText)
        label.setText(text)
        label.setWordWrap(True)
        label.setOpenExternalLinks(True)
        label.setTextInteractionFlags(Qt.TextInteractionFlag.TextBrowserInteraction)
        label.setStyleSheet("""
            margin: 8px 0;
            line-height: 1;
        """)
        return label

    def generate_software_description(self):
        return """
        <style>
            li { margin: 8px 0; }
            b { font-weight: bold; }  /* 移除HTML中的字号设置 */
        </style>
        <ol>
            <li><b>关于数据丢失风险的温馨提示：</b>
                <ul style='list-style-type: square;'>
                    <li>建议使用HeidiSQL（推荐）或Navicat工具进行数据库操作。</li>
                    <li>如果使用MySQL数据库，不建议用Workbench执行数据库操作，可能出现数据异常丢失的情况；</li>
                    <li>定期备份是防范数据风险的最佳实践，建议建立数据库的周期性备份机制；</li>
                    <li>备份与恢复操作均十分便捷，通过简单的导出/导入即可完成；</li>
                    <li>若出现数据异常，可通过备份文件快速恢复数据库至正常状态；</li>
                    <li><span style="color: rgb(144, 0, 0); font-weight: bold;">因个人能力有限，故而软件的维护更新并不会频繁，软件运行时也可能会出现暂未发现的bug，而修正更新或不能及时，
                        还请见谅。打算用该软件的用户，也请自行斟酌这种情况。</span></p></li>
                    <li><span style="color: rgb(144, 0, 0); font-weight: bold;">同时，请您充分评估数据安全需求，审慎决定是否使用本软件。感谢您的理解与支持！</span></p></li>
                </ul>
            </li>
            <li><b>软件功能：</b>
                <ul style='list-style-type: square;'>
                    <li><span style="color: rgb(144, 0, 0); font-weight: bold;">用户登录密码随机加密（仅为了防止他人进入系统误删数据），默认Admin账号密码为空。登录不同的账号，可绑定不同的诊金；</span></p></li>
                    <li>病历记录分针灸和中药两部分，其他疗法并入针灸文本框；</li>
                    <li>中药有单独的处方和中药配置系统；</li>
                    <li>支持图片嵌入（其中，患者对比页的图片支持批量上传）、自动计价、界面伸缩、板块拖拽隐藏；</li>
                    <li><span style="color: rgb(0, 128, 0); font-weight: bold;">继往病历高亮对比功能，包括病证图片，针灸疗法，用药和剂量差异等；</span></p></li>
                    <li>支持MariaDB和Mysql数据库，推荐使用MariaDB（10.3.39）搭配自带的HeidiSQL软件，或Navicat（Premium Lite 17.1.13）管理软件；</li>                    
                </ul>
            </li>

            <li><b>设计宗旨：</b><br>
                <span style="color: rgb(0, 128, 0); font-weight: bold;">清虚内守中医处方软件是专门为中医师设计的，并不涉及过多繁杂的功能，以便中医师不再为数据的保存分类以及查找对比而苦恼，可以不受干扰的潜心于中医广阔的天地中，以医入道。</span></p>
            </li>

            <li><b>开发背景：</b><br>
                本人在使用一款名为“中医处方系统”(广东惠州龙门沙迳人氏中医师陈焕林先生制作)的软件之时常报错，该软件在win7／win10 64位系统上无法正常运行，或因其设计于2011年之时是主要支持windows xp/win 7 32位系统，故特请X.L重新设计一款类似的软件。
                因开发该软件之时，本人也只是初学Python编程，软件的开发工作主要功能是由X.L耗费心力编写的，本人仅参与软件的界面设计和一小部分功能编写。
                后续将由本人继续开发和维护。本软件的开发过程中借助了DeepSeek的强大功能，在此对于DeepSeek表示深深的敬佩和赞叹；
            </li>

            <li><b>开发初衷：</b><br>
                陈先生在其免费软件界面状态栏中称其初衷是为中医学之发展尽一份心力，本人亦然。夕人曰：“寄蜉蝣于天地，渺浮海之一粟。哀吾生之须臾，羡长江之无穷。”
                大道无形，运行日月。大道无情，生育天地。人于天地之间，何其渺小，天行健，君子以自强不息，吾等学人自当遨游于广阔天地之中，无拘无束。
            </li>

            <li><b>软件界面设计说明：</b><br>
                对功能作了优化布局，以便让用户尽量在一个界面上看到大部分需要看到的内容，不必“多点一下”费时费力在软件中隐藏的菜单里找。
            </li>

            <li><b>结构框架：</b><br>
                参考广东惠州龙门沙迳人氏中医师陈先生的“中医处方系统”的优秀设计。同时，在此也感谢陈先生对于中医发展的贡献。
            </li>

            <li><b>数据库说明：</b><br>
                使用MariaDB或MySQL数据库。<span style="color: rgb(0, 128, 0); font-weight: bold;">关于sql格式数据库的导入/导出，使用MariaDB时，推荐使用其自带的HeidiSQL，兼容性好，使用Navicat可能出现只导入了部分表格的情况。如果使用Mysql数据库，搭配Navicat则比较好。</span></p>本软件的数据库zy.sql是个只有结构没有数据的空白数据库，以便用户导入自己的数据，通过HeidiSQL或navicat可以轻松导入csv格式的数据。医师陈先生的数据库是mdb格式，
                如果想从其“中医处方系统”将数据导入到MariaDB(win7推荐mariadb-10.3.39版)或Mysql（win7推荐5.7版）中，可另外下载chl.sql(以陈先生姓名拼音缩写为名，以示数据来源和赞叹)文件，这个文件已经将原mdb格式的文件数据导入到符合本软件使用的sql中了。其中的数据，仅作为演示之用。
                实际用时，医师应根据情况而定，并自行承担责任。
            </li>

        </ol>
            <h4>许可协议</h4>
            <table border="1">
                <tr><th>组件</th><th>许可证</th></tr>
                <tr><td>PySide6</td><td>LGPLv3</td></tr>
                <tr><td>pymysql</td><td>MIT</td></tr>
            </table>
            <p style='margin-top:12px;'>详细说明及最新版本请访问项目主页：
            <a href='https://github.com/franklenglw/zhongyi/' style='text-decoration: none; color: #2980b9;'>
            https://github.com/franklenglw/zhongyi/</a></p>
            """
