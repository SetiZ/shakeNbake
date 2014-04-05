 #! /usr/bin/env python


import shakeNbake
import pprint

shakeNbake.sixaxis.init("/dev/input/js0")
pp = pprint.PrettyPrinter(indent=4)
player = shakeNbake.audio.Player()

while(1):
    if shakeNbake.sixaxis.getButton()["ps"] == True:
        shakeNbake.sixaxis.shutdown()
        break
    if shakeNbake.sixaxis.getShake() == True:
        player.setUri(shakeNbake.soundcloud_api.getTrack())
    if shakeNbake.sixaxis.getButton()["cross"] == True:
        print "Play!"
        player.play()
    
