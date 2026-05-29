import subprocess
import time
import csv
import os
import re
import sys
import psutil

def run_process_with_metrics(cmd):
    start_time = time.time()
    max_mem = 0
    stdout = ""
    status = "SUCESSO"
    
    import tempfile
    with tempfile.TemporaryFile(mode="w+", encoding="utf-8") as temp_out:
        try:
            p = subprocess.Popen(cmd, stdout=temp_out, stderr=subprocess.STDOUT)
            try:
                pp = psutil.Process(p.pid)
                while p.poll() is None:
                    try:
                        mem = pp.memory_info().rss / (1024 * 1024) # MB
                        if mem > max_mem:
                            max_mem = mem
                    except (psutil.NoSuchProcess, psutil.AccessDenied):
                        pass
                    time.sleep(0.01)
            except psutil.NoSuchProcess:
                pass
            p.wait()
            temp_out.seek(0)
            stdout = temp_out.read()
            if p.returncode != 0:
                status = "ERRO"
                print(f"Error executing {cmd}")
        except Exception as e:
            status = "ERRO"
            print(f"Exception executing {cmd}: {e}")
        
    end_time = time.time()
    wall_time = end_time - start_time
    return wall_time, max_mem, stdout, status

def run_python_baseline(script_path):
    print(f"    Running python {script_path}")
    wall_time, max_mem, stdout, status = run_process_with_metrics(['python', script_path])
    return wall_time, max_mem, status

def run_vistrails_workflow(vt_path):
    print(f"    Running vistrails {vt_path}")
    wall_time, max_mem, stdout, status = run_process_with_metrics(['julia', 'scripts/motor_vistrails_cli.jl', vt_path])
    
    if status == "SUCESSO":
        match_time = re.search(r'TEMPO_EXECUCAO_SEGUNDOS:\s*([0-9.]+)', stdout)
        match_status = re.search(r'RESULTADO_EXECUCAO:\s*([A-Z]+)', stdout)
        
        if match_time and match_status:
            # Substituímos o status pelo do script Julia caso tenha falhado internamente
            final_status = match_status.group(1)
            # Usar o tempo do script Julia
            parsed_time = float(match_time.group(1))
            return parsed_time, max_mem, final_status
        else:
            print(f"Could not parse metrics from {vt_path} output.")
            return wall_time, max_mem, "ERRO_PARSE"
    return wall_time, max_mem, status

def main():
    experiments = [
        ("Matemática: MDC", "workflows_python/matematica_mdc.py", "workflows_vt/matematica_mdc.vt"),
        ("ML: Treinamento Pipeline", "workflows_python/ml_treinamento_pipeline.py", "workflows_vt/ml_treinamento_pipeline.vt"),
        ("ML: Otimização GridSearch", "workflows_python/ml_otimizacao_hiperparametros.py", "workflows_vt/ml_otimizacao_hiperparametros.vt"),
        ("Matemática: Números Primos", "workflows_python/matematica_numeros_primos.py", "workflows_vt/matematica_numeros_primos.vt"),
        ("Gráfico de Linha (Tendência)", "workflows_python/grafico_linha_tendencia.py", "workflows_vt/grafico_linha_tendencia.vt"),
        ("Gráfico de Dispersão", "workflows_python/grafico_dispersao_dados.py", "workflows_vt/grafico_dispersao_dados.vt"),
        ("Gráfico de Barras", "workflows_python/grafico_barras_comparativo.py", "workflows_vt/grafico_barras_comparativo.vt"),
        ("Gráfico Histograma", "workflows_python/grafico_histograma_frequencia.py", "workflows_vt/grafico_histograma_frequencia.vt"),
        ("API: Manipulação Saídas", "workflows_python/api_manipulacao_saidas.py", "workflows_vt/api_manipulacao_saidas.vt"),
        ("API: Processamento Imagem", "workflows_python/api_processamento_imagem.py", "workflows_vt/api_processamento_imagem.vt")
    ]
    
    num_repetitions = 10
    results = []
    
    os.makedirs('resultados', exist_ok=True)
    
    for name, py_path, vt_path in experiments:
        print(f"\n--- Testando Workflow: {name} ---")
        
        for i in range(1, num_repetitions + 1):
            print(f"  [Python] Repeticao {i}/{num_repetitions}...")
            elapsed, max_mem, status = run_python_baseline(py_path)
            results.append([name, "Python", i, elapsed, max_mem, status])
            
        for i in range(1, num_repetitions + 1):
            print(f"  [VisTrails] Repeticao {i}/{num_repetitions}...")
            elapsed, max_mem, status = run_vistrails_workflow(vt_path)
            results.append([name, "VisTrails", i, elapsed, max_mem, status])

    csv_file = 'resultados/metricas_avaliacao_performance.csv'
    with open(csv_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Workflow', 'Ambiente', 'Repeticao', 'Tempo_Segundos', 'Memoria_Pico_MB', 'Status'])
        writer.writerows(results)
        
    print(f"\nExperimentos concluídos! Dados salvos em {csv_file}")

if __name__ == '__main__':
    main()
