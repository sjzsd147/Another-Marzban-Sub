# Another-Marzban-Sub

A simple yet fancy multi-language Marzban subscription page. / 一个简单、美观且支持多语言的 Marzban 订阅模板。

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

[🖥️ View Sample Page / 查看示例页面](https://sjzsd147.github.io/Another-Marzban-Sub/sample.html)

![Sample](https://github.com/sjzsd147/Another-Marzban-Sub/blob/main/img/sample.png)

## ✨ Features / 特性

- 🌐 **Multi-language Support / 多语言支持**: English, 简体中文, 繁體中文, 日本語, and Farsi (Persian, with RTL layout support).
- 🌓 **Dynamic Theme / 动态主题**: Light and Dark mode with a modern glassmorphism design.
- 📊 **User Dashboard / 用户面板**: Clean display of account status, duration, traffic usage, and reset strategies.
- 📱 **Client Setup Guide / 客户端设置指南**: Built-in OS-specific guides (Windows, macOS, Android, iOS) with one-click import support (Clash, v2rayNG, Shadowrocket).
- 🔲 **Fancy QR Codes / 精美二维码**: High-quality QR code generation for the subscription link, individual nodes, and all nodes aggregated.
- 📋 **Easy Management / 便捷管理**: One-click copy for subscription URLs, individual node links, or all nodes at once.
- 🚀 **Responsive Design / 响应式设计**: Looks great on both desktop and mobile devices.

## 🚀 Installation / 安装指南

### 1. Download the file / 下载文件:
```bash
sudo wget -N -P /var/lib/marzban/templates/subscription/ https://github.com/sjzsd147/Another-Marzban-Sub/raw/refs/heads/main/index.html
```

### 2. Modify the config / 修改配置:

- **Using command / 命令行快捷修改**

```bash
echo 'CUSTOM_TEMPLATES_DIRECTORY="/var/lib/marzban/templates/"' | sudo tee -a /opt/marzban/.env
echo 'SUBSCRIPTION_PAGE_TEMPLATE="subscription/index.html"' | sudo tee -a /opt/marzban/.env
```

- **Or edit `/opt/marzban/.env` manually / 或手动编辑 `/opt/marzban/.env`**

```env
CUSTOM_TEMPLATES_DIRECTORY="/var/lib/marzban/templates/"
SUBSCRIPTION_PAGE_TEMPLATE="subscription/index.html"
```

### 3. Restart Marzban / 重启 Marzban
```bash
marzban restart
```

## 🔄 Updating / 更新指南

To update the template to the latest version, run the following commands: / 如果需要更新到最新版本的模板，请运行以下命令：

```bash
sudo wget -N -P /var/lib/marzban/templates/subscription/ https://github.com/sjzsd147/Another-Marzban-Sub/raw/refs/heads/main/index.html
marzban restart
```

## 📝 Credits
- Icons: [FontAwesome](https://fontawesome.com/)
- Fonts: [Google Fonts (Poppins)](https://fonts.google.com/)
- QR Code: [qr-code-styling](https://github.com/kozakdenys/qr-code-styling)
