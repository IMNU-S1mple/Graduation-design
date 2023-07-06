import sys
import time

import requests
from PyQt5.QtCore import QThread, pyqtSignal


class whereIP(QThread):
    signal = pyqtSignal(str)

    def __init__(self, ip):
        super(whereIP, self).__init__()
        self.ip = ip

    def query_location_by_ip(self, ip):
        try:
            url = f'https://ip.taobao.com/outGetIpInfo?ip={ip}&accessKey=alibaba-inc'
            response = requests.get(url)
            data = response.json()
            if data['code'] == 0:
                data = response.json()["data"]
                country = data.get("country", "未知")
                city = data.get("city", "未知")
                ip = data.get("ip", "未知")
                isp = data.get("isp", "未知")
                region = data.get("region", "未知")

                from prettytable import PrettyTable

                res = '''\
                                                {:-<40}
                                                 国家名称: {} 
                                                | 省份名称: {} |
                                                | 城市名称: {}   |
                                                | 查询的IP地址: {}      |
                                                 ISP名称: {}     
                                                {:-<40}
                                                '''.format('', country, region, city, ip, isp,
                                                           '')

                # ISP Internet Service Provider
                lines = res.split('\n')
                table = PrettyTable(['IP属地查询'])

                # 将每行字符串划分为单元格，然后加入到表格中
                for line in lines:
                    cells = [cell.strip() for cell in line.split('|') if cell.strip()]
                    if cells:
                        table.add_row(cells)
                # 将表格输出
                self.signal.emit(table.get_string())
            else:
                print("IP查询失败")
        except Exception as e :
            print(e)

    def run(self):
        self.query_location_by_ip(self.ip)




if __name__ == "__main__":
    from PyQt5.QtCore import QCoreApplication
    app = QCoreApplication([])

    where_ip = whereIP("110.242.68.3")
    where_ip.signal.connect(print)  # 连接 signal 信号到 print 函数
    where_ip.start()

    sys.exit(app.exec_())
