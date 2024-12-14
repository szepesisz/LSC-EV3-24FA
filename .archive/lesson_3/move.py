#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port
from pybricks.robotics import DriveBase


ev3 = EV3Brick()

left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

robot = DriveBase(
    left_motor=left_motor,
    right_motor=right_motor,
    wheel_diameter=42.12,
    axle_track=105
    )

robot.straight(1000)
robot.straight(-500)
robot.turn(180)
robot.straight(500)




