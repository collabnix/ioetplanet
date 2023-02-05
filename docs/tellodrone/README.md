### Streaming Tello Video using Docker container



Here is an example of a Python script to configure and fetch values from the camera module of a Tello drone:

```
import socket

TELLO_IP = '192.168.10.1'
TELLO_PORT = 8889

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', TELLO_PORT))

# Configure the camera settings
sock.sendto(b'command', (TELLO_IP, TELLO_PORT))
sock.sendto(b'set camera 0', (TELLO_IP, TELLO_PORT))

# Fetch the camera values
sock.sendto(b'camera?', (TELLO_IP, TELLO_PORT))

# Receive the values from the drone
data, server = sock.recvfrom(1518)

# Print the received data
print(data.decode(encoding='utf-8'))
```

This script uses the socket library in Python to create a UDP socket and send commands to the Tello drone. The script first binds the socket to the Tello's IP address and port, then sends the command command to enter command mode. Next, it sends the set camera 0 command to configure the camera, and finally sends the camera? command to fetch the current camera values. The received data is decoded and printed to the console.

