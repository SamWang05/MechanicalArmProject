from lib import servoPositioningLib as sPos
from lib import armPositioningLib as aPos

s1 = sPos.servoProperties("servo one", 1, 0.0, 0.0, 0.0, 270.0, 11.1, 24.9, 0)
s1.printServoProperties()


s1.setServoName("Servo One")
s1.setServoId(2)
s1.setServoActPos(1.0)
s1.setServoTarPos(1.2)
s1.setServoVoltage(12.6)
s1.setServoTemp(25.7)
s1.flipServoLock()

s1.printServoProperties()