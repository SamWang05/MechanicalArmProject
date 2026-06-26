# Library of functions relating to serial connection between Rasp. Pi and Bus Servo Driver Board

# Copyright 2026, 2026 Sam Wang
# This file is part of my Mechanical Arm Project
# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
# You should have received a copy of the GNU General Public License along with this program. If not, see <https://www.gnu.org/licenses/>.

import time
import serial

# Currently testing to see if serial connection can be established

serialPort = serial.Serial('/dev/ttyUSB0', 9600)

print(serialPort.name)
print("Successfully printed serial port name")

serialPort.close()