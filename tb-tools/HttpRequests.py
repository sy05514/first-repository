from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineCore import QWebEngineUrlRequestInterceptor
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineProfile


class Window(QWebEngineView):

    def __init__(self, *args, **kwargs):
        print('被实例化了')
        super(Window, self).__init__(*args, **kwargs)

