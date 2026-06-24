#!/usr/bin/env python

# Problema I/O-bound: gera um arquivo de log grande simulando eventos
# de um sistema (uma escrita por linha, sem buffer manual), depois le
# o arquivo linha a linha e agrega estatisticas por tipo de evento e
# por nivel de severidade. Estressa I/O sequencial de leitura/escrita.

import os
import random

LOG_FILE = "dados/eventos.log"

TIPOS_EVENTO = ["LOGIN", "LOGOUT", "ERRO_REDE", "TIMEOUT", "REQUISICAO_API", "CACHE_MISS"]
NIVEIS = ["INFO", "WARNING", "ERROR", "CRITICAL"]


def gerar_log_se_necessario(path, num_linhas=20000, semente=2024):
    if os.path.exists(path):
        return

    random.seed(semente)
    os.makedirs(os.path.dirname(path), exist_ok=True)

    with open(path, "w", encoding="utf-8") as f:
        for i in range(num_linhas):
            timestamp = 1_700_000_000 + i
            tipo = random.choice(TIPOS_EVENTO)
            nivel = random.choices(NIVEIS, weights=[60, 25, 10, 5])[0]
            duracao_ms = random.randint(1, 5000)
            f.write(f"{timestamp}|{nivel}|{tipo}|duracao_ms={duracao_ms}\n")


def processar_log(path):
    contagem_por_tipo = {}
    contagem_por_nivel = {}
    duracao_total_por_tipo = {}
    total_linhas = 0

    with open(path, "r", encoding="utf-8") as f:
        for linha in f:
            linha = linha.strip()
            if not linha:
                continue

            total_linhas += 1
            partes = linha.split("|")
            nivel = partes[1]
            tipo = partes[2]
            duracao_ms = int(partes[3].split("=")[1])

            contagem_por_tipo[tipo] = contagem_por_tipo.get(tipo, 0) + 1
            contagem_por_nivel[nivel] = contagem_por_nivel.get(nivel, 0) + 1
            duracao_total_por_tipo[tipo] = duracao_total_por_tipo.get(tipo, 0) + duracao_ms

    return total_linhas, contagem_por_tipo, contagem_por_nivel, duracao_total_por_tipo


def main():
    gerar_log_se_necessario(LOG_FILE)

    total_linhas, contagem_tipo, contagem_nivel, duracao_total = processar_log(LOG_FILE)

    print(f"Total de eventos processados: {total_linhas}")

    print("\nEventos por tipo:")
    for tipo in sorted(contagem_tipo, key=lambda t: contagem_tipo[t], reverse=True):
        media_duracao = duracao_total[tipo] / contagem_tipo[tipo]
        print(f"  {tipo}: {contagem_tipo[tipo]} ocorrencias, duracao media={media_duracao:.1f}ms")

    print("\nEventos por nivel de severidade:")
    for nivel in sorted(contagem_nivel, key=lambda n: contagem_nivel[n], reverse=True):
        percentual = (contagem_nivel[nivel] / total_linhas) * 100
        print(f"  {nivel}: {contagem_nivel[nivel]} ocorrencias ({percentual:.1f} por cento)")

    # Limpeza para nao acumular entre execucoes
    os.remove(LOG_FILE)


if __name__ == "__main__":
    main()
