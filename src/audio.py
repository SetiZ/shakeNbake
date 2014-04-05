import pygst
pygst.require("0.10")
import gst

class Player(object):
    def __init__(self):
        self.music_stream_uri = "https://ec-media.soundcloud.com/pfr6pW44eSLy.128.mp3?f10880d39085a94a0418a7ef69b03d522cd6dfee9399eeb9a525089a68f9b73f53532ea7531d94cb4a4ed251148ea758b1bcbbf24a01a4180284692cf3413c971854ff4c1b&AWSAccessKeyId=AKIAJ4IAZE5EOI7PA7VQ&Expires=1396719389&Signature=LBHKGSRhelsHJPYXwOMyLn%2FDN%2Bs%3D"
        self.player = gst.element_factory_make("playbin", "player")

    def setUri(self, uri):
        self.music_stream_uri = uri

    def check_state(self):
        if self.player.get_state() != gst.STATE_PLAYING:
            return True
        else:
            return False

    def play(self):
        #set the uri
        self.player.set_property('uri', self.music_stream_uri)
        #start playing
        if self.check_state():
            self.player.set_state(gst.STATE_PLAYING)

    def stop(self):
        self.player.set_state(gst.STATE_NULL)

