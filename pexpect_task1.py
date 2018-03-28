import pexpect

username = 'ignw'
password = 'password'
device_ip = '10.1.2.101'

connection = pexpect.spawn(f'ssh {username}@{device_ip}')
#print(connection)
#print(type(connection))

connection.expect('Password:')
connection.sendline(password)

print(connection.before)
print(connection.after)

connection.sendline('show run interface g1')
connection.expect('ip-10-1-2-101#')
interface_output = connection.before
split_output = interface_output.decode().split('\r\n')
#print(split_output)
for line in split_output:
    if line.startswith('interface'):
        interface_name = line[10:]
    elif line.startswith(' ip address'):
        interface_ip_address = line[12:]
    elif line.startswith(' description'):
        interface_description = line[12:]

print(f'Interface: {interface_name}, Description: {interface_description},'
      f'IP: {interface_ip_address}')

print(f'Interface: {interface_name}\nDescription: {interface_description}\n'
      f'IP: {interface_ip_address}')
        


