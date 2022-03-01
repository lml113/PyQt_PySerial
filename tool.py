# -*- coding: utf-8 -*-
# 中间层
import sys
import threading
from time import sleep
from uart import Uart

class Tool(object):
    def __init__(self,parent):
        self.parent = parent
        self.uart = Uart()
        print('Tool start......')

        # self.uart.start_uart(self.parent.uart_port,self.parent.config_uart_baud)# 打开串口

        self.start_recv_thread()# 开启接收多线程
        self.start_uart_thread()# 开启接收多线程

    def uart_recv_thread(self):# 接收线程执行程序
        print('start uart_recv_thread.')
        while(True):
            if self.uart.err == 0:
                try:
                    recv_data_raw = self.uart.serial.readline()
                    data = 'DEVICE--->PC: '+recv_data_raw.decode()
                    self.parent.textBrowser.append(data)
                    print(data)
                except:
                    print('recv data error!')
    def uart_running_thread(self):# uart运行线程执行程序
        print('start uart_running_thread.')
        while(True):
            comx = self.uart.comx
            self.uart.uart_COMX()
            if comx != self.uart.comx:
                self.parent.comboBox_1.clear()
                for item in self.uart.comx:
                    self.parent.comboBox_1.addItem(str(item)[0:4])
            sleep(1) 
    def start_recv_thread(self):# 创建接收线程
        thread = threading.Thread(target=self.uart_recv_thread,daemon=True)# 创建接收线程
        thread.start()# 启动接收线程
    def start_uart_thread(self):# 创建uart运行线程
        thread = threading.Thread(target=self.uart_running_thread,daemon=True)# 创建uart运行线程
        thread.start()# 启动uart运行线程

        
