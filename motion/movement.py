import time
import pigpio

class Movement:
    def __init__(self):

        self.pi = pigpio.pi()
        
        self.pin_f = 11
        self.pin_b = 12
        self.pin_r = 23
        self.pin_l = 15

        self.THRUSTER_PINS = [self.pin_f, self.pin_b, self.pin_r, self.pin_l]

        print("Initialisation. Setting pulse width to 1500")
        for pin in self.THRUSTER_PINS:
            self.pi.set_servo_pulsewidth(pin, 1500)

        time.sleep(1)

    def forward(self, thrust):
        print('Forward')
        self.pi.set_servo_pulsewidth(self.pin_l, 1500 + thrust)
        self.pi.set_servo_pulsewidth(self.pin_r, 1500 + thrust)

    def backward(self, thrust):
        print('Backward')
        self.pi.set_servo_pulsewidth(self.pin_l, 1500 - thrust)
        self.pi.set_servo_pulsewidth(self.pin_r, 1500 - thrust)

    def left(self, thrust):
        print('Left')
        self.pi.set_servo_pulsewidth(self.pin_l, 1500 - thrust)
        self.pi.set_servo_pulsewidth(self.pin_r, 1500 + thrust)

    def right(self, thrust):
        print('Right')
        self.pi.set_servo_pulsewidth(self.pin_l, 1500 + thrust)
        self.pi.set_servo_pulsewidth(self.pin_r, 1500 - thrust)

    def up(self, thrust):
        print('Up')
        self.pi.set_servo_pulsewidth(self.pin_f, 1500 + thrust)
        self.pi.set_servo_pulsewidth(self.pin_b, 1500 + thrust)

    def down(self, thrust):
        print('Down')
        self.pi.set_servo_pulsewidth(self.pin_f, 1500 - thrust)
        self.pi.set_servo_pulsewidth(self.pin_b, 1500 - thrust)

    def tilt_forward(self, thrust):
        print('Tilt_Forward')
        self.pi.set_servo_pulsewidth(self.pin_f, 1500 - thrust)
        self.pi.set_servo_pulsewidth(self.pin_b, 1500 + thrust)

    def tilt_backward(self, thrust):
        print('Tilt_Backward')
        self.pi.set_servo_pulsewidth(self.pin_f, 1500 + thrust)
        self.pi.set_servo_pulsewidth(self.pin_b, 1500 - thrust)

    def hold(self):
        print('Hold')
        for pin in self.THRUSTER_PINS:
            self.pi.set_servo_pulsewidth(pin, 1500)

    def custom_thrusts(self, thrusts):
        ''' 
        Args:
        thrusts -- A dictionary of pins and their respective thrusts 
        '''

        print('Custom Thrusts')
        for pin, thrust in thrusts.items():
            self.pi.set_servo_pulsewidth(pin, thrust)
