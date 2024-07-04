import socket

def scan_host(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Adjust timeout as needed
        result = sock.connect_ex((ip, port))
        if result == 0:
            print(f"Host {ip} is reachable on port {port}")
        sock.close()
    except socket.error:
        print(f"Couldn't connect to {ip}:{port}")

