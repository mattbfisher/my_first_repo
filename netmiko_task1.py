from netmiko import ConnectHandler
import re

cisco_cloud_router = {'device_type':'cisco_ios',
                    'ip':'10.1.2.101',
                    'username':'ignw',
                    'password':'password'}
connection=ConnectHandler(**cisco_cloud_router)
#print(connection)
#print(type(connection))
output = connection.send_command("show run interface g1")
print(output)

hostname = connection.find_prompt()
print(hostname[:-1])


ip_output = connection.send_command('show run int g1 | i ip address')
int_ip_address = re.search("ip address (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})$",ip_output)
int_ip_address2 = re.search("ip address (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) \d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} secondary",ip_output)
if int_ip_address:
    print(f'IP Address {int_ip_address.groups()[0]}')
else:
    print("No IP address")
if int_ip_address2:
    print(f'Secondary IP: {int_ip_address2.groups()[0]}')

commands = ['int loop0',
            'description I made this with Python\1',
            'ip address 10.1.255.1 255.255.255.255',
            'no shut']


#connection.config_mode()
#connection.send_config_set(commands)
#connection.send_command('wr')
#connection.exit_config_mode()
    

ip_output = connection.send_command('show run int loop0 | i ip address')
int_ip_address = re.search("ip address (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})$",ip_output)
if int_ip_address:
    print(f'IP Address {int_ip_address.groups()[0]}')
else:
    print("No IP address")


#show int loop0  | i line protocol

show_output = connection.send_command('show int loop0 | i line protocol')
int_status = re.search("^\w*\ is (\w*\s*\w*), line protocol is (\w*)",show_output)
print(f'It looks like the loopback0 is {int_status.groups()[0]}/{int_status.groups()[1]}')

if int_status.groups()[0] == "up":
    print('It looks like loopback1 is \"up/up\"! Way to go!')


connection.disconnect()


