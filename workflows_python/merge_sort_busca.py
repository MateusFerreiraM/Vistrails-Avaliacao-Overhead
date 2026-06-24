#!/usr/bin/env python

# Problema mais complexo: implementacao manual de Merge Sort para
# ordenar uma lista grande, seguida de buscas binarias multiplas
# para validar a ordenacao e medir acertos.

import random


def merge_sort(lista):
    if len(lista) <= 1:
        return lista

    meio = len(lista) // 2
    esquerda = merge_sort(lista[:meio])
    direita = merge_sort(lista[meio:])

    return merge(esquerda, direita)


def merge(esquerda, direita):
    resultado = []
    i = j = 0

    while i < len(esquerda) and j < len(direita):
        if esquerda[i] <= direita[j]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1

    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])
    return resultado


def busca_binaria(lista, alvo):
    inicio, fim = 0, len(lista) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2
        if lista[meio] == alvo:
            return meio
        elif lista[meio] < alvo:
            inicio = meio + 1
        else:
            fim = meio - 1

    return -1


def gerar_lista_aleatoria(tamanho, semente=42):
    random.seed(semente)
    return [random.randint(0, tamanho * 10) for _ in range(tamanho)]


def main():
    tamanho = 5000
    dados = gerar_lista_aleatoria(tamanho)

    dados_ordenados = merge_sort(dados)

    # Confere se a ordenacao esta correta
    ordenado_corretamente = all(
        dados_ordenados[i] <= dados_ordenados[i + 1]
        for i in range(len(dados_ordenados) - 1)
    )

    # Realiza varias buscas binarias: algumas com valores existentes,
    # outras com valores que provavelmente nao existem
    num_buscas = 200
    acertos = 0
    for _ in range(num_buscas):
        alvo = random.choice(dados_ordenados)
        indice = busca_binaria(dados_ordenados, alvo)
        if indice != -1:
            acertos += 1

    print(f"Tamanho da lista: {tamanho}")
    print(f"Ordenacao correta: {ordenado_corretamente}")
    print(f"Buscas realizadas: {num_buscas}")
    print(f"Buscas com sucesso: {acertos}")
    print(f"Menor valor: {dados_ordenados[0]}")
    print(f"Maior valor: {dados_ordenados[-1]}")


if __name__ == "__main__":
    main()
