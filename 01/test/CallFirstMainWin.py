from PyQt5.QtPrintSupport import QPrinter
import pandas as pd
from ImportAll import *
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QWidget
from PyQt5.QtCore import Qt, QEventLoop, QTimer, pyqtSlot
from UI.MainForm import *
from UI.ChildrenForm2  import *
from UI.Subdomain import *
from UI.Fin_Scan import *
from UI.Port_Scan import *
from UI.Dir_Search import *
from UI.Thread_Ping import *
from UI.WhereIP import *
from UI.Code_Audit import *
from UI.Get_CPE import *
from UI.Search_CVE_Through_CPE import *
from UI.URG_Scan import *
from UI.Ping_Scan import *
from UI.Rst_Scan import *
from UI.Icmp_Scan import *
from UI.Syn_Scan import *
from UI.Udp_Scan import *
from UI.Window_Scan import *
from UI.Null_Scan import *
from UI.GUI_Converter import *


from HostDetection.PingScan import pingscan
from HostDetection.CheckCDN import checkcdn
from HostDetection.My_Utils import My_Utils
from HostDetection.WhereIP import whereIP
from HostDetection.CodeAudit import codeAudit
from HostDetection.SubDomain import Subdomain
from HostDetection.MultiThreadedPortScan import PortScanner
from HostDetection.Dirsearch import DirSearch
from HostDetection.NmapGetCPE import NmapGetCPE
from HostDetection.SearchCVEThroughCPE import SearchCVEThroughCPE
from HostDetection.FinScan import FinScan
from HostDetection.UrgScan import UrgScan
from HostDetection.IcmpScan import IcmpScan
from HostDetection.NullScan import NullScan
from HostDetection.RstScan import RstScan
from HostDetection.SynScan import SynScan
from HostDetection.UdpScan import UdpScanner
from HostDetection.WindowScan import WindowScan
from HostDetection.Converter import converter


class MainForm(QMainWindow, Ui_MainWindow):
    button_page_mapping = {
        'pushButton_2': [2, 'child'],
        'pushButton_3': [3, 'subdomainform'],
        'pushButton_4': [4, 'fin_scan'],
        'pushButton_5': [5, 'urg_scan'],
        'pushButton_6': [6, 'port_scan'],
        'pushButton_7': [7, 'dir_search'],
        'pushButton_9': [8, 'thread_ping'],
        'pushButton_10': [9, 'where_ip'],
        'pushButton_11': [10, 'code_audit'],
        'pushButton_14': [11, 'get_cpe'],
        'pushButton_15': [12, 'search_cve_through_cpe'],
        'pushButton_18': [13, 'ping_scan'],
        'pushButton_19': [14, 'rst_scan'],
        'pushButton_16': [15, 'icmp_scan'],
        'pushButton_20': [16, 'syn_scan'],
        'pushButton_21': [17, 'udp_scan'],
        'pushButton_22': [18, 'window_scan'],
        'pushButton_17': [19, 'null_scan'],
        'pushButton': [20, 'gui_converter']
    }

    def __init__(self):
        try:

            super(MainForm, self).__init__()

            # self.child = children()生成子窗口实例self.child
            self.child = Ui_ChildrenForm()
            self.subdomainform = Ui_SubdomainForm()
            self.fin_scan = Ui_Fin_Scan()
            self.urg_scan = Ui_URG_Scan()
            self.port_scan = Ui_PortSacnForm()
            self.dir_search = Ui_DirSearchForm()
            self.thread_ping = Ui_Thread_Ping()
            self.where_ip = Ui_WhereIP()
            self.code_audit = Ui_Code_Audit()
            self.get_cpe = Ui_GetCPE()
            self.search_cve_through_cpe = Ui_Search_CVE_Through_CPE()
            self.ping_scan = Ui_Ping_Scan()
            self.rst_scan = Ui_Rst_Scan()
            self.icmp_scan = Ui_Icmp_Scan()
            self.syn_scan = Ui_Syn_Scan()
            self.udp_scan = Ui_Udp_Scan()
            self.window_scan = Ui_Window_Scan()
            self.null_scan = Ui_Null_Scan()
            self.gui_converter = Ui_Converter()

            self.setupUi(self)
            self.initIco()

            self.init_pages_and_connections()

            # 菜单的点击事件，当点击关闭菜单时连接槽函数 close()
            # self.fileCloseAction.triggered.connect(self.close)
            # 菜单的点击事件，当点击打开菜单时连接槽函数 openMsg()
            # self.fileOpenAction.triggered.connect(self.openMsg)
            self.child.pushButton_2.clicked.connect(self.childFrom_openMsg)


            # 点击actionTst,子窗口就会显示在主窗口的MaingridLayout中
            # self.addWinAction.triggered.connect()

            self.label_2.setText("<A href='https://imnu-s1mple.github.io/'>欢迎访问作者的博客 By:WYQ</a>")
            self.label_2.setAlignment(Qt.AlignCenter)
            self.label_2.setToolTip('这是一个超链接标签')
            self.label_2.setOpenExternalLinks(True)

            # self.pushButton.clicked.connect(self.getTextEdit)

            self.child.pushButton.clicked.connect(self.Check_CDN)
            self.subdomainform.pushButton.clicked.connect(self.SubDomainAction)
            self.fin_scan.pushButton.clicked.connect(self.FinScan)
            self.urg_scan.pushButton.clicked.connect(self.URG_Scan)
            self.port_scan.pushButton.clicked.connect(self.Port_Scan)
            self.dir_search.pushButton_2.clicked.connect(self.Dir_Search)
            self.thread_ping.pushButton.clicked.connect(self.functhread)
            self.where_ip.pushButton.clicked.connect(self.whereIP)
            self.code_audit.pushButton.clicked.connect(self.codeAudit)
            self.get_cpe.pushButton.clicked.connect(self.Get_CPE)
            self.search_cve_through_cpe.pushButton.clicked.connect(self.SearchCVEThroughCPE)
            self.icmp_scan.pushButton.clicked.connect(self.Icmp_Scan)
            self.null_scan.pushButton.clicked.connect(self.Null_Scan)
            self.ping_scan.pushButton.clicked.connect(self.Ping_Scan)
            self.rst_scan.pushButton.clicked.connect(self.Rst_Scan)
            self.syn_scan.pushButton.clicked.connect(self.Syn_Scan)
            self.udp_scan.pushButton.clicked.connect(self.Udp_Scan)
            self.window_scan.pushButton.clicked.connect(self.Window_Scan)
            self.gui_converter.pushButton.clicked.connect(self.Converter)

            # sys.stdout = EmittingStr(textWritten=self.outputWritten)
            # sys.stderr = EmittingStr(textWritten=self.outputWritten)

            self.pushButton_12.clicked.connect(self.on_button_click)
            self.pushButton_13.clicked.connect(self.DownPDF)

            self.dir_search.pushButton.clicked.connect(self.dirFilename)

            self.dir_search.label.setTextInteractionFlags(Qt.TextSelectableByMouse)
            self.child.label.setTextInteractionFlags(Qt.TextSelectableByMouse)
            self.fin_scan.label.setTextInteractionFlags(Qt.TextSelectableByMouse)
            self.port_scan.label.setTextInteractionFlags(Qt.TextSelectableByMouse)
            self.subdomainform.label.setTextInteractionFlags(Qt.TextSelectableByMouse)
            self.urg_scan.label.setTextInteractionFlags(Qt.TextSelectableByMouse)
            self.thread_ping.label.setTextInteractionFlags(Qt.TextSelectableByMouse)
            self.where_ip.label.setTextInteractionFlags(Qt.TextSelectableByMouse)
            self.get_cpe.label.setTextInteractionFlags(Qt.TextSelectableByMouse)
            self.search_cve_through_cpe.label.setTextInteractionFlags(Qt.TextSelectableByMouse)




            self.pingscan = None
            self.checkcdn = None
            self.portscan = None

        except Exception as e:
            print(e)

    def init_pages_and_connections(self):
        for button_name, page_info in self.button_page_mapping.items():
            index, page_name = page_info
            form = QWidget()
            eval('self.{}.setupUi(form)'.format(page_name))
            self.stackedWidget.addWidget(form)
            eval('self.{}.clicked.connect(self.show_page)'.format(button_name))

    def show_page(self):
        index = self.button_page_mapping[self.sender().objectName()][0]
        self.stackedWidget.setCurrentIndex(index)

    def initIco(self):
        self.setWindowIcon(QIcon('./ico/yellowPeople.ico'))

    def functhread(self):
        if My_Utils.is_valid_ipv4(self.thread_ping.lineEdit.text()):
            target = self.thread_ping.lineEdit.text()
            threadNum = self.thread_ping.comboBox.currentText()

            self.pingscan = pingscan(target,int(threadNum))
            self.pingscan.signal.connect(self.updatetxt)
            self.pingscan.progress.connect(self.progress)
            self.pingscan.start()

        elif My_Utils.is_valid_cidr(self.thread_ping.lineEdit.text()):

            target = self.thread_ping.lineEdit.text()
            threadNum = self.thread_ping.comboBox.currentText()

            self.pingscan = pingscan(target, int(threadNum))
            self.pingscan.signal.connect(self.updatetxt)
            self.pingscan.progress.connect(self.progress)
            self.pingscan.start()
        else:
            self.textEdit_2.setText("Invalid parameter")

    @pyqtSlot()
    def on_button_click(self):
        if self.pingscan is not None and  self.pingscan.isRunning():
            if self.pushButton_12.text() == "暂停":
                self.pingscan.pause()
                self.pushButton_12.setText("继续")
            else:
                self.pingscan.resume()
                self.pushButton_12.setText("暂停")
        if self.checkcdn is not None and  self.checkcdn.isRunning():
            if self.pushButton_12.text() == "暂停":
                self.checkcdn.pause()
                self.pushButton_12.setText("继续")
            else:
                self.checkcdn.resume()
                self.pushButton_12.setText("暂停")
        if self.portscan is not None and  self.portscan.isRunning():
            if self.pushButton_12.text() == "暂停":
                self.portscan.pause()
                self.pushButton_12.setText("继续")
            else:
                self.portscan.resume()
                self.pushButton_12.setText("暂停")

    def updatetxt(self,str):
        self.textEdit_2.append(str)

    def DownPDF(self):
        printer = QPrinter(QPrinter.HighResolution)
        printer.setOutputFormat(QPrinter.PdfFormat)
        printer.setOutputFileName('output.pdf')

        # Create a Pandas DataFrame from QTextEdit content
        content = self.textEdit_2.toPlainText()
        data = [line for line in content.split('\n')]
        df = pd.DataFrame(data)

        # Convert DataFrame to HTML and set it as QTextEdit content
        html = df.to_html(index=False, header=False, border=0)
        self.textEdit_2.setHtml(html)

        # Print QTextEdit content to PDF
        self.textEdit_2.document().print_(printer)

        # Reset QTextEdit content back to plain text
        self.textEdit_2.setPlainText(content)

        print("PDF saved successfully.")

    def childFrom_openMsg(self):
        file, ok = QFileDialog.getOpenFileName(self, "打开", r"C:\Users\wuyanqing\Desktop\Graduation design\code\Exploring activities\01\test\Function", "All Files (*);;Text Files (*.txt)")
        # 在状态栏显示文件地址
        self.statusbar.showMessage(file)
        self.child.textEdit.setText(file)

    def dirFilename(self):
        file, ok = QFileDialog.getOpenFileName(self, "打开",r"C:\Users\wuyanqing\Desktop\Graduation design\code\Exploring activities\01\test\Function","All Files (*);;Text Files (*.txt)")
        self.dir_search.textEdit_2.setText(file)


    def Check_CDN(self):
        if self.child.textEdit.toPlainText():
            target = self.child.textEdit.toPlainText()
            self.checkcdn = checkcdn(target)
            self.checkcdn.signal.connect(self.updatetxt)
            self.checkcdn.progress.connect(self.progress)
            self.checkcdn.start()
        else :
            print("Invalid parameter")

    def whereIP(self):
        if self.where_ip.lineEdit.text():
            ip = self.where_ip.lineEdit.text()
            self.whereisip = whereIP(ip)
            self.whereisip.signal.connect(self.updatetxt)
            self.whereisip.start()
        else :
            print("Invalid parameter")

    def codeAudit(self):
        if self.code_audit.textEdit_2.toPlainText():
            self.audit = codeAudit(self.code_audit.textEdit_2.toPlainText(),self.code_audit.lineEdit.text())
            self.audit.signal.connect(self.updatetxt)
            self.audit.start()
        else :
            print("No parameter")

    def SubDomainAction(self):
        if self.subdomainform.lineEdit.text():
            self.subdomain = Subdomain(self.subdomainform.lineEdit.text(), int(self.subdomainform.comboBox.currentText()))
            self.subdomain.signal.connect(self.updatetxt)
            self.subdomain.start()
        else :
            print("No parameter")

    def Port_Scan(self):
        if self.port_scan.lineEdit.text():
            self.portscan = PortScanner(self.port_scan.lineEdit.text(),self.port_scan.comboBox.currentText())
            self.portscan.signal.connect(self.updatetxt)
            self.portscan.progress.connect(self.progress)
            self.portscan.start()
        else :
            print("No parameter")

    def Dir_Search(self):
        if self.dir_search.textEdit.toPlainText() and self.dir_search.textEdit_2.toPlainText():
            self.search = DirSearch(self.dir_search.textEdit.toPlainText(),self.dir_search.textEdit_2.toPlainText())
            self.search.signal.connect(self.updatetxt)
            self.search.progress.connect(self.progress)
            self.search.start()

        else :
            print("No parameter")

    def Get_CPE(self):
        if self.get_cpe.lineEdit.text():
            self.getcpe = NmapGetCPE(self.get_cpe.lineEdit.text())
            self.getcpe.signal.connect(self.updatetxt)
            self.getcpe.start()
        else :
            print("No parameter")

    def SearchCVEThroughCPE(self):
        if self.search_cve_through_cpe.lineEdit.text():
            self.cpe = SearchCVEThroughCPE(self.search_cve_through_cpe.lineEdit.text())
            self.cpe.signal.connect(self.updatetxt)
            self.cpe.start()
        else:
            print("No parameter")

    def FinScan(self):
        if My_Utils.is_valid_ipv4(self.fin_scan.lineEdit.text()):
            self.scan = FinScan(self.fin_scan.lineEdit.text())
            self.scan.signal.connect(self.updatetxt)
            self.scan.start()
        else:
            self.textEdit_2.setText("Invalid parameter")

    def URG_Scan(self):
        if My_Utils.is_valid_ipv4(self.urg_scan.lineEdit.text()):
            self.scan = UrgScan(self.urg_scan.lineEdit.text())
            self.scan.signal.connect(self.updatetxt)
            self.scan.start()
        else:
            self.textEdit_2.setText("Invalid parameter")

    def Icmp_Scan(self):
        if My_Utils.is_valid_ipv4(self.icmp_scan.lineEdit.text()):
            self.scan = IcmpScan(self.icmp_scan.lineEdit.text())
            self.scan.signal.connect(self.updatetxt)
            self.scan.start()
        else:
            self.textEdit_2.setText("Invalid parameter")

    def Null_Scan(self):
        if My_Utils.is_valid_ipv4(self.null_scan.lineEdit.text()):
            self.scan = NullScan(self.null_scan.lineEdit.text())
            self.scan.signal.connect(self.updatetxt)
            self.scan.start()
        else:
            self.textEdit_2.setText("Invalid parameter")

    def Ping_Scan(self):
        if My_Utils.is_valid_ipv4(self.ping_scan.lineEdit.text()):
            self.scan = pingscan(self.ping_scan.lineEdit.text(),1)
            self.scan.signal.connect(self.updatetxt)
            self.scan.start()
        else:
            self.textEdit_2.setText("Invalid parameter")

    def Rst_Scan(self):
        if My_Utils.is_valid_ipv4(self.rst_scan.lineEdit.text()):
            self.scan = RstScan(self.rst_scan.lineEdit.text())
            self.scan.signal.connect(self.updatetxt)
            self.scan.start()
        else:
            self.textEdit_2.setText("Invalid parameter")

    def Syn_Scan(self):
        if My_Utils.is_valid_ipv4(self.syn_scan.lineEdit.text()):
            self.scan = SynScan(self.syn_scan.lineEdit.text())
            self.scan.signal.connect(self.updatetxt)
            self.scan.start()
        else:
            self.textEdit_2.setText("Invalid parameter")

    def Udp_Scan(self):
        if My_Utils.is_valid_ipv4(self.udp_scan.lineEdit.text()):
            self.scan = UdpScanner(self.udp_scan.lineEdit.text())
            self.scan.signal.connect(self.updatetxt)
            self.scan.start()
        else:
            self.textEdit_2.setText("Invalid parameter")

    def Window_Scan(self):
        if My_Utils.is_valid_ipv4(self.window_scan.lineEdit.text()):
            self.scan = WindowScan(self.window_scan.lineEdit.text())
            self.scan.signal.connect(self.updatetxt)
            self.scan.start()
        else:
            self.textEdit_2.setText("Invalid parameter")

    def Converter(self):
        if self.gui_converter.textEdit_2.toPlainText():
            self.scan = converter(self.gui_converter.textEdit_2.toPlainText(),self.gui_converter.comboBox.currentText())
            self.scan.signal.connect(self.updatetxt)
            self.scan.start()
        else:
            self.textEdit_2.setText("Invalid parameter")





    def outputWritten(self, text):
        # self.textEdit.clear()
        cursor = self.textEdit_2.textCursor()
        cursor.movePosition(QtGui.QTextCursor.End)
        cursor.insertText(text)
        self.textEdit_2.setTextCursor(cursor)
        self.textEdit_2.ensureCursorVisible()

    def progress(self, value):
        self.progressBar.setValue(value)
        QApplication.processEvents()


# 重定向信号
class EmittingStr(QtCore.QObject):
        textWritten = QtCore.pyqtSignal(str)  # 定义一个发送str的信号

        def write(self, text):
            self.textWritten.emit(str(text))
            loop = QEventLoop()
            QTimer.singleShot(1000, loop.quit)
            loop.exec_()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainForm()
    win.setWindowTitle("Scanner")
    win.show()
    sys.exit(app.exec_())



