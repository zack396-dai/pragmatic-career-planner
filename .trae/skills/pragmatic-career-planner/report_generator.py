# -*- coding: utf-8 -*-
"""
升学规划报告生成器
配合pragmatic-career-planner技能使用，生成带时间戳的MD和HTML报告
"""

import os
import re
from datetime import datetime
import markdown2


class CareerReportGenerator:
    """升学规划报告生成器"""

    def __init__(self, base_dir=None):
        """
        初始化报告生成器

        Args:
            base_dir: 报告输出目录，默认为项目根目录下的reports文件夹
        """
        if base_dir is None:
            # 获取项目根目录（技能文件夹的上级目录）
            skill_dir = os.path.dirname(os.path.abspath(__file__))
            project_root = os.path.dirname(os.path.dirname(skill_dir))
            base_dir = os.path.join(project_root, 'reports')

        self.base_dir = base_dir
        self.ensure_output_dir()

    def ensure_output_dir(self):
        """确保输出目录存在"""
        if not os.path.exists(self.base_dir):
            os.makedirs(self.base_dir)

    def generate_timestamp(self):
        """
        生成时间戳

        Returns:
            str: 格式为YYYYMMDD_HHMMSS的时间戳
        """
        return datetime.now().strftime('%Y%m%d_%H%M%S')

    def generate_filename(self, report_type='升学规划报告'):
        """
        生成带时间戳的文件名

        Args:
            report_type: 报告类型

        Returns:
            tuple: (md文件名, html文件名)
        """
        timestamp = self.generate_timestamp()
        md_filename = f"{report_type}_{timestamp}.md"
        html_filename = f"{report_type}_{timestamp}.html"
        return md_filename, html_filename

    def create_markdown_report(self, content, report_type='升学规划报告'):
        """
        创建Markdown格式的报告

        Args:
            content: 报告内容（Markdown格式）
            report_type: 报告类型

        Returns:
            str: 生成的MD文件路径
        """
        md_filename, _ = self.generate_filename(report_type)
        md_filepath = os.path.join(self.base_dir, md_filename)

        # 添加报告头部信息
        header = f"""# {report_type}

**生成时间**: {datetime.now().strftime('%Y年%m月%d日 %H:%M:%S')}

---

"""

        # 写入文件
        with open(md_filepath, 'w', encoding='utf-8') as f:
            f.write(header + content)

        return md_filepath

    def create_html_report(self, content, report_type='升学规划报告'):
        """
        创建HTML格式的报告

        Args:
            content: 报告内容（Markdown格式）
            report_type: 报告类型

        Returns:
            str: 生成的HTML文件路径
        """
        _, html_filename = self.generate_filename(report_type)
        html_filepath = os.path.join(self.base_dir, html_filename)

        # 转换Markdown为HTML
        html_content = markdown2.markdown(content, extras=['tables', 'fenced-code-blocks', 'footnotes'])

        # 生成完整的HTML页面
        full_html = f"""
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{report_type}</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{ font-family: '微软雅黑', Arial, sans-serif; line-height: 1.6; color: #333; }}
        .container {{ max-width: 800px; margin: 0 auto; padding: 40px 20px; }}
        h1, h2, h3, h4, h5, h6 {{ color: #0066cc; margin-top: 1.5em; margin-bottom: 0.5em; }}
        h1 {{ font-size: 24px; border-bottom: 2px solid #0066cc; padding-bottom: 10px; }}
        h2 {{ font-size: 20px; border-bottom: 1px solid #e0e0e0; padding-bottom: 8px; }}
        h3 {{ font-size: 16px; }}
        p {{ margin-bottom: 1em; }}
        ul, ol {{ margin-left: 2em; margin-bottom: 1em; }}
        li {{ margin-bottom: 0.5em; }}
        table {{ border-collapse: collapse; width: 100%; margin: 1em 0; }}
        th, td {{ border: 1px solid #ddd; padding: 8px; text-align: left; }}
        th {{ background-color: #0066cc; color: white; font-weight: bold; }}
        tr:nth-child(even) {{ background-color: #f2f2f2; }}
        blockquote {{ border-left: 4px solid #0066cc; background-color: #f5f5f5; padding: 10px 15px; margin: 1em 0; }}
        pre {{ background-color: #f5f5f5; padding: 15px; border-radius: 4px; overflow-x: auto; font-family: Consolas, Monaco, monospace; font-size: 14px; margin: 1em 0; }}
        code {{ background-color: #f0f0f0; padding: 2px 4px; border-radius: 3px; font-family: Consolas, Monaco, monospace; font-size: 14px; }}
        .header {{ text-align: center; margin-bottom: 40px; padding-bottom: 20px; border-bottom: 2px solid #0066cc; }}
        .header h1 {{ margin-top: 0; border-bottom: none; }}
        .header .subtitle {{ font-size: 16px; color: #666; margin-top: 10px; }}
        .header .timestamp {{ font-size: 14px; color: #999; margin-top: 10px; }}
        .footer {{ margin-top: 40px; padding-top: 20px; border-top: 1px solid #e0e0e0; text-align: center; color: #999; font-size: 14px; }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>{report_type}</h1>
            <div class="subtitle">务实派升学规划报告</div>
            <div class="timestamp">生成时间：{datetime.now().strftime('%Y年%m月%d日 %H:%M:%S')}</div>
        </div>
        
        <div class="content">
            {html_content}
        </div>
        
        <div class="footer">
            <p>本报告由务实派升学规划技能生成</p>
        </div>
    </div>
</body>
</html>
        """

        # 写入文件
        with open(html_filepath, 'w', encoding='utf-8') as f:
            f.write(full_html)

        return html_filepath

    def generate_reports(self, content, report_type='升学规划报告'):
        """
        生成Markdown和HTML格式的报告

        Args:
            content: 报告内容（Markdown格式）
            report_type: 报告类型

        Returns:
            dict: 包含md和html文件路径的字典
        """
        md_path = self.create_markdown_report(content, report_type)
        html_path = self.create_html_report(content, report_type)

        return {
            'md': md_path,
            'html': html_path,
            'report_type': report_type,
            'timestamp': self.generate_timestamp()
        }


def generate_report_from_content(content, report_type='升学规划报告'):
    """
    从内容生成报告的便捷函数

    Args:
        content: 报告内容（Markdown格式）
        report_type: 报告类型

    Returns:
        dict: 包含md和html文件路径的字典
    """
    generator = CareerReportGenerator()
    return generator.generate_reports(content, report_type)


# 使用示例
if __name__ == '__main__':
    # 示例内容
    sample_content = """## 一、用户基本信息

| 项目 | 内容 |
|------|------|
| 分数 | 580分 |
| 位次 | 省排名15000 |
| 家庭情况 | 普通工薪家庭 |
| 性格特点 | 内向、踏实 |

## 二、专业推荐

### 推荐专业：电气工程及其自动化

**为什么推荐？**

- 国家在推，政策支持力度大
- 缺人，每年缺口约20万
- 钱还行，起薪8000，干5年平均能到15000
- AI暂时替代不了，饭碗相对稳

**但有几个坑你得知道：**

- 第一，学习难度大，数学物理要好
- 第二，工作环境可能需要下现场
- 第三，需要考证（注册电气工程师）

**什么人适合报？**

- 家里条件一般的，想靠技术吃饭的
- 数学好、能吃苦、能接受倒班的

**什么人别报？**

- 想坐办公室吹空调的
- 数学物理差的
- 家里能托底想轻松的

## 三、备选方案

如果分数不够，可以考虑：

1. 软件工程
2. 信息安全
3. 集成电路

---

> 记住一句话：今天的热门可能是明天的冷门，选专业要看十年后，不是看今天。
"""

    # 生成报告
    result = generate_report_from_content(sample_content, '升学规划报告')

    print(f"报告生成成功！")
    print(f"MD文件路径: {result['md']}")
    print(f"HTML文件路径: {result['html']}")
    print(f"时间戳: {result['timestamp']}")
