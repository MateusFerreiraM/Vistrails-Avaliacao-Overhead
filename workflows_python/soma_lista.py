#!/usr/bin/env python

# Problema simples: leitura de um arquivo de texto (IO) contendo
# numeros (um por linha) e soma de todos os valores.

import os

DATA_FILE = "dados/numeros.txt"


def gerar_arquivo_se_necessario(path, quantidade=1000):
    """Garante que o arquivo de entrada exista, gerando-o se preciso."""
    if not os.path.exists(path):
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            for i in range(1, quantidade + 1):
                f.write(f"{i}\n")


def ler_numeros(path):
    """Le o arquivo e retorna uma lista de inteiros."""
    numeros = []
    with open(path, "r", encoding="utf-8") as f:
        for linha in f:
            linha = linha.strip()
            if linha:
                numeros.append(int(linha))
    return numeros


def somar(numeros):
    total = 0
    for n in numeros:
        total += n
    return total


def main():
    gerar_arquivo_se_necessario(DATA_FILE)
    numeros = ler_numeros(DATA_FILE)
    total = somar(numeros)
    print(f"Quantidade de numeros lidos: {len(numeros)}")
    print(f"Soma total: {total}")


if __name__ == "__main__":
    main()
