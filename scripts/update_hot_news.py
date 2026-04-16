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

def fetch_mit_tech_review_rss():
    """通过 RSS 获取 MIT Technology Review AI 新闻"""
    news_list = []
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        response = requests.get('https://www.technologyreview.com/topic/artificial-intelligence/feed/', headers=headers, timeout=15)
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
                    'source': 'MIT Tech Review'
                })
                
        print(f"MIT Tech Review: 获取到 {len(news_list)} 条新闻")
    except Exception as e:
        print(f"MIT Tech Review RSS 获取失败: {e}")
    return news_list

def fetch_theverge_ai():
    """爬取 The Verge AI 页面获取新闻"""
    news_list = []
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        response = requests.get('https://www.theverge.com/ai-artificial-intelligence', headers=headers, timeout=15)
        
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 查找文章链接
        seen_urls = set()
        all_links = soup.find_all('a', href=True)
        
        for link in all_links:
            href = link.get('href', '')
            text = link.get_text(strip=True)
            
            # 筛选 The Verge 自己的文章
            if href and text and len(text) > 15:
                # 匹配 /2026/ 格式的文章链接
                if '/2026/' in href and 'theverge.com' not in href and not href.startswith('http'):
                    full_url = 'https://www.theverge.com' + href
                    if full_url not in seen_urls:
                        seen_urls.add(full_url)
                        news_list.append({
                            'title': text,
                            'url': full_url,
                            'source': 'The Verge'
                        })
                elif 'theverge.com/2026/' in href and full_url not in seen_urls:
                    seen_urls.add(href)
                    news_list.append({
                        'title': text,
                        'url': href,
                        'source': 'The Verge'
                    })
        
        # 限制数量
        news_list = news_list[:5]
        print(f"The Verge: 获取到 {len(news_list)} 条新闻")
    except Exception as e:
        print(f"The Verge 爬取失败: {e}")
    return news_list

def fetch_hacker_news():
    """通过 Hacker News API 获取 AI 相关热门文章"""
    news_list = []
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        
        # AI 相关关键词
        ai_keywords = ['AI', 'artificial intelligence', 'machine learning', 'deep learning', 
                      'GPT', 'LLM', 'neural network', 'OpenAI', 'Anthropic', 'Claude',
                      'ChatGPT', 'transformer', 'AGI', 'agent', 'LLMs']
        
        # 获取 Top Stories
        response = requests.get('https://hacker-news.firebaseio.com/v0/topstories.json', 
                              headers=headers, timeout=15)
        story_ids = response.json()[:100]  # 检查前100个热门故事
        
        for story_id in story_ids:
            try:
                story_response = requests.get(
                    f'https://hacker-news.firebaseio.com/v0/item/{story_id}.json',
                    headers=headers, timeout=10
                )
                story = story_response.json()
                
                if story and 'title' in story and 'url' in story:
                    title = story['title']
                    # 检查标题是否包含 AI 关键词
                    title_lower = title.lower()
                    if any(keyword.lower() in title_lower for keyword in ai_keywords):
                        news_list.append({
                            'title': title,
                            'url': story['url'],
                            'source': 'Hacker News'
                        })
                        
                if len(news_list) >= 5:
                    break
                    
            except Exception:
                continue
                
        print(f"Hacker News: 获取到 {len(news_list)} 条 AI 新闻")
    except Exception as e:
        print(f"Hacker News API 获取失败: {e}")
    return news_list

def fetch_reddit():
    """通过 Reddit RSS 获取 AI 相关热门帖子"""
    news_list = []
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        
        # AI 相关子版块
        subreddits = ['MachineLearning', 'artificial', 'OpenAI', 'ChatGPT', 'LocalLLaMA']
        
        for subreddit in subreddits:
            try:
                response = requests.get(
                    f'https://www.reddit.com/r/{subreddit}/hot/.rss',
                    headers=headers, timeout=15
                )
                
                if response.status_code == 200:
                    root = ET.fromstring(response.content)
                    
                    # Reddit RSS 使用 Atom 格式
                    entries = root.findall('.//{http://www.w3.org/2005/Atom}entry')
                    if not entries:
                        entries = root.findall('.//item')
                    
                    for entry in entries[:3]:
                        # Atom 格式
                        title_elem = entry.find('{http://www.w3.org/2005/Atom}title')
                        link_elem = entry.find('{http://www.w3.org/2005/Atom}link')
                        
                        if title_elem is not None:
                            title = title_elem.text
                            # 获取链接
                            if link_elem is not None:
                                link = link_elem.get('href', '')
                            else:
                                link = f'https://www.reddit.com/r/{subreddit}/'
                            
                            if title and link:
                                news_list.append({
                                    'title': title,
                                    'url': link,
                                    'source': f'Reddit r/{subreddit}'
                                })
                                
            except Exception as e:
                print(f"Reddit r/{subreddit} 获取失败: {e}")
                continue
                
        # 限制总数
        news_list = news_list[:8]
        print(f"Reddit: 获取到 {len(news_list)} 条 AI 新闻")
    except Exception as e:
        print(f"Reddit RSS 获取失败: {e}")
    return news_list

def fetch_ai_valley():
    """爬取 AI Valley (theaivalley.com) 获取 AI 新闻"""
    news_list = []
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        response = requests.get('https://theaivalley.com', headers=headers, timeout=15)
        
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 查找文章链接
        seen_urls = set()
        for link in soup.find_all('a', href=True):
            href = link.get('href', '')
            text = link.get_text(strip=True)
            
            # 筛选文章链接
            if href and text and len(text) > 20 and '/p/' in href:
                if href not in seen_urls:
                    seen_urls.add(href)
                    news_list.append({
                        'title': text[:100],
                        'url': href,
                        'source': 'AI Valley'
                    })
                    
        # 限制数量
        news_list = news_list[:5]
        print(f"AI Valley: 获取到 {len(news_list)} 条新闻")
    except Exception as e:
        print(f"AI Valley 爬取失败: {e}")
    return news_list

def fetch_every():
    """爬取 Every (every.to) 获取 AI 相关内容"""
    news_list = []
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        response = requests.get('https://every.to', headers=headers, timeout=15)
        
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 查找文章链接
        seen_urls = set()
        for link in soup.find_all('a', href=True):
            href = link.get('href', '')
            text = link.get_text(strip=True)
            
            # 筛选文章链接
            if href and text and len(text) > 15:
                if href.startswith('/') and not href.startswith('//'):
                    full_url = 'https://every.to' + href
                elif href.startswith('https://every.to/'):
                    full_url = href
                else:
                    continue
                    
                if full_url not in seen_urls and '/p/' in full_url or '/source-code/' in full_url or '/vibe-check/' in full_url:
                    seen_urls.add(full_url)
                    news_list.append({
                        'title': text[:100],
                        'url': full_url,
                        'source': 'Every'
                    })
                    
        # 限制数量
        news_list = news_list[:5]
        print(f"Every: 获取到 {len(news_list)} 条新闻")
    except Exception as e:
        print(f"Every 爬取失败: {e}")
    return news_list

def fetch_google_blog():
    """获取 Google The Keyword 博客的 AI 相关内容"""
    news_list = []
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        # Google Blog 的 AI 分类页面
        response = requests.get('https://blog.google/technology/ai/', headers=headers, timeout=15)
        
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 查找文章链接
        seen_urls = set()
        for link in soup.find_all('a', href=True):
            href = link.get('href', '')
            text = link.get_text(strip=True)
            
            # 筛选文章链接
            if href and text and len(text) > 15:
                if href.startswith('/'):
                    full_url = 'https://blog.google' + href
                elif href.startswith('https://blog.google/'):
                    full_url = href
                else:
                    continue
                    
                if full_url not in seen_urls and '/products/' not in full_url and '/technology/ai/' not in full_url.rstrip('/'):
                    seen_urls.add(full_url)
                    news_list.append({
                        'title': text[:100],
                        'url': full_url,
                        'source': 'Google Blog'
                    })
                    
        # 限制数量
        news_list = news_list[:5]
        print(f"Google Blog: 获取到 {len(news_list)} 条新闻")
    except Exception as e:
        print(f"Google Blog 爬取失败: {e}")
    return news_list

def fetch_smol_ai_news():
    """获取 AI News (news.smol.ai) 的内容"""
    news_list = []
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        response = requests.get('https://news.smol.ai/', headers=headers, timeout=15)
        
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 查找文章链接
        seen_urls = set()
        for link in soup.find_all('a', href=True):
            href = link.get('href', '')
            text = link.get_text(strip=True)
            
            # 筛选文章链接
            if href and text and len(text) > 20:
                if href.startswith('/'):
                    full_url = 'https://news.smol.ai' + href
                elif href.startswith('https://'):
                    full_url = href
                else:
                    continue
                    
                if full_url not in seen_urls and 'issues' in full_url:
                    seen_urls.add(full_url)
                    news_list.append({
                        'title': text[:100],
                        'url': full_url,
                        'source': 'AI News'
                    })
                    
        # 限制数量
        news_list = news_list[:5]
        print(f"AI News: 获取到 {len(news_list)} 条新闻")
    except Exception as e:
        print(f"AI News 爬取失败: {e}")
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

def translate_title_to_chinese(title, source):
    """将英文标题翻译成中文（用于首页展示），失败返回 None"""
    # 如果已经是中文，直接返回
    if any('\u4e00' <= char <= '\u9fff' for char in title):
        return title[:30]
    
    # 英文标题需要翻译
    prompt = f"""请将以下AI新闻标题翻译成简洁的中文（不超过25个字）：

原标题：{title}

要求：
1. 简洁准确，突出重点
2. 不超过25个中文字
3. 直接输出翻译结果，不要有其他内容"""

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
            'temperature': 0.3,
            'max_tokens': 100
        }
        
        response = requests.post(ZHIPU_API_URL, headers=headers, json=data, timeout=30)
        result = response.json()
        
        if 'choices' in result and len(result['choices']) > 0:
            translated = result['choices'][0]['message']['content'].strip()
            # 检查翻译结果是否包含中文
            if any('\u4e00' <= char <= '\u9fff' for char in translated):
                return translated[:30] if len(translated) > 30 else translated
            else:
                print(f"翻译结果不含中文: {translated}")
                return None
        else:
            print(f"翻译API返回异常: {result}")
            return None
    except Exception as e:
        print(f"翻译失败: {e}")
        return None

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

::: warning 访问说明
- **国内可访问**：InfoQ、量子位、AI科技评论
- **需科学上网**：TechCrunch、MIT Tech Review
- 建议优先阅读国内来源的热点内容
:::

---

## 📚 历史热点

想查看更多历史热点新闻？点击下方链接浏览：

| 时间范围 | 说明 | 链接 |
|---------|------|------|
| 📅 最近七天 | 按日期详细展示 | [查看详情](/hot/history-demo.html#📅-最近七天) |
| 📆 最近一个月 | 按周分组展示 | [查看详情](/hot/history-demo.html#📆-最近一个月) |
| 📊 最近三个月 | 按月展示重大事件 | [查看详情](/hot/history-demo.html#📊-最近三个月) |
| 🗓️ 三个月以上 | 按季度展示行业回顾 | [查看详情](/hot/history-demo.html#🗓️-三个月以上) |

---

## 🔗 更多AI媒体

以下是我们未收录但值得关注的主流AI媒体，欢迎访问：

| 媒体名称 | 简介 | 链接 |
|---------|------|------|
| 36氪 | 国内领先的科技商业媒体，覆盖AI创业、融资动态 | [访问官网](https://36kr.com) |
| 机器之心 | 专业AI垂直媒体，深度技术解读 | [访问官网](https://www.jiqizhixin.com) |
| 新智元 | AI领域头部社区，热点响应快 | [访问官网](https://www.jiqizhixin.com) |
| The Verge | 国际顶级科技媒体，AI新闻覆盖广 | [访问官网](https://www.theverge.com/ai-artificial-intelligence) ⚠️ |
| VentureBeat AI | 商业科技媒体，融资产品消息快 | [访问官网](https://venturebeat.com/category/ai/) ⚠️ |
| Wired AI | 科技文化媒体，深度分析文章 | [访问官网](https://www.wired.com/tag/artificial-intelligence/) ⚠️ |

> ⚠️ 标记的网站需要科学上网才能访问
"""
    
    return markdown

def update_homepage(news_items):
    """更新首页热点模块，翻译失败则跳过更新"""
    # 读取首页文件
    with open('docs/index.md', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 生成首页热点数据
    today = datetime.now().strftime('%Y年%m月%d日')
    today_short = datetime.now().strftime('%Y-%m-%d')
    
    # 取前3条新闻作为首页展示，并翻译标题
    top_news = news_items[:3]
    
    print("正在翻译首页热点标题...")
    translated_titles = []
    translation_failed = False
    
    for item in top_news:
        translated = translate_title_to_chinese(item['title'], item['source'])
        if translated is None:
            print(f"  ❌ 翻译失败: {item['source']}: {item['title'][:30]}")
            translation_failed = True
        else:
            print(f"  ✅ {item['source']}: {item['title'][:30]} -> {translated}")
            translated_titles.append(translated)
    
    # 如果翻译失败，跳过首页更新
    if translation_failed or len(translated_titles) < 3:
        print("⚠️ 翻译未完全成功，跳过首页更新，保留上次内容")
        return False
    
    # 更新 updateTime 和 hotNews
    content = re.sub(
        r"const updateTime = ref\('.*?'\)",
        f"const updateTime = ref('{today} 07:00')",
        content
    )
    
    # 更新热点数据（使用翻译后的中文标题）
    new_hot_news = f"""const hotNews = ref([
  {{ title: '{translated_titles[0]}', desc: '{top_news[0]['source']}', date: '{today_short}' }},
  {{ title: '{translated_titles[1]}', desc: '{top_news[1]['source']}', date: '{today_short}' }},
  {{ title: '{translated_titles[2]}', desc: '{top_news[2]['source']}', date: '{today_short}' }}
])"""
    
    content = re.sub(
        r"const hotNews = ref\(\[[\s\S]*?\]\)",
        new_hot_news,
        content
    )
    
    # 写回文件
    with open('docs/index.md', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("✅ 首页热点模块已更新")
    return True



def main():
    print("开始获取新闻...")
    
    # 获取各来源新闻
    all_news = []
    all_news.extend(fetch_techcrunch_rss())
    all_news.extend(fetch_infoq_rss())
    all_news.extend(fetch_qbitai_rss())
    all_news.extend(fetch_leiphone_rss())
    all_news.extend(fetch_mit_tech_review_rss())
    all_news.extend(fetch_theverge_ai())
    all_news.extend(fetch_hacker_news())
    all_news.extend(fetch_reddit())
    all_news.extend(fetch_ai_valley())
    all_news.extend(fetch_every())
    all_news.extend(fetch_google_blog())
    all_news.extend(fetch_smol_ai_news())
    
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
