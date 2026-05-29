# Comparação Python Puro vs VisTrails (VisTrailsJL)

Este repositório contém scripts e workflows criados para analisar e comparar o impacto do uso de sistemas de workflow científico (no caso, a reimplementação experimental em Julia, VisTrailsJL) em contrapartida à execução direta ("Python Puro"). O objetivo é avaliar os trade-offs entre a **automação e proveniência** versus o **overhead de execução e memória**.

## Estrutura do Projeto

*   **`workflows_vt/`**: Workflows experimentais construídos com VisTrails (`.vt`).
*   **`workflows_python/`**: Scripts em Python puro contendo a mesma lógica dos workflows, servindo de base de comparação (baseline).
*   **`scripts/`**: Os motores de execução (`executar.py`, `gerar_graficos.py`, `executar_vt.jl`).
*   **`resultados/`**: 
    *   `metricas.csv`: O arquivo contendo os dados brutos de tempo e pico de memória.
    *   `graficos/`: Os gráficos analíticos oficiais gerados.
    *   `imagens/`: Pasta temporária para abrigar imagens de teste geradas pelos códigos avaliados.

## Experimentos Criados

Expandimos a base para avaliar **10 workflows distintos** com complexidades variadas. Os fluxos escolhidos foram batizados com nomenclaturas simplificadas:

1.  **`mdc` (Matemática)**: Cálculo recursivo de Máximo Divisor Comum.
2.  **`pipeline` (Machine Learning)**: Um pipeline rodando classificador SVC (Scikit-Learn).
3.  **`grid_search` (Machine Learning)**: Pipeline efetuando a otimização de parâmetros com GridSearchCV.
4.  **`primos` (Matemática Computacional)**: Pipeline recursivo de busca por números primos.
5.  **`linha` (Visualização 2D)**: Geração de gráficos de linha utilizando o Matplotlib.
6.  **`dispersao` (Visualização 2D)**: Geração de gráfico de dispersão com Matplotlib.
7.  **`barras` (Visualização 2D)**: Gráfico de barras configurado e exibido com Matplotlib.
8.  **`histograma` (Visualização 2D)**: Cálculo e plotagem de um histograma sobre dados estatísticos usando Matplotlib.
9.  **`saidas` (Teste de API I/O)**: Teste de latência básica simulando portas de saídas.
10. **`imagemagick` (Pipeline Estrutural)**: Simula o tráfego final entre um módulo e uma porta de saída.

## Metodologia e Execução

Desenvolvemos um script orquestrador (`scripts/executar.py`) responsável por rodar **10 repetições** de todos os pipelines listados (Python puro em paralelo a `VisTrailsJL`). O orquestrador avalia simultaneamente:
1. O Tempo de Execução Absoluto.
2. O Pico de Memória RAM consumida.

Para executar todos os 200 cenários de teste:
```bash
# Certifique-se de ter os pacotes instalados
pip install scikit-learn matplotlib pandas seaborn psutil

# Dispare o orquestrador e aguarde os resultados
python scripts/executar.py
```

*Os resultados brutos são exportados automaticamente para `resultados/metricas.csv`.*

## Análise de Dados e Conclusão

Após os experimentos serem gerados, a comparação gráfica e analítica pode ser feita chamando o visualizador (que automaticamente remove *outliers* das execuções):

```bash
python scripts/gerar_graficos.py
```

Isso processará o arquivo `.csv` e salvará na pasta `resultados/graficos/` as análises finais de tempo (em escalas absoluta e logarítmica), overhead percentual, e picos de memória.

### Principais Conclusões

Com os dados coletados ao rodar os pipelines com sucesso, as diferenças entre o motor de workflows e a abstração isolada se tornaram nítidas:

- **Overhead Intrínseco de Compilação/Injeção:** Em tarefas extremamente leves (como `mdc`, `saidas`, ou `primos`), rodar o Python puro é ordens de grandeza mais veloz. O VisTrailsJL obriga a inicialização da máquina de estados, injeção do ambiente, resolução das conexões das portas e a computação, resultando em sobrecarga temporal e de RAM altas.
- **Diluição de Overhead:** Em pipelines com processamento vetorial e renderização pesada (como treinamento no `pipeline` ou montagem gráfica no `dispersao` e `histograma`), a sobrecarga do VisTrailsJL é diluída e quase "escondida" frente à carga computacional.
- **O Trade-off Valioso:** Para experimentos pesados, utilizar a arquitetura do VisTrails vale o pequeno overhead adicional. A capacidade de versionar estados e re-executar sub-partes sem custo se prova superior ao trabalho isolado de construir scripts soltos.
