from scipy import signal
import matplotlib.pyplot as plt
import numpy as np
import math

length = 0.5
rate = 44100
frequency = 120
length = int(length * rate)
factor = float(frequency) * (math.pi * 2) / rate
# t = np.linspace(0, 4, 400)
# t = np.linspace(-np.pi, np.pi, 201)
t = np.arange(length) * factor

# s = signal.square(t)*(1 - math.exp(-t*0.1))
duration = 0.1
sample_freq = 10000
freq = 120
duty_cycle = 0.5
s = signal.square(2 * math.pi * freq * t, duty=duty_cycle)


# plt.plot(t,2* signal.sawtooth(2 * np.pi * 1 * t,0.5))
# x = np.linspace(-np.pi, np.pi, length)


# plt.plot(x, np.sin(np.arange(length) * factor))
plt.plot(t,s)
plt.xlabel("Time[s]")
plt.ylabel("Amplitude[V]")
plt.title("Signal for sampling")
plt.show()
