import os

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot, QUrl
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QTextEdit
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineProfile

import ui, sys, HttpRequests

userArray = []
accountArray = []

class myDialog(ui.Ui_MainWindow):

    def __init__(self, Dialog):
        super().setupUi(Dialog)  # 调用父类的setupUI函数
        self.toolButton.clicked.connect(lambda: self.openFile())
        self.pushButton.clicked.connect(lambda: self.land())

    # 打开文件，存储用户信息
    def openFile(self):
        filepath, filetype = QFileDialog.getOpenFileName(filter="*.txt")
        if not filepath:
            return
        # 清空存储用户信息
        userArray = []
        accountArray = []
        self.lineEdit.setText('')
        self.statusbar.showMessage('')
        self.listWidget.clear()
        with open(filepath) as f:
            infoArr = f.read().split()
            if len(infoArr) % 2 != 0:
                self.statusbar.showMessage('当前文档格式有误')
                return
            for index, val in enumerate(infoArr):
                if index % 2 == 0:
                    userArray.append(val)
                else:
                    accountArray.append(val)
        self.statusbar.showMessage('文件载入成功')
        # 写入文件路径
        self.lineEdit.setText(filepath)
        # 文件内容写入listWidget
        for index, val in enumerate(userArray):
            self.listWidget.insertItem(index, userArray[index] + '    ' + accountArray[index])

    # 登录页
    def land(self):
        self.webView = QWebEngineView()
        self.webView.load(QUrl('https://www.baidu.com'))
        self.webView.setWindowTitle('webView')
        self.webView.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = myDialog(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
