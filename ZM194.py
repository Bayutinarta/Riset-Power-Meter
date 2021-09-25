import minimalmodbus as mm
from datetime import datetime
import csv
import time
import os

inst = mm.Instrument('/dev/ttyUSB0', 1)
inst.serial.baudrate = 9600

def read_modbus():
    data = {
        'Voltage phase Va' : inst.read_float(0x0000),
    }
    return data

while True:
    print(read_modbus())
    time.sleep(1)