from netmiko import ConnectHandler
from getpass import getpass

device1 = {
    "ip": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": getpass(),
    "device_type": "cisco_ios",
}

net_connect = ConnectHandler(**device1)
print(new_connect.find_prompt())
output = net_connect.send_command_timing('ping')
if 'Protocol' in output:
	output += net_connect.send_command_timing('ip')
if 'Target IP' in output:
	output += net_connect.send_command_timing('8.8.8.8')
if 'Repeat count' in output:
	output +- net_connect.send_command_timing('5')
if 'Datagram size' in output:
	output += net_connect.send_command_timing('100')
if 'Timeout in seconds' in output:
	output += net_connect.send_command_timing('2')
if 'Extended commands' in output:
	output += net_connect.send_command_timing('n')
if "Sweep range" in output:
	output += net_connect.send_command_timing('n')

print(output)