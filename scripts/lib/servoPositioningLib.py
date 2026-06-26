# Library of functions relating to handling servo data and robot positioning

# Copyright 2026, 2026 Sam Wang
# This file is part of my Mechanical Arm Project
# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
# You should have received a copy of the GNU General Public License along with this program. If not, see <https://www.gnu.org/licenses/>.


# Define new class for all servo properties. This is an ADT to store the
# given servo's name, angle position, current draw, etc.
class servoProperties:

    # Initialize

    def __init__(self, name: str, idNum: int, targetAnglePosition: int, actualAnglePosition: int, 
    voltage: float, temp: float, minAngle: int, maxAngle: int):

        self.__servoName = name
        self.__servoId = idNum

        self.__servoActualPosition = targetAnglePosition     # targetAnglePosition is the desired angle at any given moment
        self.__servoTargetPosition = actualAnglePosition     # actualAnglePosition is the angle specified by servo feedback, compared against target
        self.__servoMinAngle = minAngle
        self.__servoMaxAngle = maxAngle

        self.__servoVoltage = voltage
        self.__servoTemp = temp

    # Get Functions

    def getServoName(self):
        return self.__servoName

    def getServoId(self):
        return self.__servoId
    
    def getServoActualPosition(self):
        return self.__servoTargetPosition

    def getServoTargetPosition(self):
        return self.__servoActualPosition

    def getServoMinAngle(self):
        return self.__servoMinAngle

    def getServoMaxAngle(self):
        return self.__servoMaxAngle

    def getServoVoltage(self):
        return self.__servoVoltage

    def getServoTemp(self):
        return self.__servoTemp
    
    # Print Servo Properties

    def printServoProperties(self):
        print("Name: " + self.getServoName())
        print("Id: " + str(self.getServoId()))
        print("Actual Position: " + str(self.getServoActualPosition()) + " degrees")
        print("Target Position: " + str(self.getServoTargetPosition()) + " degrees")
        print("Min Angle: " + str(self.getServoMinAngle()) + " degrees")
        print("Max Angle: " + str(self.getServoMaxAngle()) + " degrees")
        print("Voltage: " + str(self.getServoVoltage()) + " V")
        print("Temperature: " + str(self.getServoTemp()) + " oC")

    def printTest(self):
        print(self.getServoProperties())