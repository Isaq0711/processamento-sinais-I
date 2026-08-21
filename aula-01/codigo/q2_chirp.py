F0, F1 = 500, 10000
METODOS = ["linear", "quadratic", "logarithmic"]
JANELA_PLOT = 0.05

sinais_q2 = {}
for metodo in METODOS:
    t, x = gerar_chirp(F0, F1, DURACAO, FS, metodo=metodo)
    sinais_q2[metodo] = (t, x)
    n_j = int(JANELA_PLOT * FS)
    plotar_tempo(t[:n_j]*1000, x[:n_j],
                 titulo=f"Chirp {metodo} — {F0} Hz a {F1} Hz (primeiros 50 ms)",
                 xlabel="Tempo (ms)")

for metodo, (_, x) in sinais_q2.items():
    print(f"Chirp {metodo}:")
    tocar(x, FS)