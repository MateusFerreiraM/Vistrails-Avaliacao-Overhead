#!/usr/bin/env python

# Problema mais complexo: construcao de um grafo nao-direcionado,
# busca em largura (BFS) para caminho mais curto entre dois nos,
# e identificacao de componentes conectados via DFS.

import random
from collections import deque


def gerar_grafo_aleatorio(num_nos, num_arestas, semente=7):
    random.seed(semente)
    grafo = {i: set() for i in range(num_nos)}

    arestas_criadas = 0
    tentativas = 0
    max_tentativas = num_arestas * 10

    while arestas_criadas < num_arestas and tentativas < max_tentativas:
        a = random.randint(0, num_nos - 1)
        b = random.randint(0, num_nos - 1)
        tentativas += 1

        if a != b and b not in grafo[a]:
            grafo[a].add(b)
            grafo[b].add(a)
            arestas_criadas += 1

    return grafo


def bfs_caminho_mais_curto(grafo, origem, destino):
    if origem == destino:
        return [origem]

    visitados = {origem}
    fila = deque([[origem]])

    while fila:
        caminho = fila.popleft()
        no_atual = caminho[-1]

        for vizinho in grafo[no_atual]:
            if vizinho == destino:
                return caminho + [vizinho]
            if vizinho not in visitados:
                visitados.add(vizinho)
                fila.append(caminho + [vizinho])

    return None  # Sem caminho entre origem e destino


def dfs_componente(grafo, no_inicial, visitados):
    pilha = [no_inicial]
    componente = set()

    while pilha:
        atual = pilha.pop()
        if atual not in visitados:
            visitados.add(atual)
            componente.add(atual)
            for vizinho in grafo[atual]:
                if vizinho not in visitados:
                    pilha.append(vizinho)

    return componente


def encontrar_componentes_conectados(grafo):
    visitados = set()
    componentes = []

    for no in grafo:
        if no not in visitados:
            componente = dfs_componente(grafo, no, visitados)
            componentes.append(componente)

    return componentes


def main():
    num_nos = 300
    num_arestas = 400

    grafo = gerar_grafo_aleatorio(num_nos, num_arestas)

    componentes = encontrar_componentes_conectados(grafo)
    maior_componente = max(componentes, key=len)

    origem, destino = 0, num_nos - 1
    caminho = bfs_caminho_mais_curto(grafo, origem, destino)

    print(f"Numero de nos: {num_nos}")
    print(f"Numero de arestas: {num_arestas}")
    print(f"Quantidade de componentes conectados: {len(componentes)}")
    print(f"Tamanho do maior componente: {len(maior_componente)}")

    if caminho:
        print(f"Caminho mais curto entre {origem} e {destino}: {len(caminho) - 1} arestas")
    else:
        print(f"Nao ha caminho entre {origem} e {destino} (nos em componentes diferentes)")


if __name__ == "__main__":
    main()
