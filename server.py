from http.server import BaseHTTPRequestHandler, HTTPServer
import  requests
hostName = "localhost"
serverPort = 8080


class MyServer(BaseHTTPRequestHandler):
    def coins(self):
        print("parwyy")
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes("<p>part begin round 1</p>", "utf-8"))
        
        response = requests.post("http://%s:%s" % (hostName, serverPort), json={"key": "value"})
        self.wfile.write(bytes("<p>part begin round 2</p>", "utf-8"))
        print("Status code: ", response.status_code)
        print("Printing Entire Post Request")
        print(response.json())
        self.wfile.write(bytes("<p>part begin round 3</p>", "utf-8"))
        self.wfile.write(bytes("<p>%s</p>" %(response.json()), "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(
            bytes("<html><head><title>Simple Web Server</title></head>", "utf-8"))
        self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))
        if self.path == "/coins":
            MyServer.coins(self)
        elif self.path == " ":
            pass
        else:    
            self.wfile.write(bytes("<body>", "utf-8"))
            self.wfile.write(
                bytes("<p>Please visit <a href=\"/coins\">/coins</a> to play the game.</p>", "utf-8"))
            self.wfile.write(bytes("</body></html>", "utf-8"))

        def do_POST(self):
            self.response.write("This works nicely!")
        def post(self):
            self.response.out.write("maybe  works nicely!")
    


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass
    
    webServer.server_close()

# if __name__ == '__main__':
#     # from BaseHTTPServer import HTTPServer
#     server = HTTPServer(('localhost', 8080), MyServer)
#     print ('Starting server, use <Ctrl-C> to stop')
#     server.serve_forever()
