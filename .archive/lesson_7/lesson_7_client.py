import socket

import keyboard

state = {
    'w': False,
    'a': False,
    's': False,
    'd': False
}


def send(v, t):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect( ('192.168.0.78', 8000) )
        s.sendall(f'{v} {t}\n'.encode('utf-8'))
        data = s.recv(1024)
        print(data)
        pass

def handle(k):
    if k.name not in state:
        return

    et = k.event_type == keyboard.KEY_DOWN
    
    if state[k.name] == et:
        return

    state[k.name] = et
    print(state)

    v = 100 * (state['w'] - state['s']) 
    t = 100 * (state['d'] - state['a'])

    send(v, t)


def main():
    keyboard.hook(handle)
    input()


main()
