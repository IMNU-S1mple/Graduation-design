# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Thread_Ping.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Thread_Ping(object):
    def setupUi(self, Thread_Ping):
        Thread_Ping.setObjectName("Thread_Ping")
        Thread_Ping.resize(400, 300)
        self.label = QtWidgets.QLabel(Thread_Ping)
        self.label.setGeometry(QtCore.QRect(30, 30, 231, 16))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Thread_Ping)
        self.lineEdit.setGeometry(QtCore.QRect(30, 50, 181, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(Thread_Ping)
        self.pushButton.setGeometry(QtCore.QRect(280, 50, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.comboBox = QtWidgets.QComboBox(Thread_Ping)
        self.comboBox.setGeometry(QtCore.QRect(210, 50, 69, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")

        self.retranslateUi(Thread_Ping)
        QtCore.QMetaObject.connectSlotsByName(Thread_Ping)

    def retranslateUi(self, Thread_Ping):
        _translate = QtCore.QCoreApplication.translate
        Thread_Ping.setWindowTitle(_translate("Thread_Ping", "Form"))
        self.label.setText(_translate("Thread_Ping", "测试用例:192.168.0.1/24"))
        self.lineEdit.setText(_translate("Thread_Ping", "URL/IP/CIDR"))
        self.pushButton.setText(_translate("Thread_Ping", "Start"))
        self.comboBox.setItemText(0, _translate("Thread_Ping", "10"))
        self.comboBox.setItemText(1, _translate("Thread_Ping", "20"))
        self.comboBox.setItemText(2, _translate("Thread_Ping", "30"))
        self.comboBox.setItemText(3, _translate("Thread_Ping", "40"))
        self.comboBox.setItemText(4, _translate("Thread_Ping", "50"))
        self.comboBox.setItemText(5, _translate("Thread_Ping", "60"))
        self.comboBox.setItemText(6, _translate("Thread_Ping", "70"))
        self.comboBox.setItemText(7, _translate("Thread_Ping", "80"))
        self.comboBox.setItemText(8, _translate("Thread_Ping", "90"))
        self.comboBox.setItemText(9, _translate("Thread_Ping", "100"))
