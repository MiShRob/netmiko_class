
from netmiko import ConnectHandler, file_transfer

device1 = {
    "ip": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": "88newclass",
    "device_type": "cisco_ios",

}

device8 = { #NX-OSv Switch
    "ip" : "nxos1.lasthop.io",
    "username" : "pyclass",
    "password" : "88newclass",
    "device_type": "cisco_nxos",
}


source_file = "rollback_config.txt"
dest_file = "rollback_config.txt"
direction = "get" # Other option is PUT 
file_system = "bootflash:"

# Create the Netmiko SSH connection
ssh_conn = ConnectHandler(**device8)
transfer_dict = file_transfer(
	ssh_conn,
	source_file=source_file,
	dest_file=dest_file,
	file_system=file_system,
	direction=direction,
	overwrite_file=True,
	)

print(transfer_dict)