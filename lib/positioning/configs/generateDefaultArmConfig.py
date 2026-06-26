# Library of functions relating to serial connection between Rasp. Pi and Bus Servo Driver Board

# Copyright 2026, 2026 Sam Wang
# This file is part of my Mechanical Arm Project
# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
# You should have received a copy of the GNU General Public License along with this program. If not, see <https://www.gnu.org/licenses/>.

import configparser

config = configparser.ConfigParser()


# Assuming 6-Servo Arm:
# Note that all servo min/max positions are pseudo-hardware-dependent and should not be changed

config['CONSTANTS'] = {
    'ShoulderToUpperElbowLen': 161.6,
    'UElbowToLElbowLen': 139.1,
    'LElbowToWristLen': 146.0,
    'WristToHandLen': 86.45,
}

config['HIP'] = {
    'Name': 'Hip',
    'IDNum': '1',

    'ServoTargetPosition': 135,
    'ServoMinPosition': 1,
    'ServoMaxPosition': 269,

    'ServoLockStatus': 0,
}

config['SHOULDER'] = {
    'Name': 'Shoulder',
    'IDNum': '2',

    'ServoTargetPosition': 67.5,
    'ServoMinPosition': 1,
    'ServoMaxPosition': 269,

    'ServoLockStatus': 0,
}

config['UPPER ELBOW'] = {
    'Name': 'ElbowUpper',
    'IDNum': '3',

    'ServoTargetPosition': 135,
    'ServoMinPosition': 1,
    'ServoMaxPosition': 269,

    'ServoLockStatus': 0,
}

config['LOWER ELBOW'] = {
    'Name': 'ElbowLower',
    'IDNum': '4',

    'ServoTargetPosition': 135,
    'ServoMinPosition': 1,
    'ServoMaxPosition': 269,

    'ServoLockStatus': 0,
}

config['WRIST'] = {
    'Name': 'Wrist',
    'IDNum': '5',

    'ServoTargetPosition': 135,
    'ServoMinPosition': 1,
    'ServoMaxPosition': 269,

    'ServoLockStatus': 0,
}

config['HAND'] = {
    'Name': 'Hand',
    'IDNum': '6',

    'ServoTargetPosition': 135,
    'ServoMinPosition': 1,
    'ServoMaxPosition': 269,

    'ServoLockStatus': 0,
}


# Generate config file
with open('inis/armConfig.ini', 'w') as configfile:
  config.write(configfile)