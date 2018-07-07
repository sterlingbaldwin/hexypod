import sys, os
from servocontroller import ServoController, servo_position

channel_pos = {
    '0': {
        'start': 600,
        'stop': 1600
    }
}

def calibrate(SerialController):
    inputval = raw_input()
    pos = servo_position['start'] + 200
    channel = 0
    time = 1000
    SerialController.write(channel, pos, time)
    while True:
        val = raw_input()
        if val == 'w':
            channel += 1
            pos = servo_position['start'] + 500
        elif val == 's':
            channel -= 1
            pos = servo_position['start'] + 500
        elif val == 'd':
            pos += 100
        elif val == 'a':
            pos -= 100
        SerialController.write(channel, pos, time)


if __name__ == "__main__":
    sc = ServoController()

    if not sc.is_open():
        print "Serial connection failed"
        sys.exit(1)
    
    calibrate(sc)
    