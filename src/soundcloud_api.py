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
            succeed = True
        except Exception, e:
            print 'Retry'

def getTrack():
    random_int = random.randint(0,len(tracks_list)-1)
    # find all sounds of buskers licensed under 'creative commons share alike'
    #tracks = client.get('/tracks', license='cc-by-sa', limit=1, offset=random_int)

    track = tracks_list[random_int]

    try:
        stream_url = client.get(track.stream_url, allow_redirects=False)
    except Exception, e:
        print "Get track error, default track "
        return "https://soundcloud.hs.llnwd.net/43Jmlyo2Tmi3.128.mp3?AWSAccessKeyId=AKIAJ4IAZE5EOI7PA7VQ&Expires=1396778878&Signature=Z3BHM9fUUwzLaU9o3LuQ7%2BMi%2BUE%3D&e=1396778878&h=7d995790c40f722608d7c997c7380b8c"
    print track.title
    return stream_url.location


search()
