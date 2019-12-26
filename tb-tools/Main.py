import os

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QFileDialog, QMessageBox

import ui, sys

userArray = []
accountArray = []

class myDialog(ui.Ui_MainWindow):

    def __init__(self, Dialog):
        super().setupUi(Dialog)  # 调用父类的setupUI函数
        self.toolButton.clicked.connect(lambda: self.openFile())

    # 打开文件，存储用户信息
    def openFile(self):
        filepath, filetype = QFileDialog.getOpenFileName(filter="*.txt")
        if not filepath:
            return
        # 清空存储用户信息
        userArray = []
        accountArray = []
        self.statusbar.showMessage('')
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

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = myDialog(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
