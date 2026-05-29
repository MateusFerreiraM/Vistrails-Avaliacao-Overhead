import time
import matplotlib.pyplot as plt

def run():
    x = [1, 2, 3, 4, 3, 4, 2, 4, 5, 4, 5, 3, 5, 2, 4]
    plt.hist(x)
    plt.savefig('resultados/imagens/histograma.png')
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
