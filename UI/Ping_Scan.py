# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ping_Scan.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Ping_Scan(object):
    def setupUi(self, Ping_Scan):
        Ping_Scan.setObjectName("Ping_Scan")
        Ping_Scan.resize(396, 290)
        self.pushButton = QtWidgets.QPushButton(Ping_Scan)
        self.pushButton.setGeometry(QtCore.QRect(200, 39, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(Ping_Scan)
        self.lineEdit.setGeometry(QtCore.QRect(20, 40, 181, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(Ping_Scan)
        self.label.setGeometry(QtCore.QRect(20, 20, 301, 16))
        self.label.setObjectName("label")

        self.retranslateUi(Ping_Scan)
        QtCore.QMetaObject.connectSlotsByName(Ping_Scan)

    def retranslateUi(self, Ping_Scan):
        _translate = QtCore.QCoreApplication.translate
        Ping_Scan.setWindowTitle(_translate("Ping_Scan", "Form"))
        self.pushButton.setText(_translate("Ping_Scan", "Start"))
        self.lineEdit.setText(_translate("Ping_Scan", "URL"))
        self.label.setText(_translate("Ping_Scan", "PingScan  测试用例:127.0.0.1"))
