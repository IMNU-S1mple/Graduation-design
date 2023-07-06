import threading
import subprocess
import time

from PyQt5.QtCore import QThread, pyqtSignal, QObject
import subprocess
import platform
from My_Utils import *

class pingscan(QThread):
    signal = pyqtSignal(str)
    progress = pyqtSignal(int)

    def pause(self):
        self.pause_event.set()

    def resume(self):
        self.pause_event.clear()

    def __init__(self,ip,threadNum):
        # super().__init__()
        super(pingscan, self).__init__()
        self.max_threads = threadNum
        self.ip = ip
        self.pause_event = threading.Event()

    def run(self):
        threads = []
        if My_Utils.is_valid_cidr(self.ip):
            ips = My_Utils.cidr_to_ips(self.ip)
            for num,ip in enumerate(ips):
                self.progress.emit(int((num + 1) / len(ips) * 100))
                t = threading.Thread(target=self.ping, args=(ip,))
                threads.append(t)
                t.start()

                # 如果当前线程数达到最大线程数，则等待这些线程完成
                if len(threads) >= self.max_threads:
                    for t in threads:
                        t.join()
                    threads.clear()
        elif My_Utils.is_valid_ipv4(self.ip):
            self.ping(self.ip)
        # 等待所有剩余线程完成
        for t in threads:
            t.join()
        self.signal.emit("扫描完成")

    def ping(self,host):
        while self.pause_event.is_set():
            time.sleep(0.5)

        """
        使用ping命令探测主机存活
        :param host: 主机IP地址
        :return: 成功返回True，失败返回False
        """
        # 判断操作系统类型，构造ping命令
        if platform.system().lower() == "windows":
            cmd = f"ping -n 1 {host}"
        else:
            cmd = f"ping -c 1 {host}"

        # 执行ping命令
        result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)

        # 判断命令执行结果，成功返回True，失败返回False
        if result.returncode == 0 and ("TTL" in result.stdout or "ttl" in result.stdout):
            self.signal.emit(f"{host}  is up")
            return True
        else:
            self.signal.emit(f"{host}  is down")
            return False
