'''
Script description 
get temperature an humidity from DHT11 Arduino
date 08/10/20024
developer: Jeison M.
'''

#import libraries

import serial
import time

#arduino port
arduino_port='COM6'
arduino_bau = 9600

service = serial.Serial(
    arduino_port,
    arduino_bau,
    timeout=1
)

time.sleep(1) #Delay

while  True:
    data = service.readline().decode('utf-8').rstrip()


    if data:

        print(data)
        ''''
        temperature,humidity = data.split(",")

        print(f"temperature: {temperature}c°")
        print(f"humidity: {humidity}%")

        '''
    time.sleep(1)