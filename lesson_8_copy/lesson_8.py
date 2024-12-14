from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, InfraredSensor, TouchSensor, ColorSensor
from pybricks.parameters import Port
from pybricks.robotics import DriveBase
from pybricks.tools import wait

import socket
import sys
import threading
import json
import itertools
import time
import copy

ev3 = EV3Brick()

left_motor = Motor(Port.A)


dist_sensor = InfraredSensor(Port.S1)

DATA = {
    'data': {},
    'current': 0
}

def turn():
    while True:
        for d in itertools.chain(range(0, 180), range(180, 0, -1)):
            left_motor.track_target(d)
            DATA['data'][str(d)] = dist_sensor.distance()
            DATA['current'] = d
            wait(10)


def turn_to_deg(d):
    left_motor.track_target(d)
    return dist_sensor.distance()



def server():
    s = socket.socket()
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind( ('0.0.0.0', 8000) )
    s.listen(1)    
    print('running')
    data = {}
    try:
        while True:
            cl, addr = s.accept()

            while True:
                line = cl.readline()
                if not line:
                    break
                d = turn_to_deg(int(line))

                response = '%s\n' % int(d)
                # cl.send('HTTP/1.0 200 OK\r\nContent-type: application/json\r\n\r\n')
                cl.send(response)
            cl.close()
    except KeyboardInterrupt:
        sys.exit(0)
    finally:
        s.close()




def main():
    # t1 = threading.Thread(target=turn)
    # t1.start()
    server()

if __name__ == '__main__':
    main()
