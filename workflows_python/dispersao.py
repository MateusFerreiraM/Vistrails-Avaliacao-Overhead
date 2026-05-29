import time
from math import pi
import numpy.random as random
import matplotlib.pyplot as plt

def run():
    N = 30
    X = 0.9 * random.rand(N)
    Y = 0.9 * random.rand(N)
    s = pi * (10 * random.rand(N))**2
    plt.scatter(X, Y, s=s, c='r', marker='o')
    plt.savefig('resultados/imagens/dispersao.png')
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
