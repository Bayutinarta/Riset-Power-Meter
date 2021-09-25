from dds238 import DDS238
from datetime import datetime
import time
import os
import csv

x = DDS238(modbus_device = '/dev/ttyUSB0', meter_id=1)

def read_meter():
    data = {
        'datetime' : datetime.now(),
        'voltage' : x.voltage,
        'current' : x.current,
        'frequency' : x.frequency,
        'export_energy' : x.export_energy,
        'import_energy' : x.import_energy,
        'power' : x.power,
        'reactive_power' : x.reactive_power,
        'power_factor' : x.power_factor, 
    }
    return data

def saving_data(data):
    if not os.path.exists('DDS238-2.csv'):
        with open('DDS238-2.csv', 'w') as file:
            writer = csv.DictWriter(file, fieldnames=data.keys())
            writer.writeheader()
    else:
        with open ('DDS238-2.csv', 'a') as file:
            writer = csv.DictWriter(file, fieldnames = data.keys())
            writer.writerow(data)

print('Reading DDS238-2 ...')

while True:
    saving_data(read_meter())