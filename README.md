# processamento-sinais-I
Repositório contendo os códigos e arquivos utilizados nas aulas
práticas da disciplina de Processamento de Sinais I,
ministrada pelo Prof. Rafael S. Chaves.

## Conteúdo

- Aula 01 — Sinais e Sistemas (sinais cossenoidais, chirps, amostragem
  de áudio, convolução com resposta ao impulso)

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
cd ap1-sinais-sistemas

Antes de executar, disponibilize os arquivos de dados indicados na
seção da aula correspondente (abaixo) na subpasta `dados/`.

Abra o notebook no ambiente de sua preferência (Jupyter Notebook/Lab,
VS Code, Google Colab etc.). No Colab, ou em qualquer ambiente sem
acesso direto ao sistema de arquivos local, use o bloco de upload
comentado na célula de setup (`files.upload()`) para enviar os
arquivos de dados.


## Organização das pastas 
aula-0N/
notebook (ou codigo/) -> células/scripts da atividade
dados/ -> arquivos de entrada fornecidos pelo professor
resultados/ -> figuras/saídas geradas ao rodar o notebook


---

## Aula 01 — Sinais e Sistemas

Geração de sinais cossenoidais e chirps, leitura/reprodução de áudio
em diferentes frequências de amostragem, análise espectral (FFT) e
convolução com resposta ao impulso.

**Pasta:** `ap1-sinais-sistemas/`

**Arquivos de dados necessários** (colocar em
`ap1-sinais-sistemas/dados/`):

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

**Relatório:** `Relatorio_AP1_ProcessamentoSinais_Isaque.docx`
(fundamentação teórica, metodologia e discussão dos resultados).

---

## Resultados

Os resultados apresentados nos relatórios de cada aula podem ser
reproduzidos executando os notebooks disponíveis nas pastas
correspondentes, desde que os arquivos de dados indicados estejam
presentes em `dados/`.

## Autores

Isaque Soares, Guilherme Archanjo e Marcelo Auday
CEFET-RJ
