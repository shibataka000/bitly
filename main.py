import BaseHTTPServer as B,cgi,hashlib as h,random as r,redis as e
u,p="localhost",8080
d=e.StrictRedis(host=u)
d.set("","")
class I(B.BaseHTTPRequestHandler):
    def do_GET(self):
        if d.exists(self.path):
            self.send_response(301)
            self.send_header("Location",d.get(self.path))
            self.end_headers()
        else:
            self.send_error(500)
    def do_POST(self):
        s,f="",cgi.FieldStorage(fp=self.rfile,headers=self.headers,environ={"REQUEST_METHOD":"POST"}).file.read()
        while d.exists(s):
            s=h.md5(f+str(r.random())).hexdigest()[:9]
        d.set("/"+s,f)
        self.send_response(200)
        self.end_headers()
        print s
        self.wfile.write("http://%s:%d/%s"%(u,p,s))
B.HTTPServer(("",p),I).serve_forever()
