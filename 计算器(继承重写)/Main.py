from PyQt5 import QtCore, QtGui, QtWidgets
import GuiCacular, sys


class myDialog(GuiCacular.Ui_MainWindow):
    firstNum = '0'
    secondNum = '0'
    firstClickType = 'number'
    secondClickType = 'number'

    def __init__(self, Dialog):
        super().setupUi(Dialog)  # 调用父类的setupUI函数
        self.pushButton.clicked.connect(lambda: self.clickNum('7'))
        self.pushButton_2.clicked.connect(lambda: self.clickNum('8'))
        self.pushButton_3.clicked.connect(lambda: self.clickNum('9'))
        self.pushButton_4.clicked.connect(lambda: self.clickNum('4'))
        self.pushButton_5.clicked.connect(lambda: self.clickNum('5'))
        self.pushButton_6.clicked.connect(lambda: self.clickNum('6'))
        self.pushButton_7.clicked.connect(lambda: self.clickNum('1'))
        self.pushButton_8.clicked.connect(lambda: self.clickNum('2'))
        self.pushButton_9.clicked.connect(lambda: self.clickNum('3'))
        self.pushButton_10.clicked.connect(lambda: self.clickNum('0'))
        self.pushButton_17.clicked.connect(self.clickClear)

    # 按键为数字时
    def clickNum(self, index):
        if len(self.label.text()) > 10:
            print('数据过长，请清理后重试')
            return
        if self.firstClickType == 'number':
            if self.label.text() == '0':
                self.label.setText(index)
            else:
                self.label.setText(self.label.text() + index)
        elif self.firstClickType == '+':
            self.label.setText(self.label.text() + index)

    # 清空按钮
    def clickClear(self):
        self.firstClickType = 'number'
        self.secondClickType = 'number'
        self.label.setText('0')

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = myDialog(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
