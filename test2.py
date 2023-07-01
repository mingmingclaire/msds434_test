import http.server
import socketserver

PORT = 8002

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("ec2-54-69-182-7.us-west-2.compute.amazonaws.com", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
