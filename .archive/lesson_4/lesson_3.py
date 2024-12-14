from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, InfraredSensor, TouchSensor
from pybricks.parameters import Port
from pybricks.robotics import DriveBase
from pybricks.tools import wait

ev3 = EV3Brick()

left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

robot = DriveBase(
    left_motor=left_motor,
    right_motor=right_motor,
    wheel_diameter=42.12,
    axle_track=105
)

def square(l):
    for _ in range(4):
        robot.straight(l)
        robot.turn(90)


def task_1():
    square(100)


def task_2():
    pass


def polygon(n, l):
    for _ in range(n):
        robot.straight(l)
        robot.turn(360/n)


def task_3():
    polygon(6, 100)


def task_4():
    """
    Házikó
    """
    l = 100
    square(l)
    robot.turn(90)
    polygon(3, l)
    robot.turn(-90)


dist_sensor = InfraredSensor(Port.S1)


def task_5():
    thresh = 20
    v = 50  # velocity
    robot.drive(v, 0)  # mm/sec, deg/sec
    while True:
        if dist_sensor.distance() < thresh:
            robot.turn(90)
            robot.straight(100)
            robot.turn(-90)
            robot.drive(v, 0)

        wait(10)

touch_sensor = TouchSensor(Port.S4)

def task_6():
    th = 20
    v = 50

    robot.drive(v, 0)  
    while True:
        if dist_sensor.distance() < th:
            robot.drive(-v, 0)

        if touch_sensor.pressed():
            robot.drive(v, 0)


def task_7():
    """Jedi"""
    th = 20
    v = 50

    robot.drive(v, 0)  
    while True:
        if dist_sensor.distance() < th:
            robot.drive(-v, 0)
        else:
            robot.drive(v, 0)

def task_8():
    d = 30
    v = 200
    while True:
        dist_diff_ratio = (dist_sensor.distance() - d) / d
        # dist_diff_ratio = min((1, dist_diff_ratio))
        if dist_diff_ratio > 1:
            robot.drive(0, 0)
        else:
            robot.drive(v*dist_diff_ratio, 0)
        wait(10)

import threading

def task_9():
    import time

    def count_1():
        c = 0
        while True:
            print('c1', c)
            c += 1
            time.sleep(1)

    def count_2():
        c = 0
        while True:
            print('c2', c)
            c += 1
            time.sleep(1.5)
    
    t1 = threading.Thread(target=count_1)
    # t2 = threading.Thread(target=count_2)
    t1.start()
    # t2.start()
    count_2()
    
def task_10():
    d = 30
    v = 400

    ddr = 1

    def set_ddr():
        nonlocal ddr
        while True:
            ddr = (dist_sensor.distance() - d) / d
            wait(10)

    t = threading.Thread(target=set_ddr)
    t.start()
    

    while True:
        if ddr > 1:
            robot.drive(0, 0)
        else:
            robot.drive(v*ddr, 0)
        wait(10) 


if __name__ == '__main__':
    import sys
    globals()['task_' + sys.argv[1]]()