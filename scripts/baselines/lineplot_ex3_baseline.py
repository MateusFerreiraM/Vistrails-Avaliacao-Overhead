import time
import matplotlib.pyplot as plt

def run():
    x = [1, 2, 3, 4]
    y = [20, 21, 20.5, 20.8]
    plt.plot(x, y)
    plt.savefig('lineplot_ex3_baseline.png')
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
