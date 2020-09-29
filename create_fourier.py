

import requests
from wav import WAV_file

def create_fourier(track, url, sample_size=1000):
    '''Performs a Fourier analysis of the MP3 file, sample size
    (the number of data points of the track it analyses) defaulting to 1000'''
    r = requests.get(url+'.mp3')
    with open('./mp3s/{}.mp3'.format(track.replace(' ', '')), "wb") as file:
        file.write(r.content)
    w = WAV_file('./mp3s/{}.mp3'.format(track.replace(' ', '')), track)
    w.fourier_transform(sample_size)
    w.save()
    return True
