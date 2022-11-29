# Works for Cisco ios devices

import serial
from netmiko import ConnectHandler

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

print("Connecting...")
with ConnectHandler(**device) as conn:
    print("Connected")
    if not conn.check_enable_mode():
        conn.enable()
        output = conn.send_command("show version")
    output = conn.send_command("show version")
print(output)
