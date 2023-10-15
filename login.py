# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_login(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(417, 500)
        MainWindow.setMaximumSize(QtCore.QSize(417, 500))
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        MainWindow.setFocusPolicy(QtCore.Qt.NoFocus)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: rgb(0, 85, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(110, 80, 221, 41))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:15px;\n"
"border-style:outset;\n"
"border-width:2px;")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(110, 220, 221, 41))
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:15px;\n"
"border-style:outset;\n"
"border-width:2px;")
        self.lineEdit_2.setInputMask("")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(170, 320, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton {\n"
"    \n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(0, 0, 0);\n"
"    border-radius:15px;\n"
"    border-style:outset;    \n"
"    border-width:2px;\n"
"    border-color:white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    transition:0.5;\n"
"    opacity:0.7;\n"
"    background-color: rgb(24, 24, 24);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius:15px;\n"
"    border-style:outset;    \n"
"    border-width:3px;\n"
"    border-color:white;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 80, 31, 41))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("imagens/login-img.png"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(80, 220, 31, 41))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("imagens/cadeado.png"))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(120, 280, 211, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.r_adm = QtWidgets.QRadioButton(self.centralwidget)
        self.r_adm.setGeometry(QtCore.QRect(20, 420, 141, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.r_adm.setFont(font)
        self.r_adm.setObjectName("r_adm")
        self.r_usuario = QtWidgets.QRadioButton(self.centralwidget)
        self.r_usuario.setGeometry(QtCore.QRect(20, 460, 82, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.r_usuario.setFont(font)
        self.r_usuario.setObjectName("r_usuario")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 380, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.bt_sair = QtWidgets.QPushButton(self.centralwidget)
        self.bt_sair.setGeometry(QtCore.QRect(10, 10, 401, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.bt_sair.setFont(font)
        self.bt_sair.setStyleSheet("QPushButton {\n"
"    \n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(0, 0, 0);\n"
"    \n"
"    border-width:2px;\n"
"    border-style:outset;    \n"
"    border-color:white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    transition:0.5;\n"
"    opacity:0.7;\n"
"    background-color: rgb(24, 24, 24);\n"
"    color: rgb(255, 255, 255);\n"
"    \n"
"    border-style:outset;    \n"
"    border-width:3px;\n"
"    border-color:white;\n"
"}")
        self.bt_sair.setObjectName("bt_sair")
        self.label.raise_()
        self.lineEdit.raise_()
        self.lineEdit_2.raise_()
        self.pushButton.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.r_adm.raise_()
        self.r_usuario.raise_()
        self.label_4.raise_()
        self.bt_sair.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Login"))
        self.pushButton.setText(_translate("MainWindow", "LOGIN"))
        self.r_adm.setText(_translate("MainWindow", "Administrador"))
        self.r_usuario.setText(_translate("MainWindow", "Usuario"))
        self.label_4.setText(_translate("MainWindow", "Selecione:"))
        self.bt_sair.setText(_translate("MainWindow", "SAIR"))