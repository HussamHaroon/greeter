from http.server import HTTPServer, BaseHTTPRequestHandler

class GreeterHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        from datetime import date
        today = date.today().strftime("%d %B %Y")
        body = f"Hi, Hussam!<br>Today is {today}".encode()
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

if __name__ == "__main__":
    HTTPServer(("", 8000), GreeterHandler).serve_forever()
