import soundcloud
import random
import sys

# create a client object with your app credentials
client = soundcloud.Client(client_id='283a6af84980b4412fe06e181c3fa6ae')

# fetch track to stream
 #track = client.get('/tracks/293')

tracks_list = None 

genres_list = ["ambient", "country", "folk", "pop", "metal", "triphop"]
current_genre_idx = 0

def search(step=None):
    global genres_list
    global current_genre_idx
    global tracks_list
    succeed = False

    if step == "Next":
        current_genre_idx = (1+current_genre_idx) % len(genres_list)
    elif step == "Previous":
        current_genre_idx = (current_genre_idx-1) % len(genres_list)

    print genres_list[current_genre_idx]
    while succeed == False:
        try:
            tracks_list = client.get('/tracks', license='cc-by-sa', genres=genres_list[current_genre_idx])
            succeed == True
        except Exception, e:
            print 'Retry'

def getTrack():
    random_int = random.randint(0,len(tracks_list)-1)
    # find all sounds of buskers licensed under 'creative commons share alike'
    #tracks = client.get('/tracks', license='cc-by-sa', limit=1, offset=random_int)

    track = tracks_list[random_int]

    stream_url = client.get(track.stream_url, allow_redirects=False)
    print track.title
    return stream_url.location


search()