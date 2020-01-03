from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineCore import QWebEngineUrlRequestInterceptor
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineProfile


class HttpRequests(QWebEngineView):

    def __init__(self, *args, **kwargs):
        super(HttpRequests, self).__init__(*args, **kwargs)

