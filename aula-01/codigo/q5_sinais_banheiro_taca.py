fs_b, h_banheiro = ler_wav("h_banheiro.wav")
fs_t, sinal_taca = ler_wav("sinal_taca.wav")

plotar_tempo(np.arange(len(h_banheiro))/fs_b, h_banheiro, titulo=f"h_banheiro.wav (fs = {fs_b} Hz)")
plotar_tempo(np.arange(len(sinal_taca))/fs_t, sinal_taca, titulo=f"sinal_taca.wav (fs = {fs_t} Hz)")

print("h_banheiro.wav:"); tocar(h_banheiro, fs_b)
print("sinal_taca.wav:"); tocar(sinal_taca, fs_t)