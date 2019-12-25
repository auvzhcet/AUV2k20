import curses
from curses import wrapper
import pigpio
import time

pin_f = 11

thruster_pins = [pin_f]

width_h = 1600
width_l = 1400
thrust = 0

pi = pigpio.pi()
print("Initialisation. Setting pulse width to 1500")
for pin in thruster_pins:
    pi.set_servo_pulsewidth(pin,1500)

button_delay = 0.01

time.sleep(1)

def hold(pins):
    for pin in pins:
        pi.set_servo_pulsewidth(pin,1500)

def motion(key):
    global thrust, thruster_pins

    if key == 'w':
        print("Move")
        pi.set_servo_pulsewidth(pin_f,width_h + thrust)

    elif key == 'q':
        print("Quit")
        hold(thruster_pins)
        time.sleep(1)
        exit()

    elif key == 'h':
        print('Hold')
        hold(thruster_pins)

    elif key == '+':
        if 0 <= thrust < 100:
            thrust += 10
        print('Incresed Thrust To:', thrust)

    elif key == '-':
        if 0 < thrust <= 100:
            thrust -= 10
        print('Decreased Thrust To:', thrust)

    else:
        print('None')
        hold(thruster_pins)

def main(stdscr):
        global thrust, thruster_pins
        print('In the main loop.')
        stdscr.nodelay(True)
        stdscr.clear()

        while True:
            c = stdscr.getch()
            curses.flushinp()

            if c == -1:
                stdscr.clear()
                stdscr.addstr('Thrust is ' + str(thrust) + '\n')
                hold(thruster_pins)

            else:
                stdscr.clear()
                stdscr.addstr('Pressed ' + chr(c) + '\n')
                motion(chr(c))

            time.sleep(0.06)

curses.wrapper(main)
