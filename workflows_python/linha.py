import time
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def run():
    x = [1, 2, 3, 4]
    y = [20, 21, 20.5, 20.8]
    plt.figure(figsize=(8, 6))
    plt.plot(x, y, color='darkorange', marker='o', linestyle='-', linewidth=2, markersize=8, label='Série Histórica')
    plt.title('Evolução Temporal (Gráfico de Linha)', fontsize=14, fontweight='bold', pad=15)
    plt.xlabel('Tempo (Meses)', fontsize=12)
    plt.ylabel('Valor da Ação / Temperatura', fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend()
    plt.savefig('resultados/subprodutos_descartaveis/linha.png', bbox_inches='tight')
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
