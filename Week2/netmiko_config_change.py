from netmiko import ConnectHandler

device1 = {
    "ip": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": "88newclass",
    "device_type": "cisco_ios",

}

net_connect = ConnectHandler(**device1)
print(net_connect.find_prompt())

cfg = [
	'logging buffered 10000',
	'no logging console'
	]

output = net_connect.send_config_set(cfg)
print(output)

net_connect.disconnect()