# 部署指南

## 🚀 部署到Vercel完整步骤

### 准备工作

✅ 项目已准备就绪：
- 配置文件已优化
- SEO已配置
- .gitignore已创建
- vercel.json已创建

### 部署方式选择

**推荐：GitHub + Vercel自动部署**

优势：
- 自动部署：每次push自动更新
- 预览部署：每个PR都有预览链接
- 团队协作：方便多人开发

---

## 方式一：GitHub自动部署（推荐）

### 步骤1：创建GitHub仓库

1. 访问 [github.com](https://github.com)
2. 点击 "New repository"
3. 填写信息：
   - Repository name: `ai-knowledge-site`
   - Description: `AI知识科普网站`
   - 选择 **Public**（公开）
   - ✅ Add a README file
   - ✅ Add .gitignore (Node)
4. 点击 "Create repository"

### 步骤2：推送代码到GitHub

在本地执行：

```bash
# 进入项目目录
cd ai-knowledge-site

# 初始化Git（如果还没有）
git init

# 添加远程仓库
git remote add origin https://github.com/你的用户名/ai-knowledge-site.git

# 添加所有文件
git add .

# 提交
git commit -m "Initial commit: AI知识库网站"

# 推送到GitHub
git push -u origin main
```

### 步骤3：连接Vercel

1. 访问 [vercel.com](https://vercel.com)
2. 点击 "Sign Up" 或 "Log In"
3. 选择 "Continue with GitHub"
4. 授权Vercel访问GitHub

### 步骤4：导入项目

1. 点击 "Add New..." → "Project"
2. 选择 "Import Git Repository"
3. 找到 `ai-knowledge-site` 仓库
4. 点击 "Import"

### 步骤5：配置项目

Vercel会自动检测VitePress，默认配置即可：

- **Framework Preset**: VitePress
- **Root Directory**: ./
- **Build Command**: `npm run docs:build`
- **Output Directory**: `docs/.vitepress/dist`
- **Install Command**: `npm install`

点击 "Deploy"

### 步骤6：等待部署

- 部署时间：约1-2分钟
- 状态显示：Building → Ready
- 获得地址：`https://ai-knowledge-site.vercel.app`

### 步骤7：配置域名（可选）

1. 项目设置 → Domains
2. 添加自定义域名
3. 配置DNS解析

---

## 方式二：Vercel CLI部署（快速）

### 步骤1：安装Vercel CLI

```bash
npm i -g vercel
```

### 步骤2：登录Vercel

```bash
vercel login
```

选择登录方式：
- GitHub（推荐）
- GitLab
- Bitbucket
- Email

### 步骤3：部署

```bash
# 进入项目目录
cd ai-knowledge-site

# 部署到预览环境
vercel

# 部署到生产环境
vercel --prod
```

### 步骤4：查看部署结果

部署完成后会显示：
```
✔ Production: https://ai-knowledge-site-xxx.vercel.app
```

---

## 📊 部署后配置

### 1. 设置带宽限制

**重要：防止意外超限**

1. 进入项目 → Settings → Usage Limits
2. 设置：
   - Bandwidth Limit: `90 GB`
   - 启用 "Send email alerts"
3. 保存设置

### 2. 启用Analytics

1. 项目 → Analytics
2. 点击 "Enable Web Analytics"
3. 查看实时访问数据

### 3. 配置环境变量（如需要）

1. Settings → Environment Variables
2. 添加变量（如果有API密钥等）

### 4. 设置通知

1. Settings → Notifications
2. 启用：
   - Deployment notifications
   - Usage alerts
   - Error alerts

---

## 🔍 验证部署

### 检查网站

1. 访问分配的域名
2. 检查所有页面是否正常
3. 测试搜索功能
4. 检查热点内容

### 检查性能

使用工具测试：
- [PageSpeed Insights](https://pagespeed.web.dev/)
- [GTmetrix](https://gtmetrix.com/)

预期结果：
- 性能评分：>90
- 加载时间：<2秒

---

## 📈 SEO提交

### Google收录

1. 访问 [Google Search Console](https://search.google.com/search-console/)
2. 添加网站：`https://你的域名.vercel.app`
3. 验证所有权（选择HTML标签验证）
4. 提交sitemap：`https://你的域名.vercel.app/sitemap.xml`

### 百度收录

1. 访问 [百度搜索资源平台](https://ziyuan.baidu.com/)
2. 添加网站
3. 验证
4. 提交sitemap

### Bing收录

1. 访问 [Bing Webmaster Tools](https://www.bing.com/webmasters)
2. 添加网站
3. 提交sitemap

---

## 🔄 后续更新

### 自动部署

通过GitHub推送自动触发：

```bash
# 修改内容后
git add .
git commit -m "Update content"
git push

# Vercel自动部署，1-2分钟生效
```

### 手动部署

```bash
vercel --prod
```

### 查看部署历史

1. Vercel Dashboard → Deployments
2. 查看所有部署记录
3. 可以回滚到任意版本

---

## ⚠️ 常见问题

### Q1: 部署失败怎么办？

**检查：**
- package.json是否正确
- 依赖是否完整
- 构建命令是否正确

**解决：**
```bash
# 本地测试构建
npm run docs:build

# 查看错误日志
# Vercel Dashboard → Deployments → 点击失败部署 → View Logs
```

### Q2: 如何更新内容？

**方式1：GitHub推送（推荐）**
```bash
git add .
git commit -m "Update"
git push
```

**方式2：Vercel CLI**
```bash
vercel --prod
```

### Q3: 如何绑定自定义域名？

1. 购买域名（阿里云、腾讯云等）
2. Vercel → Settings → Domains
3. 添加域名
4. 配置DNS解析：
   - 类型：CNAME
   - 值：cname.vercel-dns.com

### Q4: 如何查看访问日志？

1. Vercel Dashboard → Logs
2. 查看实时访问
3. 查看错误日志

---

## 🎉 部署完成检查清单

- [ ] 网站可以正常访问
- [ ] 所有页面链接正常
- [ ] 搜索功能正常
- [ ] 设置了带宽限制（90GB）
- [ ] 启用了Analytics
- [ ] 设置了通知
- [ ] 提交到Google Search Console
- [ ] 提交到百度搜索资源平台
- [ ] 分享给朋友测试

---

## 📞 获取帮助

- Vercel文档：[vercel.com/docs](https://vercel.com/docs)
- VitePress文档：[vitepress.dev](https://vitepress.dev)
- 社区支持：[GitHub Discussions](https://github.com/vercel/vercel/discussions)

---

**预计完成时间：10-15分钟**

祝你部署顺利！🚀
