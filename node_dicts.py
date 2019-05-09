device1 = { # (Cisco 1111)
    "ip": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": "88newclass",
    "device_type": "cisco_ios" }

device2 = { # (Cisco 1111)
    "ip": "cisco4.lasthop.io",
    "username": "pyclass",
    "password": "88newclass",
    "device_type": "cisco_ios" }

device3 = { #Arista vEOS switch
    "ip": "arista1.lasthop.io",
    "ssh_port": 22,
    "eapi_port" : 443
    "username" : "pyclass",
    "password" : "88newclass"
    "device_type": "arista"
}

device4 = { #Arista vEOS switch
    "ip": "arista2.lasthop.io",
    "ssh_port": 22,
    "eapi_port": 443
    "username": "pyclass",
    "password": "88newclass"
}

device5 = { #Arista vEOS switch
    "ip": "arista3.lasthop.io",
    "ssh_port": 22,
    "eapi_port": 443
    "username": "pyclass",
    "password": "88newclass"
}

device6 = { #Arista vEOS switch
    "ip": "arista4.lasthop.io",
    "ssh_port": 22,
    "eapi_port": 443
    "username": "pyclass",
    "password": "88newclass"
}

device7 = { #Juniper SRX
    "hostname": "srx2.lasthop.io",
    "ssh_port": 22,
    "netconf_port": 830,
    "username": "pyclass",
    "password": "88newclass"
}

device8 = { #NX-OSv Switch
    "hostname" : "nxos1.lasthop.io",
    "ssh_port" : 22,
    "nxapi_port" : 8443,
    "username" : "pyclass",
    "password" : "88newclass",
}

device9 = { #NX-OSv Switch
    "hostname" : "nxos2.lasthop.io",
    "ssh_port" : 22,
    "nxapi_port" : 8443,
    "username" : "pyclass",
    "password" : "88newclass",
}


devices = {
    "dev1":{
        "ip": "cisco4.lasthop.io",
        "username": "pyclass",
        "password": "88newclass",
        "device_type": "cisco_nxos" },
    "dev2": {
        "ip": "cisco3.lasthop.io",
        "username": "pyclass",
        "password": "88newclass",
        "device_type": "cisco_nxos" }
    }
