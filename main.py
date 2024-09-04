from http.server import BaseHTTPRequestHandler, HTTPServer
import time
from urllib.parse import urlparse, parse_qs

hostName = "localhost"
serverPort = 8080


def get_html_content():
    try:
        with open("index.html", "r") as file:
            return file.read()
    except FileNotFoundError:
        return "<html><body><h1>File not found</h1></body></html>"
    except IOError:
        return "<html><body><h1>Error reading file</h1></body></html>"

class MyServer(BaseHTTPRequestHandler):
    """
        Class for handling requests from the clients
    """

    def do_GET(self):
        """ Method for handling incoming GET requests """
        query_components = parse_qs(urlparse(self.path).query)
        print(query_components)
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(get_html_content(), "utf-8"))


if __name__ == "__main__":

    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
