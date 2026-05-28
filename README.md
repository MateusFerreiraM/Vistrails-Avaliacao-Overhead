# Comparação Python Puro vs VisTrails (VisTrailsJL)

Este repositório contém scripts e workflows criados para analisar e comparar o impacto do uso de sistemas de workflow científico (no caso, a reimplementação experimental em Julia, VisTrailsJL) em contrapartida à execução direta ("Python Puro"). O objetivo é avaliar os trade-offs entre a **automação e proveniência** versus o **overhead de execução**.

## Estrutura do Projeto

*   **`vistrails-python/examples/`**: Workflows experimentais construídos originalmente com VisTrails (`.vt`).
*   **`scripts/`**: Scripts em Python puro contendo a mesma lógica dos workflows, para que as medições de baseline fossem viáveis. Também estão aqui os orquestradores.
*   **`resultados/`**: Dados de saída exportados (`metricas.csv`) e gráficos para análise visual dos tempos de execução.

## Experimentos Criados

Durante o projeto, a pedido da professora, expandimos a base para avaliar **10 workflows distintos** com complexidades variadas. Esses arquivos `.vt` originais se encontram na pasta de exemplos do próprio ecossistema Vistrails e executam com sucesso no VisTrailsJL. Os fluxos escolhidos foram:

1.  **`gcd` (Algoritmo Numérico Simples)**: Cálculo recursivo de Máximo Divisor Comum.
2.  **`pipeline` (Machine Learning com Scikit-Learn)**: Um pipeline rodando classificador SVC (Scikit-Learn).
3.  **`grid_search` (Machine Learning)**: Pipeline efetuando a otimização de parâmetros com GridSearchCV.
4.  **`primes` (Matemática Computacional)**: Pipeline recursivo de busca por números primos.
5.  **`lineplot_ex3` (Visualização 2D)**: Geração de gráficos de linha utilizando o Matplotlib.
6.  **`scatter` (Visualização de Dispersão)**: Geração de gráfico de dispersão com Matplotlib.
7.  **`bar_ex1` (Visualização de Barras)**: Gráfico de barras configurado e exibido com Matplotlib.
8.  **`hist_ex1` (Histograma)**: Cálculo e plotagem de um histograma sobre dados estatísticos usando Matplotlib.
9.  **`outputs` (Teste de API I/O)**: Teste de latência básica simulando portas de saídas, retornando a string de status "Hello, world".
10. **`imagemagick` (Pipeline de Saída Estrutural)**: Simula o tráfego final entre um módulo estrutural (imagemagick) e uma porta de saída do pipeline.

*Nota: Alguns exemplos mais legados contendo integrações descontinuadas ou componentes interativos antigos (como módulos vtk ou webservices complexos) reportaram inconsistência estrutural e foram despriorizados em prol desses 10 exemplos limpos que executam o fluxo com 100% de precisão dentro do interpretador.*

## Fase 2: Executando os Experimentos

Desenvolvemos um script orquestrador (`scripts/run_experiments.py`) responsável por rodar as 3 repetições de todos os pipelines listados (Python puro em paralelo a `VisTrailsJL`), cronometrando e tabulando o tempo de todos eles de maneira automatizada.

Para rodá-lo:
```bash
# Certifique-se de ter os pacotes instalados
pip install scikit-learn matplotlib pandas seaborn

# Dispare o orquestrador e aguarde os resultados
python scripts/run_experiments.py
```

*Os resultados brutos são exportados automaticamente para `resultados/metricas.csv`.*

## Fase 3 e 4: Análise de Dados e Conclusão

Após os experimentos serem gerados, a comparação gráfica e analítica pode ser feita chamando o visualizador:

```bash
python scripts/plot_results.py
```

Isso processará o `metricas.csv` e produzirá gráficos (`grafico_tempo_medio.png` e `grafico_boxplot.png`) demonstrando as disparidades de execução.

### Principais Conclusões

Com os dados coletados ao rodar os 10 pipelines com sucesso, as diferenças entre o motor de workflows (VisTrailsJL) e a abstração isolada ("Python Puro") se tornaram nítidas:

- **Overhead Intrínseco de Compilação/Injeção:** Em tarefas extremamentes leves (como `gcd`, `outputs`, ou `primes`), rodar o Python puro é ordens de grandeza mais veloz. O VisTrailsJL obriga a inicialização da máquina de estados em Julia, injeção do ambiente via `PyCall`, resolução das conexões das portas (Action Replay) e, por fim, a computação, resultando em sobrecarga temporal alta.
- **Diluição de Overhead:** Em pipelines com maior uso de I/O, processamento vetorial e renderização pesada (como treinamento de ML no `pipeline` ou montagem gráfica no `scatter` e `hist_ex1`), a sobrecarga do VisTrailsJL é quase "escondida". A proporção de tempo gasto fazendo o setup do fluxo visual frente ao tempo bruto usado pela própria biblioteca de Machine Learning cai assustadoramente, tornando o VisTrails uma opção fantástica.
- **O Trade-off Valioso:** Para experimentos duradouros e pipelines robustos, utilizar a arquitetura de proveniência do VisTrails vale o overhead inicial. A capacidade de versionar estados, auditar os resultados passados e re-executar sub-partes sem custo manual se provou superior ao trabalho isolado de construir scripts soltos em Python puro.
