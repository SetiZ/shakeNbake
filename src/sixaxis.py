import sys
import os
import time
import struct
import threading

button_map = [
        "select" ,
        "l3" ,
        "r3" ,
        "start" ,
        "up" ,
        "right" ,
        "down" ,
        "left" ,
        "l2" ,
        "r2" ,
        "l1" ,
        "r1" ,
        "triangle" ,
        "round" ,
        "cross" ,
        "square" ,
        "ps" 
        ]

button_pressed = {
        "select" : False,
        "l3" : False,
        "r3" : False,
        "start" : False,
        "up" : False,
        "right" : False,
        "down" : False,
        "left" : False,
        "l2" : False,
        "r2" : False,
        "l1" : False,
        "r1" : False,
        "triangle" : False,
        "round" : False,
        "cross" : False,
        "square" : False,
        "ps" : False
        }

axis_map = {}

running = 1

class ThreadClass(threading.Thread):
    def run(self):
        global pipe
        global action
        global spacing
        global button_pressed
        global button_map
        global running

        while 1:
            if(running == 0):
                exit()

            data = pipe.read(8)
            timestamp, value, type, number = struct.unpack('IhBB', data)

            if type & 0x01:
                if value == 1:
                    button_pressed[button_map[number]] = True
                elif value == 0:
                    button_pressed[button_map[number]] = False

            if type & 0x02:
                if number == 1:
                    print "Shake"



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

def getButton():
    global button_pressed
    return button_pressed

def shutdown():
    global running
    running = 0
    t.join()
