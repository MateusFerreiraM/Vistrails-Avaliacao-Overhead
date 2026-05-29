import time
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def run():
    height = [2,5,7]
    left = [3,5,4]
    plt.bar(left, height)
    plt.savefig('resultados/imagens/barras.png')
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
