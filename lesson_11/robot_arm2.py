
import threading

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (
    Motor,
    TouchSensor
)
from pybricks.parameters import Port, Direction, Button
from pybricks.tools import wait

ev3 = EV3Brick()

motor_turn = Motor(
    port=Port.C,
    positive_direction=Direction.CLOCKWISE,
    # gears=[12, 36]
    )
motor_raise = Motor(Port.B)




def calibrate():
    motor_turn.reset_angle(0)
    motor_raise.reset_angle(0)
    
    motor_turn.run_angle(90, 90)
    motor_raise.run_angle(40, 45)    



def process1():
    while True:
        bl = ev3.buttons.pressed()

        if len(bl) == 0:
            motor_turn.brake()
            motor_raise.brake()
            continue

        if len(bl) != 1:
            continue

        b = bl[0]
        if b == Button.LEFT:
            motor_turn.run(90)
        if b == Button.RIGHT:
            motor_turn.run(-90)

        if b == Button.UP:
            motor_raise.run(-90)
        if b == Button.DOWN:
            motor_raise.run(90)


        wait(20)


def process2():
    v_r = 0
    def control_raise():
        while True:
            motor_raise.run(v_r)
    
    v_t = 0
    def control_turn():
        while True:
            motor_turn.run(v_t)

    t1 = threading.Thread(target=control_raise)
    t2 = threading.Thread(target=control_turn)

    # t1.start()
    # t2.start()

    bl = {
        Button.LEFT: False,
        Button.RIGHT: False,
        Button.UP: False,
        Button.DOWN: False
    }
    v = 180

    while True:
        buttons = ev3.buttons.pressed()
        for b in bl:
            bl[b] = b in buttons

        vt = v * (bl[Button.LEFT] - bl[Button.RIGHT])
        vr = v * (bl[Button.DOWN] - bl[Button.UP])

        motor_turn.run(vt)
        motor_raise.run(vr)

        wait(20)




def main():
    print('Started')
    # health_check()
    # calibrate()
    # process1()
    process2()

if __name__ == '__main__':
    main()
