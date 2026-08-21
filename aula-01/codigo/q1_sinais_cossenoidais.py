FS, DURACAO, FREQUENCIAS = 44100, 5, [500, 5000, 10000]
JANELA_PLOT = 0.01  # s

sinais_q1 = {}
for f in FREQUENCIAS:
    t, x = gerar_cosseno(f, DURACAO, FS)
    sinais_q1[f] = (t, x)
    n_j = int(JANELA_PLOT * FS)
    plotar_tempo(t[:n_j]*1000, x[:n_j],
                 titulo=f"Sinal cossenoidal — f = {f} Hz (janela de 10 ms)",
                 xlabel="Tempo (ms)")

for f, (_, x) in sinais_q1.items():
    print(f"Sinal cossenoidal de {f} Hz:")
    tocar(x, FS)
