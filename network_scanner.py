import subprocess
import ipaddress
import sys
import argparse

def network_scanner(start_ip, end_ip):
    try:
        start = ipaddress.IPv4Address(start_ip)
        end = ipaddress.IPv4Address(end_ip)
    except ValueError as e:
        print(f"Error: {e}")
        return
    
    for ip_int in range(int(start), int(end)+1):
        ip = ipaddress.IPv4Address(ip_int)
        result = subprocess.run(['ping', '-c', '1', str(ip)], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        if result.returncode == 0:
            print(f"{ip} is reachable")
        else:
            print(f"{ip} is not reachable")

if __name__ == "__main__":
    start_ip = input("Enter starting IP address: ")
    end_ip = input("Enter ending IP address: ")
    network_scanner(start_ip, end_ip)

from utils import parse_args
from scanner import scan_host

def main():
    args = parse_args()
    scan_host(args.ip, args.port)

if __name__ == '__main__':
    main()

if len(sys.argv) != 3:
    print("Usage: python network_scanner.py <starting_ip> <port>")
    sys.exit(1)

starting_ip = sys.argv[1]
port = sys.argv[2]    

# Initialize ArgumentParser
parser = argparse.ArgumentParser(description='Network Scanner')

# Add arguments
parser.add_argument('ip', type=str, help='IP address to scan')
parser.add_argument('port', type=int, help='Port number to scan')

# Parse arguments
args = parser.parse_args()

# Access arguments
ip_address = args.ip
port_number = args.port

# Your scanning logic using ip_address and port_number
print(f"Scanning {ip_address}:{port_number}")
# Add your scanning logic here



