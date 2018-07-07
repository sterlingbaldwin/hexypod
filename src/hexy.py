import sys
from time import sleep
from servocontroller import ServoController


class Hexy(object):
    """
    Your friendly neighborhood spiderbot man!
    """

    def __init__(self):
        self.controller = ServoController()

    def servoCalibate(self):
        """
        Calibrate start/stop/middle for each legs 3 servos
        
        d -> move to next servo
        a -> move to previous servo
        w -> go to pos + 500
        s -> go to pos - 500
        ' ' -> go to pos 1000
        """
        servo = 0
        pos = 1000
        while True:
            cmd = input("cmd>>")
            if cmd == 'd': 
                servo += 1
                pos = self.controller.getPos(servo)
                msg = 'servo: {srv}, pos: {pos}'.format(srv=str(servo), pos=str(pos))
                print(msg)
            elif cmd == 'a':
                servo -= 1
                pos = self.controller.getPos(servo)
                msg = 'servo: {srv}, pos: {pos}'.format(srv=str(servo), pos=str(pos))
                print(msg)
            elif cmd == 'w':
                time = 500
                self.controller.goToPos(servo, pos + 50, time)
                sleep(time/1000.0)
                pos = self.controller.getPos(servo)
                msg = 'servo: {srv}, pos: {pos}'.format(srv=str(servo), pos=str(pos))
                print(msg)
            elif cmd == 's':
                time = 500
                self.controller.goToPos(servo, pos - 50, time)
                sleep(time/1000.0)
                pos = self.controller.getPos(servo)
                msg = 'servo: {srv}, pos: {pos}'.format(srv=str(servo), pos=str(pos))
                print(msg)
            elif cmd == ' ':
                pos = 1000
                time = 1000
                self.controller.goToPos(servo, pos, time)
                sleep(time/1000.0)
                pos = self.controller.getPos(servo)
                msg = 'servo: {srv}, pos: {pos}'.format(srv=str(servo), pos=str(pos))
                print(msg)
            elif cmd == 'i':
                pos = self.controller.getPos(servo)
                msg = 'servo: {srv}, pos: {pos}'.format(srv=str(servo), pos=str(pos))
                print(msg)
            elif cmd == 'q':
                sys.exit()

if __name__== "__main__":
    hexy = Hexy()
    hexy.servoCalibate()
