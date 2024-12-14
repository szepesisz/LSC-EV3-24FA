import socket
import time

import keyboard


# EDCP -- EV3 drive controll protocol

HOST = '192.168.1.180'   
PORT = 8000
def send(v, t):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(f'{v} {t}\n'.encode('utf-8'))
        data = s.recv(1024)
        print(data)

# send(100, 0)
state = {
    'w': False,
    'a': False,
    's': False,
    'd': False
}

def handle(k):
    if k.name not in (state.keys()):
        return
    et = k.event_type == keyboard.KEY_DOWN
    if state[k.name] == et:
        return
    state[k.name] = et
    print(state)

    v = state['w'] - state['s']
    t = state['d'] - state['a']
    send(v*100, t*100)

def main():
    keyboard.hook(handle)
    input()

main()