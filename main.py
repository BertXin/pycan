import wx
import threading
from app.gui.main_window import MainWindow
from app.internal.common.web.web import app
from app.internal.login import login  # 导入 login 模块以注册路由
from app.internal.user import user  # 导入 user 模块以注册路由

def run_gui():
    app = wx.App(False)
    frame = MainWindow(None, "Your App")
    frame.Show(True)
    app.MainLoop()

def run_server():
    app.run(debug=True, use_reloader=False)

def main():
    # 创建并启动后端服务器线程
    server_thread = threading.Thread(target=run_server)
    server_thread.start()

    # 运行GUI
    run_gui()

if __name__ == "__main__":
    main()
