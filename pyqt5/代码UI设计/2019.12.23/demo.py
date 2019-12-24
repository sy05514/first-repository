import sys
from PyQt5.QtWidgets import QDesktopWidget,QMainWindow,QApplication,QHBoxLayout,QWidget,QPushButton
from PyQt5.QtGui import QIcon

class Demo(QMainWindow):
    def __init__(self):
        super(Demo, self).__init__()

        # 设置主窗口的标题
        self.setWindowTitle('第一个主窗口应用')

        # 设置窗口尺寸
        self.resize(400,300)

        # 添加Button
        self.button = QPushButton('退出应用程序')
        self.button.clicked.connect(self.onClick_Button)

        # 创建水平布局
        layout = QHBoxLayout()
        layout.addWidget(self.button)

        mainFrame = QWidget()
        mainFrame.setLayout(layout)

        self.setCentralWidget(mainFrame)

        self.status = self.statusBar()
        # 设置消息
        self.status.showMessage('只存在5秒的消息', 5000)

    # 设置窗口位置
    def center(self):
        # 获取屏幕坐标
        screen = QDesktopWidget().screenGeometry()
        # 获取窗口坐标系
        size = self.geometry()
        newLeft = (screen.width() - size.width())/2 -500
        newTop = (screen.height()-size.height())/2
        self.move(newLeft, newTop)

    # 按钮单击事件的方法
    def onClick_Button(self):
        sender = self.sender()
        print(sender.text() + '按钮被按下')
        app = QApplication.instance()
        # 退出应用程序
        app.quit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    # 设置图标
    app.setWindowIcon(QIcon('child2.png'))

    main = Demo()
    main.center()

    main.show()

    sys.exit(app.exec_())