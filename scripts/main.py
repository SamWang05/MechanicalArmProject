from lib import servoPositioningLib as sPos

s1 = sPos.servoProperties("Servo One", 1, 0, 0, 11.1, 24.9, 270, 0)
s1.printServoProperties()