# -*- coding: utf-8 -*-
# 获取当前串口号
import serial.tools.list_ports

if __name__ == "__main__":
    uart_class = list(serial.tools.list_ports.comports())
    for i in uart_class:
        print(str(i)[0:4])
        print(type(i))
    pass