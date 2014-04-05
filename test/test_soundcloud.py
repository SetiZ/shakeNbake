import soundcloud
import random

# create a client object with your app credentials
client = soundcloud.Client(client_id='283a6af84980b4412fe06e181c3fa6ae')

# fetch track to stream
 #track = client.get('/tracks/293')

random_int = random.randint(0,1000)
print random_int
# find all sounds of buskers licensed under 'creative commons share alike'
tracks = client.get('/tracks', license='cc-by-sa', limit=1, offset=random_int)

track = tracks[0]

print track.title
stream_url = client.get(track.stream_url, allow_redirects=False)
print stream_url.location

#for track in tracks:
	# get the tracks streaming URL
#	stream_url = client.get(track.stream_url, allow_redirects=False)
#	print track.title
	# print the tracks stream URL
	# print stream_url.location
