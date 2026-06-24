#!/usr/bin/env python

# Problema CPU-bound: calculo intensivo de fatoriais grandes (numeros
# enormes, sem limite de precisao) e da sequencia de Fibonacci usando
# memoizacao manual (sem bibliotecas), forcando uso pesado de CPU
# sem qualquer operacao de I/O.

import sys


def fatorial(n):
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado


def fibonacci_memo(n, cache=None):
    if cache is None:
        cache = {}

    if n in cache:
        return cache[n]
    if n <= 1:
        return n

    cache[n] = fibonacci_memo(n - 1, cache) + fibonacci_memo(n - 2, cache)
    return cache[n]


def contar_digitos(numero):
    return len(str(numero))


def main():
    if hasattr(sys, "set_int_max_str_digits"):
        sys.set_int_max_str_digits(2_000_000)  # Permite numeros muito grandes (Python 3.11+)
    sys.setrecursionlimit(10_000)  # Necessario para Fibonacci recursivo com indice grande

    # Calcula uma serie de fatoriais grandes
    fatoriais_calculados = []
    for n in range(100, 1001, 100):
        resultado = fatorial(n)
        fatoriais_calculados.append((n, contar_digitos(resultado)))

    # Calcula Fibonacci para um indice grande, usando memoizacao
    indice_fib = 5000
    cache = {}
    valor_fib = fibonacci_memo(indice_fib, cache)
    digitos_fib = contar_digitos(valor_fib)

    print("Fatoriais calculados (n -> quantidade de digitos do resultado):")
    for n, digitos in fatoriais_calculados:
        print(f"  {n}! possui {digitos} digitos")

    print(f"\nFibonacci({indice_fib}) possui {digitos_fib} digitos")
    print(f"Tamanho do cache de memoizacao utilizado: {len(cache)}")


if __name__ == "__main__":
    main()
