from netmiko import ConnectHandler

f_handle = open('cisco_ver.txt', 'w')

device1 = {
    "ip": "cisco4.lasthop.io",
    "username": "pyclass",
    "password": "88newclass",
    "device_type": "cisco_nxos" }
print(f"Opening connection to {device1['ip']}")
net_connect = ConnectHandler(**device1)
print("Sending 'show version'")
output = net_connect.send_command('show version')

print("Writing to file... ")
f_handle.write(output)
f_handle.close()
