from PyQt5.QtCore import QThread, pyqtSignal
from scapy.all import  sr1, conf
from scapy.layers.inet import IP, TCP


class WindowScan(QThread):
    signal = pyqtSignal(str)

    def __init__(self,target_ip):
        super(WindowScan, self).__init__()
        self.target_ip = target_ip


    def run(self) -> None:
        self.host_alive(self.target_ip)

    def host_alive(self,target_ip, port=80):
        conf.verb = 0  # 关闭Scapy的冗长输出
        ip_packet = IP(dst=target_ip)
        tcp_packet = TCP(dport=port, flags="S")
        response = sr1(ip_packet / tcp_packet, timeout=5)

        if response is not None and response[TCP].flags == "SA":
            # 如果窗口大小大于0，说明主机存活
            if response[TCP].window > 0:
                self.signal.emit(f"{target_ip} Window is up")
                return True
        self.signal.emit(f"{target_ip} Window is down")
        return False

if __name__ == "__main__":
    target_ip = "127.0.0.1"
    is_alive = WindowScan(target_ip)
    start = is_alive.start()
    if start:
        print(f"Host {target_ip} is {'alive' if is_alive else 'not alive'}")