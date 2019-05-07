from netmiko import ConnectHandler

device1 = {
    "ip": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": "88newclass",
    "device_type": "cisco_nxos",
    #"global_delay_factor": 2,
}

net_connect = ConnectHandler(**device1)
output = net_connect.send_command('show int br', delay_factor=5, max_loops=1000)
# If delay_factor is over 10, we will need to start adding , mac_loops = 1000
print(output)

