import socket

def check_server(address, port):
    # Create a TCP socket
    s = socket.socket()
    try:
        s.connect((address, port))
        print(f"Successfully connected to {address} on port {port}")
    except socket.error as e:
        print(f"Failed to connect to {address} on port {port}: {e}")
    finally:
        s.close()

if __name__ == "__main__":
    check_server("34.67.14.196", 8000)
