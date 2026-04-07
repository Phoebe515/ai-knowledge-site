# 🚀 一键部署指南

## ⚡ 最快部署方式（5分钟完成）

### 第一步：创建GitHub仓库（2分钟）

1. 打开浏览器，访问：https://github.com/new
2. 填写信息：
   - Repository name: `ai-knowledge-site`
   - Description: `AI知识科普网站`
   - 选择 **Public**
   - **不要**勾选 "Add a README file"
   - **不要**勾选 ".gitignore"
3. 点击 "Create repository"

### 第二步：推送代码（1分钟）

复制以下命令，在终端执行：

```bash
cd /Users/peijie01/.qianfan/workspace/879a840256894d59a9ae6dfedd349999/ai-knowledge-site

# 配置Git（只需执行一次）
git config user.email "your-email@example.com"
git config user.name "Your Name"

# 提交代码
git add .
git commit -m "Initial commit: AI知识库网站"
git branch -M main

# 推送到GitHub（替换YOUR_USERNAME为你的GitHub用户名）
git remote add origin https://github.com/YOUR_USERNAME/ai-knowledge-site.git
git push -u origin main
```

### 第三步：连接Vercel（2分钟）

1. 打开浏览器，访问：https://vercel.com
2. 点击 "Sign Up" 或 "Log In"
3. 选择 **"Continue with GitHub"**
4. 授权Vercel访问GitHub
5. 点击 **"Add New..."** → **"Project"**
6. 找到 `ai-knowledge-site` 仓库
7. 点击 **"Import"**
8. 点击 **"Deploy"**
9. 等待1-2分钟
10. **完成！** 获得公网地址

---

## 📊 部署后立即操作（必做）

### 1. 设置带宽限制（防止超限）

```
1. Vercel Dashboard → 选择项目
2. Settings → Usage Limits
3. 设置 Bandwidth Limit: 90 GB
4. 启用 "Send email alerts"
5. Save
```

### 2. 启用网站分析

```
1. 项目页面 → Analytics
2. 点击 "Enable Web Analytics"
3. 开始监控访问数据
```

### 3. 修改Sitemap域名

部署后，修改配置文件：

```bash
# 编辑 docs/.vitepress/config.js
# 找到 sitemap.hostname
# 改为你的实际域名，例如：
sitemap: {
  hostname: 'https://ai-knowledge-site.vercel.app'
}
```

然后推送更新：
```bash
git add .
git commit -m "Update sitemap domain"
git push
```

### 4. 提交到搜索引擎

**Google收录：**
1. 访问：https://search.google.com/search-console/
2. 添加网站：`https://你的域名.vercel.app`
3. 验证所有权
4. 提交sitemap：`https://你的域名.vercel.app/sitemap.xml`

**百度收录：**
1. 访问：https://ziyuan.baidu.com/
2. 添加网站
3. 提交sitemap

---

## ✅ 部署完成检查清单

部署完成后，请检查：

- [ ] 网站可以正常访问
- [ ] 首页热点模块显示正常
- [ ] 所有导航链接可用
- [ ] 搜索功能正常
- [ ] 移动端显示正常
- [ ] 已设置带宽限制（90GB）
- [ ] 已启用Analytics
- [ ] 已修改sitemap域名
- [ ] 已提交到Google Search Console
- [ ] 已提交到百度搜索资源平台

---

## 🎉 部署成功后

**你的网站地址：**
```
https://ai-knowledge-site.vercel.app
或
https://你的自定义域名
```

**可以立即：**
- ✅ 分享给朋友
- ✅ 在社交媒体发布
- ✅ 开始SEO优化
- ✅ 监控访问数据

---

## ⚠️ 常见问题

### Q: 推送代码时提示权限错误？

**A:** 
1. 确保已登录GitHub账号
2. 或使用SSH方式：
```bash
git remote set-url origin git@github.com:YOUR_USERNAME/ai-knowledge-site.git
```

### Q: Vercel部署失败？

**A:** 
1. 检查package.json是否正确
2. 查看Vercel部署日志
3. 本地测试构建：`npm run docs:build`

### Q: 如何更新内容？

**A:** 
```bash
# 修改内容后
git add .
git commit -m "Update content"
git push

# Vercel自动部署，1-2分钟生效
```

---

## 📞 需要帮助？

如果遇到问题，告诉我具体的错误信息，我会帮你解决！

**准备好了吗？开始部署吧！** 🚀
