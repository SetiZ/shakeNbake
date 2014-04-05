import sys
import os
import struct
import threading

joy = { 'leftx': 0.0, 'lefty': 0.0, 'rightx': 0.0, 'righty': 0.0, 
        'trig0': False, 'trig1': False, 'trig2': False, 'trig3': False, 
        'buttonup': False, 'buttondown': False, 'buttonleft': False, 'buttonright': False,
        'triangle': False, 'circle': False, 'cross': False, 'square': False, 
        'select': False, 'start': False, 'ps': False}

button_map = {
        "Cross" : 14,
        "Square" : 15

        }

running = 1

class ThreadClass(threading.Thread):
    def run(self):
        global pipe
        global action
        global spacing
        global running

        while 1:
            if(running == 0):
                exit()

            data = pipe.read(8)
            time, value, type, number = struct.unpack('IhBB', data)

            if type & 0x01:
                print "Button ", number


t = ThreadClass()

def init(path):
    global pipe
    global action
    global spacing
    running = 1
    action = []
    spacing = 0
    try:
        pipe = open(path, 'r')
    except:
        return False
    t.start()
    return True

def shutdown():
    global running
    running = 0
    t.join()
