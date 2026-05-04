import re

def create_sample_html():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Replacements
    content = content.replace('{{ user.username }}', 'Demo_User')
    content = content.replace('{{ user.subscription_url }}', 'https://example.com/sub/demo123')
    
    # Status
    content = content.replace('{{ user.status.value }}', 'active')
    content = content.replace('{{ user.status.value | capitalize }}', 'Active')
    
    # Duration
    content = re.sub(r'\{% if user\.expire %\}.*?\{% endif %\}', '2099-12-31', content, count=1)
    
    # Traffic
    content = re.sub(r'\{\{ user\.used_traffic \| bytesformat \}\}.*?\{% endif %\}', '12.50 GB / 100.00 GB', content, flags=re.DOTALL)
    
    # Reset
    reset_block = r'\{% set reset_val = user\.data_limit_reset_strategy.*?reset_val \}\}<\/span>'
    content = re.sub(reset_block, '<span data-i18n="reset_month">month</span>', content, flags=re.DOTALL)

    # Nodes
    nodes_block = r'\{% for link in user\.links %\}[\s\S]*?\{% endfor %\}'
    sample_nodes = """<div class="proxy-item">
                        <span class="node-name" data-url="vless://00000000-0000-0000-0000-000000000000@1.1.1.1:443?type=tcp&security=tls#HongKong-01"
                            onclick="copyText('vless://00000000-0000-0000-0000-000000000000@1.1.1.1:443?type=tcp&security=tls#HongKong-01', this, true)">Loading...</span>
                        <div class="node-actions">
                            <i class="fas fa-qrcode" onclick="showNodeQR('vless://00000000-0000-0000-0000-000000000000@1.1.1.1:443?type=tcp&security=tls#HongKong-01')" title="QR Code"></i>
                            <i class="fas fa-clone"
                                onclick="copyText('vless://00000000-0000-0000-0000-000000000000@1.1.1.1:443?type=tcp&security=tls#HongKong-01', this.parentElement.previousElementSibling, true)"
                                title="Copy"></i>
                        </div>
                    </div>
                    <div class="proxy-item">
                        <span class="node-name" data-url="trojan://password@2.2.2.2:443?security=tls#Singapore-01"
                            onclick="copyText('trojan://password@2.2.2.2:443?security=tls#Singapore-01', this, true)">Loading...</span>
                        <div class="node-actions">
                            <i class="fas fa-qrcode" onclick="showNodeQR('trojan://password@2.2.2.2:443?security=tls#Singapore-01')" title="QR Code"></i>
                            <i class="fas fa-clone"
                                onclick="copyText('trojan://password@2.2.2.2:443?security=tls#Singapore-01', this.parentElement.previousElementSibling, true)"
                                title="Copy"></i>
                        </div>
                    </div>
                    <div class="proxy-item">
                        <span class="node-name" data-url="ss://YWVzLTI1Ni1nY206cGFzc3dvcmQ@3.3.3.3:443#Japan-01"
                            onclick="copyText('ss://YWVzLTI1Ni1nY206cGFzc3dvcmQ@3.3.3.3:443#Japan-01', this, true)">Loading...</span>
                        <div class="node-actions">
                            <i class="fas fa-qrcode" onclick="showNodeQR('ss://YWVzLTI1Ni1nY206cGFzc3dvcmQ@3.3.3.3:443#Japan-01')" title="QR Code"></i>
                            <i class="fas fa-clone"
                                onclick="copyText('ss://YWVzLTI1Ni1nY206cGFzc3dvcmQ@3.3.3.3:443#Japan-01', this.parentElement.previousElementSibling, true)"
                                title="Copy"></i>
                        </div>
                    </div>"""
    content = re.sub(nodes_block, sample_nodes, content, flags=re.DOTALL)

    with open('sample.html', 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == '__main__':
    create_sample_html()
