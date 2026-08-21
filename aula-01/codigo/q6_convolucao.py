def igualar_fs(x, fs_x, fs_alvo):
    if fs_x == fs_alvo:
        return x
    d = gcd(fs_x, fs_alvo)
    return resample_poly(x, fs_alvo // d, fs_x // d)

def convoluir_e_avaliar(nome, x, fs_x, h, fs_h):
    h_rs = igualar_fs(h, fs_h, fs_x)
    y = fftconvolve(x, h_rs, mode="full")
    y = y / np.max(np.abs(y))
    plotar_tempo(np.arange(len(y))/fs_x, y, titulo=f"y[n] = {nome}[n] * h_banheiro[n]")
    return y, fs_x

y_audio, fs_y_audio = convoluir_e_avaliar("audio", x_handel, fs, h_banheiro, fs_b)
print("Áudio propagado no banheiro:"); tocar(y_audio, fs_y_audio)

y_taca, fs_y_taca = convoluir_e_avaliar("taca", sinal_taca, fs_t, h_banheiro, fs_b)
print("Taça propagada no banheiro:"); tocar(y_taca, fs_y_taca)