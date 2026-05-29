import time
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def run():
    x = [1, 2, 3, 4, 3, 4, 2, 4, 5, 4, 5, 3, 5, 2, 4]
    plt.figure(figsize=(8, 6))
    plt.hist(x, bins=5, color='mediumseagreen', edgecolor='black', alpha=0.8, label='Densidade de Ocorrências')
    plt.title('Distribuição de Frequência (Histograma)', fontsize=14, fontweight='bold', pad=15)
    plt.xlabel('Valores do Conjunto', fontsize=12)
    plt.ylabel('Número de Ocorrências', fontsize=12)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.legend()
    plt.savefig('resultados/imagens/histograma.png', bbox_inches='tight')
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
