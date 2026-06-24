#!/usr/bin/env python

# Problema simples: leitura de um arquivo de texto (IO) e contagem
# de frequencia de cada palavra.

import os
from collections import Counter

DATA_FILE = "dados/texto.txt"

TEXTO_BASE = (
    "vistrails python julia performance overhead workflow "
    "pipeline execucao tempo memoria dados experimento "
    "python vistrails workflow analise grafico resultado "
)


def gerar_arquivo_se_necessario(path, repeticoes=200):
    if not os.path.exists(path):
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            for _ in range(repeticoes):
                f.write(TEXTO_BASE + "\n")


def ler_texto(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def contar_palavras(texto):
    palavras = texto.split()
    return Counter(palavras)


def main():
    gerar_arquivo_se_necessario(DATA_FILE)
    texto = ler_texto(DATA_FILE)
    contagem = contar_palavras(texto)

    total_palavras = sum(contagem.values())
    palavra_mais_comum, freq = contagem.most_common(1)[0]

    print(f"Total de palavras lidas: {total_palavras}")
    print(f"Palavra mais frequente: '{palavra_mais_comum}' ({freq} vezes)")


if __name__ == "__main__":
    main()
