# -*- coding: utf-8 -*-
import sys
import serial
import threading
from time import sleep

class Uart(object):
    def __init__(self,port,baud):
        self.port = port
        self.baud = baud
        self.err = 0
        try:
            self.serial = serial.Serial(self.port,self.baud)
            print("Open serial success.")
            self.err = 0
        except:
            print('Open serial error!')
            self.err = -1
    def uart_recv_thread(self):# 接收线程执行程序
        print('start uart_recv_thread.')
        while(True):
            try:
                recv_data_raw = self.serial.readline()
                data = 'DEVICE--->PC: '+recv_data_raw.decode()
                print(data)
            except:
                print('recv data error!')
                break
    def start_recv_thread(self):# 创建接收线程
        thread = threading.Thread(target=self.uart_recv_thread,daemon=True)# 创建接收线程
        thread.start()# 启动接收线程
    def send_uart_data(self,data):
        self.serial.write(data.encode())
    def uart_close(self):
        self.serial.close()


if __name__ == "__main__":
    myuart = Uart('COM9',115200)
    if 0 == myuart.err:
        print('Init Uart Success.')
    else:
        print('Init Uart Error!')

    # 如果打开串口成功，启动接受线程，准备接收数据
    myuart.start_recv_thread()

    while(True):
        input_data = input('Please input data...')
        if input_data == 'quit':
            # 退出
            myuart.uart_close()
            break
        else:
            # 发送数据给设备
            myuart.send_uart_data(input_data)
        sleep(0.1)
    pass