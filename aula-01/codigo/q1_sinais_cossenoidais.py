import numpy as np
import matplotlib.pyplot as plt

fs = 44100
T = 5
frequencias = [500, 5000, 10000]
t = np.arange(0, T, 1/fs)

for f in frequencias:
    x = np.cos(2 * np.pi * f * t)

    plt.figure(figsize=(8, 3))
    plt.plot(t * 1000, x)  # Tempo em milissegundos (ms) facilita a leitura
    plt.title(f'Sinal cossenoidal - {f} Hz')
    plt.xlabel('Tempo (ms)')
    plt.ylabel('Amplitude')
    plt.grid(True)
    
    # Exibe 5 períodos exatos para qualquer frequência
    plt.xlim(0, (5 / f) * 1000) 
    plt.show()
