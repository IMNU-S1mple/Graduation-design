# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Fin_Scan.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Fin_Scan(object):
    def setupUi(self, Fin_Scan):
        Fin_Scan.setObjectName("Fin_Scan")
        Fin_Scan.resize(396, 291)
        self.pushButton = QtWidgets.QPushButton(Fin_Scan)
        self.pushButton.setGeometry(QtCore.QRect(200, 30, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(Fin_Scan)
        self.lineEdit.setGeometry(QtCore.QRect(20, 31, 181, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(Fin_Scan)
        self.label.setGeometry(QtCore.QRect(20, 10, 291, 16))
        self.label.setObjectName("label")

        self.retranslateUi(Fin_Scan)
        QtCore.QMetaObject.connectSlotsByName(Fin_Scan)

    def retranslateUi(self, Fin_Scan):
        _translate = QtCore.QCoreApplication.translate
        Fin_Scan.setWindowTitle(_translate("Fin_Scan", "Form"))
        self.pushButton.setText(_translate("Fin_Scan", "Start"))
        self.lineEdit.setText(_translate("Fin_Scan", "URL"))
        self.label.setText(_translate("Fin_Scan", "FinScan   测试用例:127.0.0.1"))
