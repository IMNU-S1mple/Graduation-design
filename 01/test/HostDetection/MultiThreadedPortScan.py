# coding:utf-8

import socket
import threading
import time
from datetime import datetime
from multiprocessing.dummy import Pool as ThreadPool

from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication, QProgressBar, QVBoxLayout, QWidget, QPlainTextEdit


class PortScanner(QThread):

    signal = pyqtSignal(str)
    progress = pyqtSignal(int)
    pause_event = threading.Event()

    def pause(self):
        self.pause_event.set()

    def resume(self):
        self.pause_event.clear()

    def __init__(self, remote_server_ip, mode,timeout=0.5, thread_pool_size=100):
        super().__init__()
        self.remote_server_ip = remote_server_ip
        self.timeout = timeout
        self.thread_pool_size = thread_pool_size
        self.completed_ports = 0
        socket.setdefaulttimeout(self.timeout)
        self.mode = mode

    def scan_port(self, port):
        while self.pause_event.is_set():
            time.sleep(0.5)
        try:
            s = socket.socket(2, 1)
            res = s.connect_ex((self.remote_server_ip, port))

            if res == 0:
                self.signal.emit(f'IP {self.remote_server_ip} Port {port}: OPEN')
            s.close()

        except Exception as e:
            print(str("多线程扫描出现了问题"))

        finally:
            self.completed_ports += 1
            progress_percentage = (self.completed_ports / 65535) * 100
            self.progress.emit(progress_percentage)

    def run(self):
        if self.mode == "AllPortsScan":
            self.scan_all_ports()
        elif self.mode == "SomePortsScan":
            self.scan_some_ports()

    def scan_all_ports(self):
        self.signal.emit(f'{self.remote_server_ip} 全部端口扫描开始')
        ports = list(range(1, 65536))
        t1 = datetime.now()
        pool = ThreadPool(processes=self.thread_pool_size)
        results = pool.map(self.scan_port, ports)
        pool.close()
        pool.join()

        self.signal.emit('Multiprocess Scanning Completed in %s' % (datetime.now() - t1))

    def scan_some_ports(self):
        self.signal.emit(f'{self.remote_server_ip} 部分端口扫描开始')
        ports_to_scan = [
            # 通用端口 (40)
            20, 21, 22, 23, 25, 53, 80, 110, 111, 113,
            119, 123, 137, 138, 139, 143, 161, 162, 179, 389,
            443, 445, 465, 514, 515, 587, 631, 636, 993, 995,
            1025, 1080, 1221, 1433, 2049, 3306, 3389, 5432, 5900, 6000,
            # Linux 特定端口 (10)
            873, 989, 990, 6667, 8000, 8080, 8443, 10000, 1521, 8081,
            # Windows 特定端口 (12)
            42, 67, 68, 69, 79, 88, 102, 135, 156, 500,
            1900, 4500
        ]

        t1 = datetime.now()
        pool = ThreadPool(processes=self.thread_pool_size)
        results = pool.map(self.scan_port, ports_to_scan)
        pool.close()
        pool.join()

        self.signal.emit('Multiprocess Scanning Completed in %s' % (datetime.now() - t1))



if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    remote_server_ip = input('输入要扫描的IP：')
    scanner = PortScanner(remote_server_ip,"SomePortsScan")

    progressBar = QProgressBar()
    progressBar.setRange(0, 100)

    results_text = QPlainTextEdit()
    results_text.setReadOnly(True)

    layout = QVBoxLayout()
    layout.addWidget(progressBar)
    layout.addWidget(results_text)

    main_widget = QWidget()
    main_widget.setLayout(layout)
    main_widget.show()

    scanner.progress.connect(progressBar.setValue)
    scanner.signal.connect(results_text.insertPlainText)
    scanner.start()

    sys.exit(app.exec_())
