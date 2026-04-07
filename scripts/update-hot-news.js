// 热点更新脚本
// 此脚本用于定时更新热点内容

const fs = require('fs');
const path = require('path');

// 获取当前日期
const now = new Date();
const dateStr = now.toLocaleDateString('zh-CN', {
  year: 'numeric',
  month: 'long',
  day: 'numeric',
  hour: '2-digit',
  minute: '2-digit'
});

// 更新时间戳文件
const timestampFile = path.join(__dirname, '../docs/hot/.update-time');
fs.writeFileSync(timestampFile, `最近更新：${dateStr}`);

console.log(`✅ 热点内容更新时间已更新: ${dateStr}`);
console.log('📅 下次更新时间：明天早上7:00');
