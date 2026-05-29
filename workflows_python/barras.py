import time
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def run():
    height = [2,5,7]
    left = [3,5,4]
    plt.figure(figsize=(8, 6))
    plt.bar(left, height, color='skyblue', edgecolor='black', label='Frequência por Categoria')
    plt.title('Distribuição Categórica (Gráfico de Barras)', fontsize=14, fontweight='bold', pad=15)
    plt.xlabel('Categoria', fontsize=12)
    plt.ylabel('Altura / Valor', fontsize=12)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.legend()
    plt.savefig('resultados/subprodutos_descartaveis/barras.png', bbox_inches='tight')
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
