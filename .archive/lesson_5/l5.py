from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, InfraredSensor, TouchSensor, ColorSensor
from pybricks.parameters import Port
from pybricks.robotics import DriveBase
from pybricks.tools import wait

from bc import ITFReader

ev3 = EV3Brick()

left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

robot = DriveBase(
    left_motor=left_motor,
    right_motor=right_motor,
    wheel_diameter=42.12,
    axle_track=105
)

color_sensor = ColorSensor(Port.S2)

def task_0():
    while True:
        print('Reflection:', color_sensor.reflection())
        print('Color:', color_sensor.color())
        print('Ambient:', color_sensor.ambient())
        print('RGB:', color_sensor.rgb())
        print('------------------')
        wait(1_000)


black, white = 6, 86

def task_1():
    """Follow line zigzag"""
    turn = 40
    v = 30

    thresh = (black + white) / 2
    while True:
        if color_sensor.reflection() > thresh:
            robot.drive(v, turn)
        else:
            robot.drive(v, -turn)
        wait(10)


def task_2():
    """Follow line smooth"""
    max_turn = 70
    v = 30
    thresh = (black + white) / 2

    while True:
        r = color_sensor.reflection()
        t = (r - thresh) / (thresh-black) * max_turn
        robot.drive(v, t)
        print(t)
        wait(10)


def task_3():
    """Barcode reader"""
    digits_to_read = 2

    reader = ITFReader(10, 20)

    code_length = 140
    thresh = (black + white) / 2

    robot.drive(35, 0)

    dists = []
    v0 = False
    while sum(dists) + robot.distance() < code_length:
        r = color_sensor.reflection()
        b = (r - thresh) < 0
        if b is not v0:
            print(b, robot.distance(), sum(dists))
            if not dists:
                dists.append(0)
            else:
                dists.append(robot.distance())
            robot.reset()
            v0 = b
        wait(10)
    dists.append(robot.distance())
    print('Measured distances:', dists)
    n = reader.read(dists[1:])
    print('Identified number:', n)
    ev3.speaker.say(str(n))

## 03 20 17 18
#  2017 03 18



if __name__ == '__main__':
    import sys
    globals()['task_' + sys.argv[1]]()