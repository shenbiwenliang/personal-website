#!/bin/bash

echo "🚀 自动部署个人网站"
echo "=================="

# 检查是否有未提交的更改
if [ -n "$(git status --porcelain)" ]; then
    echo "📝 发现未提交的更改，正在提交..."
    git add .
    git commit -m "Auto update: $(date '+%Y-%m-%d %H:%M:%S')"
fi

echo "📤 推送到 GitHub..."
git push origin main

if [ $? -eq 0 ]; then
    echo ""
    echo "✅ 推送成功！"
    echo ""
    echo "⏰ GitHub Pages 通常需要 2-5 分钟生效"
    echo "🌐 网站地址: https://shenbiwenliang.github.io/personal-website"
    echo ""
    echo "💡 提示: 按 Ctrl+F5 强制刷新浏览器缓存"
else
    echo "❌ 推送失败，请检查网络连接"
fi