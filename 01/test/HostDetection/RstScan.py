from PyQt5.QtCore import QThread, pyqtSignal
from scapy.all import sr1, conf
from scapy.layers.inet import IP, TCP


class RstScan(QThread):
    signal = pyqtSignal(str)

    def __init__(self, host, port=80):
        super(RstScan, self).__init__()
        self.host = host
        self.port = port

    def rst_host_scan(self, target_ip, timeout=5):
        conf.verb = 0  # 关闭Scapy的冗长输出
        ip_packet = IP(dst=target_ip)
        tcp_packet = TCP(sport=54321, dport=self.port, flags='R')
        packet = ip_packet / tcp_packet

        response = sr1(packet, timeout=timeout)

        if response is not None and response.haslayer(TCP) and response[TCP].flags == 'RA':
            # print(f"{target_ip} Rst  is up")
            self.signal.emit(f"{target_ip} Rst  is up")
            return True
        else:
            # print(f"{target_ip} Rst  is down")
            self.signal.emit(f"{target_ip} Rst  is down")

        return False

    def run(self) -> None:
        self.rst_host_scan(self.host)

if __name__ == "__main__":
    scan = RstScan("192.168.234.131")
    scan.start()
    scan.wait()
