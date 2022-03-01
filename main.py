# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import Ui_PyQt_PySerial
from tool import Tool

class myMainWindow(QMainWindow,Ui_PyQt_PySerial.Ui_MainWindow):
    def __init__(self):
        super(myMainWindow,self).__init__()
        self.setupUi(self)
        self.InitUI()
    def InitUI(self):
        self.setWindowIcon(QIcon('./image/uart.ico'))
        self.setWindowTitle('串口助手')
        # self.textBrowser.setFont(QFont('Arial',16))
        self.settings = QSettings("config.ini",QSettings.IniFormat)
        self.settings.setIniCodec('UTF-8')

        self.uart_port = ''
        self.config_uart_baud = self.settings.value("SETUP/UART_BAUD",0,type=str)
        self.comboBox_2.setCurrentText(self.config_uart_baud)

        self.radioButton_1.setChecked(True)
        self.radioButton_3.setChecked(True)
        # 绑定信号与槽
        self.comboBox_1.currentIndexChanged.connect(self.comboBoxChanged)
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
        # 实例化Tool
        self.tool = Tool(self)
    def comboBoxChanged(self):
        comboBox_x = self.sender()
        self.tool.uart.uart_close()
        #print(comboBox_x.currentText())
        if comboBox_x==self.comboBox_1:
            self.uart_port = self.comboBox_1.currentText()
        elif comboBox_x==self.comboBox_2:
            uart_baud = self.comboBox_2.currentText()
            print('current uaet baud is ',uart_baud)
            self.settings.setValue('SETUP/UART_BAUD',uart_baud)
        elif comboBox_x==self.comboBox_3:
            print(self.comboBox_3.currentText())
        elif comboBox_x==self.comboBox_4:
            print(self.comboBox_4.currentText())
        elif comboBox_x==self.comboBox_5:
            print(self.comboBox_5.currentText())
        else :
            print(self.comboBox_6.currentText())
    def PushButton_send(self):
        print('you clicked btn_send')
        if self.tool.uart.err == 0:
            send_data = self.textEdit.toPlainText()
            self.tool.uart.send_uart_data(send_data)
        else:
            print('串未打开')
    def action_x_cd(self):
        action_x = self.sender()
        if action_x == self.action_start:
            print('start!!!')
            if self.uart_port != '':
                print(self.uart_port)
                self.tool.uart.start_uart(self.uart_port,self.config_uart_baud)
        elif action_x == self.action_stop:
            print('stop!!!')
            self.tool.uart.uart_close()
        elif action_x == self.action_pause:
            print('pause!!!')
        else :
            print('clear!!!')
            self.textBrowser.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    ui = myMainWindow()
    ui.show()

    sys.exit(app.exec_())
