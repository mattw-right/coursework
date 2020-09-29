
from pydub import AudioSegment
from scipy.io import wavfile as wav
import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft
import random
import matplotlib.pyplot as plt


def stereo_to_mono(d):
    return d.sum(axis=1) / 2


class WAV_file():

    def __init__(self, address, track):
        self.file_address = address
        self.track = track
        if address[-3:] == 'mp3':
            sound = AudioSegment.from_mp3(address)
            self.file_address = address[:-3] + 'wav'
            sound.export(self.file_address, format="wav")
        self.rate, self.aud_data = wav.read(self.file_address)
        self.aud_data = stereo_to_mono(self.aud_data)

    def fourier_transform(self, sample_size):
        self.raw_transformed = np.array(list(fft(self.aud_data))[0::len(list(fft(self.aud_data)))//sample_size])
        if len(self.raw_transformed)>sample_size:
            self.raw_transformed = self.raw_transformed[:sample_size]
        self.absolute_tranformed = abs(self.raw_transformed)
        self.normalised_transformed = [float(i)/sum(self.absolute_tranformed) for i in self.absolute_tranformed]

    def get_raw_transformed(self):
        return self.raw_transformed

    def get_absolute_transformed(self):
        return self.absolute_tranformed

    def get_normalised_transformed(self):
        return self.normalised_transformed

    def plot(self):
        plt.plot(self.normalised_transformed)
        return True

    def save(self):
        with open("./fouriers/{}.txt".format(self.track), "w") as text_file:
            for i in self.normalised_transformed:
                text_file.write(str(i)+'\n')
