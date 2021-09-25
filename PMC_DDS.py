import minimalmodbus as mm
import datetime as dt
import csv 
import time 
import os
import serial
from dds238 import DDS238

inst=mm.Instrument('/dev/ttyUSB1',50)
inst.serial.baudrate=9600
x = DDS238(modbus_device = '/dev/ttyUSB0', meter_id=1)

def read_modbus():
    data={
        'Datetime' : dt.datetime.now(),
        'KWH_Import_PMC':inst.read_long(40)/100,
        'KWH_Export_PMC':inst.read_long(42)/100,
        # 'KWH_Nett_PMC':inst.read_long(44)/100,
        # 'KWH_Total_PMC':inst.read_long(46)/100,
        'Daya':inst.read_float(4),
        'Daya Reaktif':inst.read_float(8),
        'Faktor_Daya_PMC':inst.read_float(10),
        'Tegangan_PMC':inst.read_float(0),
        'Arus_PMC':inst.read_float(2),
        'Frequensi':inst.read_float(12),
        'Tegangan_DDS' : x.voltage,
        'Arus_DDS' : x.current,
        'Frequency_DDS' : x.frequency,
        'Export_energy_DDS' : x.export_energy,
        'Import_energy_DDS' : x.import_energy,
        'Power_DDS' : x.power,
        'Reactive_power_DDS' : x.reactive_power,
        'Power_factor_DDS' : x.power_factor,
    }
    return data

print('Reading PMC220 ...')
while True:

    if os.path.exists('PMC_DDS.csv'):
        with open('PMC_DDS.csv','a') as csv_file:
            write = csv.DictWriter(csv_file, fieldnames = read_modbus().keys())
            
            write.writerow(read_modbus())
    else:
        with open ('PMC_DDS.csv', 'w') as csv_file:
            write = csv.DictWriter(csv_file, fieldnames = read_modbus().keys())
            write.writeheader()
            write.writerow(read_modbus())
    time.sleep(1)
