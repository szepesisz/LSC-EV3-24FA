
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
    gears=[12, 36]
    )
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
    motor_turn.run(30)
    while not sensor_turn.pressed():
        wait(50)
    motor_turn.hold()
    motor_turn.reset_angle(180)
    motor_turn.run_angle(90)

def manual_control():
    v_grip = 90
    motor_grip.run_until_stalled(v_grip, duty_limit=10)
    motor_grip.run_angle(-v_grip, 90)
    grip_closed = False

    v = 120
    while True:
        pressed = ev3.buttons.pressed()
        if not pressed:
            motor_turn.brake()
            motor_raise.brake()
            continue
        if len(pressed) != 1:
            continue
        b = pressed[0]
        if b == Button.LEFT:
            motor_turn.run(v)
        elif b == Button.RIGHT:
            motor_turn.run(-v)
        elif b == Button.UP:
            motor_raise.run(-v)
        elif b == Button.DOWN:
            motor_raise.run(v)
        elif b == Button.CENTER:
            pass

        wait(20)


def manual_control_2():
    v = 120

    bs = {
        Button.LEFT: False,
        Button.RIGHT: False,
        Button.UP: False,
        Button.DOWN: False
    }

    while True:
        bp = ev3.buttons.pressed()
        for b in bs:
            bs[b] = b in bp

        vt = v * (bs[Button.RIGHT] - bs[Button.LEFT])
        vr = v * (bs[Button.DOWN] - bs[Button.UP])

        motor_turn.run(vt)
        motor_raise.run(vr)




def main():
    """
    Operating the Robot Arm
    """
    # health_check()
    # calibrate()
    # manual_control()
    manual_control_2()

if __name__ == '__main__':
    main()
