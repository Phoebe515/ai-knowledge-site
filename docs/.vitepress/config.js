import { defineConfig } from 'vitepress'

export default defineConfig({
  title: 'AI知识库',
  description: '聚焦大语言模型、Agent、Skill与AI热点',
  lang: 'zh-CN',
  
  // SEO优化：站点地图
  sitemap: {
    hostname: 'https://ai-knowledge-site-sage.vercel.app'
  },
  
  themeConfig: {
    logo: '/logo.svg',
    siteTitle: 'AI知识库',
    
    nav: [
      { text: '首页', link: '/' },
      { text: '🔥 热点', link: '/hot/' },
      { 
        text: '入门科普', 
        items: [
          { text: '大语言模型', link: '/beginner/llm/' },
          { text: 'Agent', link: '/beginner/agent/' },
          { text: 'Skill', link: '/beginner/skill/' }
        ]
      },
      { 
        text: '进阶科普', 
        items: [
          { text: '大语言模型', link: '/advanced/llm/' },
          { text: 'Agent', link: '/advanced/agent/' },
          { text: 'Skill', link: '/advanced/skill/' }
        ]
      }
    ],
    
    sidebar: {
      '/hot/': [
        {
          text: '🔥 AI热点',
          items: [
            { text: '热点列表', link: '/hot/' }
          ]
        }
      ],
      '/beginner/llm/': [
        {
          text: '入门 - 大语言模型',
          items: [
            { text: '什么是大语言模型', link: '/beginner/llm/what-is-llm' },
            { text: '如何使用ChatGPT', link: '/beginner/llm/how-to-use-chatgpt' },
            { text: '提示工程基础', link: '/beginner/llm/prompt-engineering-basics' },
            { text: '主流大模型对比', link: '/beginner/llm/llm-comparison' }
          ]
        }
      ],
      '/beginner/agent/': [
        {
          text: '入门 - Agent',
          items: [
            { text: '什么是AI Agent', link: '/beginner/agent/what-is-agent' },
            { text: 'Agent能做什么', link: '/beginner/agent/agent-capabilities' },
            { text: '如何使用Agent工具', link: '/beginner/agent/agent-tools' }
          ]
        }
      ],
      '/beginner/skill/': [
        {
          text: '入门 - Skill',
          items: [
            { text: '什么是AI Skill', link: '/beginner/skill/what-is-skill' },
            { text: '常用AI工具推荐', link: '/beginner/skill/ai-tools' },
            { text: '如何快速上手', link: '/beginner/skill/quick-start' }
          ]
        }
      ],
      '/advanced/llm/': [
        {
          text: '进阶 - 大语言模型',
          items: [
            { text: 'Transformer架构详解', link: '/advanced/llm/transformer' },
            { text: '模型训练与微调', link: '/advanced/llm/training-fine-tuning' },
            { text: 'RAG技术详解', link: '/advanced/llm/rag' },
            { text: '模型部署与优化', link: '/advanced/llm/deployment-optimization' },
            { text: '开源模型生态', link: '/advanced/llm/open-source-models' }
          ]
        }
      ],
      '/advanced/agent/': [
        {
          text: '进阶 - Agent',
          items: [
            { text: 'Agent架构设计', link: '/advanced/agent/architecture' },
            { text: '工具调用机制', link: '/advanced/agent/tool-calling' },
            { text: '多Agent协作', link: '/advanced/agent/multi-agent' },
            { text: 'Agent开发实战', link: '/advanced/agent/development' }
          ]
        }
      ],
      '/advanced/skill/': [
        {
          text: '进阶 - Skill',
          items: [
            { text: 'Skill开发指南', link: '/advanced/skill/development-guide' },
            { text: '主流Skill平台对比', link: '/advanced/skill/platform-comparison' },
            { text: 'Skill最佳实践', link: '/advanced/skill/best-practices' },
            { text: 'Skill安全与隐私', link: '/advanced/skill/security-privacy' }
          ]
        }
      ]
    },
    
    socialLinks: [
      { icon: 'github', link: 'https://github.com/your-username/ai-knowledge-site' }
    ],
    
    footer: {
      message: '基于 VitePress 构建 | 每日早7点更新热点',
      copyright: 'Copyright © 2026 AI知识库'
    },
    
    search: {
      provider: 'local'
    },
    
    outline: {
      level: [2, 3],
      label: '目录'
    }
  },
  
  markdown: {
    lineNumbers: true,
    math: true
  },
  
  head: [
    ['meta', { name: 'theme-color', content: '#667eea' }],
    ['meta', { name: 'apple-mobile-web-app-capable', content: 'yes' }],
    ['meta', { name: 'apple-mobile-web-app-status-bar-style', content: 'black' }],
    // SEO优化
    ['meta', { name: 'keywords', content: 'AI,人工智能,大语言模型,LLM,Agent,Skill,ChatGPT,GPT,Claude,机器学习,深度学习' }],
    ['meta', { name: 'author', content: 'AI知识库' }],
    ['meta', { property: 'og:type', content: 'website' }],
    ['meta', { property: 'og:title', content: 'AI知识库 - 聚焦大语言模型、Agent、Skill与AI热点' }],
    ['meta', { property: 'og:description', content: '从入门到进阶，系统学习AI核心知识' }],
    ['meta', { name: 'twitter:card', content: 'summary_large_image' }]
  ]
})
