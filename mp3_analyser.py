

from pydub import AudioSegment
from scipy.io import wavfile as wav
import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft
import scipy



sound = AudioSegment.from_mp3("jimmy.mp3")
sound.export("jimmy.wav", format="wav")
sound = AudioSegment.from_mp3("bob.mp3")
sound.export("bob.wav", format="wav")


def stereo_to_mono(d):
    return d.sum(axis=1) / 2

rate, aud_data = wav.read('jimmy.wav')
jimmy_data = stereo_to_mono(aud_data)

rate, aud_data = wav.read('bob.wav')
bob_data = stereo_to_mono(aud_data)


#r = np.array(fft(aud_data))
r = np.array(fft(jimmy_data[:10000]))
s = np.array(fft(bob_data[:10000]))

#normalise
r = [float(i)/sum(abs(r)) for i in abs(r)]
s = [float(i)/sum(abs(s)) for i in abs(s)]

plt.plot(r)
plt.plot(s)
plt.show()






#python mp3_analyser.py
