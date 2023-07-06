import base64
import urllib.parse

from PyQt5.QtCore import QThread, pyqtSignal


class converter(QThread):
    signal = pyqtSignal(str)

    def __init__(self,data,mode):
        super(converter, self).__init__()
        self.data = data.encode('utf-8')
        self.mode = mode

    # Base64编码
    def b64encode(self,data):
        return base64.b64encode(data).decode('utf-8')

    # Base64解码
    def b64decode(self,data):
        return base64.b64decode(data).decode('utf-8')

    # URL编码
    def urlencode(self,data):
        return urllib.parse.quote(data)

    # URL解码
    def urldecode(self,data):
        return urllib.parse.unquote(data)

    def run(self):
        if self.mode == 'b64encode':
            result = self.b64encode(self.data)
        elif self.mode == 'b64decode':
            result = self.b64decode(self.data)
        elif self.mode == 'urlencode':
            result = self.urlencode(self.data)
        elif self.mode == 'urldecode':
            result = self.urldecode(self.data)
        else:
            result = '未知的编解码类型'
        self.signal.emit(result)

if __name__ == '__main__':
    c = converter("WYQ%40qq.com","urldecode")
    c.start()
    c.wait()
