import serial
import asyncio
from time import sleep

class ServoController(object):
    """
    Control a Veyron 24 channel servo controller over serial connection
    """
    def __init__(self, port='/dev/ttyAMA0', baudrate=115200, channels=24):
        """
        Initialize the connection with the controller
        
        Parameters:
            port (str): the serial port name
            baudrate (int): the speed of the serial connection
            channels (int): the number of servo channels to control
        """
        self.ser = serial.Serial()
        self.port = port
        self.baudrate = baudrate
        self.ser.port = self.port
        self.ser.baudrate = self.baudrate
        self.channels = channels

        try:
            self.ser.open()
            if not self.ser.is_open:
                raise Exception('Unable to open serial port at {}'.format(self.port))
        except Exception as e:
            raise e

    def gotoOffset(self, channel, offset):
        msg = '#{} PO{}\r'.format(channel, offset)
        msg = msg.encode('ascii')
        print(msg)
        self.ser.write(msg)

    def goToPos(self, channel, pos, time):
        msg = '#{} P{} T{}\r'.format(channel, pos, time)
        msg = msg.encode('ascii')
        print(msg)
        self.ser.write(msg)
        self.ser.flush()
    
    def moveWait(self):
        ret = ''
        while ret != '.':
            msg = 'Q'.encode('ascii')
            self.ser.reset_input_buffer()
            self.ser.write(msg)
            while self.ser.in_waiting == 0:
                sleep(0.01)
    
    def _move_wait(self):
        pass


    def getPos(self, channel):
        loop = asyncio.get_event_loop()
        pos = loop.run_until_complete(self._get_pos(channel))
        _, pos = pos.split(':')
        pos = pos.split('u')[0]
        return int(pos)

    @asyncio.coroutine
    def _get_pos(self, channel):
        self.ser.reset_input_buffer()
        msg = 'QP{}\r'.format(channel+1)
        msg = msg.encode('ascii')
        print(msg)
        self.ser.write(msg)
        while self.ser.in_waiting == 0:
            sleep(0.01)
        return str(self.ser.read(self.ser.in_waiting))

    def close(self):
        self.ser.close()

    def is_open(self):
        return self.ser.is_open
