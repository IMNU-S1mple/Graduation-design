# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Null_Scan.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Null_Scan(object):
    def setupUi(self, Null_Scan):
        Null_Scan.setObjectName("Null_Scan")
        Null_Scan.resize(396, 293)
        self.pushButton = QtWidgets.QPushButton(Null_Scan)
        self.pushButton.setGeometry(QtCore.QRect(200, 39, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(Null_Scan)
        self.lineEdit.setGeometry(QtCore.QRect(20, 40, 181, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(Null_Scan)
        self.label.setGeometry(QtCore.QRect(20, 20, 311, 16))
        self.label.setObjectName("label")

        self.retranslateUi(Null_Scan)
        QtCore.QMetaObject.connectSlotsByName(Null_Scan)

    def retranslateUi(self, Null_Scan):
        _translate = QtCore.QCoreApplication.translate
        Null_Scan.setWindowTitle(_translate("Null_Scan", "Form"))
        self.pushButton.setText(_translate("Null_Scan", "Start"))
        self.lineEdit.setText(_translate("Null_Scan", "URL"))
        self.label.setText(_translate("Null_Scan", "NullScan  测试用例:127.0.0.1"))
