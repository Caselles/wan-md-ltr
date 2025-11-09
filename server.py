from http.server import SimpleHTTPRequestHandler, HTTPServer

PORT = 8000

class CORSRequestHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        return super().end_headers()

if __name__ == "__main__":
    print(f"Serving at http://localhost:{PORT}")
    HTTPServer(("0.0.0.0", PORT), CORSRequestHandler).serve_forever()
