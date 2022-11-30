# Does not work
# Should put usb device into variable and then variable name into device dict

import subprocess
import serial
from netmiko import ConnectHandler

serial_conn = subprocess.check_output(['ls /dev/ | grep "cu.usbserial"'], shell=True, text=True)
print(serial_conn)
serial_port2 = "/dev/" + serial_conn
#str(serial_port2).strip()
print(serial_port2)
serial_port = "/dev/cu.usbserial-A9CB9ZHA"
serial_variable = type(serial_port)
print("The variable serial_port is: ", type(serial_port))
print("The variable serial_port2 is: ", type(serial_port2))

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
        "port": serial_port2,    # name that prints matches requested name but throws error
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

"""
Connecting...
Traceback (most recent call last):
  File "/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages/netmiko/utilities.py", line 247, in check_serial_port
    cdc = next(serial.tools.list_ports.grep(name))
StopIteration

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/Users/travis.jackson/PycharmProjects/net_scripts/serial_connect.py", line 30, in <module>
    with ConnectHandler(**device) as conn:
  File "/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages/netmiko/ssh_dispatcher.py", line 365, in ConnectHandler
    return ConnectionClass(*args, **kwargs)
  File "/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages/netmiko/base_connection.py", line 396, in __init__
    comm_port = check_serial_port(comm_port)
  File "/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages/netmiko/utilities.py", line 257, in check_serial_port
    raise ValueError(msg)
ValueError: dev/cu.usbserial-A9CB9ZHA
 not found. available devices are: /dev/cu.Bluetooth-Incoming-device /Port - n/a,/dev/cu.usbserial-A9CB9ZHA - FT232R USB UART,
 """
