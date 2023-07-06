import threading
import time

from PyQt5.QtCore import QThread, pyqtSignal
import socket
from threading import Thread, Semaphore


class checkcdn(QThread):
    signal = pyqtSignal(str)
    progress = pyqtSignal(int)

    def pause(self):
        self.pause_event.set()

    def resume(self):
        self.pause_event.clear()

    def __init__(self,target):
        super(checkcdn, self).__init__()
        self.target = target
        self.sm = Semaphore(20)
        timeout = 5.0
        # 超时判断
        socket.setdefaulttimeout(timeout)
        self.pause_event = threading.Event()

    def get_ip_list(self,domain):  # 获取域名解析出的IP列表
        dict = {}
        with self.sm:
            try:
                addrs = socket.getaddrinfo(domain, None)
                for item in addrs:
                    while self.pause_event.is_set():
                        time.sleep(0.5)
                    if item[4][0] in dict:
                        dict.get(domain).append(str(item[4][0]))
                    else:
                        dict.setdefault(domain, []).append(str(item[4][0]))
            except Exception as e:
                self.signal.emit('[-] Error: {} info: {}'.format(domain, e))
                pass
            except socket.timeout as e:
                self.signal.emit('[-] {} time out'.format(domain))
                pass
        return dict

    def open_url_txt(self,filename):
        url_list = []
        with open(filename, 'r') as f:
            for l in f:
                url_list.append(l.strip())
        return url_list

    def save_info(self,url, ip, key):
        if key == 1:
            with open('url_ip.csv', 'a+') as f:
                url_info = url + ',' + ip + '\n'
                f.write(url_info)

        else:
            with open('error_info.txt', 'a+') as f:
                f.write(url + ' ' + ','.join(ip) + '\n')

    def main(self,urls):
        url_list = self.open_url_txt(urls)
        for i,url in enumerate(url_list):
            datas = self.get_ip_list(url)
            for key in datas:
                self.progress.emit(int((i+1)/len(url_list)*100))
                if len(datas[key]) > 1:
                    self.signal.emit('[-] The Url: {} Maybe Exist CDN'.format(key))
                else:
                    self.signal.emit('[*] Url:{} IP:{}'.format(key, datas[key][0]))

    def run(self):
        self.main(self.target)

if __name__ == '__main__':
    urls = r"C:\Users\wuyanqing\Desktop\Graduation design\code\Exploring activities\01\test\Function\url_list.txt"
    cdn = checkcdn(urls)
    cdn.run()
