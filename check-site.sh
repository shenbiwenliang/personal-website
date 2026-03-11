#!/bin/bash

echo "🔍 网站状态检查"
echo "================"

SITE_URL="https://shenbiwenliang.github.io/personal-website"

echo "📡 检查网站可达性..."
if curl -s --head "$SITE_URL" | head -n 1 | grep "200\|304"; then
    echo "✅ 网站正常访问"
else
    echo "⚠️ 网站可能存在问题"
fi

echo ""
echo "🔄 检查缓存状态..."
curl -I "$SITE_URL" | grep -E "ETag|Cache-Control|Last-Modified"

echo ""
echo "📊 检查最新内容..."
curl -L -s "$SITE_URL" | grep -o "四旋翼\|穿越机\|✈️\|🏎️" | sort | uniq -c

echo ""
echo "💡 建议操作:"
echo "1. 等待几分钟让 GitHub Pages 部署完成"
echo "2. 使用 Ctrl+F5 强制刷新浏览器"
echo "3. 在无痕窗口中测试网站"