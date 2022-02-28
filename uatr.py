# -*- coding: utf-8 -*-
import sys
import serial
import threading

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

if __name__ == "__main__":
    myuart = Uart('COM5',115200)
    if 0 == myuart.err:
        print('Init Uart Success.')
    else:
        print('Init Uart Error!')
    pass