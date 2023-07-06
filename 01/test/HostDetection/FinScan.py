from PyQt5.QtCore import QThread, pyqtSignal
from scapy.all import *


from scapy.layers.inet import IP, TCP, ICMP


class FinScan(QThread):
    signal = pyqtSignal(str)


    def __init__(self,host):
        super(FinScan, self).__init__()
        self.host = host

    def fin_host_scan(self,target_ip, target_port=80):
        # 创建一个TCP数据包，设置目标IP、目标端口和FIN标志位
        packet = IP(dst=target_ip) / TCP(dport=target_port, flags='F')

        # 发送数据包并等待响应
        response = sr1(packet, timeout=2, verbose=0)  # verbose 参数用于控制该函数的详细输出信息。

        '''
        如果目标端口没有正在进行的TCP连接，那么目标主机通常会回复一个具有RST（Reset）和ACK（Acknowledgment）标志位的TCP数据包，
        表示"没有这个连接，无法关闭"。这种情况下，目标主机会设置RST和ACK标志位为1。

        如果目标端口正在进行TCP连接并且发送FIN数据包的主机是连接的一部分，那么目标主机将正常关闭连接。在这种情况下，
        目标主机将发送一个具有ACK标志位的TCP数据包，并在稍后发送具有FIN标志位的数据包来关闭连接。
        '''

        # 分析响应
        if response is None:
            # print(f"{target_ip} is down")
            self.signal.emit(f"{target_ip} is down")
            return False
        elif response.haslayer(TCP):
            if response[TCP].flags == 'RA':
                # print(f"{target_ip} Fin  is up")
                self.signal.emit(f"{target_ip} Fin  is up")
                return True
            elif response[TCP].flags == 'R':
                # print(f"{target_ip} Fin  is up")
                self.signal.emit(f"{target_ip} Fin  is up")
                return True
        elif response.haslayer(ICMP):
            # print(f"{target_ip} Fin is up")
            self.signal.emit(f"{target_ip} Fin is up")
            return True

    def run(self) -> None:
        self.fin_host_scan(self.host)

if __name__ == '__main__':
    scan = FinScan("192.168.234.131")
    scan.start()
    scan.wait()

