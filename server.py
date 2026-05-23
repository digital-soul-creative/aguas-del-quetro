from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

class Handler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/thank-you-page':
            self.path = '/thank-you-page'
            return SimpleHTTPRequestHandler.do_GET(self)
        if self.path == '/thank-you-page/':
            self.path = '/thank-you-page'
            return SimpleHTTPRequestHandler.do_GET(self)
        return SimpleHTTPRequestHandler.do_GET(self)

if __name__ == '__main__':
    ThreadingHTTPServer(('0.0.0.0', 5000), Handler).serve_forever()