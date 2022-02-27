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
        # 绑定信号与槽
        self.comboBox_2.currentIndexChanged.connect(self.comboBoxChanged)
        self.comboBox_3.currentIndexChanged.connect(self.comboBoxChanged)
        self.comboBox_4.currentIndexChanged.connect(self.comboBoxChanged)
        self.comboBox_5.currentIndexChanged.connect(self.comboBoxChanged)
        self.comboBox_6.currentIndexChanged.connect(self.comboBoxChanged)
        self.pushButton.clicked.connect(self.PushButton_send)
        self.action_start.triggered.connect(self.action_x_cd)
        self.action_stop.triggered.connect(self.action_x_cd)
        self.action_pause.triggered.connect(self.action_x_cd)
        self.action_clear.triggered.connect(self.action_x_cd)
    def comboBoxChanged(self):
        comboBox_x = self.sender()
        print(comboBox_x.currentText())
        """ if comboBox_x==self.comboBox_2:
            print(self.comboBox_2.currentText())
        elif comboBox_x==self.comboBox_3:
            print(self.comboBox_3.currentText())
        elif comboBox_x==self.comboBox_4:
            print(self.comboBox_4.currentText())
        elif comboBox_x==self.comboBox_5:
            print(self.comboBox_5.currentText())
        else :
            print(self.comboBox_6.currentText()) """
    def PushButton_send(self):
        print(self.textEdit.toPlainText())
        self.textBrowser.setText(self.textEdit.toPlainText())
    def action_x_cd(self):
        action_x = self.sender()
        if action_x == self.action_start:
            print('start!!!')
        elif action_x == self.action_stop:
            print('stop!!!')
        elif action_x == self.action_pause:
            print('pause!!!')
        else :
            print('clear!!!')


if __name__ == "__main__":
    app = QApplication(sys.argv)

    ui = myMainWindow()
    ui.show()

    sys.exit(app.exec_())
