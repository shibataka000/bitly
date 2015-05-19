import BaseHTTPServer as B, cgi, hashlib as h, random as r
d = {"":""}
p = 8080
def get_su(fu):
    su = ""
    while su in d:
        su = h.md5(fu+str(r.random())).hexdigest()[:9]
    d["/"+su] = fu
    return su
class I(B.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path in d:
            self.send_response(301)
            self.send_header("Location", d[self.path])
            self.end_headers()
        else:
            self.send_error(500)
    def do_POST(self):
        fu = cgi.FieldStorage(fp=self.rfile, headers=self.headers, environ={"REQUEST_METHOD":"POST"}).file.read()
        self.send_response(200)
        self.end_headers()
        self.wfile.write("http://localhost:"+str(p)+"/"+get_su(fu))
B.HTTPServer(("",p), I).serve_forever()
