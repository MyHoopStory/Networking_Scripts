# Works for Cisco ios devices

import serial
from netmiko import ConnectHandler

# Establish serial connection settings

device = {
    "device_type": "cisco_ios_serial",
    "username": "cisco",
    "password": "cisco",
    "secret": "cisco",
    "fast_cli": False,
    "conn_timeout": 30.0,
    "serial_settings": {
        "baudrate": serial.Serial.BAUDRATES[12],
        "bytesize": serial.EIGHTBITS,
        "parity": serial.PARITY_NONE,
        "stopbits": serial.STOPBITS_ONE,
        "port": "/dev/cu.usbserial-A9CB9ZHA",
    },
}

# Connect to device and verify by performing the show version command

print("Connecting...")
with ConnectHandler(**device) as conn:
    print("Connected")
    if not conn.check_enable_mode():
        conn.enable()
        output = conn.send_command("show version")
    output = conn.send_command("show version")
print(output)   # Capture success or failure instead of printing to the screen

# Enable a default remote connection for advanced configurations/automation
"""
- Connect to the vlan
    'conf t'
    'interface vlan 1'
- Set a management IP/subnet
- Set the default gateway
- Assign hostname and domain name?
- Set user and password
- Enable SSH
- Test remote connection
"""

default_mgmt= [
    'conf t',
    'hostname lasC3560X-test',
    'ip domain-name lasC3560X-test.com',
    'username techno privilege 15 secret test123',
    'crypto key generate rsa',
    '2048',
    'ip ssh version 2',
    'vlan 128',
    'interface vlan 128',
    'ip address 10.9.128.99 255.255.255.0',
    'int gi0/47',
    'switchport mode access',
    'switchport access vlan 128',
    'no shut',
    'exit'

]

def_mgmt_conf = conn.send_config_set(default_mgmt)
def_mgmt_output = conn.send_command("show ip arp")
print(def_mgmt_output)
conn.disconnect()

r_device = {
'device_type': 'cisco_ios',
    'host': '10.9.128.99',
    'username': 'cisco',
    'password': 'cisco',
    'port': 20022,
}

print("Connecting...")
with ConnectHandler(**r_device) as ssh:
    print("Connected")
    if not ssh.check_enable_mode():
        ssh.enable()
        ssh_output = ssh.send_command("show version")
    ssh_output = ssh.send_command("show version")
print(ssh_output)
ssh.disconnect()
# Create Customer's environment
