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

color_sensor = ColorSensor(Port.S2)

body = """<!DOCTYPE html>
<html>
<body style="background-color:{hex_code};">
<h1>{hex_code}</h1>
<p>{details}</p>
</body>
</html>
"""

def server():
    s = socket.socket()
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind( ('0.0.0.0', 8000) )
    s.listen(1)    
    print('running')
    try:
        while True:
            cl, addr = s.accept()
            print('connection from ', addr)
            while True:
                line = cl.readline()
                print(line)
                if not line or line == b'\r\n':
                    break
            rgb = color_sensor.rgb()
            rgb = [int(255 * (c/100)) for c in rgb]
            print(rgb)
            r, g, b = rgb
            hex_code = "#{:02x}{:02x}{:02x}".format(r,g,b)
            print(rgb)

            response = body.format(hex_code=hex_code, details=rgb)
            print(response)
            cl.send('HTTP/1.0 200 OK\r\ncontent-type: text/html\r\n\r\n')
            cl.send(response)
            cl.close()
    except KeyboardInterrupt:
        sys.exit(0)
    finally:
        s.close()




def main():
    server()

if __name__ == '__main__':
    main()
