import configparser
from . import servoPositioningLib as sPos

# Initialize Configs

config = configparser.ConfigParser()

config.read('scripts/configs/inis/armConfig.ini')


def initializeHip():
    servoHip = sPos.servoProperties(
        config['HIP']['Name'],
        int(config['HIP']['IDNum']),

        float(config['HIP']['ServoTargetPosition']),
        1.75, # Actual Angle Position -> Replace with data from serial read

        float(config['HIP']['ServoMinPosition']),
        float(config['HIP']['ServoMaxPosition']),

        11.1, # Servo Voltage -> Replace with data from serial read
        27.3, # Servo Temp -> Replace with data from serial read

        config['HIP'].getboolean('ServoLockStatus'),
    )

    return servoHip