# Library of functions relating to handling servo data and robot positioning

# Copyright 2026, 2026 Sam Wang
# This file is part of my Mechanical Arm Project
# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
# You should have received a copy of the GNU General Public License along with this program. If not, see <https://www.gnu.org/licenses/>.


# Defines all servo properties such as  servo's name, angle position, current draw, etc.
class servoProperties:

    # Initialize
    def __init__(self, name: str, idNum: int, targetAnglePosition: float, actualAnglePosition: float, 
    minAngle: float, maxAngle: float, voltage: float, temp: float, lockStatus: bool):

        self.__servoName = name
        self.__servoId = idNum

        self.__servoActualPosition = targetAnglePosition     # targetAnglePosition is the desired angle at any given moment
        self.__servoTargetPosition = actualAnglePosition     # actualAnglePosition is the angle specified by servo feedback, compared against target
        self.__servoMinAngle = minAngle
        self.__servoMaxAngle = maxAngle

        self.__servoVoltage = voltage
        self.__servoTemp = temp
        self.__servoLockStat = lockStatus


    # Get Functions - Outside of initialization, these should NOT 
    # be used on their own. Use the functions under armPosition instead!!!
    def getServoName(self):
        return self.__servoName

    def getServoId(self):
        return self.__servoId
    
    def getServoActPos(self):
        return self.__servoTargetPosition

    def getServoTarPos(self):
        return self.__servoActualPosition

    def getServoMinAngle(self):
        return self.__servoMinAngle

    def getServoMaxAngle(self):
        return self.__servoMaxAngle

    def getServoVoltage(self):
        return self.__servoVoltage

    def getServoTemp(self):
        return self.__servoTemp
    
    def getServoLockStat(self):
        return self.__servoLockStat

    # Set Functions - Outside of initialization, these should NOT 
    # be used on their own. Use the functions under armPosition instead!!!
    def setServoName(self, newName):
        if type(newName) == str:
            self.__servoName = newName

    def setServoId(self, newId):
        if type(newId) == int:
            self.__servoId = newId

    def setServoActPos(self, newActualPosition):     # Note: No filter can be placed for actual position, it should always reflect the exact angle given by the servo
        if type(newActualPosition) == float:
            self.__servoActualPosition = newActualPosition

    def setServoTarPos(self, newTargetPosition):
        if type(newTargetPosition) == float:
            if newTargetPosition < self.getServoMinAngle():
                self.__servoTargetPosition = self.getServoMinAngle()
            elif newTargetPosition > self.getServoMaxAngle():
                self.__servoTargetPosition = self.getServoMaxAngle()
            else:
                self.__servoTargetPosition = newTargetPosition

    def setServoVoltage(self, newVoltage):
        if type(newVoltage) == float:
            self.__servoVoltage = newVoltage

    def setServoTemp(self, newTemperature):
        if type(newTemperature) == float:
            self.__servoTemp = newTemperature

    def setServoLockStat(self, newLockStat):
        if newLockStat == bool:
            self.__servoLockStat = newLockStat


    # Print Servo Properties
    def printServoProperties(self):
        print("----- Servo '" + self.getServoName() + "' Properties -----\n")
        print("   Id: " + str(self.getServoId()))
        print("   Actual Position: " + str(self.getServoActPos()) + " degrees")
        print("   Target Position: " + str(self.getServoTarPos()) + " degrees")
        print("   Min Angle: " + str(self.getServoMinAngle()) + " degrees")
        print("   Max Angle: " + str(self.getServoMaxAngle()) + " degrees")
        print("   Voltage: " + str(self.getServoVoltage()) + " V")
        print("   Temperature: " + str(self.getServoTemp()) + " oC")
        print("   Lock Status: " + str(self.getServoLockStat()) + " - [False = Locked | True = Unlocked]")
        print("\n")


    # Complex Actions
    def flipServoLock(self):
        self.setServoLockStat(self.getServoLockStat() ^ 0b1)


# Describes position of the arm at a given moment as a series of polar coordinates (radius, angle)
class armPosition:

    # Initialize
    def __init__(self, hipObj = object, shoulderObj = object, 
    upperElbowObj = object, lowerElbowObj = object, wristObj = object, 
    handObj = object):

        self.__hipTarAngle = hipObj.getServoTarPos()
        self.__shoulderTarAngle = shoulderObj.getServoTarPos()
        self.__upperElbowTarAngle = upperElbowObj.getServoTarPos()
        self.__lowerElbowTarAngle = lowerElbowObj.getServoTarPos()
        self.__wristTarAngle = wristObj.getServoTarPos()
        self.__handTarAngle = handObj.getServoTarPos()

    def getTarPosArray(self):
        return [self.__hipTarAngle, self.__shoulderTarAngle, self.__upperElbowTarAngle, 
        self.__lowerElbowTarAngle, self.__wristTarAngle, self.__handTarAngle]


# under init func., add the various lengths of each component as is necessary
# also, under generateDefaultArmConfig, add a header for [CONSTANTS]
# find a way to call the angle measurement from different objects of servoProperties to populate arm position angles
#   Solution: literally just pass object to armPosition lol