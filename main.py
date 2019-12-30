import time

from motion import movement

m = movement.Movement()
thrust = 100

thrust_time = int(input("Enter thrust time: "))

m.forward(thrust)
time.sleep(thrust_time)
m.hold()
