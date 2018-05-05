from time import sleep
import serial

servo_position = {
    'start': 500,
    'stop': 2500
}

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
    
    def write(self, channel, pos, time):
        msg = b'#{ch} P{pos} T{time} \r'.format(
            ch=channel, pos=pos, time=time)
        self.ser.write(msg)
    
    def moveToInitialPos(self):
        """
        Blocking call to move all servos to the start position
        """
        msg = ''
        for i in range(self.channels+1):
            msg += ' #{ch} P{pos}'.format(ch=i, pos=servo_position['start'])
        msg += ' T500'
        self.ser.write(msg)
        sleep(0.5)


    def close(self):
        self.moveToInitialPos()
        self.ser.close()
