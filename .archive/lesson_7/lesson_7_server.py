from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, InfraredSensor, TouchSensor, ColorSensor
from pybricks.parameters import Port
from pybricks.robotics import DriveBase
from pybricks.tools import wait

import socket
import sys

ev3 = EV3Brick()

left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

robot = DriveBase(
    left_motor=left_motor,
    right_motor=right_motor,
    wheel_diameter=42.12,
    axle_track=105
)


def server():
    s = socket.socket()
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind( ('0.0.0.0', 8000) )
    s.listen(1)    
    print('running')
    try:
        while True:
            cl, addr = s.accept()
            print('Connection from ', addr)
            line = cl.readline()
            print(line)
            cl.send('0')
            cl.close()
            speed, turn = line.decode('utf-8').split()
            robot.drive(int(speed), int(turn))

    except KeyboardInterrupt:
        sys.exit(0)
    finally:
        s.close()




def main():
    server()

if __name__ == '__main__':
    main()
