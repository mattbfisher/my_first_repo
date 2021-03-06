import xml.dom.minidom
from ncclient import manager

m = manager.connect(host='10.1.2.101', port=830, username='ignw',
                    password='password', device_params={'name': 'csr'})

print(m.server_capabilities)

for cap in m.server_capabilities:
    print(cap)

print(dir(m))

csr_config = (m.get_config(source='running'))

print(csr_config.xml)

print(xml.dom.minidom.parseString(csr_config.xml).toprettyxml())
