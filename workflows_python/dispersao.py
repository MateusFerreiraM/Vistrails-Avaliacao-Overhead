import time
from math import pi
import numpy.random as random
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def run():
    N = 30
    X = 0.9 * random.rand(N)
    Y = 0.9 * random.rand(N)
    s = pi * (10 * random.rand(N))**2
    plt.figure(figsize=(8, 6))
    plt.scatter(X, Y, s=s, c='crimson', marker='o', alpha=0.6, edgecolors='black', label='Amostras Aleatórias')
    plt.title('Análise de Correlação (Gráfico de Dispersão)', fontsize=14, fontweight='bold', pad=15)
    plt.xlabel('Eixo X (Variavel Aleatória 1)', fontsize=12)
    plt.ylabel('Eixo Y (Variavel Aleatória 2)', fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.legend()
    plt.savefig('resultados/imagens/dispersao.png', bbox_inches='tight')
    plt.close()

if __name__ == '__main__':
    start = time.time()
    try:
        run()
        print(f"RESULTADO_EXECUCAO: SUCESSO")
    except Exception as e:
        print(f"RESULTADO_EXECUCAO: ERRO")
        print(e)
    end = time.time()
    print(f"TEMPO_EXECUCAO_SEGUNDOS: {end - start}")
