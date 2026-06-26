# Library of functions relating to handling servo data and robot positioning

# Copyright 2026, 2026 Sam Wang
# This file is part of my Mechanical Arm Project
# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
# You should have received a copy of the GNU General Public License along with this program. If not, see <https://www.gnu.org/licenses/>.


# Define new class for all servo properties. This is an ADT to store the
# given servo's name, angle position, current draw, etc.
class servoProperties:

    def __init__(self, name: str, idNum: int, targetAnglePosition: int, actualAnglePosition: int, 
    voltage: float, temp: float, maxAngle: int, minAngle: int):

        # Define all values for each servo
        self.servoName = name
        self.servoId = idNum

        self.servoActualPosition = targetAnglePosition     # targetAnglePosition is the desired angle at any given moment
        self.servoTargetPosition = actualAnglePosition     # actualAnglePosition is the angle specified by servo feedback, compared against target
        self.servoMaxAngle = maxAngle
        self.servoMinAngle = minAngle

        self.servoVoltage = voltage
        self.servoTemp = temp