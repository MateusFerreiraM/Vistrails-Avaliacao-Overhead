#!/usr/bin/env python

# Problema simples: soma de duas matrizes NxN geradas em memoria.

def gerar_matriz(n, valor_base):
    return [[valor_base + i + j for j in range(n)] for i in range(n)]


def somar_matrizes(a, b):
    n = len(a)
    resultado = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            resultado[i][j] = a[i][j] + b[i][j]
    return resultado


def main():
    n = 100
    a = gerar_matriz(n, 1)
    b = gerar_matriz(n, 2)
    resultado = somar_matrizes(a, b)

    soma_total = sum(sum(linha) for linha in resultado)
    print(f"Tamanho da matriz: {n}x{n}")
    print(f"Soma total de todos os elementos resultantes: {soma_total}")


if __name__ == "__main__":
    main()
