# Another-Marzban-Sub

A simple yet fancy multi-language Marzban subscription page.
一个简单、美观且支持多语言的 Marzban 订阅模板。

[🖥️ View Sample Page / 查看示例页面](https://sjzsd147.github.io/Another-Marzban-Sub/sample.html)

![Sample](https://github.com/sjzsd147/Another-Marzban-Sub/blob/main/img/sample.png)

## Installation / 安装指南

### 1. Download the file / 下载文件:
```bash
sudo wget -N -P /var/lib/marzban/templates/subscription/ https://github.com/sjzsd147/Another-Marzban-Sub/raw/refs/heads/main/index.html
```

### 2. Modify the config / 修改配置:

- Using command / 命令行快捷修改

```bash
echo 'CUSTOM_TEMPLATES_DIRECTORY="/var/lib/marzban/templates/"' | sudo tee -a /opt/marzban/.env
echo 'SUBSCRIPTION_PAGE_TEMPLATE="subscription/index.html"' | sudo tee -a /opt/marzban/.env
```

- Or edit `/opt/marzban/.env` manually / 或手动编辑 `/opt/marzban/.env`
```env
CUSTOM_TEMPLATES_DIRECTORY="/var/lib/marzban/templates/"
SUBSCRIPTION_PAGE_TEMPLATE="subscription/index.html"
```


### 3. Restart Marzban / 重启 Marzban
```bash
marzban restart
```
