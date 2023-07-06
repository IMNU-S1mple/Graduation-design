from PyQt5.QtCore import QThread, pyqtSignal
import mysql.connector

class SearchCVEThroughCPE(QThread):
    signal = pyqtSignal(str)

    def __init__(self,cpe):
        super(SearchCVEThroughCPE, self).__init__()
        self.cpe = cpe
    def search(self):
        # 数据库连接配置
        config = {
            'user': 'root',
            'password': 'root',
            'host': '192.168.234.131',
            'database': 'vulnerability_database',
            'raise_on_warnings': True
        }

        # 连接到数据库
        cnx = mysql.connector.connect(**config)
        cursor = cnx.cursor()

        # 定义SQL查询
        sql_query = f'''
        SELECT cve.cve_id, cpe.cpe, cve.description
        FROM cve_cpe
        JOIN cve ON cve.id = cve_cpe.cve_id
        JOIN cpe ON cpe.id = cve_cpe.cpe_id
        WHERE cpe.cpe LIKE "%{self.cpe}%";
        '''

        # 执行查询
        cursor.execute(sql_query)

        # 获取所有查询结果
        result = cursor.fetchall()

        # 输出标题
        print("{:<15} {:<60} {:<100}".format("CVE ID", "CPE", "Description"))
        print("-" * 175)
        self.signal.emit("{:<15} {:<60} {:<100}".format("CVE ID", "CPE", "Description"))
        self.signal.emit("-" * 175)

        if len(result)>0:
            # 逐行输出结果
            for row in result:
                print("{:<15} {:<60} {:<100}".format(row[0], row[1], row[2]))
                self.signal.emit("{:<15} {:<60} {:<100}".format(row[0], row[1], row[2]))
        else:
            self.signal.emit("No Vulnerability")
        # 关闭连接
        cursor.close()
        cnx.close()



    def run(self) -> None:
        self.search()
if __name__ == '__main__':
    cpe = SearchCVEThroughCPE("cpe:2.3:a:apache:http_server:2.4.47")
    cpe.search()
