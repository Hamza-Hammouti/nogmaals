from RobotArm import RobotArm

robotArm = RobotArm('exercise 4')

# Jouw python instructies zet je vanaf hier:

for x in range(3):
    robotArm.grab()
    for x in range(2):
        robotArm.moveRight()
    robotArm.drop()
    for x in range(2):
        robotArm.moveLeft()
robotArm.moveRight()
robotArm.moveRight()
for x in range(3):
    robotArm.grab()
    for x in range(1):
        robotArm.moveLeft()                   
    robotArm.drop();
    for x in range(1):
        robotArm.moveRight() 

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()