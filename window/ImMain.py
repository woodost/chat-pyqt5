from PyQt5.QtWidgets import QMainWindow,QMessageBox
from socket import *
from temp.login import *
from window.Fish import *

class ImMainWindow(QMainWindow, Ui_LoginWindow):
    def __init__(self, parent=None):
        super(ImMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.login)

    def login(self):
        name = self.lineEdit.text()
        password = self.lineEdit_2.text()
        login_info = ['login']
        login_info.append(name)
        login_info.append(password)
        login_info = ' '.join(login_info)
        self.s.send(str(login_info).encode())
        self.login_recv()

    def login_recv(self):
        recv_info = self.s.recv(self.buffsize).decode('utf-8')
        print(recv_info)
        if str(recv_info) == 'true':
            QMessageBox.information(self, '登录成功', '登录成功!', QMessageBox.Ok | QMessageBox.Close, QMessageBox.Close)
            self.change_main_window()
        elif str(recv_info)=='false-user':
            QMessageBox.information(self, '失败', '登录失败，无此账号!!', QMessageBox.Ok | QMessageBox.Close,QMessageBox.Close)
        elif str(recv_info)=='false-pw':
            QMessageBox.information(self, '失败', '登录失败，密码错误!!', QMessageBox.Ok | QMessageBox.Close,QMessageBox.Close)
        elif str(recv_info)=='false-login':
            QMessageBox.information(self, '失败', '此账号已登录!', QMessageBox.Ok | QMessageBox.Close,QMessageBox.Close)

    def change_main_window(self):
        self.hide()  # 隐藏此窗口
        self.fish = FishWindow()  # 将第二个窗口换个名字
        self.fish.show()  # 经第二个窗口显示出来

    def tcp_start(self):
        address = '127.0.0.1'
        port = 6338
        self.buffsize = 1024
        self.s = socket(AF_INET, SOCK_STREAM)
        self.s.connect((address, port))

