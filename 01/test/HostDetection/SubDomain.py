import time
import socket

import requests
from PyQt5.QtCore import QThread, pyqtSignal
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urlunparse

class Subdomain(QThread):
    signal = pyqtSignal(str)

    def __init__(self,domain,page):
        super(Subdomain, self).__init__()
        self.domain = domain
        self.page = page
    def search_1(self,domain,page):
        Subdomain = []
        headers = {
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.8',
            'Cache-Control': 'max-age=0',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36',
            'Connection': 'keep-alive',
            'Referer': 'http://www.baidu.com/'
        }
        for i in range(1, page):
            # url = "https://www.bing.com/search?q=site%3abaidu.com&sp=-1&lq=0&pq=site%3abaidu.com&sc=1-14&qs=n&sk=&cvid=52B4A73FC4EB461CBA0FE449C64C3204&ghsh=0&ghacc=0&ghpl=&first=15&FORM=PERE1"
            url = "https://www.bing.com/search?q=site%3a" + domain + "&sp=-1&lq=0&pq=site%3a" + domain + "&sc=1-14&qs=n&sk=&cvid=52B4A73FC4EB461CBA0FE449C64C3204&ghsh=0&ghacc=0&ghpl=&first=" + str(
                (int(i) - 1) * 10) + "&FORM=PERE1"
            # url = "https://cn.bing.com/search?q=site%3A" + site + "&go=Search&qs=ds&first=" + str((int(i) - 1) * 10) + "&FORM=PERE"
            # conn = requests.session()
            # conn.get('http://cn.bing.com', headers=headers)
            # html = conn.get(url, stream=True, headers=headers)
            html = requests.get(url, stream=True, headers=headers)
            soup = BeautifulSoup(html.content, 'html.parser')
            # print(soup)

            job_bt = soup.findAll('h2')
            for i in job_bt:
                link = self.extract_base_url(i.a.get('href'))
                if link in Subdomain:
                    pass
                else:
                    self.signal.emit(link)
                    Subdomain.append(link)
                    print(link)

        unique_base_urls = set(self.extract_base_url(url) for url in Subdomain)


    def extract_base_url(self,domain):
        parsed = urlparse(domain)
        return urlunparse((parsed.scheme, parsed.netloc, '', '', '', ''))

    def load_subdomains(self,file_path):
        with open(file_path, 'r') as file:
            return [line.strip() for line in file.readlines()]

    def search_2(self, domain):
        subdomains = self.load_subdomains(r"C:\Users\wuyanqing\Desktop\Graduation design\code\Exploring activities\01\test\Function\SubDomain.dic")

        for subdomain in subdomains:
            zym_url = subdomain + "." + self.domain
            try:
                ip = socket.gethostbyname(zym_url)
                # print(zym_url + "-->" + ip)
                self.signal.emit(zym_url)
                time.sleep(0.1)
            except Exception as e:
                # print(zym_url + "-->" + ip + "--error")
                time.sleep(0.1)

    def run(self):
        self.search_1(self.domain,self.page)
        self.search_2(self.domain)
        self.signal.emit("Subdomain scan completed.")




if __name__ == '__main__':
    domain = Subdomain("baidu.com",10)
    domain.start()
    domain.wait()
