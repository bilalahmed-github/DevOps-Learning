from http.server import HTTPServer, SimpleHTTPRequestHandler

HOST = '34.67.14.196'
PORT = 8000

def run():
    server = HTTPServer((HOST, PORT), SimpleHTTPRequestHandler)
    print(f"Server running on {HOST}:{PORT}")
    server.serve_forever()

if __name__ == "__main__":
    run()
