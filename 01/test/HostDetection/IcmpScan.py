from PyQt5.QtCore import QThread, pyqtSignal
from scapy.all import sr1
from scapy.layers.inet import IP, ICMP


class IcmpScan(QThread):
    signal = pyqtSignal(str)

    def __init__(self, host):
        super(IcmpScan, self).__init__()
        self.host = host

    def icmp_host_scan(self, target_ip):
        packet = IP(dst=target_ip) / ICMP()
        response = sr1(packet, timeout=2, verbose=0)
        if response:
            self.signal.emit(f"{target_ip} Icmp is up")
            return True
        else:
            self.signal.emit(f"{target_ip} Icmp is down")
            return False

    def run(self):
        self.icmp_host_scan(self.host)
