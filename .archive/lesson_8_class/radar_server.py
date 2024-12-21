import socket

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, InfraredSensor
from pybricks.parameters import Port


ev3 = EV3Brick()

motor = Motor(Port.A)
dist_sensor  = InfraredSensor(Port.S1)

def main():
    s = socket.socket()
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind( ('0.0.0.0', 8000) )
    s.listen(1)
    print('Running')
    while True:
        cl, addr = s.accept()
        print('Connection accepted from {a}'.format(a=addr))
        while True:
            line = cl.readline()
            if not line:
                break
            deg = int(line)
            
            motor.track_target(deg)
            dist = dist_sensor.distance()            
            response = '{}\n'.format(dist)
            cl.send(response)
        cl.close()



main()




