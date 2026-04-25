import pandas as pd

import time

limites = {
    "combustivel": 30
}

constantes_pouso = {
    "taxa_consumo_base": 1.2,
    "coeficiente_escala": 0.001,
}

dados_modulos_df = pd.read_csv("data.csv")
dados_modulos = dados_modulos_df.to_dict(orient="records")

def busca_por_prioridade(lista: list, prioridade: str) -> list:
    resposta = []
    for item in lista:
        if item["prioridade"] == prioridade:
            resposta.append(item)

    return resposta

def ordena_por_eta(lista: list) -> list:
    return bubble_sort_por_parametro(lista, "eta_orbita_min")

def ordena_por_combustivel(lista: list) -> list:
    return bubble_sort_por_parametro(lista, "combustivel")

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

def verifica_autorizacao_pouso(modulo: dict) -> bool:
    return modulo["combustivel"] >= limites["combustivel"]

def pousa_modulo(modulo: dict):
    print(f"Pousando módulo {modulo['id']}...")
    time.sleep(0.5)
    print("Módulo pousado com sucesso!")
    time.sleep(0.5)

def ordena_modulos(lista: list) -> list:
    modulos_alta = busca_por_prioridade(lista, "Alta")
    modulos_media = busca_por_prioridade(lista, "Média")
    modulos_baixa = busca_por_prioridade(lista, "Baixa")

    grupos_prioridade = [
        modulos_alta,
        modulos_media,
        modulos_baixa
    ]

    resposta = []

    for grupo in grupos_prioridade:
        ordenados_por_eta = ordena_por_eta(grupo)
        for modulo in ordenados_por_eta:
            resposta.append(modulo)

    return resposta

def calcula_combustivel_restante(modulo: dict) -> float:
    combustivel_inicial = modulo["combustivel"]
    eta = modulo["eta_orbita_min"]
    massa = modulo["massa_kg"]
    taxa_base = constantes_pouso["taxa_consumo_base"]
    coeficiente = constantes_pouso["coeficiente_escala"]
    fator_massa = massa * coeficiente
    consumo_total = (taxa_base + fator_massa) * eta
    combustivel_restante = combustivel_inicial - consumo_total

    return combustivel_restante

# Execução principal
modulos_em_espera = ordena_modulos(dados_modulos)
modulos_autorizados = []
modulos_pousados = []
modulos_alerta = []

for modulo in modulos_em_espera:
    if verifica_autorizacao_pouso(modulo):
        modulos_autorizados.append(modulo)
    else:
        modulos_alerta.append(modulo)

print(f"Temos {len(modulos_autorizados)} módulos liberados para pouso e {len(modulos_alerta)} módulos em alerta.")

for modulo in modulos_alerta:
    print(f"Módulo {modulo['id']} bloqueado para pouso.")

input("Pressione enter para iniciar pousos de módulos liberados...")

for modulo in modulos_autorizados:
    print(f"Módulo {modulo['id']} liberado com sucesso! Preparando para pouso.")
    pousa_modulo(modulo)
    modulos_pousados.append(modulo)

print(f"Pousamos {len(modulos_pousados)} módulos!")