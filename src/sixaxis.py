import sys
import os
import time
import struct
import threading
import numpy

button_name = [
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

axis_values = [0, 0, 0, 0, 0, 0, 0]

shake_energy = [0]*100
shake_energy_idx = 0
previous_shake = 0

def computeShakeEnergy():
    global shake_energy
    return sum(shake_energy)/len(shake_energy)

shake = False

running = 1

class ThreadClass(threading.Thread):
    def run(self):
        global pipe
        global action
        global spacing
        global button_pressed
        global button_map
        global running
        global axis_values
        global shake 
        global shake_energy
        global shake_energy_idx
        shake_allowed_time = 0

        while 1:
            if(running == 0):
                exit()

            data = pipe.read(8)
            timestamp, value, type_, id_ = struct.unpack('IhBB', data)

            if type_ & 0x01:
                if value == 1:
                    button_pressed[button_name[id_]] = True
                elif value == 0:
                    button_pressed[button_name[id_]] = False
                    

            if type_ & 0x02:
                if id_ < 7:
                    shake_energy_idx = (shake_energy_idx + 1) % len(shake_energy)
                    shake_energy[shake_energy_idx] = numpy.abs(axis_values[id_] - value)
                    if computeShakeEnergy() > 10000:
                        shake = True
                    else:
                        shake = False
                        
                    axis_values[id_] = value

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

def getShake():
    global shake
    return shake

def shutdown():
    global running
    running = 0
    t.join()
