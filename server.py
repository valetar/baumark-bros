import http.server, socketserver

PORT = 3000
DIRECTORY = "/Users/alexandervalet/Documents/BaumarktBros/baumark-bros"

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)
    def log_message(self, format, *args):
        pass  # suppress request logs

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    httpd.allow_reuse_address = True
    print(f"Serving on http://localhost:{PORT}", flush=True)
    httpd.serve_forever()
