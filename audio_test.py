import pyaudio
import numpy as np
import wave
import sys
import math
import random
from scipy import signal
"""
A square sine wave may be the best way to achieve the robotic noise that you are looking for.
Starting from ~100 hertz and moving to the thousands. Each new wave creates a tone and I will
have to figure out how automatically create a tone or assign a tone to each value in an array

ADSR may not be necessary
The frequency at the stream is different than when making the sine wave.
Look into sweeping for the final analysis
Sweep poly and chirp from scipy may act as alternatives
"""

# p = pyaudio.PyAudio()
# chunk = 1024
#
# if len(sys.argv) < 2:
#     print("Plays a wave file. \n\nUsage: %s filename.wav" % sys.argv[0])
#     sys.exit(-1)
#
# wf = wave.open(sys.argv[1], 'rb')
#
#
# stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
#                 channels=wf.getnchannels(),
#                 rate=wf.getframerate(),
#                 output=True)
#
# data = wf.readframes(chunk)
#
# while len(data) > 0:
#     stream.write(data)
#     data = wf.readframes(chunk)
#
# stream.stop_stream()
# stream.close()
# p.terminate()


# better attempt
# volume = 0.5
# fs = 44100
# duration = 1.0
# freq = 200
# FORMAT = pyaudio.paFloat32
# # FORMAT = pyaudio.paInt16
#
# samples = (np.sin(2*np.pi*np.arange(fs*duration)*freq/fs)).astype(np.float32)
# # print(samples)
#
# stream = p.open(format=FORMAT,
#                 channels=2,
#                 rate=fs,
#                 output=True)
#
# stream.write(samples)
# stream.stop_stream()
# stream.close()
# p.terminate()


def sine(frequency, length, rate):
    length = int(length * rate)
    # 22050 = 0.5 * 44100
    factor = float(frequency) * (math.pi * 2) / rate
    # 0.02137137 = 150 * 2pi/44100
    # np.arange(length) creates an array with length of LENGTH (22050)
    # return np.sin(np.arange(length) * factor)
    # return signal.sawtooth(np.arange(length)*factor)
    t = np.arange(length)*factor
    return signal.square(t)


# duration = 0.1
# sample_freq = 10000
# freq = 120
# duty_cycle = 0.5
# freq = (10, 1000, 50)
# duration = (0.1, 0.5, 0.1)
# duty_cycle = (0.1, 0.9, 0.01)
# sample_freq = 10000
# t = np.arange(0, duration, 1 / sample_freq)
# s = signal.square(2 * math.pi * freq * t, duty=duty_cycle)


def play_tone(stream, frequency=150, length=0.25, rate=44100):
    count = 0
    # frequencies = list(range(0, 1250, 10))
    # random.shuffle(frequencies)
    for frequency in range(0, 1250, 10):
    # for frequency in frequencies:
        count += 1
        print(count)
        chunks = list()
        chunks.append(sine(frequency, length, rate))
        # print(chunks)
        chunk = np.concatenate(chunks) * 0.25
        # print(chunk)
        stream.write(chunk.astype(np.float32).tobytes())


if __name__ == '__main__':
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paFloat32,
                    channels=1,
                    rate=66150,
                    output=1)

    play_tone(stream)

    stream.close()
    p.terminate()
