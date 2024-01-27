import soundcard as sc
import numpy
# not working for android.
# is this shit realy installed?
# don't know if working for android or windows. check first.
# you can use numba. just maybe.
# but useless on ARM.
# get a list of all speakers:
# this is shit.
speakers = sc.all_speakers()
print(speakers)
# get the current default speaker on your system:
default_speaker = sc.default_speaker()
# get a list of all microphones:
mics = sc.all_microphones(include_loopback=True,exclude_monitors=False)
print(mics)
# get the current default microphone on your system:
#default_mic = sc.default_microphone()
default_mic=mics[0]

data = default_mic.record(samplerate=48000, numframes=48000*5)
# reshape the thing?
"""data=numpy.linspace(-1000,10000,48000*5)
data=numpy.sin(data)
data=data.tolist()
data=list(zip(data,data))
data=numpy.array(data)"""
print(data)
print("finished record")
#numpy.random.shuffle(data)
# this will generate white noise.
# junk^2 = worse junk
# junk*0 = clear
# no output.
# what the fuck?
# so it makes the sound.
# but how to record that back? get the thing?
default_speaker.play(data/numpy.max(data), samplerate=48000)
#print(data/numpy.max(data))
#print(data.shape)
#print(data)
# nothing there. but still playing?
#check this!
# search for a sound card by substring:
# check all these shits.
