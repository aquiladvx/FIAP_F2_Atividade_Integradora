import pandas as pd

def bubble_sort_por_parametro(lista: list, parametro: str, reverso: bool = False) -> list:
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if reverso:
                condicao = lista[j][parametro] < lista[j + 1][parametro]
            else:
                condicao = lista[j][parametro] > lista[j + 1][parametro]

            if condicao:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

    return lista

def busca_por_prioridade(lista: list, prioridade: str) -> list:
    resposta = []
    for item in lista:
        if item["prioridade"] == prioridade:
            resposta.append(item)

    return resposta

def carregar_dados(caminho: str) -> list:
    df = pd.read_csv(caminho)
    return df.to_dict(orient="records")
