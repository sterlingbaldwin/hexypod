import serial
from time import sleep

START = 500
STOP = 2500


ser = serial.Serial()
ser.port = '/dev/ttyAMA0'
ser.baudrate = 115200
ser.open()
print(ser.is_open)
print(ser.name)

while True:
    try:
        time = 0.5
        msg = b'#0 P{position} T{time} \r'.format(
            position=(START + 50), time=time*1000)
        print('writing {msg}'.format(msg=msg))
        ser.write(msg)
        sleep(time)

        time = 1.0
        msg = b'#0 P{position} T{time} \r'.format(
            position=(STOP - 50), time=time*1000)
        print('writing {msg}'.format(msg=msg))
        ser.write(msg)
        sleep(time)

        time = 0.5
        msg = b'#0 P{position} T{time} \r'.format(
            position=(START + STOP)/2, time=time*1000)
        print('writing {msg}'.format(msg=msg))
        ser.write(msg)
        sleep(time+0.5)
    except KeyboardInterrupt as e:
        ser.close()
        print(ser.is_open)
        break