import network
import time
import secrets
from machine import Pin
import socket

pin = Pin("LED", Pin.OUT)

ssid = secrets.SSID
password = secrets.PASSWORD

wlan = network.WLAN(network.STA_IF)
wlan.active(True)

wlan.connect(ssid, password)

# wait for connect or fail
max_wait = 10

while max_wait > 0:
    if wlan.status() < 0 or wlan.status() >= 3:
        break
    max_wait -= 1
    print("waiting for connection...")
    time.sleep(1)
    
if wlan.status() != 3:
    raise RuntimeError('Network Connection Failed')
else:
    print('connected')
    pin.value(1)
    status = wlan.ifconfig()
    print('ip = ' + status[0])

html = """<!DOCTYPE html>
<html>
<head>
    <title>ESP Web Server</title>
</head>
<body>
    <h1>ESP Web Server</h1>
    <p>LED is now ON</p>
</body>
</html>
"""

addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(addr)
s.listen(1)

print('listening on', addr)
# Listen for connections
while True:
    try:
        cl, addr = s.accept()
        print('Client connected from:', addr)
        cl_file = cl.makefile('rwb', 0)
        while True:
            line = cl_file.readline()
            if not line or line == b'\r\n':
                break
        response = html
        cl.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
        cl.send(response)
        cl.close()
        
    except OSError as e:
        cl.close()
        print('connection closed')