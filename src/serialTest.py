import serial
from time import sleep
import sys
START = 500
STOP = 2500


ser = serial.Serial()
ser.port = '/dev/ttyAMA0'
ser.baudrate = 115200
ser.open()
print(ser.is_open)
print(ser.name)

position = 999
pos_offset = 0
time = 1.0
channel = 0

msg = b'#{ch} P1000 T{time}\r'.format(
    ch=channel,
    time=time*1000)
print('writing {msg}'.format(msg=msg))
ser.write(msg)
sleep(time)
while True:
    try:
        
        msg = b'#{ch} PO{pos}\r'.format(
            ch=channel,
            pos=pos_offset)
        print('writing {msg}'.format(msg=msg))
        ser.write(msg)
        
        # msg = b'#{ch} P{position} T{time}\r'.format(
        #     ch=channel,
        #     position=(position + pos_offset),
        #     time=time*1000)
        # print('writing {msg}'.format(msg=msg))
        # ser.write(msg)
        # sleep(time+0.5)

        # msg = b'#{ch} P{position} T{time}\r'.format(
        #     position=(position - pos_offset),
        #     time=time*1000,
        #     ch=channel)
        # print('writing {msg}'.format(msg=msg))
        # ser.write(msg)
        # sleep(time+0.5)

        # msg = b'#{ch} P{position} T{time}\r'.format(
        #     position=position,
        #     time=time*1000,
        #     ch=channel)
        # print('writing {msg}'.format(msg=msg))
        # ser.write(msg)

        pos_offset = 100
        i = raw_input()
        if i == 'w':
            pos_offset = 0
            channel += 1
        if i == 's':
            pos_offset = 0
            channel -= 1
        if i == 'q':
            msg = b'\x1b \r'
            print('writing {msg}'.format(msg=msg))
            ser.write(msg)
            sys.exit()
        if i == 'a':
            msg = 'QP{}\r'.format(channel)
            print('writing {msg}'.format(msg=msg))
            ser.reset_input_buffer()
            ser.write(msg)
            sleep(0.01)
            b = ''
            i = ser.in_waiting
            print 'i = ', str(i)
            if i == 1:
                print ord(ser.read(1))
            else:
                print ser.read(i)
            # print b
            
            # print int(format(ord(b), 'b'), 2)

    except KeyboardInterrupt as e:
        ser.close()
        print(ser.is_open)
        break