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

def fetch_qbitai_rss():
    """通过 RSS 获取量子位新闻"""
    news_list = []
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        response = requests.get('https://www.qbitai.com/feed', headers=headers, timeout=15)
        root = ET.fromstring(response.content)
        
        items = root.findall('.//item')[:5]
        for item in items:
            title_elem = item.find('title')
            link_elem = item.find('link')
            
            if title_elem is not None and link_elem is not None:
                title = title_elem.text
                link = link_elem.text
                news_list.append({
                    'title': title,
                    'url': link,
                    'source': '量子位'
                })
                
        print(f"量子位: 获取到 {len(news_list)} 条新闻")
    except Exception as e:
        print(f"量子位 RSS 获取失败: {e}")
    return news_list

def fetch_leiphone_rss():
    """通过 RSS 获取AI科技评论（雷锋网）新闻"""
    news_list = []
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        response = requests.get('https://www.leiphone.com/feed', headers=headers, timeout=15)
        root = ET.fromstring(response.content)
        
        items = root.findall('.//item')
        for item in items:
            title_elem = item.find('title')
            link_elem = item.find('link')
            categories = [c.text for c in item.findall('category') if c.text]
            
            if title_elem is not None and link_elem is not None:
                title = title_elem.text
                link = link_elem.text
                # 筛选 AI 相关文章
                ai_keywords = ['AI', '人工智能', '大模型', 'GPT', 'LLM', 'Agent', '深度学习', '机器学习']
                if any(keyword in title for keyword in ai_keywords) or any(keyword in str(categories) for keyword in ai_keywords):
                    news_list.append({
                        'title': title,
                        'url': link,
                        'source': 'AI科技评论'
                    })
                    
        # 限制数量
        news_list = news_list[:5]
        print(f"AI科技评论: 获取到 {len(news_list)} 条 AI 新闻")
    except Exception as e:
        print(f"AI科技评论 RSS 获取失败: {e}")
    return news_list

def generate_news_detail_with_zhipu(title, source):
    """使用智谱 AI 生成单条新闻的详细内容"""
    prompt = f"""你是一个AI领域的专业编辑。请根据以下新闻标题，生成一段简短的新闻摘要（50-80字）。

新闻标题：{title}
来源：{source}

要求：
1. 用中文撰写，语言简洁专业
2. 50-80字
3. 直接输出摘要内容，不要有其他开场白"""

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

def generate_summary_with_zhipu(news_items):
    """使用智谱 AI 生成热点摘要"""
    if not news_items:
        return "今日暂无热点新闻"
    
    # 构建提示词
    news_text = "\n".join([f"- [{item['source']}] {item['title']}" for item in news_items[:8]])
    
    prompt = f"""你是一个AI领域的专业编辑。请根据以下今日AI新闻标题，生成一份简洁的热点摘要。

今日新闻标题：
{news_text}

要求：
1. 用中文撰写，语言简洁专业
2. 提炼3-5个核心热点，每个热点用1-2句话概括
3. 按重要性排序
4. 格式如下：

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
    """生成 Markdown 格式的热点页面（类似第一版排版）"""
    today = datetime.now().strftime('%Y年%m月%d日')
    today_short = datetime.now().strftime('%Y年%m月%d')
    
    markdown = f"""---
title: AI热点
description: 追踪AI领域最新动态，了解前沿技术与行业趋势
---

# 🔥 AI热点

追踪AI领域最新动态，了解前沿技术与行业趋势

<div style="margin: 20px 0; padding: 12px 16px; background: #fff3e0; border-radius: 8px; font-size: 13px; color: #f57c00; display: inline-flex; align-items: center; gap: 8px;">
  <span>⏰</span>
  <span>每日早7点自动更新 | 最近更新：{today} 07:00</span>
</div>

---

## {today_short}

"""
    
    # 为每条新闻生成卡片
    for i, item in enumerate(news_items[:8], 1):
        # 生成新闻摘要
        print(f"正在生成第 {i} 条新闻摘要...")
        desc = generate_news_detail_with_zhipu(item['title'], item['source'])
        
        # 生成新闻卡片
        markdown += f"""### {item['title']}

<span class="difficulty-beginner">热点</span> <span style="color: #999; font-size: 13px;">📖 {item['source']}</span>

{desc}

**来源：** [{item['source']}]({item['url']})

---

"""
    
    markdown += """::: tip 提示
热点内容每日早7点自动更新，确保信息的时效性和准确性。所有热点均标明来源，欢迎查阅原文。
:::
"""
    
    return markdown

def update_homepage(news_items):
    """更新首页热点模块"""
    # 读取首页文件
    with open('docs/index.md', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 生成首页热点数据
    today = datetime.now().strftime('%Y年%m月%d日')
    today_short = datetime.now().strftime('%Y-%m-%d')
    
    # 取前3条新闻作为首页展示
    top_news = news_items[:3]
    
    # 更新 updateTime 和 hotNews
    content = re.sub(
        r"const updateTime = ref\('.*?'\)",
        f"const updateTime = ref('{today} 07:00')",
        content
    )
    
    # 更新热点数据
    new_hot_news = f"""const hotNews = ref([
  {{ title: '{top_news[0]['title'][:25]}...', desc: '{top_news[0]['source']}', date: '{today_short}' }},
  {{ title: '{top_news[1]['title'][:25]}...', desc: '{top_news[1]['source']}', date: '{today_short}' }},
  {{ title: '{top_news[2]['title'][:25]}...', desc: '{top_news[2]['source']}', date: '{today_short}' }}
])"""
    
    content = re.sub(
        r"const hotNews = ref\(\[[\s\S]*?\]\)",
        new_hot_news,
        content
    )
    
    # 写回文件
    with open('docs/index.md', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("首页热点模块已更新")

def main():
    print("开始获取新闻...")
    
    # 获取各来源新闻
    all_news = []
    all_news.extend(fetch_techcrunch_rss())
    all_news.extend(fetch_infoq_rss())
    all_news.extend(fetch_qbitai_rss())
    all_news.extend(fetch_leiphone_rss())
    
    print(f"共获取到 {len(all_news)} 条新闻")
    
    if not all_news:
        print("未获取到任何新闻，跳过更新")
        return
    
    # 生成摘要
    print("正在生成摘要...")
    summary = generate_summary_with_zhipu(all_news)
    
    # 生成 Markdown
    print("正在生成热点页面...")
    markdown = generate_markdown(all_news, summary)
    
    # 写入热点页面
    output_path = 'docs/hot/index.md'
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(markdown)
    
    print(f"热点页面已更新: {output_path}")
    
    # 更新首页热点模块
    print("正在更新首页热点模块...")
    update_homepage(all_news)

if __name__ == '__main__':
    main()
