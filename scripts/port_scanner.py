# Simple Port Scanner for Local Lab
import socket

# Replace '127.0.0.1' with your VM or local lab IP
target = '127.0.0.1'
ports = [22, 80, 443]

print(f"Scanning {target}...")

for port in ports:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((target, port))
    if result == 0:
        print(f"Port {port} is open")
    else:
        print(f"Port {port} is closed")
    sock.close()
