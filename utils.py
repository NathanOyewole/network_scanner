import argparse

def parse_args():
    parser = argparse.ArgumentParser(description='Simple Network Scanner')
    parser.add_argument('ip', help='IP address to scan')
    parser.add_argument('port', type=int, help='Port number to scan')
    return parser.parse_args()

