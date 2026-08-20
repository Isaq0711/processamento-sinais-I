
import numpy as np
import matplotlib.pyplot as plt

fs = 44100
T = 5

frequencias = [500, 5000, 10000]

t = np.arange(0, T, 1/fs)

for f in frequencias:
    x = np.cos(2 * np.pi * f * t)

    plt.figure(figsize=(10, 4))
    plt.plot(t, x)
    plt.title(f'Sinal cossenoidal - {f} Hz')
    plt.xlabel('Tempo (s)')
    plt.ylabel('Amplitude')
    plt.grid()
    plt.xlim(0, 0.01)
    plt.show()
