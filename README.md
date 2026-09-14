# processamento-sinais-I
Repositório contendo os códigos e arquivos utilizados nas aulas
práticas da disciplina de Processamento de Sinais I,
ministrada pelo Prof. Rafael S. Chaves.

## Conteúdo

- Aula 01 — Sinais e Sistemas (sinais cossenoidais, chirps, amostragem
  de áudio, convolução com resposta ao impulso)
- Aula 02 — Amostragem (análise espectral, subamostragem,
  sobreamostragem, amostragem na frequência de Nyquist e reconstrução)

## Requisitos
Para executar os códigos, são necessários:

- Python 3.10+
- NumPy
- SciPy
- Matplotlib
- Um ambiente com kernel Jupyter/IPython para abrir arquivos `.ipynb`
  (ex.: Jupyter Notebook/Lab, VS Code com a extensão Jupyter, Google
  Colab, Kaggle Notebooks, entre outros)
- IPython (para reprodução de áudio inline via `IPython.display.Audio`)

## Instalação

Clone o repositório: git clone [https://github.com/Isaq0711/processamento-sinais-I] 

Entre na pasta: cd processamento-sinais-I

Instale as dependências:pip install -r requirements.txt

## Como utilizar

Cada aula possui uma pasta própria. Por exemplo, para a Aula 01: 
cd aula-01

Antes de executar, disponibilize os arquivos de dados indicados na
seção da aula correspondente (abaixo) na subpasta `dados/`.

Abra o notebook no ambiente de sua preferência (Jupyter Notebook/Lab,
VS Code, Google Colab etc.). No Colab, ou em qualquer ambiente sem
acesso direto ao sistema de arquivos local, use o bloco de upload
comentado na célula de setup (`files.upload()`) para enviar os
arquivos de dados.


## Organização das pastas 
aula-0N/

codigo -> células/scripts da atividade

dados/ -> arquivos de entrada fornecidos pelo professor

resultados/ -> figuras/saídas geradas ao rodar o notebook


---

## Aula 01 — Sinais e Sistemas

Geração de sinais cossenoidais e chirps, leitura/reprodução de áudio
em diferentes frequências de amostragem, análise espectral (FFT) e
convolução com resposta ao impulso.

**Pasta:** `aula-01`

**Arquivos de dados necessários** (colocar em
`aula-01/dados/`):

- `handel.wav`
- `h_banheiro.wav`
- `sinal_taca.wav`

**Ordem de execução das células** (reaproveitam variáveis entre si):

1. **Setup** — importações e funções utilitárias (`gerar_cosseno`,
   `gerar_chirp`, `ler_wav`, `tocar`, `plotar_tempo`,
   `plotar_espectro`, `calcular_espectro`)
2. **Questão 1** — sinais cossenoidais (500, 5000, 10000 Hz)
3. **Questão 2** — chirps (linear, quadrático, logarítmico)
4. **Questão 3** — leitura, reprodução em fs/2fs/4fs e espectro de
   `handel.wav` (gera `x_handel` e `fs`, usados na Questão 6)
5. **Questão 5** — leitura e reprodução de `h_banheiro.wav` e
   `sinal_taca.wav` (gera `h_banheiro`, `fs_b`, `sinal_taca`, `fs_t`,
   usados na Questão 6)
6. **Questão 6** — convolução dos sinais das Questões 3 e 5 com
   `h_banheiro.wav`, simulando sua propagação no ambiente

A Questão 4 é respondida em texto no relatório (procedimento de
medição da resposta ao impulso de uma sala) e não possui célula de
código associada.

**Saídas:** cada célula exibe o gráfico correspondente diretamente
como saída (`plt.show()`) e, quando aplicável, um player de áudio
inline (`IPython.display.Audio`).

---
## Aula 02 — Amostragem

Análise espectral (via `calculate_spectrum()`) de sinais cossenoidais,
chirps e de áudio real; subamostragem e sobreamostragem (implementação
própria vs. `scipy.signal.resample()`); amostragem exatamente na
frequência de Nyquist e reconstrução por interpolação sinc e por
segurador de ordem zero (ZOH); espectro de sinais convoluídos com a
resposta ao impulso do banheiro.

**Pasta:** `aula-02/`

**Arquivos de dados necessários** (colocar em `aula-02/dados/`):

- `handel.wav`
- `h_banheiro.wav`
- `sinal_taca.wav`

**Ordem de execução das células** (reaproveitam variáveis entre si):

1. **Setup** — importações, funções utilitárias (`gerar_cosseno`,
   `gerar_chirp`, `ler_wav`, `tocar`, `plotar_tempo`) e
   `calculate_spectrum()`
2. **Questão 1** — espectro de cossenoides (500, 5000, 10000,
   50000 Hz)
3. **Questão 2** — espectro de chirps (linear, quadrático,
   logarítmico)
4. **Questão 3** — espectro de `handel.wav` (gera `x_handel` e
   `fs_handel`, usados nas Questões 4–8 e 10)
5. **Questões 4–5** — subamostragem própria (`subamostrar()`) e via
   `scipy.signal.resample()`, para M ∈ {2, 4, 8}
6. **Questões 6–7** — sobreamostragem própria (`sobreamostrar()`) e
   via `scipy.signal.resample()`, para L ∈ {2, 4, 8}
7. **Questão 8** — amostragem de x(t) = cos(2000πt) + sin(5000πt) na
   frequência de Nyquist e reconstrução por interpolação sinc e por
   segurador de ordem zero
8. **Questão 9** — espectro de `h_banheiro.wav` e `sinal_taca.wav`
   (gera `h_banheiro`, `fs_banheiro`, `sinal_taca`, `fs_taca`, usados
   na Questão 10)
9. **Questão 10** — convolução dos sinais das Questões 3 e 9 com
   `h_banheiro.wav` e espectro das respostas

**Saídas:** cada célula exibe o gráfico correspondente diretamente
como saída (`plt.show()`) e, quando aplicável, um player de áudio
inline (`IPython.display.Audio`).

## Resultados

Os resultados apresentados nos relatórios de cada aula podem ser
reproduzidos executando os notebooks disponíveis nas pastas
correspondentes, desde que os arquivos de dados indicados estejam
presentes em `dados/`.

## Autores

Isaque Soares, Guilherme Archanjo e Marcelo Auday

CEFET-RJ
