# coding: utf-8

import BaseHTTPServer
import cgi
import hashlib
import random

db = {"":""}
port = 8080

def get_short_url(full_url):
    short_url = ""
    while short_url in db:
        short_url = hashlib.md5(full_url+str(random.random())).hexdigest()[:5]
    db["/"+short_url] = full_url
    return short_url

class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_GET(self):
        print db
        print self.path[1:]
        if self.path in db:
            self.send_response(301)
            self.send_header("Location", db[self.path])
            self.end_headers()
        else:
            self.send_error(500)

    def do_POST(self):
        form = cgi.FieldStorage(fp=self.rfile, headers=self.headers, environ={"REQUEST_METHOD":"POST"})
        url = form.file.read()
        self.send_response(200)
        self.end_headers()
        self.wfile.write("http://localhost:"+str(port)+"/"+get_short_url(url))

if __name__=="__main__":
    BaseHTTPServer.HTTPServer(("",port), MyHandler).serve_forever()
