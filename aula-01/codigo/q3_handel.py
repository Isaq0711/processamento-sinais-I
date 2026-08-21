fs, x_handel = ler_wav("handel.wav")
t = np.arange(len(x_handel)) / fs
plotar_tempo(t, x_handel, titulo=f"Sinal handel.wav (fs = {fs} Hz)")

print("fs original:"); tocar(x_handel, fs)
print("2×fs:");         tocar(x_handel, 2*fs)
print("4×fs:");         tocar(x_handel, 4*fs)

freqs_h, mag_h = calcular_espectro(x_handel, fs)
plotar_espectro(freqs_h, mag_h, titulo="Espectro — handel.wav", xlim=(0, fs/2))

_, cos_500 = gerar_cosseno(500, 5, fs)
freqs_c, mag_c = calcular_espectro(cos_500, fs)
plotar_espectro(freqs_c, mag_c, titulo="Espectro — cosseno puro de 500 Hz")

_, chirp_lin = gerar_chirp(500, 10000, 5, fs, "linear")
freqs_ch, mag_ch = calcular_espectro(chirp_lin, fs)
plotar_espectro(freqs_ch, mag_ch, titulo="Espectro — chirp linear 500-10000 Hz", xlim=(0, 12000))
