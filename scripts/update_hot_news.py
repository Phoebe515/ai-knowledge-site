#!/usr/bin/env python3
"""
AI 热点新闻爬取与摘要生成脚本
通过 RSS 获取 TechCrunch、InfoQ 的 AI 相关新闻，使用智谱 AI 生成摘要
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

def fetch_techcrunch_rss():
    """通过 RSS 获取 TechCrunch AI 新闻"""
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
            categories = [c.text for c in item.findall('category')]
            
            # 筛选 AI 分类的文章
            if title_elem is not None and link_elem is not None:
                if 'AI' in categories or 'artificial intelligence' in str(categories).lower():
                    title = title_elem.text
                    link = link_elem.text
                    news_list.append({
                        'title': title,
                        'url': link,
                        'source': 'TechCrunch'
                    })
                    
        # 限制数量
        news_list = news_list[:5]
        print(f"TechCrunch: 获取到 {len(news_list)} 条 AI 新闻")
    except Exception as e:
        print(f"TechCrunch RSS 获取失败: {e}")
    return news_list

def fetch_infoq_rss():
    """通过 RSS 获取 InfoQ 新闻"""
    news_list = []
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        response = requests.get('https://www.infoq.cn/feed', headers=headers, timeout=15)
        root = ET.fromstring(response.content)
        
        items = root.findall('.//item')[:8]
        for item in items:
            title_elem = item.find('title')
            link_elem = item.find('link')
            
            if title_elem is not None and link_elem is not None:
                title = title_elem.text
                link = link_elem.text
                # 清理链接中的追踪参数
                if '?' in link:
                    link = link.split('?')[0]
                news_list.append({
                    'title': title,
                    'url': link,
                    'source': 'InfoQ'
                })
                
        print(f"InfoQ: 获取到 {len(news_list)} 条新闻")
    except Exception as e:
        print(f"InfoQ RSS 获取失败: {e}")
    return news_list

def generate_summary_with_zhipu(news_items):
    """使用智谱 AI 生成热点摘要"""
    if not news_items:
        return "今日暂无热点新闻"
    
    # 构建提示词
    news_text = "\n".join([f"- [{item['source']}] {item['title']}" for item in news_items])
    
    prompt = f"""你是一个AI领域的专业编辑。请根据以下今日AI新闻标题，生成一份简洁的热点摘要。

今日新闻标题：
{news_text}

要求：
1. 用中文撰写，语言简洁专业
2. 提炼3-5个核心热点，每个热点用1-2句话概括
3. 按重要性排序
4. 格式如下：

## 今日AI热点摘要

1. **热点标题**
   简要描述...

2. **热点标题**
   简要描述...

---

请直接输出摘要内容，不要有其他开场白。"""

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
            'max_tokens': 1000
        }
        
        response = requests.post(ZHIPU_API_URL, headers=headers, json=data, timeout=30)
        result = response.json()
        
        if 'choices' in result and len(result['choices']) > 0:
            return result['choices'][0]['message']['content']
        else:
            print(f"智谱AI返回异常: {result}")
            return "摘要生成失败，请稍后重试"
    except Exception as e:
        print(f"智谱AI调用失败: {e}")
        return "摘要生成失败，请稍后重试"

def generate_markdown(news_items, summary):
    """生成 Markdown 格式的热点页面"""
    today = datetime.now().strftime('%Y年%m月%d日')
    
    # 按来源分组
    news_by_source = {}
    for item in news_items:
        source = item['source']
        if source not in news_by_source:
            news_by_source[source] = []
        news_by_source[source].append(item)
    
    markdown = f"""---
title: AI 热点
---

# 🔥 AI 热点

> 更新时间：{today} 07:00

{summary}

---

## 详细新闻列表

"""
    
    for source, items in news_by_source.items():
        markdown += f"### {source}\n\n"
        for item in items:
            markdown += f"- [{item['title']}]({item['url']})\n"
        markdown += "\n"
    
    markdown += """---

> 以上新闻来源于 TechCrunch、InfoQ，每日早 7:00 自动更新
"""
    
    return markdown

def main():
    print("开始获取新闻...")
    
    # 获取各来源新闻
    all_news = []
    all_news.extend(fetch_techcrunch_rss())
    all_news.extend(fetch_infoq_rss())
    
    print(f"共获取到 {len(all_news)} 条新闻")
    
    if not all_news:
        print("未获取到任何新闻，跳过更新")
        return
    
    # 生成摘要
    print("正在生成摘要...")
    summary = generate_summary_with_zhipu(all_news)
    
    # 生成 Markdown
    markdown = generate_markdown(all_news, summary)
    
    # 写入文件
    output_path = 'docs/hot/index.md'
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(markdown)
    
    print(f"热点页面已更新: {output_path}")

if __name__ == '__main__':
    main()
