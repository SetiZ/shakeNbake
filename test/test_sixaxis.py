 #! /usr/bin/env python


import shakeNbake
import pprint

shakeNbake.sixaxis.init("/dev/input/js0")
shakeNbake.soundcloud_api.search()
pp = pprint.PrettyPrinter(indent=4)
player = shakeNbake.audio.Player()

allow_next = True
lag = 0
while(1):
    lag += 1
    if shakeNbake.sixaxis.getButton()["ps"] == True:
        shakeNbake.sixaxis.shutdown()
        break
    if shakeNbake.sixaxis.getShake() == True:
        if player.check_state():
            player.setUri(shakeNbake.soundcloud_api.getTrack())
    if shakeNbake.sixaxis.getButton()["cross"] == True:
        if player.check_state():
            player.stop()
        print "Bake"
        player.play()
    if shakeNbake.sixaxis.getButton()["l1"] & allow_next:
        shakeNbake.soundcloud_api.search("Previous")
        allow_next = False
    if shakeNbake.sixaxis.getButton()["r1"] & allow_next:
        shakeNbake.soundcloud_api.search("Next")
        allow_next = False
    if lag % 400000 == 0:
        allow_next = True
    
