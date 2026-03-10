# 个人网站部署指南

## 第一步：创建 GitHub 仓库

1. 打开浏览器访问：https://github.com/new?name=personal-website&description=A+personal+website&visibility=public
2. 点击 "Create repository"
3. 在创建后的页面中，你会看到类似这样的 URL：`https://github.com/YOUR_USERNAME/personal-website.git`

## 第二步：配置本地 Git 仓库

打开命令提示符，进入项目目录：

```bash
cd C:\Users\kmd123\Desktop\claude
```

## 第三步：添加远程仓库并推送

将下面的 `YOUR_USERNAME` 替换为你的实际 GitHub 用户名：

```bash
git remote add origin https://github.com/YOUR_USERNAME/personal-website.git
git branch -M main
git push -u origin main
```

## 第四步：启用 GitHub Pages

1. 访问你的仓库：https://github.com/YOUR_USERNAME/personal-website
2. 点击 "Settings" 选项卡
3. 在左侧菜单中找到 "Pages"
4. 在 "Source" 部分选择 "main" 分支
5. 点击 "Save"
6. 几分钟后，你会在页面顶部看到一个绿色的通知，显示你的网站已部署

## 第五步：访问你的网站

你的网站将在以下地址可用：
```
https://YOUR_USERNAME.github.io/personal-website
```

例如，如果你的用户名是 `johndoe`，那么你的网站地址就是：
```
https://johndoe.github.io/personal-website
```

## 自定义你的网站

你可以随时编辑 `index.html` 文件来更改网站内容：
- 修改标题和描述
- 添加个人信息
- 展示作品集
- 更新联系方式

然后重新提交并推送更改：
```bash
git add index.html
git commit -m "Update website content"
git push
```

## 注意事项

- GitHub Pages 通常需要几分钟到半小时才能生效
- 确保你的用户名拼写正确，否则网站将无法访问
- 如果遇到问题，可以查看 GitHub 的 Pages 文档