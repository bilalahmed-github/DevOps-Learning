from http.server import HTTPServer, SimpleHTTPRequestHandler

# Define the host and port
HOST = '34.67.14.196'  # or '0.0.0.0' to make it accessible externally
PORT = 8000

class MyRequestHandler(SimpleHTTPRequestHandler):
    # You can customize the request handling here if needed
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b"Hello, World! This is a simple server running on port 8000.")

# Set up the server
def run_server():
    server_address = (HOST, PORT)
    httpd = HTTPServer(server_address, MyRequestHandler)
    print(f"Server started at http://{HOST}:{PORT}")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print("\nServer stopped.")

if __name__ == "__main__":
    run_server()
