'''

TestFSM converts CLI output to structured data.. eg, lists, dicts etc.
    RegEx parser

	Uses NTC-templates

	git clone https://github.com/networktocode/ntc-templates

	# export NET_TEXTFSM=/path/to/NTC/Templates

'''

from netmiko import ConnectHandler


device1 = {
    "ip": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": "88newclass",
    "device_type": "cisco_ios",

}

net_connect = ConnectHandler(**device1)
print(net_connect.find_prompt())


output = net_connect.send_command("show ip int brief", use_textfsm=True)
print(output)

net_connect.disconnect()