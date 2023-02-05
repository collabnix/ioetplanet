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
