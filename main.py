import BaseHTTPServer as B,cgi,hashlib as h,random as r
d,p={"":""},8080
class I(B.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path in d:
            self.send_response(301)
            self.send_header("Location",d[self.path])
            self.end_headers()
        else:
            self.send_error(500)
    def do_POST(self):
        s,f="",cgi.FieldStorage(fp=self.rfile,headers=self.headers,environ={"REQUEST_METHOD":"POST"}).file.read()
        while s in d:
            s=h.md5(f+str(r.random())).hexdigest()[:9]
        d["/"+s]=f
        self.send_response(200)
        self.end_headers()
        self.wfile.write("http://localhost:"+str(p)+"/"+s)
B.HTTPServer(("",p),I).serve_forever()
