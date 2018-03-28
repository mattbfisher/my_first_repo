import json
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning


requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

username = 'ignw'
password = 'password'
url = "https://10.1.2.101/restconf"
headers = {'content-type': 'application/yang-data+json',
           'accept': 'application/yang-data+json'}
endpoint = '/data/Cisco-IOS-XE-native:native/interface/'
data = {
'Cisco-IOS-XE-native:Loopback': {
    'name': 99,
    'description': 'RESTCONNFFFFF WHY IS IT  YELLING!',
    'ip': {
        'address': {
            'primary': {
                'address': '10.1.255.255',
                'mask': '255.255.255.255'
                }
            }
        }
    }
}
resp = requests.post(f'{url}/{endpoint}',
                    auth=(username, password), headers=headers,
                    verify=False, data=json.dumps(data))
print(resp.status_code)
print(resp.text)
