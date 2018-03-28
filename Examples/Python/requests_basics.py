import requests


asa_ip = '10.10.10.44'
username = 'admin'
password = 'password'

s = requests.Session()
r = s.get(f'https://{asa_ip}/api/interfaces/physical/', auth=(username, password), verify=False)

r = s.get(f'https://{asa_ip}/api/interfaces/physical?securityLevel', auth=(username, password), verify=False)
print(r.text)