import socket

def check_port(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(10)  # Timeout in seconds
    try:
        result = sock.connect_ex((ip, port))
        if result == 0:
            print(f"Port {port} on {ip} is open.")
        else:
            print(f"Port {port} on {ip} is closed.")
    except socket.error as err:
        print(f"Socket error: {err}")
    finally:
        sock.close()

if __name__ == "__main__":
    SERVER_IP = "34.67.14.196"
    PORT = 8000
    check_port(SERVER_IP, PORT)
