from PyQt5.QtCore import QThread, pyqtSignal
import nmap
import sys

class NmapGetCPE(QThread):
    signal = pyqtSignal(str)

    def __init__(self,host):
        super(NmapGetCPE, self).__init__()
        self.host = host


    def nmapAscan(self,host):
        nm = nmap.PortScanner()
        raw_result = nm.scan(hosts=host, arguments='-v -n -A')
        print(raw_result)
        for host, result in raw_result['scan'].items():
            if result['status']['state'] == 'up':
                self.signal.emit('#' * 17 + 'Host:' + host + '#' * 17)
                self.signal.emit('-' * 20 + '操作系统猜测' + '-' * 20)
                for os in result['osmatch']:
                    self.signal.emit('操作系统为:' + os['name'] + '准确度为:' + os['accuracy'])
                idno = 1
                try:
                    for port in result['tcp']:
                        try:
                            self.signal.emit('-' * 17 + 'TCP服务详细信息' + '[' + str(idno) + ']')
                            idno = idno + 1
                            self.signal.emit('TCP端口号:' + str(port))
                            try:
                                self.signal.emit('状态:' + result['tcp'][port]['state '])
                            except:
                                pass
                            try:
                                self.signal.emit('原因:' + result['tcp'][port]['reason'])
                            except:
                                pass
                            try:
                                self.signal.emit('额外信息:' + result['tcp'][port]['extrainfo'])
                            except:
                                pass
                            try:
                                self.signal.emit('名字:' + result['tcp'][port]['name'])
                            except:
                                pass
                            try:
                                self.signal.emit('版本:' + result['tcp'][port]['version'])
                            except:
                                pass
                            try:
                                self.signal.emit('产品:' + result['tcp'][port]['product'])
                            except:
                                pass
                            try:
                                self.signal.emit('CPE:' + self.convert_cpe_version(result['tcp'][port]['cpe']))
                            except:
                                pass
                            try:
                                self.signal.emit('脚本:' + result['tcp'][port]['script'])
                            except:
                                pass
                        except:
                            pass
                except:
                    pass

    def run(self) -> None:
        self.nmapAscan(self.host)

    def convert_cpe_version(self,cpe_str):
        cpe_parts = cpe_str.split(":")
        cpe_parts.pop(0)
        cpe_parts[0] = cpe_parts[0].replace("/", "")
        new_cpe_str = "cpe:2.3:" + ":".join(cpe_parts)
        return new_cpe_str

if __name__ == "__main__":
    cpe = NmapGetCPE("47.75.212.155")
    cpe.start()
    cpe.wait()
    print("NmapGetCPE 线程已经结束。")