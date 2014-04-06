import soundcloud
import random
import sys

# create a client object with your app credentials
client = soundcloud.Client(client_id='283a6af84980b4412fe06e181c3fa6ae')

# fetch track to stream
 #track = client.get('/tracks/293')

tracks_list = None 

def search():
    global tracks_list
    tracks_list = client.get('/tracks', license='cc-by-sa')

def getTrack():
    random_int = random.randint(0,len(tracks_list)-1)
    # find all sounds of buskers licensed under 'creative commons share alike'
    #tracks = client.get('/tracks', license='cc-by-sa', limit=1, offset=random_int)

    track = tracks_list[random_int]

    stream_url = client.get(track.stream_url, allow_redirects=False)
    print track.title
    return stream_url.location
