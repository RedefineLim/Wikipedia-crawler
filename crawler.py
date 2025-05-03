import wikipediaapi
from weasyprint import HTML
import os
import time

import wikipediaapi
from weasyprint import HTML
import os
import time
import re
import base64
import requests

import wikipediaapi
from weasyprint import HTML
import os
import time
import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def wiki_to_pdf_with_math(page_title, language='zh', output_folder='wiki_pdfs'):
    # 创建输出文件夹
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # 设置维基百科API
    wiki = wikipediaapi.Wikipedia(
        language=language,
        extract_format=wikipediaapi.ExtractFormat.HTML,
        user_agent='WikiPDFGenerator/1.0'
    )
    
    print(f"正在访问维基百科文章: {page_title}")
    page = wiki.page(page_title)
    
    if not page.exists():
        print(f"错误: 页面 '{page_title}' 不存在!")
        return None
    
    # 提取内容
    html_content = page.text
    
    # 创建包含MathJax的临时HTML
    temp_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <script type="text/javascript" async
            src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js?config=TeX-MML-AM_CHTML">
        </script>
        <script type="text/x-mathjax-config">
            MathJax.Hub.Config({{
                tex2jax: {{
                    inlineMath: [['$','$'], ['\\\\(','\\\\)']],
                    displayMath: [['$$','$$'], ['\\\\[','\\\\]'], ['<math>','</math>']]
                }}
            }});
        </script>
    </head>
    <body>
        <h1>{page.title}</h1>
        {html_content}
    </body>
    </html>
    """
    
    # 保存临时HTML文件
    temp_html_path = os.path.join(output_folder, "temp.html")
    with open(temp_html_path, "w", encoding="utf-8") as f:
        f.write(temp_html)
    
    # 使用Selenium渲染公式
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    
    driver = webdriver.Chrome(options=options)
    driver.get(f"file:///{os.path.abspath(temp_html_path)}")
    
    # 等待MathJax渲染完成
    try:
        WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.CLASS_NAME, "MathJax_CHTML"))
        )
        time.sleep(3)  # 额外等待以确保所有公式都渲染完成
    except:
        print("警告: 可能没有公式需要渲染或渲染超时")
    
    # 获取渲染后的页面内容
    rendered_html = driver.page_source
    driver.quit()
    
    # 移除临时文件
    os.remove(temp_html_path)
    
    # 创建安全的文件名
    safe_filename = "".join([c if c.isalnum() or c in (' ', '.', '_') else '_' for c in page.title])
    pdf_path = os.path.join(output_folder, f"{safe_filename}.pdf")
    
    print(f"正在生成PDF文件...")
    # 转换HTML为PDF
    HTML(string=rendered_html).write_pdf(pdf_path)
    
    print(f"PDF文件已保存至: {pdf_path}")
    return pdf_path



def batch_wiki_to_pdf(titles_list, language='zh', output_folder='wiki_pdfs'):
    """
    批量爬取多个Wikipedia页面并转换成PDF
    
    参数:
        titles_list (list): Wikipedia页面标题列表
        language (str): Wikipedia页面的语言代码
        output_folder (str): PDF文件保存的文件夹
    """
    successful = 0
    failed = 0
    
    for title in titles_list:
        print(f"\n处理: {title}")
        result = wiki_to_pdf_with_math(title, language, output_folder)
        
        if result:
            successful += 1
        else:
            failed += 1
    
    print(f"\n批量处理完成! 成功: {successful}, 失败: {failed}")

# 示例使用
if __name__ == "__main__":
    # 单个页面爬取示例
    wiki_to_pdf_with_math("卡尔曼滤波")
    
    # # 批量爬取示例
    # titles = ["Python", "机器学习", "深度学习", "自然语言处理"]
    # batch_wiki_to_pdf(titles)
