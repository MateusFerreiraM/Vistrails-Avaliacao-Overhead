#!/usr/bin/env python

# Problema simples: geracao de dados em memoria e escrita (IO) em
# um arquivo CSV, com calculo de estatisticas basicas.

import os
import csv

OUTPUT_FILE = "dados/saida_estatisticas.csv"


def gerar_dados(quantidade=500):
    # Gera uma sequencia de valores simples e deterministicos
    return [(i, i * 2, i * i) for i in range(1, quantidade + 1)]


def calcular_estatisticas(dados):
    coluna_quadrados = [linha[2] for linha in dados]
    total = sum(coluna_quadrados)
    media = total / len(coluna_quadrados)
    maximo = max(coluna_quadrados)
    return total, media, maximo


def escrever_csv(path, dados):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["indice", "dobro", "quadrado"])
        writer.writerows(dados)


def main():
    dados = gerar_dados()
    escrever_csv(OUTPUT_FILE, dados)
    total, media, maximo = calcular_estatisticas(dados)

    print(f"Linhas escritas em {OUTPUT_FILE}: {len(dados)}")
    print(f"Soma dos quadrados: {total}")
    print(f"Media dos quadrados: {media:.2f}")
    print(f"Maior quadrado: {maximo}")


if __name__ == "__main__":
    main()
