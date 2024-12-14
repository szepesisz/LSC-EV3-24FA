#!/usr/bin/env pybricks-micropython

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
    axle_track=106
    )

def square(l):
    for _ in range(4):
        robot.straight(l)
        robot.turn(90)

def task_1():
    square(100)


def triangle(l):
    for _ in range(3):
        robot.straight(l)
        robot.turn(120)

def task_2():
    triangle(100)
    

def polygon(n, l=100):
    for _ in range(n):
        robot.straight(l)
        robot.turn(360/n)


def task_3():
    polygon(6)



def task_4():
    l = 100 

    square(l)
    robot.turn(90)
    triangle(l)
    robot.turn(-90)



dist_sensor = InfraredSensor(Port.S1)

def task_5():
    thresh = 20

    robot.drive(50, 0)

    while True:
        # print(dist_sensor.distance())
        if dist_sensor.distance() < thresh:
            robot.turn(90)
            robot.straight(100)
            robot.turn(-90)
            robot.drive(50, 0)

        wait(10)


touch_sensor = TouchSensor(Port.S4)


def task_6():
    robot.drive(50, 0)
    while True:
        if dist_sensor.distance() < 20:
            robot.drive(-50, 0)
        
        if touch_sensor.pressed():
            robot.drive(50, 0)
        wait(10)


def task_7():
    d = 40
    while True:
        if dist_sensor.distance() < d:
            robot.drive(-50, 0)
        else:
            robot.drive(50, 0)
        wait(10)


def task_8():
    while True:
        d = 30
        # dist_diff = min((dist_sensor.distance() - d) / d, 1)

        dist_diff = (dist_sensor.distance() - d) / d

        print(dist_diff)
        if dist_diff > 1:
            robot.drive(0, 0)
        else:
            robot.drive(200 * dist_diff, 0)
        wait(10)


import threading

def task_9():
    d = 30


    dist_diff = 1

    def set_dd():
        nonlocal dist_diff
        while True:
            dist_diff = (dist_sensor.distance() - d) / d
            wait(10)

    t = threading.Thread(target=set_dd)
    t.start()
    
    while True:
        print(dist_diff)
        if dist_diff > 1:
            robot.drive(0, 0)
        else:
            robot.drive(100 * dist_diff, 0)
        wait(10)
        
if __name__ == '__main__':
    import sys
    tn = sys.argv[1]
    globals().get('task_'+str(tn))()