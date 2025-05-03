# Wikipedia Math Crawler

一个用于抓取维基百科文章并将其转换为PDF的工具，特别支持数学公式的正确渲染。

## 功能特点

- 抓取任意维基百科页面内容
- 使用MathJax正确渲染LaTeX数学公式
- 生成高质量PDF文件
- 支持多语言维基百科（默认中文）
- 自动处理文件命名和存储

## 环境要求

- Python 3.6+
- Chrome浏览器
- ChromeDriver（与Chrome版本匹配）

## 必要依赖库

```
pip install wikipediaapi weasyprint selenium
```

## 安装指南

1. 克隆仓库到本地：
```bash
git clone https://github.com/RedefineLim/Wikipedia-crawler.git
cd Wikipedia-crawler
```

2. 安装所需依赖：
```bash
pip install -r requirements.txt
```

3. 确保已安装Chrome浏览器，并下载与Chrome版本匹配的ChromeDriver[1]

## 使用方法

### 基本用法

```python
from wiki_crawler import wiki_to_pdf_with_math

# 抓取单个页面并转换为PDF
wiki_to_pdf_with_math("人工智能")

# 指定不同语言（例如英文）
wiki_to_pdf_with_math("Artificial Intelligence", language="en")

# 自定义输出文件夹
wiki_to_pdf_with_math("相对论", output_folder="physics_papers")
```

### 批量处理

```python
# 批量处理多个页面
topics = ["机器学习", "深度学习", "神经网络", "自然语言处理"]
for topic in topics:
    wiki_to_pdf_with_math(topic, output_folder="AI_topics")
```

## 工作原理

1. 使用wikipediaapi获取指定维基百科页面的HTML内容[2]
2. 创建包含MathJax脚本的临时HTML文件
3. 使用Selenium和Chrome浏览器在无头模式下渲染页面内容，确保LaTeX公式正确显示
4. 等待MathJax完成渲染后，获取渲染后的HTML内容
5. 使用WeasyPrint将渲染后的HTML转换为PDF文件[2]
6. 自动清理临时文件，返回生成的PDF路径

## 常见问题

- **公式渲染失败**：请确保网络连接正常，MathJax CDN可以访问
- **ChromeDriver错误**：确保ChromeDriver版本与Chrome浏览器版本匹配
- **中文乱码**：检查编码设置，确保使用UTF-8编码处理所有文本

## 后续改进计划

- 添加多线程支持，提高批量处理效率
- 增加自定义样式选项
- 支持更多维基百科元素（如表格、图片等）的优化处理
- 实现命令行界面

## 许可证

MIT License

## 致谢

本项目基于[AndreiRegiani/wikipedia-crawler](https://github.com/AndreiRegiani/wikipedia-crawler)进行了修改和扩展，特别增加了对数学公式的支持[1]。

Citations:

[1] https://github.com/SJTUzhou/wiki_crawler/blob/main/README.md

[2] https://stackoverflow.com/questions/51445418/how-do-i-build-a-basic-web-crawler-for-wikipedia-pages-to-gather-links

[3] https://github.com/uhub/awesome-python/blob/master/README.md

[4] https://www.academia.edu/41461428/Ryan_Mitchell_Web_Scraping_with_Python_COLLECTING_MORE_DATA_FROM_THE_MODERN_WEB

[5] https://sciendo.com/2/v2/download/chapter/9781785881930/10.0000/9781785881930-001.pdf?
Token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VycyI6W3sic3ViIjoyNTY3ODUxNywicHVicmVmIjoiNzY0NDg4IiwibmFtZSI6Ikdvb2dsZSBHb29nbGVib3QgLSBXZWIgQ3Jhd2xlciBTRU8iLCJ0eXBlIjoiaW5zdGl0dXRpb24iLCJsb2dvdXRfbGluayI6Imh0dHBzOi8vY29ubmVjdC5saWJseW54LmNvbS9sb2dvdXQvNjdmY2RjYTA4MzhiNzEzZmU0YzgyMzFjMTEyYmE4NDUiLCJhdXRoX21ldGhvZCI6ImlwIiwiaXAiOiI2Ni4yNDkuNjYuNCJ9XSwiaWF0IjoxNzQ0NjI3NjQ1LCJleHAiOjE3NDU4MzcyNDV9.BUy78stAz47NotVr599g68Pm32XJ5OVodHUVFNiTZ60

[6] https://github.com/charlesl46/Wikipedia2LaTeX

[7] https://arxiv.org/html/2404.10690v1

[8] https://stackoverflow.com/questions/53804643/how-can-i-get-a-wikipedia-articles-text-using-python-3-with-beautiful-soup

[9] https://github.com/Kozea/WeasyPrint/issues/59

[10] https://docs.mathjax.org/_/downloads/en/stable/pdf/

[11] https://stackoverflow.com/questions/76139495/how-can-i-export-a-markdown-file-as-a-pdf-using-the-exact-same-style-as-github

[12] https://pandoc.org/MANUAL.html

[13] https://github.com/mkdocs/mkdocs/issues/253

[14] https://github.com/johnjosephhorton/texscrap

[15] https://news.ycombinator.com/item?id=38126623

[16] https://tex.stackexchange.com/questions/290617/markdown-mathjax-pdf

[17] https://learn.microsoft.com/en-us/azure/devops/project/wiki/markdown-guidance?view=azure-devops

[18] https://chromewebstore.google.com/detail/wikipedia-with-mathjax/fhomhkjcommffnlajeemenejemmegcmi

[19] https://www.reddit.com/r/Python/comments/h0if8o/convert_equations_in_pdf_to_equation_in_python/

[20] https://obsidian.md/plugins?id=
