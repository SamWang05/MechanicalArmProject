# Library of functions relating to serial connection between Rasp. Pi and Bus Servo Driver Board

import time
import serial

# Currently testing to see if serial connection can be established

serialPort = serial.Serial('/dev/ttyUSB0', 9600)

print(serialPort.name)
print("Successfully printed serial port name")

serialPort.close()