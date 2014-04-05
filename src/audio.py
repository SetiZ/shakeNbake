import pygst
pygst.require("0.10")
import gst

class Player(object):
    def __init__(self):
        self.music_stream_uri = ""
        self.player = gst.element_factory_make("playbin", "player")

    def setUri(self, uri):
        self.music_stream_uri = uri

    def play(self):
        #set the uri
        self.player.set_property('uri', self.music_stream_uri)
        print "Playing ", self.music_stream_uri
        #start playing
        self.player.set_state(gst.STATE_PLAYING)

    def stop(self):
        pass

