import time
import socket
import itertools

import matplotlib.pyplot as plt
import numpy as np

import requests


radar_url = 'http://192.168.1.180:8000/'

max_d = 60

def radar_data():
    pos = 180
    obj_d = 0.5
    d = {}
    while True:
        for phi in range(360):
            d[phi] = None if phi != pos else obj_d
            yield phi,  d
        pos += np.random.randint(-5, 5)
        obj_d = np.random.randint(0, 5) / 10
        time.sleep(0.1)


def radar_data():
    while True:
        r = requests.get(radar_url)
        d = r.json()
        current = d['current']/180*np.pi
        data = {int(k)/180*np.pi: v if v < max_d else None for k, v in d['data'].items()}
        yield current, data
        time.sleep(0.1)



x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)

# You probably won't need this if you're embedding things in a tkinter plot...
plt.ion()


fig = plt.figure()
ax = fig.add_subplot(111, projection='polar')
#ax = fig.add_subplot(111)
line1, = ax.plot(x, y, 'o') # Returns a tuple of line objects, thus the comma
line2, = ax.plot(np.pi, max_d, 'ro')

ax.set_rlim(0, max_d)




for c, d in radar_data():
    line1.set_xdata(list(d.keys()))
    line1.set_ydata(list(d.values()))

    line2.set_xdata(list(d.keys()))
    _d = [max_d if i == c else None for i in d.keys()]
    line2.set_ydata(_d)

    fig.canvas.draw()
    fig.canvas.flush_events()
