from netmiko import ConnectHandler

devices = [{
    "ip": "cisco4.lasthop.io",
    "username": "pyclass",
    "password": "88newclass",
    "device_type": "cisco_nxos" },
    {
    "ip": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": "88newclass",
    "device_type": "cisco_nxos" }]

for dev in devices:
    print("=" * 80)
    print(f"Respones for 'show ip int br' in {dev['ip']}")
    print("=-" * 40)

    # Could probably do some error checking here.. try/except
    connector = ConnectHandler(**dev)
    output = connector.send_command('show ip int br')
    print(output)
