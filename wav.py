
from pydub import AudioSegment
from scipy.io import wavfile as wav
import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft
import random
import matplotlib.pyplot as plt


def stereo_to_mono(d):
    '''Converts a stereo MP3 to a mono one, for easier analysis'''
    return d.sum(axis=1) / 2


class WAV_file():

    def __init__(self, address, track):
        '''Extracts the audio data from the specified audio file, and converts it to mono'''
        self.file_address = address
        self.track = track
        if address[-3:] == 'mp3':
            sound = AudioSegment.from_mp3(address)
            self.file_address = address[:-3] + 'wav'
            sound.export(self.file_address, format="wav")
        self.rate, self.aud_data = wav.read(self.file_address)
        self.aud_data = stereo_to_mono(self.aud_data)

    def fourier_transform(self, sample_size):
        '''Performs a Fourier analysis on the audio data, calculates the absolute value of the transform
        (to remove the imaginary part of the result), and normalises it.'''
        self.raw_transformed = np.array(list(fft(self.aud_data))[0::len(list(fft(self.aud_data)))//sample_size])
        if len(self.raw_transformed)>sample_size:
            self.raw_transformed = self.raw_transformed[:sample_size]
        self.absolute_tranformed = abs(self.raw_transformed)
        self.normalised_transformed = [float(i)/sum(self.absolute_tranformed) for i in self.absolute_tranformed]

    def get_raw_transformed(self):
        '''Returns the raw Fourier data'''
        return self.raw_transformed

    def get_absolute_transformed(self):
        '''Returns the absolute values of the Fourier data'''
        return self.absolute_tranformed

    def get_normalised_transformed(self):
        '''Returns the normalised form of the Fourier data'''
        return self.normalised_transformed

    def plot(self):
        '''Plots the Fourier data on a matplotlib graph'''
        plt.plot(self.normalised_transformed)
        return True

    def save(self):
        '''Saves the normalised Fourier data to a text file'''
        with open("./fouriers/{}.txt".format(self.track), "w") as text_file:
            for i in self.normalised_transformed:
                text_file.write(str(i)+'\n')
