import os
import sys
import threading
import time

from PyQt5.QtCore import QThread, pyqtSignal


sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from PingScan import pingscan

class FuncThread(QThread):
    signal = pyqtSignal(str)

    def __init__(self):
        super(FuncThread, self).__init__()

        self.pingscan = pingscan()
        self.pingscan.signal.connect(self.getstr)

    def getstr(self,str):
        self.signal.emit(str)

    def run(self):
        self.pingscan.start()



