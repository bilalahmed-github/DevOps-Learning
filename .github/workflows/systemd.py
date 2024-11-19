from http.server import HTTPServer, SimpleHTTPRequestHandler

HOST = '0.0.0.0'
PORT = 8000

def run():
    server = HTTPServer((HOST, PORT), SimpleHTTPRequestHandler)
    print(f"Server running on {HOST}:{PORT}")
    server.serve_forever()

if __name__ == "__main__":
    run()
