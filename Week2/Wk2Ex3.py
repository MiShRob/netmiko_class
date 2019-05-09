from netmiko import ConnectHandler
from getpass import getpass

device2 = { # (Cisco 1111)
    "ip": "cisco4.lasthop.io",
    "username": "pyclass",
    "password": getpass(),
    "device_type": "cisco_ios" 
    }

net_connect = ConnectHandler(**device2)

output = net_connect.send_command('show version', use_textfsm=true)

print(output)
net_connect.disconnect()