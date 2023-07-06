import sys
import os
import random
from datetime import datetime
from multiprocessing.pool import ThreadPool
import functools

import requests
import time
import threading

from PyQt5.QtCore import QThread, pyqtSignal


class DirSearch(QThread):
    signal = pyqtSignal(str)
    progress = pyqtSignal(int)

    def __init__(self, url, dir, thread_pool_size=100):
        super(DirSearch, self).__init__()
        self.url = url
        self.dir = dir
        self.thread_pool_size = thread_pool_size
        self.completed_ports = 0

    def _scan_single_dir(self, single_dir, *args):
        total_lines = args[0]
        target_url = f"{self.url}/{single_dir}"
        code = requests.get(url=target_url).status_code
        if code == 200 or code == 403:
            result = f"{target_url}-------{code}"
            self.signal.emit(result)
        self.completed_ports += 1
        progress_percentage = (self.completed_ports / total_lines) * 100
        self.progress.emit(progress_percentage)


    def open_dir_txt(self, filename):
        url_list = []
        with open(filename, 'r') as f:
            for l in f:
                url_list.append(l.strip())
        line_count = len(url_list)
        return url_list, line_count

    def run(self):
        dir_list, total_lines = self.open_dir_txt(self.dir)
        t1 = datetime.now()

        pool = ThreadPool(processes=self.thread_pool_size)

        # 使用 zip() 将 dir_list 和一个重复 total_lines 的列表组合成元组列表
        args = zip(dir_list, [total_lines] * len(dir_list))
        pool.starmap(self._scan_single_dir, args)

        pool.close()
        pool.join()

        elapsed_time = datetime.now() - t1
        self.signal.emit(f'Dirsearch Completed in {elapsed_time}')


if __name__ == '__main__':
    search = DirSearch("https://www.imnu.edu.cn", r"C:\Users\wuyanqing\Desktop\Graduation design\code\Exploring activities\01\test\Function\dir.txt")
    search.start()
    search.wait()
