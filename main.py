from scripts.lib import initialize as init

servoHip = init.initializeHip()
servoShoulder = init.initializeShoulder()
servoUpperElbow = init.initializeUpperElbow()
servoLowerElbow = init.initializeLowerElbow()
servoWrist = init.initializeWrist()
servoHand = init.initializeHand()

servoHip.printServoProperties()
servoShoulder.printServoProperties()
servoUpperElbow.printServoProperties()
servoLowerElbow.printServoProperties()
servoWrist.printServoProperties()
servoHand.printServoProperties()