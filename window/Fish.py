from PyQt5.QtWidgets import QMainWindow
from temp.fish import *

class FishWindow(QMainWindow, Ui_FishWindow):
    def __init__(self, parent=None):
        super(FishWindow, self).__init__(parent)
        self.setupUi(self)