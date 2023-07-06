import time

import openai
from PyQt5.QtCore import QThread, pyqtSignal


class codeAudit(QThread):
    signal = pyqtSignal(str)

    def __init__(self,code,Key):
        super(codeAudit, self).__init__()
        self.code = code
        self.key = Key

    def run(self):
        openai.api_key = self.key

        # code = """<?php
        #     $con=mysqli_connect("localhost","root","XFAICL1314","dvwa"); #连接数据库，我这里直接连接了dvwa的数据库
        #     if(mysqli_connect_error())
        #     {
        #         echo "连接失败:" .mysqli_connect_error();
        #     }
        #     $id=$_GET['id'];
        #     $result=mysqli_query($con,"select * from users where `user_id`=".$id);
        #     $row=mysqli_fetch_array($result);
        #     echo $row['user'] . ":" . $row['password'];
        #     echo "<br>";"""

        # create a completion
        completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", \
                                                  messages=[
                                                      {"role": "user", "content": f"请对以下代码做代码审计，然后给我修复之后的代码，Lets think step by step{self.code}"}])
        self.signal.emit(completion.choices[0].message.content)


if __name__ == "__main__":
    code = """<?php
        $con=mysqli_connect("localhost","root","XFAICL1314","dvwa"); #连接数据库，我这里直接连接了dvwa的数据库
        if(mysqli_connect_error())
        {
            echo "连接失败:" .mysqli_connect_error();
        }
        $id=$_GET['id'];
        $result=mysqli_query($con,"select * from users where `user_id`=".$id);
        $row=mysqli_fetch_array($result);
        echo $row['user'] . ":" . $row['password'];
        echo "<br>";"""
    code_audit = codeAudit(code,"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")
    code_audit.start()
    time.sleep(10)

