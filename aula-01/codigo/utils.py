import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.signal import chirp as scipy_chirp, fftconvolve, resample_poly
from math import gcd
from IPython.display import Audio, display
import os

PASTA_DADOS = "dados"


def gerar_cosseno(f, duracao, fs):
    t = np.arange(0, duracao, 1/fs)
    return t, np.cos(2*np.pi*f*t)

def gerar_chirp(f0, f1, duracao, fs, metodo="linear"):
    t = np.arange(0, duracao, 1/fs)
    return t, scipy_chirp(t, f0=f0, f1=f1, t1=duracao, method=metodo)

def ler_wav(nome_arquivo):
    fs, x = wavfile.read(os.path.join(PASTA_DADOS, nome_arquivo))
    if x.ndim > 1:
        x = x[:, 0]
    if np.issubdtype(x.dtype, np.integer):
        x = x.astype(np.float64) / np.iinfo(x.dtype).max
    else:
        x = x.astype(np.float64)
    return fs, x

def tocar(x, fs):
    display(Audio(x, rate=fs))

def plotar_tempo(t, x, titulo, xlim=None, xlabel="Tempo (s)"):
    plt.figure(figsize=(7, 3.5))
    plt.plot(t, x, linewidth=0.8)
    plt.xlabel(xlabel); plt.ylabel("Amplitude"); plt.title(titulo)
    plt.grid(True, alpha=0.3)
    if xlim is not None:
        plt.xlim(xlim)
    plt.tight_layout()
    plt.show()

def calcular_espectro(x, fs):
    n = len(x)
    X = np.fft.rfft(x)
    freqs = np.fft.rfftfreq(n, d=1/fs)
    return freqs, np.abs(X) / n

def plotar_espectro(freqs, mag, titulo, xlim=None, escala_db=True):
    plt.figure(figsize=(7, 3.5))
    mag_plot = 20*np.log10(mag + 1e-12) if escala_db else mag
    plt.plot(freqs, mag_plot, linewidth=0.8)
    plt.xlabel("Frequência (Hz)")
    plt.ylabel("Magnitude (dB)" if escala_db else "Magnitude")
    plt.title(titulo)
    plt.grid(True, alpha=0.3)
    if xlim is not None:
        plt.xlim(xlim)
    plt.tight_layout()
    plt.show()