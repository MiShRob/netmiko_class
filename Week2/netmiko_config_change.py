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

# To read from a file
# The file has lines of commands with no 
# output = net_connect.send_config_from_file(config_file='config_file.txt')

save_out = net_connect.save_config()  # This line does a 'copy run start'

print(output, save_out)


net_connect.disconnect()