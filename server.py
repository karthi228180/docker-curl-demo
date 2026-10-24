from http.server import BaseHTTPRequestHandler, HTTPServer


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello from Docker and GitHub Actions!\n")
        else:
            self.send_response(404)
            self.end_headers()

    def log_message(self, format, *args):
        print("%s - %s" % (self.address_string(), format % args))


server = HTTPServer(("0.0.0.0", 8000), Handler)
print("Server running on port 8000", flush=True)
server.serve_forever()
