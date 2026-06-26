import configparser
from . import servoPositioningLib as sPos

# Initialize Configs

config = configparser.ConfigParser()

config.read('scripts/configs/inis/armConfig.ini')


def initializeHip():
    hipServo = sPos.servoProperties(
        config['HIP']['Name'],
        int(config['HIP']['IDNum']),

        float(config['HIP']['ServoTargetPosition']),
        1.75, # Actual Angle Position -> Replace with data from serial read

        float(config['HIP']['ServoMinPosition']),
        float(config['HIP']['ServoMaxPosition']),

        11.6, # Servo Voltage -> Replace with data from serial read
        27.3, # Servo Temp -> Replace with data from serial read

        config['HIP'].getboolean('ServoLockStatus'),
    )
    return hipServo

def initializeShoulder():
    shoulderServo = sPos.servoProperties(
        config['SHOULDER']['Name'],
        int(config['SHOULDER']['IDNum']),

        float(config['SHOULDER']['ServoTargetPosition']),
        24.7, # Actual Angle Position -> Replace with data from serial read

        float(config['SHOULDER']['ServoMinPosition']),
        float(config['SHOULDER']['ServoMaxPosition']),

        11.9, # Servo Voltage -> Replace with data from serial read
        33.3, # Servo Temp -> Replace with data from serial read

        config['SHOULDER'].getboolean('ServoLockStatus'),
    )
    return shoulderServo

def initializeUpperElbow():
    upperElbowServo = sPos.servoProperties(
        config['UPPER ELBOW']['Name'],
        int(config['UPPER ELBOW']['IDNum']),

        float(config['UPPER ELBOW']['ServoTargetPosition']),
        105.6, # Actual Angle Position -> Replace with data from serial read

        float(config['UPPER ELBOW']['ServoMinPosition']),
        float(config['UPPER ELBOW']['ServoMaxPosition']),

        12.5, # Servo Voltage -> Replace with data from serial read
        99.2, # Servo Temp -> Replace with data from serial read

        config['UPPER ELBOW'].getboolean('ServoLockStatus'),
    )
    return upperElbowServo

def initializeLowerElbow():
    lowerElbowServo = sPos.servoProperties(
        config['LOWER ELBOW']['Name'],
        int(config['LOWER ELBOW']['IDNum']),

        float(config['LOWER ELBOW']['ServoTargetPosition']),
        45.8, # Actual Angle Position -> Replace with data from serial read

        float(config['LOWER ELBOW']['ServoMinPosition']),
        float(config['LOWER ELBOW']['ServoMaxPosition']),

        10.4, # Servo Voltage -> Replace with data from serial read
        60.7, # Servo Temp -> Replace with data from serial read

        config['LOWER ELBOW'].getboolean('ServoLockStatus'),
    )
    return lowerElbowServo

def initializeWrist():
    wristServo = sPos.servoProperties(
        config['WRIST']['Name'],
        int(config['WRIST']['IDNum']),

        float(config['WRIST']['ServoTargetPosition']),
        134.5, # Actual Angle Position -> Replace with data from serial read

        float(config['WRIST']['ServoMinPosition']),
        float(config['WRIST']['ServoMaxPosition']),

        10.3, # Servo Voltage -> Replace with data from serial read
        27.0, # Servo Temp -> Replace with data from serial read

        config['WRIST'].getboolean('ServoLockStatus'),
    )
    return wristServo

def initializeHand():
    handServo = sPos.servoProperties(
        config['HAND']['Name'],
        int(config['HAND']['IDNum']),

        float(config['HAND']['ServoTargetPosition']),
        118.3, # Actual Angle Position -> Replace with data from serial read

        float(config['HAND']['ServoMinPosition']),
        float(config['HAND']['ServoMaxPosition']),

        11.5, # Servo Voltage -> Replace with data from serial read
        89.6, # Servo Temp -> Replace with data from serial read

        config['HAND'].getboolean('ServoLockStatus'),
    )
    return handServo
