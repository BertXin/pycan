import wx
import wx.html2

class MainWindow(wx.Frame):
    def __init__(self, parent, title):
        super(MainWindow, self).__init__(parent, title=title, size=(800, 600))
        self.browser = wx.html2.WebView.New(self)
        self.browser.LoadURL("http://127.0.0.1:5000/login")  # Flask服务器地址
