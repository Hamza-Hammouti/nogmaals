from RobotArm import RobotArm

robotArm = RobotArm('exercise 9')

# Jouw python instructies zet je vanaf hier:

for x in range(4):
    for y in range(5):
        robotArm.grab()
        for c in range(5):
            robotArm.moveRight()
        robotArm.drop()
        for d in range(5):
            robotArm.moveLeft()
    robotArm.moveRight()
    
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()