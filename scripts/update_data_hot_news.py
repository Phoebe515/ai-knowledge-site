#!/usr/bin/env python3
"""
数据AI热点新闻爬取与摘要生成脚本
专注于数据方向的AI应用热点：数据分析、数据可视化、数据治理、BI智能化等
"""

import os
import re
import json
import requests
import xml.etree.ElementTree as ET
from datetime import datetime

# 智谱 AI API 配置
ZHIPU_API_KEY = os.environ.get('ZHIPU_API_KEY')
ZHIPU_API_URL = 'https://open.bigmodel.cn/api/paas/v4/chat/completions'

# 数据AI相关关键词
DATA_AI_KEYWORDS = [
    '数据分析', '数据可视化', '数据治理', 'BI', '商业智能', 
    '数据科学', 'AutoML', '数据库', '数据仓库', '数据湖',
    'ETL', '特征工程', '数据质量', '元数据', '数据管理',
    'data analysis', 'data visualization', 'data governance',
    'business intelligence', 'data science', 'machine learning',
    'deep learning', 'neural network', 'data pipeline',
    'feature engineering', 'data quality', 'metadata'
]

def is_data_ai_related(title, categories=None):
    """判断新闻是否与数据AI相关"""
    title_lower = title.lower()
    for keyword in DATA_AI_KEYWORDS:
        if keyword.lower() in title_lower:
            return True
    if categories:
        for cat in categories:
            cat_lower = cat.lower()
            for keyword in DATA_AI_KEYWORDS:
                if keyword.lower() in cat_lower:
                    return True
    return False

def fetch_techcrunch_data_ai():
    """获取 TechCrunch 数据AI相关新闻"""
    news_list = []
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        response = requests.get('https://techcrunch.com/feed/', headers=headers, timeout=15)
        root = ET.fromstring(response.content)
        
        items = root.findall('.//item')
        for item in items:
            title_elem = item.find('title')
            link_elem = item.find('link')
            categories = [c.text for c in item.findall('category') if c.text]
            
            if title_elem is not None and link_elem is not None:
                title = title_elem.text
                if is_data_ai_related(title, categories):
                    link = link_elem.text
                    news_list.append({
                        'title': title,
                        'url': link,
                        'source': 'TechCrunch'
                    })
                    
        news_list = news_list[:5]
        print(f"TechCrunch 数据AI: 获取到 {len(news_list)} 条新闻")
    except Exception as e:
        print(f"TechCrunch RSS 获取失败: {e}")
    return news_list

def fetch_infoq_data_ai():
    """获取 InfoQ 数据AI相关新闻"""
    news_list = []
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        response = requests.get('https://www.infoq.cn/feed', headers=headers, timeout=15)
        root = ET.fromstring(response.content)
        
        items = root.findall('.//item')
        for item in items:
            title_elem = item.find('title')
            link_elem = item.find('link')
            
            if title_elem is not None and link_elem is not None:
                title = title_elem.text
                if is_data_ai_related(title):
                    link = link_elem.text
                    if '?' in link:
                        link = link.split('?')[0]
                    news_list.append({
                        'title': title,
                        'url': link,
                        'source': 'InfoQ'
                    })
                    
        news_list = news_list[:8]
        print(f"InfoQ 数据AI: 获取到 {len(news_list)} 条新闻")
    except Exception as e:
        print(f"InfoQ RSS 获取失败: {e}")
    return news_list

def fetch_qbitai_data_ai():
    """获取量子位数据AI相关新闻"""
    news_list = []
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        response = requests.get('https://www.qbitai.com/feed', headers=headers, timeout=15)
        root = ET.fromstring(response.content)
        
        items = root.findall('.//item')
        for item in items:
            title_elem = item.find('title')
            link_elem = item.find('link')
            
            if title_elem is not None and link_elem is not None:
                title = title_elem.text
                if is_data_ai_related(title):
                    link = link_elem.text
                    news_list.append({
                        'title': title,
                        'url': link,
                        'source': '量子位'
                    })
                    
        news_list = news_list[:5]
        print(f"量子位 数据AI: 获取到 {len(news_list)} 条新闻")
    except Exception as e:
        print(f"量子位 RSS 获取失败: {e}")
    return news_list

def fetch_mit_tech_review_data_ai():
    """获取 MIT Tech Review 数据AI相关新闻"""
    news_list = []
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        response = requests.get('https://www.technologyreview.com/feed/', headers=headers, timeout=15)
        root = ET.fromstring(response.content)
        
        items = root.findall('.//item')
        for item in items:
            title_elem = item.find('title')
            link_elem = item.find('link')
            categories = [c.text for c in item.findall('category') if c.text]
            
            if title_elem is not None and link_elem is not None:
                title = title_elem.text
                if is_data_ai_related(title, categories):
                    link = link_elem.text
                    news_list.append({
                        'title': title,
                        'url': link,
                        'source': 'MIT Tech Review'
                    })
                    
        news_list = news_list[:5]
        print(f"MIT Tech Review 数据AI: 获取到 {len(news_list)} 条新闻")
    except Exception as e:
        print(f"MIT Tech Review RSS 获取失败: {e}")
    return news_list

def generate_news_detail_with_zhipu(title, source):
    """使用智谱 AI 生成单条新闻的详细内容"""
    prompt = f"""你是一个数据AI领域的专业编辑。请根据以下新闻标题，生成一段简短的新闻摘要（50-80字）。

新闻标题：{title}
来源：{source}

要求：
1. 用中文撰写，语言简洁专业
2. 50-80字
3. 突出数据AI相关内容
4. 直接输出摘要内容，不要有其他开场白"""

    try:
        headers = {
            'Authorization': f'Bearer {ZHIPU_API_KEY}',
            'Content-Type': 'application/json'
        }
        data = {
            'model': 'glm-4-flash',
            'messages': [
                {'role': 'user', 'content': prompt}
            ],
            'temperature': 0.7,
            'max_tokens': 200
        }
        
        response = requests.post(ZHIPU_API_URL, headers=headers, json=data, timeout=30)
        result = response.json()
        
        if 'choices' in result and len(result['choices']) > 0:
            return result['choices'][0]['message']['content']
        else:
            return "详情请查看原文链接"
    except Exception as e:
        print(f"智谱AI调用失败: {e}")
        return "详情请查看原文链接"

def generate_markdown(news_items):
    """生成 Markdown 格式的数据AI热点页面"""
    now = datetime.now()
    today = now.strftime('%Y年%m月%d日')
    today_short = now.strftime('%Y年%m月%d')
    hour = now.hour
    
    # 判断是上午还是下午更新
    update_time = f"{today} 09:00" if hour < 12 else f"{today} 14:00"
    
    markdown = f"""---
title: 数据AI热点
description: 盘点全网最新数据方向AI应用热点，涵盖数据分析、数据可视化、数据治理、BI智能化等领域
---

# 📊 数据AI热点

盘点全网最新数据方向AI应用热点，涵盖数据分析、数据可视化、数据治理、BI智能化等领域

<div style="margin: 20px 0; padding: 12px 16px; background: #e3f2fd; border-radius: 8px; font-size: 13px; color: #1976d2; display: inline-flex; align-items: center; gap: 8px;">
  <span>⏰</span>
  <span>每日更新两次（早9点、下午14点）| 最近更新：{update_time}</span>
</div>

---

## {today_short}

"""
    
    if not news_items:
        markdown += """### 暂无数据AI相关热点

今日暂未获取到数据AI相关热点新闻，请稍后再查看。

---

"""
    else:
        # 为每条新闻生成卡片
        for i, item in enumerate(news_items[:10], 1):
            print(f"正在生成第 {i} 条新闻摘要...")
            desc = generate_news_detail_with_zhipu(item['title'], item['source'])
            
            markdown += f"""### {item['title']}

<span class="difficulty-beginner">数据AI热点</span> <span style="color: #999; font-size: 13px;">📖 {item['source']}</span>

{desc}

**来源：** [{item['source']}]({item['url']})

---

"""
    
    markdown += """::: tip 关于数据AI热点
本页面专注于数据方向的AI应用热点，包括：
- **数据分析**：AI驱动的数据分析工具与方法
- **数据可视化**：智能图表生成、自动报告
- **数据治理**：AI辅助数据质量管理、元数据管理
- **BI智能化**：智能BI、自然语言查询
- **数据科学**：AutoML、特征工程自动化
:::

---

## 🔗 更多数据AI资源

| 资源名称 | 简介 | 链接 |
|---------|------|------|
| DBBerg | 数据技术博客 | [访问官网](https://dbberg.com) |
| DataCamp | 数据科学学习平台 | [访问官网](https://www.datacamp.com) |
| Kaggle | 数据科学竞赛平台 | [访问官网](https://www.kaggle.com) |
| Towards Data Science | 数据科学 Medium 博客 | [访问官网](https://towardsdatascience.com) |

---

> 数据AI热点每日更新两次，确保信息的时效性和准确性
"""
    
    return markdown

def main():
    print("开始获取数据AI热点新闻...")
    
    # 获取各来源新闻
    all_news = []
    all_news.extend(fetch_techcrunch_data_ai())
    all_news.extend(fetch_infoq_data_ai())
    all_news.extend(fetch_qbitai_data_ai())
    all_news.extend(fetch_mit_tech_review_data_ai())
    
    print(f"共获取到 {len(all_news)} 条数据AI相关新闻")
    
    # 生成 Markdown
    print("正在生成数据AI热点页面...")
    markdown = generate_markdown(all_news)
    
    # 写入文件
    output_path = 'docs/data-hot/index.md'
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(markdown)
    
    print(f"数据AI热点页面已更新: {output_path}")

if __name__ == '__main__':
    main()
