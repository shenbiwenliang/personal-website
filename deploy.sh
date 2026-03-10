#!/bin/bash

echo "🚀 开始部署个人网站..."

# 配置 GitHub 仓库信息
read -p "请输入你的 GitHub 用户名: " username

# 添加远程仓库
git remote add origin "https://github.com/$username/personal-website.git"

# 切换到 main 分支并重命名
git branch -M main

# 推送到 GitHub
echo "📤 正在推送到 GitHub..."
git push -u origin main

if [ $? -eq 0 ]; then
    echo ""
    echo "✅ 推送成功！"
    echo ""
    echo "📋 下一步操作："
    echo "1. 访问: https://github.com/$username/personal-website"
    echo "2. 进入 Settings -> Pages"
    echo "3. 选择 'main' 分支作为源"
    echo "4. 保存设置"
    echo ""
    echo "🌐 你的网站将在几分钟内可用，地址是:"
    echo "   https://$username.github.io/personal-website"
else
    echo "❌ 推送失败，请检查你的 GitHub 用户名和权限"
fi