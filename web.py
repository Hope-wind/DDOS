from flask import Flask
import socket

app = Flask(__name__)
@app.route("/")

def get_host_ip():
    try:
        s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        s.connect(('8.8.8.8',80))
        ip = s.getsockname()[0]

    finally:
        s.close()

    return ip



def index():
    return "Hello World"

if __name__ == "__main__":
    ip = get_host_ip()
    app.run(host=ip,port=80,debug=True)
    
