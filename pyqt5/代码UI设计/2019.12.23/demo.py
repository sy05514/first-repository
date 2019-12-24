import sys
from PyQt5.QtWidgets import QDesktopWidget,QMainWindow,QApplication
from PyQt5.QtGui import QIcon

class Demo(QMainWindow):
    def __init__(self):
        super(Demo, self).__init__()

        # 设置主窗口的标题
        self.setWindowTitle('第一个主窗口应用')

        # 设置窗口尺寸
        self.resize(400,300)

        self.status = self.statusBar()
        # 设置消息
        self.status.showMessage('只存在5秒的消息', 5000)

    def center(self):
        # 获取屏幕坐标
        screen = QDesktopWidget().screenGeometry()
        # 获取窗口坐标系
        size = self.geometry()
        newLeft = (screen.width() - size.width())/2 -500
        newTop = (screen.height()-size.height())/2
        self.move(newLeft, newTop)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    # 设置图标
    app.setWindowIcon(QIcon('child2.png'))

    main = Demo()
    main.center()
    main.show()

    sys.exit(app.exec_())