#!/usr/bin/env python

# Problema de geracao de numeros: implementa manualmente um gerador
# de numeros pseudo-aleatorios do tipo LCG (Linear Congruential
# Generator), sem usar o modulo `random` da biblioteca padrao, e
# realiza uma analise estatistica simples da distribuicao gerada.


class GeradorLCG:
    """Gerador Linear Congruencial simples (parametros do glibc rand())."""

    def __init__(self, semente=12345):
        self.estado = semente
        self.a = 1103515245
        self.c = 12345
        self.m = 2 ** 31

    def proximo(self):
        valor = self.a * self.estado + self.c
        self.estado = valor - (valor // self.m) * self.m  # equivalente ao operador modulo
        return self.estado

    def proximo_float(self):
        return self.proximo() / self.m

    def proximo_intervalo(self, minimo, maximo):
        return minimo + int(self.proximo_float() * (maximo - minimo + 1))


def gerar_amostra(gerador, quantidade, minimo, maximo):
    return [gerador.proximo_intervalo(minimo, maximo) for _ in range(quantidade)]


def calcular_distribuicao_por_faixas(amostra, minimo, maximo, num_faixas=10):
    largura_faixa = (maximo - minimo + 1) / num_faixas
    contagem_faixas = [0] * num_faixas

    for valor in amostra:
        indice_faixa = int((valor - minimo) / largura_faixa)
        indice_faixa = min(indice_faixa, num_faixas - 1)
        contagem_faixas[indice_faixa] += 1

    return contagem_faixas


def calcular_media_desvio(amostra):
    n = len(amostra)
    media = sum(amostra) / n
    variancia = sum((x - media) ** 2 for x in amostra) / n
    desvio = variancia ** 0.5
    return media, desvio


def main():
    gerador = GeradorLCG(semente=99991)

    quantidade = 100_000
    minimo, maximo = 1, 1000

    amostra = gerar_amostra(gerador, quantidade, minimo, maximo)
    media, desvio = calcular_media_desvio(amostra)
    distribuicao = calcular_distribuicao_por_faixas(amostra, minimo, maximo, num_faixas=10)

    print(f"Quantidade de numeros gerados: {quantidade}")
    print(f"Intervalo: [{minimo}, {maximo}]")
    print(f"Media: {media:.2f}")
    print(f"Desvio padrao: {desvio:.2f}")
    print("\nDistribuicao por faixas (esperado ~uniforme):")
    largura = (maximo - minimo + 1) / 10
    for i, contagem in enumerate(distribuicao):
        inicio_faixa = int(minimo + i * largura)
        fim_faixa = int(minimo + (i + 1) * largura - 1)
        print(f"  [{inicio_faixa:4d} - {fim_faixa:4d}]: {contagem} ocorrencias")


if __name__ == "__main__":
    main()
