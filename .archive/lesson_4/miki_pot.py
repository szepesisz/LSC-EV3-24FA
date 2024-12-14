from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (
    Motor, 
    InfraredSensor
)
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

dist_sensor = InfraredSensor(Port.S1)

def task_1():
    robot.drive(50, 0)
    wait(1000)  # pybricks.tools  [ms]


def task_2():
    robot.drive(50, 0)
    while True:
        if dist_sensor.distance() < 20:
            robot.drive(-50, 0)
        else:
            robot.drive(50, 0)
        wait(10)


def task_3():
    """Jedi Smooth"""
    d = 30
    v = 200

    while True:
        dist_diff_n = (dist_sensor.distance() - d) / d
        robot.drive(v * dist_diff_n, 0)
        wait(10)



# task_1()
# task_2()
task_3()
