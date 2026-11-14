import socket
import sys

def scan_ports(target, ports):
    print(f"\n[*] Scanning target: {target}")
    print("-" * 40)

    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)

        result = sock.connect_ex((target, port))

        if result == 0:
            print(f"[OPEN] Port {port}")

        sock.close()

    print("-" * 40)
    print("[+] Scan completed!")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 netscan.py <IP>")
        sys.exit(1)

    target = sys.argv[1]

    common_ports = [
        21, 22, 23, 25, 53,
        80, 110, 139, 143,
        443, 445, 3306, 5432,
        8080, 8443
    ]

    scan_ports(target, common_ports)
