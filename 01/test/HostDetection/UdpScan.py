from threading import Thread, Semaphore
from typing import List
from PyQt5.QtCore import pyqtSignal, QObject, QThread
from scapy.all import sr1, conf
from scapy.layers.inet import IP, UDP, ICMP
from scapy.volatile import RandShort


class UdpScanner(QThread):
    signal = pyqtSignal(str)

    def __init__(self, target_ip: str, target_port = 33434):
        super().__init__()
        self.target_ip = target_ip
        self.target_port = target_port

    def run(self):
        self.is_host_alive(target_ip=self.target_ip)

    def is_host_alive(self,target_ip, target_port=33434):
        '''选择端口号33434作为默认值主要是因为它通常用于traceroute工具。
        当执行traceroute操作时，它使用递增的TTL（Time-to-Live）值发送UDP数据包，从而逐跳探测到目标主机的路径。
        为了避免与常见服务发生冲突，traceroute默认使用较高的端口号（如33434）。'''
        conf.verb = 0  # 关闭Scapy的冗长输出

        # 创建一个UDP数据包
        packet = IP(dst=target_ip) / UDP(dport=target_port)

        # 发送数据包并等待响应
        response = sr1(packet, timeout=5)

        if response is None:
            self.signal.emit(f"{target_ip} UDP  is down")
            return False  # 无响应，可能主机不在线或被防火墙过滤

        if response.haslayer(ICMP):
            icmp_type = response.getlayer(ICMP).type
            icmp_code = response.getlayer(ICMP).code

            if icmp_type == 3 and icmp_code == 3:
                self.signal.emit(f"{target_ip} UDP  is up")
                return True  # ICMP端口不可达错误，主机可能在线
        self.signal.emit(f"{target_ip} UDP  is down")
        return False  # 其他情况，主机可能不在线

if __name__ == "__main__":
    target_ip = "47.75.212.155"
    alive = UdpScanner(target_ip)
    is_alive = alive.start()
    alive.wait()

    if is_alive:
        print(f"{target_ip} is alive")
    else:
        print(f"{target_ip} is not alive or is filtered by a firewall")
