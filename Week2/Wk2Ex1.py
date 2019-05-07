from netmiko import ConnectHandler

device1 = {
    "ip": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": "88newclass",
    "device_type": "cisco_ios",
}

new_connect = ConnectHandler(**device1)
print(new_connect.find_prompt())
new_connect.send_command_timing('ping')

print(new_connect.send_command('ip', expect_string='Protocol'))
