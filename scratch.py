
from listener_profile import Listener_Profile
import os

l = Listener_Profile({'Perfect Day':'https://p.scdn.co/mp3-preview/a48050121ba5ec0d7ffbc8a54fb7f46b8a0d5e70?cid=3cfe7e53e98a4e8b99785159a125ef91'}, {'Clare de Lune (piano)' : 'https://p.scdn.co/mp3-preview/fd735ecbeebf35e7b41a4192bf20aecfffc64db0?cid=3cfe7e53e98a4e8b99785159a125ef91'})
l.download_tracks()
profile = l.create_listener_profile()

tracks = os.listdir(path='./fouriers/')
fouriers = {}

for i in tracks:
    try:
        fouriers[i] = [float(i) for i in open('./fouriers/' + i).read().split('\n')[:-1]]
    except:
        pass

def fourier_distance(fourier1, fourier2):
    distance = 0
    for i, j in enumerate(fourier1):
        distance += (fourier2[i] - j)**2
    return distance**0.5

recommendations = {}

for i in list(fouriers.keys()):
    recommendations[i] = fourier_distance(profile, fouriers[i])

import operator

recommendations = sorted(recommendations.items(), key=operator.itemgetter(1))

print(recommendations)
