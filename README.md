# Another-Marzban-Sub

A simple yet fancy multilanguage Marzban subscribe page.

![Sample](https://github.com/sjzsd147/Another-Marzban-Sub/blob/main/img/sample.png)

## Installation
1. Download the file:
```bash
sudo wget -N -P /var/lib/marzban/templates/subscription/ https://github.com/sjzsd147/Another-Marzban-Sub/raw/refs/heads/main/index.html
```

2. Modify the config:

   - Using command

   ```bash
   echo 'CUSTOM_TEMPLATES_DIRECTORY="/var/lib/marzban/templates/"' | sudo tee -a /opt/marzban/.env
   echo 'SUBSCRIPTION_PAGE_TEMPLATE="subscription/index.html"' | sudo tee -a /opt/marzban/.env
   ```
   - Or edit `/opt/marzban/.env` manually
   ```
   CUSTOM_TEMPLATES_DIRECTORY="/var/lib/marzban/templates/"
   SUBSCRIPTION_PAGE_TEMPLATE="subscription/index.html"
   ```


3. Restart Marzban
```bash
marzban restart
```

