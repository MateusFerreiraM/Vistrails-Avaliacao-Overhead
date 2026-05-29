import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def remove_outliers_and_average(df, value_col):
    # Agrupa por Workflow e Ambiente
    grouped = df.groupby(['Workflow', 'Ambiente'])
    
    cleaned_rows = []
    
    for name, group in grouped:
        # Se tiver mais que 2 itens, remove o min e o max
        if len(group) > 2:
            min_idx = group[value_col].idxmin()
            max_idx = group[value_col].idxmax()
            clean_group = group.drop([min_idx, max_idx])
        else:
            clean_group = group
            
        cleaned_rows.append(clean_group)
        
    return pd.concat(cleaned_rows)

def main():
    csv_file = 'resultados/metricas.csv'
    
    if not os.path.exists(csv_file):
        print(f"Erro")
        return

    os.makedirs('resultados/graficos', exist_ok=True)
    if not os.path.exists(csv_file):
        print(f"Erro: Arquivo {csv_file} não encontrado. Rode run_experiments.py primeiro.")
        return

    df = pd.read_csv(csv_file)
    df_success = df[df['Status'] == 'SUCESSO']
    
    if df_success.empty:
        print("Nenhum experimento completou com sucesso para ser plotado.")
        return

    # Tratamento: Remoção de Outliers
    df_time_clean = remove_outliers_and_average(df_success, 'Tempo_Segundos')
    if 'Memoria_Pico_MB' in df_success.columns:
        df_mem_clean = remove_outliers_and_average(df_success, 'Memoria_Pico_MB')

    sns.set_theme(style="whitegrid", context="talk")
    palette = {'Python': '#1F77B4', 'VisTrails': '#D62728'} 

    # 1. Gráfico de Tempo Médio (após remoção de outliers)
    plt.figure(figsize=(14, 7))
    sns.barplot(
        data=df_time_clean, 
        x='Workflow', 
        y='Tempo_Segundos', 
        hue='Ambiente',
        errorbar='sd',
        capsize=0.1,
        palette=palette,
        edgecolor=".2"
    )
    plt.title('Comparação de Tempo de Execução (Sem Outliers)', fontsize=18, fontweight='bold', pad=20)
    plt.ylabel('Tempo Médio (Segundos)', fontsize=14)
    plt.xlabel('Workflow Avaliado', fontsize=14)
    plt.xticks(rotation=30, ha='right', fontsize=12)
    plt.legend(title='Ambiente')
    plt.savefig('resultados/graficos/tempo_absoluto.png', dpi=300, bbox_inches='tight')
    plt.close()

    # 2. Gráfico de Tempo em Escala Logarítmica
    plt.figure(figsize=(14, 7))
    sns.barplot(
        data=df_time_clean, 
        x='Workflow', 
        y='Tempo_Segundos', 
        hue='Ambiente',
        errorbar='sd',
        capsize=0.1,
        palette=palette,
        edgecolor=".2"
    )
    plt.yscale('log')
    plt.title('Comparação de Tempo de Execução (Escala Logarítmica)', fontsize=18, fontweight='bold', pad=20)
    plt.ylabel('Tempo (Segundos) - Escala Log', fontsize=14)
    plt.xlabel('Workflow Avaliado', fontsize=14)
    plt.xticks(rotation=30, ha='right', fontsize=12)
    plt.legend(title='Ambiente')
    plt.savefig('resultados/graficos/tempo_log.png', dpi=300, bbox_inches='tight')
    plt.close()

    # 3. Gráfico de Overhead Relativo %
    df_mean_time = df_time_clean.groupby(['Workflow', 'Ambiente'])['Tempo_Segundos'].mean().unstack()
    if 'VisTrails' in df_mean_time.columns and 'Python' in df_mean_time.columns:
        # Fórmula oficial do Overhead: ((T_VT - T_Py) / T_Py) * 100
        df_mean_time['Overhead_Perc'] = ((df_mean_time['VisTrails'] - df_mean_time['Python']) / df_mean_time['Python']) * 100
        df_mean_time = df_mean_time.sort_values(by='Overhead_Perc', ascending=False).reset_index()

        plt.figure(figsize=(14, 7))
        sns.barplot(
            data=df_mean_time,
            x='Workflow',
            y='Overhead_Perc',
            color='#FF7F0E',
            edgecolor=".2"
        )
        # Se os valores forem absurdamente altos (como no gcd, onde python é 0.08 e VT é 3.0),
        # usaremos escala log para a porcentagem ou apenas plotamos normal.
        plt.yscale('log')
        plt.title('Overhead Relativo (%) Injetado pelo VisTrails (Escala Log)', fontsize=18, fontweight='bold', pad=20)
        plt.ylabel('Overhead (%)', fontsize=14)
        plt.xlabel('Workflow Avaliado', fontsize=14)
        plt.xticks(rotation=30, ha='right', fontsize=12)
        
        for index, row in df_mean_time.iterrows():
            plt.text(index, row['Overhead_Perc'] * 1.1, f"{row['Overhead_Perc']:.0f}%", color='black', ha="center", fontsize=10)
            
        plt.savefig('resultados/graficos/overhead.png', dpi=300, bbox_inches='tight')
        plt.close()

    # 4. Gráfico de Memória
    if 'Memoria_Pico_MB' in df_success.columns:
        plt.figure(figsize=(14, 7))
        sns.barplot(
            data=df_mem_clean, 
            x='Workflow', 
            y='Memoria_Pico_MB', 
            hue='Ambiente',
            errorbar='sd',
            capsize=0.1,
            palette=palette,
            edgecolor=".2"
        )
        plt.title('Consumo de Memória (Pico RAM em MB)', fontsize=18, fontweight='bold', pad=20)
        plt.ylabel('Memória RAM (MB)', fontsize=14)
        plt.xlabel('Workflow Avaliado', fontsize=14)
        plt.xticks(rotation=30, ha='right', fontsize=12)
        plt.legend(title='Ambiente')
        plt.savefig('resultados/graficos/memoria.png', dpi=300, bbox_inches='tight')
        plt.close()

    print("Gráficos gerados com sucesso na metodologia oficial da apresentação!")

if __name__ == '__main__':
    main()
