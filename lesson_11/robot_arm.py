
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (
    Motor,
    TouchSensor
)
from pybricks.parameters import Port
from pybricks.tools import wait

ev3 = EV3Brick()

motor_turn = Motor(Port.C)
motor_raise = Motor(Port.B)
motor_grip = Motor(Port.A)

sensor_turn = TouchSensor(Port.S1)
sensor_raise = TouchSensor(Port.S3)

def health_check():
    while True:
        print(sensor_turn.pressed())
        print(sensor_raise.pressed())
        wait(500)

def main():
     health_check()

if __name__ == '__main__':
    main()
