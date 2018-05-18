import wave
import struct
from scipy import *
from pylab import *
import matplotlib.pyplot as plt


def readwav(wavefile):
    wavedata = zeros(wavefile.getnframes())
    for i in range(wavefile.getnframes()):
        val = wavefile.readframes(1)
        left = val[0:2]
        v = struct.unpack('h', left)[0]  # only one digit
        wavedata[i] = v
    return wavedata


filename_005mixture = '005mixture.wav'
filename_005s_voice = '005mixture_voice.wav'
filename_005_vocals = '005vocals.wav'

wavefile_005mixture = wave.open(filename_005mixture, 'r')

nchannels_mixture = wavefile_005mixture.getnchannels()
frame_rate_mixture = wavefile_005mixture.getframerate()
num_frames_mixture = wavefile_005mixture.getnframes()

print("framerate:", frame_rate_mixture)

mix005 = readwav(wavefile_005mixture)

wavefile_005s_voice = wave.open(filename_005s_voice, 'r')
voice005 = readwav(wavefile_005s_voice)

wavefile_005_vocals = wave.open(filename_005_vocals, 'r')
vocals005 = readwav(wavefile_005_vocals)


filename_049mixture = '049mixture.wav'
filename_049s_voice = '049mixture_voice.wav'
filename_049_vocals = '049vocals.wav'

wavefile_049mixture = wave.open(filename_049mixture, 'r')
wavefile_049s_voice = wave.open(filename_049s_voice, 'r')
wavefile_049_vocals = wave.open(filename_049_vocals, 'r')

mix049 = readwav(wavefile_049mixture)
voice049 = readwav(wavefile_049s_voice)
vocals049 = readwav(wavefile_049_vocals)

filename_055mixture = '055mixture.wav'
filename_055s_voice = '055mixture_voice.wav'
filename_055_vocals = '055vocals.wav'

wavefile_055mixture = wave.open(filename_055mixture, 'r')
wavefile_055s_voice = wave.open(filename_055s_voice, 'r')
wavefile_055_vocals = wave.open(filename_055_vocals, 'r')

mix055 = readwav(wavefile_055mixture)
voice055 = readwav(wavefile_055s_voice)
vocals055 = readwav(wavefile_055_vocals)



plt.figure(1)
specgram(mix005, NFFT=2048, Fs=wavefile_005mixture.getnframes(), noverlap=900)

plt.figure(2)
plt.subplot(211)
specgram(voice005, NFFT=2048, Fs=wavefile_005s_voice.getnframes(), noverlap=900)
plt.subplot(212)
specgram(vocals005, NFFT=2048, Fs=wavefile_005_vocals.getnframes(), noverlap=900)
show()

plt.figure(1)
specgram(mix049, NFFT=2048, Fs=wavefile_049mixture.getnframes(), noverlap=900)
plt.figure(2)
plt.subplot(211)
specgram(voice049, NFFT=2048, Fs=wavefile_049s_voice.getnframes(), noverlap=900)
plt.subplot(212)
specgram(vocals049, NFFT=2048, Fs=wavefile_049_vocals.getnframes(), noverlap=900)
show()

plt.figure(1)
specgram(mix055, NFFT=2048, Fs=wavefile_055mixture.getnframes(), noverlap=900)
plt.figure(2)
plt.subplot(211)
specgram(voice055, NFFT=2048, Fs=wavefile_055s_voice.getnframes(), noverlap=900)
plt.subplot(212)
specgram(vocals055, NFFT=2048, Fs=wavefile_055_vocals.getnframes(), noverlap=900)
show()
