from PyQt5.QtCore import QThread, pyqtSignal
from scapy.all import *
import sys

from scapy.layers.inet import IP, TCP, ICMP


class UrgScan(QThread):
    signal = pyqtSignal(str)


    def __init__(self,host):
        super(UrgScan, self).__init__()
        self.host = host

    def urg_scan(self,target_ip, port=80):
        conf.verb = 0  # 关闭Scapy的冗长输出
        packet = IP(dst=target_ip) / TCP(dport=port, flags="U")
        response = sr1(packet, timeout=2)

        if response is not None:
            # 如果目标主机响应了RST数据包，说明主机在线
            if response[TCP].flags.R:
                self.signal.emit(f"{target_ip} URG  is up")
                return True
            # 如果目标主机响应了其他类型的数据包，也认为主机在线
            else:
                self.signal.emit(f"{target_ip} URG  is down")
                return True
        self.signal.emit(f"{target_ip} URG  is down")
        return False

    def run(self) -> None:
        self.urg_scan(self.host)

if __name__ == '__main__':
    scan = UrgScan("192.168.0.1")
    scan.start()
    scan.wait()

