from getpass import getpass
from netmiko import ConnectHandler
import time


device1 = {
    "ip": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": getpass(),
    "device_type": "cisco_nxos",
    "global_delay_factor": 2,
    }


net_connect = ConnectHandler(**device1)
start_clk = time.time()
output = net_connect.send_command('show lldp neighbors detail')
cmd1_clk = time.time()
print(output)

start_clk2 = time.time()
output = net_connect.send_command('show lldp neighbors detail', delay_factor=8)
cmd2_clk = time.time()
print(output)

print("=-" * 40)
print(f"Execution of first send_command took {cmd1_clk - start_clk} seconds")
print(f"Execution of second send_command took {cmd2_clk - start_clk2} seconds")
