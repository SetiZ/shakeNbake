 #! /usr/bin/env python


import shakeNbake
import pprint

shakeNbake.sixaxis.init("/dev/input/js0")
pp = pprint.PrettyPrinter(indent=4)
while(1):
    if shakeNbake.sixaxis.getButton()["ps"] == True:
        shakeNbake.sixaxis.shutdown()
        break
    
