from RobotArm import RobotArm
# Let op: hier start het anders voor een random level:
robotArm = RobotArm()
robotArm.randomLevel(1,7)

# Jouw python instructies zet je vanaf hier:

rounds = 0
while True:
    robotArm.grab()
    scan = robotArm.scan()
    if scan != "":
        rounds += 1
        for x in range(0,rounds):
            robotArm.moveRight()
        robotArm.drop()
        for x in range(0,rounds):
            robotArm.moveLeft()
    else:
        break

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()