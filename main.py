# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import Ui_PyQt_PySerial

class myMainWindow(QMainWindow,Ui_PyQt_PySerial.Ui_MainWindow):
    def __init__(self):
        super(myMainWindow,self).__init__()
        self.setupUi(self)
        self.InitUI()
    def InitUI(self):
        self.setWindowIcon(QIcon('./image/uart.ico'))
        self.setWindowTitle('串口助手')
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)

    ui = myMainWindow()
    ui.show()

    sys.exit(app.exec_())
