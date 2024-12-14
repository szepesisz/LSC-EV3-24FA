from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port


ev3 = EV3Brick()

test_motor = Motor(Port.B)

test_motor.run_angle(
    rotation_angle=180, 
    speed=360  # 360 deg/sec -> 1 1/sec -> 1 Hz -> 60 rpm
)