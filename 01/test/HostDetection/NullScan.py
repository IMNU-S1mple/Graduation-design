from PyQt5.QtCore import QThread, pyqtSignal
from scapy.all import sr1, conf
from scapy.layers.inet import IP, TCP


class NullScan(QThread):
    signal = pyqtSignal(str)

    def __init__(self, host):
        super(NullScan, self).__init__()
        self.host = host

    def null_host_scan(self, target_ip, target_port=80):
        conf.verb = 0  # 关闭Scapy的冗长输出
        ip_packet = IP(dst=target_ip)
        tcp_packet = TCP(dport=target_port, flags=0)  # TCP标志位设置为0（Null扫描）
        response = sr1(ip_packet/tcp_packet, timeout=5)

        if response:
            if response[TCP].flags & 0x04:  # RST标志位的二进制数值为 0b00000100
                self.signal.emit(f"{target_ip} Null is up")
                return True
            else:
                self.signal.emit(f"{target_ip} Null is down")
        self.signal.emit(f"The host {target_ip} is not responding or is protected by a firewall.")
        return False

    def run(self) -> None:
        self.null_host_scan(self.host)
if __name__ == '__main__':
    target_ip = "127.0.0.1"
    scan = NullScan(target_ip)
    scan.start()
    scan.wait()
