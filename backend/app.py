from http.server import HTTPServer, BaseHTTPRequestHandler
import os

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)

            self.send_header('Content-type', 'text/plain')

            self.end_headers()

            message = "Hello from Effective Mobile!"

            self.wfile.write(message.encode('utf-8'))
        else:
            self.send_response(404)
            self.end_headers()

        pass

if __name__ == '__main__':
    port = int(os.environ.get('APP_PORT', 8080))
    server_address = ('0.0.0.0', 8080)
    httpd = HTTPServer(server_address, MyHandler)
    httpd.serve_forever()
