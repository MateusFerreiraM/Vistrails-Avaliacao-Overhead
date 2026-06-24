#!/usr/bin/env python

# Problema I/O-bound: escreve e le um grande numero de arquivos
# pequenos em disco. Esse padrao estressa o sistema de arquivos
# (muitas chamadas de syscall) em vez da CPU.

import os
import shutil

DIR_TEMP = "dados/io_bound_temp"
NUM_ARQUIVOS = 300
LINHAS_POR_ARQUIVO = 50


def limpar_diretorio(path):
    if os.path.exists(path):
        shutil.rmtree(path)
    os.makedirs(path, exist_ok=True)


def escrever_arquivos(diretorio, quantidade, linhas_por_arquivo):
    for i in range(quantidade):
        caminho = os.path.join(diretorio, f"arquivo_{i:04d}.txt")
        with open(caminho, "w", encoding="utf-8") as f:
            for linha in range(linhas_por_arquivo):
                f.write(f"arquivo={i};linha={linha};valor={i * linha}\n")


def ler_arquivos(diretorio, quantidade):
    total_linhas = 0
    soma_valores = 0

    for i in range(quantidade):
        caminho = os.path.join(diretorio, f"arquivo_{i:04d}.txt")
        with open(caminho, "r", encoding="utf-8") as f:
            for linha in f:
                total_linhas += 1
                partes = linha.strip().split(";")
                valor = int(partes[2].split("=")[1])
                soma_valores += valor

    return total_linhas, soma_valores


def main():
    limpar_diretorio(DIR_TEMP)

    escrever_arquivos(DIR_TEMP, NUM_ARQUIVOS, LINHAS_POR_ARQUIVO)
    total_linhas, soma_valores = ler_arquivos(DIR_TEMP, NUM_ARQUIVOS)

    print(f"Arquivos escritos e lidos: {NUM_ARQUIVOS}")
    print(f"Total de linhas processadas: {total_linhas}")
    print(f"Soma de todos os valores: {soma_valores}")

    # Limpeza final para nao acumular arquivos entre execucoes
    shutil.rmtree(DIR_TEMP)


if __name__ == "__main__":
    main()
