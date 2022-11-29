# Does not work
# Should put usb device into variable and then variable name into device dict

import subprocess
import serial
from netmiko import ConnectHandler

serial_conn = subprocess.check_output(['ls /dev/ | grep "cu.usbserial"'], shell=True, text=True)
print(serial_conn)
serial_port = "/dev/" + serial_conn
str(print(serial_port)).strip()

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
        "port": serial_port,    # name that prints matches requested name but throws error
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
