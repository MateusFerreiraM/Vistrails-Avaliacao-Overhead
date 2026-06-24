#!/usr/bin/env python

# Problema CPU-bound: implementa o Crivo de Eratostenes para encontrar
# todos os primos at um limite grande, e em seguida usa esses primos
# para fatorar uma serie de numeros compostos grandes. Operacao
# puramente computacional, sem I/O.


def crivo_eratostenes(limite):
    eh_primo = [True] * (limite + 1)
    eh_primo[0] = eh_primo[1] = False

    for n in range(2, int(limite ** 0.5) + 1):
        if eh_primo[n]:
            for multiplo in range(n * n, limite + 1, n):
                eh_primo[multiplo] = False

    return [n for n in range(2, limite + 1) if eh_primo[n]]


def fatorar(numero, lista_primos):
    fatores = []
    resto = numero

    for primo in lista_primos:
        if primo * primo > resto:
            break
        while resto - (resto // primo) * primo == 0:  # equivalente ao operador modulo
            fatores.append(primo)
            resto //= primo

    if resto > 1:
        fatores.append(resto)

    return fatores


def gerar_numeros_para_fatorar(quantidade, base):
    # Gera numeros compostos grandes de forma deterministica
    return [base + i * 97 + i * i for i in range(quantidade)]


def main():
    limite_crivo = 200_000
    primos = crivo_eratostenes(limite_crivo)

    print(f"Limite do crivo: {limite_crivo}")
    print(f"Quantidade de primos encontrados: {len(primos)}")
    print(f"Maior primo encontrado: {primos[-1]}")

    numeros_para_fatorar = gerar_numeros_para_fatorar(quantidade=15, base=10_000_000)

    print("\nFatoracao de numeros grandes:")
    for numero in numeros_para_fatorar:
        fatores = fatorar(numero, primos)
        fatores_str = " x ".join(str(f) for f in fatores)
        print(f"  {numero} = {fatores_str}")


if __name__ == "__main__":
    main()
