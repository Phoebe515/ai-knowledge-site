---
layout: home

hero:
  name: "AI知识库"
  text: "聚焦AI核心知识"
  tagline: 从入门到进阶，系统学习大语言模型、Agent、Skill与AI热点
  actions:
    - theme: brand
      text: 查看热点
      link: /hot/
    - theme: alt
      text: 入门科普
      link: /beginner/llm/
    - theme: alt
      text: 进阶科普
      link: /advanced/llm/
---

<script setup>
import { ref, onMounted } from 'vue'

const updateTime = ref('2026年04月20日 07:00')
const hotNews = ref([
  { title: 'OpenAI的存亡之问', desc: 'TechCrunch', date: '2026-04-20' },
  { title: '12个月窗口期', desc: 'TechCrunch', date: '2026-04-20' },
  { title: 'Palantir发布反包容性声明', desc: 'TechCrunch', date: '2026-04-20' }
])
</script>

<div class="hot-banner">
  <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px;">
    <div style="display: flex; align-items: center; gap: 12px;">
      <span style="font-size: 32px;">🔥</span>
      <h2 style="font-size: 24px; font-weight: 700; margin: 0;">AI热点</h2>
    </div>
    <div class="hot-badge">
      <span>⏰</span>
      <span>每日早7点更新</span>
    </div>
  </div>
  <div class="update-time" style="color: rgba(255,255,255,0.9); margin-bottom: 12px;">
    <span>📅</span>
    <span>最近更新：{{ updateTime }}</span>
  </div>
  <p style="color: rgba(255,255,255,0.95); font-size: 14px; margin-bottom: 16px;">
    追踪AI领域最新动态，了解前沿技术与行业趋势
  </p>
  <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 12px;">
    <div v-for="news in hotNews" :key="news.title" 
         style="background: rgba(255,255,255,0.2); backdrop-filter: blur(10px); border-radius: 8px; padding: 12px;">
      <div style="font-weight: 600; margin-bottom: 4px;">{{ news.title }}</div>
      <div style="font-size: 12px; opacity: 0.9;">{{ news.desc }}</div>
    </div>
  </div>
  <a href="/hot/" style="display: inline-block; margin-top: 16px; color: white; text-decoration: underline;">
    查看全部热点 →
  </a>
</div>

<style>
.hot-banner {
  background: linear-gradient(135deg, #ff6b6b 0%, #ff8e53 100%);
  border-radius: 16px;
  padding: 28px;
  margin-bottom: 36px;
  color: white;
  box-shadow: 0 8px 24px rgba(255, 107, 107, 0.3);
  transition: all 0.3s ease;
}

.hot-banner:hover {
  box-shadow: 0 12px 32px rgba(255, 107, 107, 0.4);
  transform: translateY(-2px);
}

@media (max-width: 768px) {
  .hot-banner > div:nth-child(4) {
    grid-template-columns: 1fr !important;
  }
}
</style>

## 📚 入门科普

适合零基础学习者，建立AI知识体系

<div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 16px; margin: 24px 0;">

<div style="background: white; border-radius: 12px; padding: 24px; border: 2px solid transparent; transition: all 0.3s;">
  <div style="font-size: 36px; margin-bottom: 10px;">🤖</div>
  <h3 style="font-size: 20px; margin-bottom: 6px;">大语言模型</h3>
  <p style="color: #666; font-size: 13px; margin-bottom: 10px;">什么是LLM、如何使用ChatGPT、提示工程基础</p>
  <div style="font-size: 12px; color: #999;">4 个知识点</div>
  <a href="/beginner/llm/" style="display: inline-block; margin-top: 12px; color: #4caf50; text-decoration: none; font-weight: 500;">开始学习 →</a>
</div>

<div style="background: white; border-radius: 12px; padding: 24px; border: 2px solid transparent; transition: all 0.3s;">
  <div style="font-size: 36px; margin-bottom: 10px;">🎯</div>
  <h3 style="font-size: 20px; margin-bottom: 6px;">Agent</h3>
  <p style="color: #666; font-size: 13px; margin-bottom: 10px;">什么是AI Agent、Agent能做什么、典型应用</p>
  <div style="font-size: 12px; color: #999;">3 个知识点</div>
  <a href="/beginner/agent/" style="display: inline-block; margin-top: 12px; color: #4caf50; text-decoration: none; font-weight: 500;">开始学习 →</a>
</div>

<div style="background: white; border-radius: 12px; padding: 24px; border: 2px solid transparent; transition: all 0.3s;">
  <div style="font-size: 36px; margin-bottom: 10px;">⚡</div>
  <h3 style="font-size: 20px; margin-bottom: 6px;">Skill</h3>
  <p style="color: #666; font-size: 13px; margin-bottom: 10px;">什么是AI Skill、常用工具介绍、快速上手</p>
  <div style="font-size: 12px; color: #999;">3 个知识点</div>
  <a href="/beginner/skill/" style="display: inline-block; margin-top: 12px; color: #4caf50; text-decoration: none; font-weight: 500;">开始学习 →</a>
</div>

</div>

## 🚀 进阶科普

适合有基础的学习者，深入技术原理

<div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 16px; margin: 24px 0;">

<div style="background: white; border-radius: 12px; padding: 24px; border: 2px solid transparent; transition: all 0.3s;">
  <div style="font-size: 36px; margin-bottom: 10px;">🤖</div>
  <h3 style="font-size: 20px; margin-bottom: 6px;">大语言模型</h3>
  <p style="color: #666; font-size: 13px; margin-bottom: 10px;">Transformer架构、模型训练、RAG技术、模型微调</p>
  <div style="font-size: 12px; color: #999;">5 个知识点</div>
  <a href="/advanced/llm/" style="display: inline-block; margin-top: 12px; color: #ff9800; text-decoration: none; font-weight: 500;">深入学习 →</a>
</div>

<div style="background: white; border-radius: 12px; padding: 24px; border: 2px solid transparent; transition: all 0.3s;">
  <div style="font-size: 36px; margin-bottom: 10px;">🎯</div>
  <h3 style="font-size: 20px; margin-bottom: 6px;">Agent</h3>
  <p style="color: #666; font-size: 13px; margin-bottom: 10px;">Agent架构设计、工具调用、多Agent协作、开发实战</p>
  <div style="font-size: 12px; color: #999;">4 个知识点</div>
  <a href="/advanced/agent/" style="display: inline-block; margin-top: 12px; color: #ff9800; text-decoration: none; font-weight: 500;">深入学习 →</a>
</div>

<div style="background: white; border-radius: 12px; padding: 24px; border: 2px solid transparent; transition: all 0.3s;">
  <div style="font-size: 36px; margin-bottom: 10px;">⚡</div>
  <h3 style="font-size: 20px; margin-bottom: 6px;">Skill</h3>
  <p style="color: #666; font-size: 13px; margin-bottom: 10px;">Skill开发、平台对比、最佳实践、性能优化</p>
  <div style="font-size: 12px; color: #999;">4 个知识点</div>
  <a href="/advanced/skill/" style="display: inline-block; margin-top: 12px; color: #ff9800; text-decoration: none; font-weight: 500;">深入学习 →</a>
</div>

</div>

<style>
@media (max-width: 768px) {
  .VPContent > div > div {
    grid-template-columns: 1fr !important;
  }
}
</style>
