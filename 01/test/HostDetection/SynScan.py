from PyQt5.QtCore import QThread, pyqtSignal
from scapy.all import *
from scapy.layers.inet import IP, TCP

class SynScan(QThread):
    signal = pyqtSignal(str)

    def __init__(self, host, port=80):
        super(SynScan, self).__init__()
        self.host = host
        self.port = port

    def syn_scan(self):
        # 构造 TCP SYN 数据包
        tcp_packet = IP(dst=self.host) / TCP(dport=self.port, flags="S")

        # 发送 TCP SYN 数据包并接收响应数据包
        response_packet = sr1(tcp_packet, timeout=1, verbose=0)

        # 解析响应数据包并判断目标主机是否处于活动状态
        if response_packet is not None and response_packet.haslayer(TCP) and response_packet[TCP].flags == "SA":
            self.signal.emit(f"{self.host} Syn  is up")
        else:
            self.signal.emit(f"{self.host} Syn  is down")

    def run(self) -> None:
        self.syn_scan()

if __name__ == "__main__":
    # 测试示例
    scan = SynScan("192.168.234.131")
    scan.start()
    scan.wait()
