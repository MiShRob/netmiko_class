from getpass import getpass
from netmiko import ConnectHandler


device1 = {
    "ip": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": getpass(),
    "device_type": "cisco_nxos",
    "global_delay_factor": 2,
    }


net_connect = ConnectHandler(**device1)
output = net_connect.send_command('show lldp neighbors detail')
print(output)

output = net_connect.send_command('show lldp neighbors detail', delay_factor=8)
print(output)