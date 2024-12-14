from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port
from pybricks.robotics import DriveBase
from pybricks.tools import wait

from barcode import ITFReader


ev3 = EV3Brick()

left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

robot = DriveBase(
    left_motor=left_motor,
    right_motor=right_motor,
    wheel_diameter=42.12,
    axle_track=105
)

color_sensor =ColorSensor(Port.S2)

white = 84
black = 6

def task_0():
    while True:
        print('Reflection', color_sensor.reflection())
        print('Color', color_sensor.color())
        print('Ambient', color_sensor.ambient())
        print('RGB', color_sensor.rgb())
        wait(1_000)

def task_1():
    """Follow line zigzag""" 
    turn = 40
    v = 30
    thresh = (white + black) /2
    while True:
        if color_sensor.reflection() > thresh:
            robot.drive(v, turn)
        else:
            robot.drive(v, -turn) 
        wait(10)

def task_2():
    """Follow line smooth"""
    max_turn = 90

    v = 30
    
    thresh = (black + white ) / 2
    while True:
        hue = color_sensor.reflection()
        t = ((hue - thresh) / (thresh-black)) * 0.7 * max_turn
        robot.drive(v, t)
        print(t)
        wait(10)



def task_3():
    """Read barcode"""

    r = ITFReader(narrow=10, wide=20)
    
    digits_to_read = 2
    code_length = r.get_length(digits_to_read)
  
    thresh = (black + white ) / 2

    robot.drive(35, 0)

    dists = []
    v0 = False
    while sum(dists)+robot.distance() < code_length:
        hue = color_sensor.reflection()
        b = (hue - thresh) < 0
        if b is not v0:
            print((b, robot.distance(), sum(dists), code_length))
            if not dists:
                dists.append(0)
            else:
                dists.append(robot.distance())
            robot.reset()
            v0 = b
        wait(10)

    dists.append(robot.distance())
    print('Measured distances:', dists)
    robot.drive(0, 0)
    n = r.read(dists[1:])
    print('Identified number:', n)
    ev3.speaker.say(str(n))

def task_4():
    """Simon says"""

if __name__ == '__main__':
    import sys
    task_no = sys.argv[1]
    globals()['task_' + task_no]()