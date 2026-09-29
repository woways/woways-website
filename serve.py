# Local dev server that mimics Vercel cleanUrls + trailingSlash:false.
# Run:  python serve.py   ->  http://localhost:8090
import http.server, socketserver, os, urllib.parse

PORT = 8090

class Handler(http.server.SimpleHTTPRequestHandler):
    def translate_path(self, path):
        # strip query/fragment
        path = path.split('?', 1)[0].split('#', 1)[0]
        p = urllib.parse.unquote(path)
        rel = p.lstrip('/')
        # root -> index.html
        if rel == '' or rel.endswith('/'):
            rel = rel + 'index.html'
        full = os.path.join(os.getcwd(), rel.replace('/', os.sep))
        # clean URL: /companies -> companies.html when the file has no extension and isn't a real dir/file
        if not os.path.splitext(full)[1] and not os.path.isfile(full) and not os.path.isdir(full):
            if os.path.isfile(full + '.html'):
                full = full + '.html'
        return full

os.chdir(os.path.dirname(os.path.abspath(__file__)))
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving woways site with clean URLs at http://localhost:{PORT}")
    httpd.serve_forever()
