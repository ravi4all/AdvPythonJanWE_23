from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import socket, threading

class Ui_MainWindow():
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1063, 736)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 10, 1041, 541))
        self.textEdit.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.textEdit.setObjectName("textEdit")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 580, 721, 71))
        self.lineEdit.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(760, 580, 291, 71))
        self.pushButton.setStyleSheet("font: 75 20pt \"MS Shell Dlg 2\";")
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1063, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Client"))
        self.pushButton.setText(_translate("MainWindow", "Send Message"))

        threading.Thread(target=self.startClient).start()
        self.pushButton.clicked.connect(self.sendMsg)

    def startClient(self):
        try:
            self.s = socket.socket()
            self.port = 9999
            self.s.connect(('localhost', self.port))
            threading.Thread(target=self.recvMsg).start()
        except BaseException as ex:
            print(ex)

    def sendMsg(self):
        try:
            msg = self.lineEdit.text()
            self.s.send(msg.encode())
        except BaseException as ex:
            print(ex)

    def recvMsg(self):
        while True:
            try:
                data = self.s.recv(1024).decode()
                print("Server :", data)
                # if data:
                #     self.textEdit.setPlainText("Client : {}".format(data))
            except BaseException as ex:
                print(ex)

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
