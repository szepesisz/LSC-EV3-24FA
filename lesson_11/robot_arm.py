
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

def calibrate():
    motor_turn.run(5)
    while not sensor_turn.pressed():
        wait(50)
    motor_turn.stop()


def main():
    # health_check()
    calibrate()

if __name__ == '__main__':
    main()
