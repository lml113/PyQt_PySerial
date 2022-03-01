# -*- coding: utf-8 -*-
# 底层
import serial
import serial.tools.list_ports

class Uart(object):
    def __init__(self):
        self.err = 1
        self.comx = list()
    def uart_COMX(self):# 获取串口列表
        self.comx = list(serial.tools.list_ports.comports())
    def start_uart(self,port,baud):
        self.err = 1
        try:
            self.serial = serial.Serial(port,baud)
            print("Open serial success.")
            self.err = 0
        except:
            print('Open serial error!')
            self.err = 1 
    def send_uart_data(self,data):
        self.serial.write(data.encode())
    def uart_close(self):
        self.err = 1
        self.serial.close()


""" if __name__ == "__main__":
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
    pass """