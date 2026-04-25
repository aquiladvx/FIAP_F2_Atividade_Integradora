from utils import *
from constants import limites, constantes_pouso
import time

CAMINHO_PADRAO_DADOS = "data/data.csv"

def executar_mgpeb(modulos_inicio):
    print("=== Sistema MGPEB iniciado ===")

    if modulos_inicio is None:
        modulos = carregar_dados(CAMINHO_PADRAO_DADOS)
    else:
        modulos = modulos_inicio

    modulos_autorizados = []
    modulos_pousados = []
    modulos_alerta = []

    # Ordena os módulos por prioridade e ETA
    modulos_ordenados_em_espera = ordena_modulos(modulos)

    # Verifica se é seguro pousar
    for modulo in modulos_ordenados_em_espera:
        if verifica_se_seguro_pousar(modulo):
            modulos_autorizados.append(modulo)
        else:
            modulos_alerta.append(modulo)

    print(f"Temos {len(modulos_autorizados)} módulos liberados para pouso e {len(modulos_alerta)} módulos em alerta.")
    for modulo in modulos_alerta:
        print(f"Módulo {modulo['id']} bloqueado para pouso.")

    # Libera pousos para modulos autorizados
    if len(modulos_autorizados) < 1:
        print("Nenhum módulo autorizado para pouso. Encerrando o sistema.")
        return
    input("Pressione enter para iniciar pousos de módulos liberados...")

    for modulo in modulos_autorizados:
        print(f"Módulo {modulo['id']} liberado com sucesso! Preparando para pouso.")
        pousa_modulo(modulo)
        modulos_pousados.append(modulo)

    print(f"Pousamos {len(modulos_pousados)} módulos!")
    print("=== Sistema MGPEB encerrado ===")

def ordena_por_eta(lista: list) -> list:
    return bubble_sort_por_parametro(lista, "eta_orbita_min")

def ordena_por_combustivel(lista: list) -> list:
    return bubble_sort_por_parametro(lista, "combustivel")

def verifica_se_seguro_pousar(modulo: dict) -> bool:
    combustivel_apos_pouso = calcula_combustivel_restante(modulo)

    return combustivel_apos_pouso >= limites["combustivel"]

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

executar_mgpeb(None)