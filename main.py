import pandas as pd
import time

limits = {
    "combustivel": 30
}

modules_data_df = pd.read_csv("data.csv")
modules_data = modules_data_df.to_dict(orient="records")


def get_by_priority(list: list, priority: str) -> list:
    response = []
    for i in list:
        if i["prioridade"] == priority:
            response.append(i)

    return response


def get_sorted_eta(list: list) -> list:
    return bubble_sort_by_parameter(list, "eta_orbita_min")


def get_sorted_fuel(list: list) -> list:
    return bubble_sort_by_parameter(list, "combustivel")


def bubble_sort_by_parameter(list: list, parameter: str, reverse: bool = False) -> list:
    n = len(list)
    for i in range(n):

        for j in range(0, n - i - 1):
            if reverse:
                condition = list[j][parameter] < list[j + 1][parameter]  # decrescente
            else:
                condition = list[j][parameter] > list[j + 1][parameter]

            if condition:
                list[j], list[j + 1] = list[j + 1], list[j]
    return list


def check_landing_authorization(module: dict) -> bool:
    return module["combustivel"] >= limits["combustivel"]

def land_module(module: dict):
    print(f"Pousando modulo {module['id']} em...")
    # for i in range(3, 0, -1):
    #     print(f"{i}...")
    #     time.sleep(0.5)
    print(f"Modulo pousado com sucesso!")
    time.sleep(0.5)


def sort_modules(list: list) -> list:
    high_priority_modules = get_by_priority(list, "Alta")
    medium_priority_modules = get_by_priority(list, "Média")
    low_priority_modules = get_by_priority(list, "Baixa")

    priority_groups = [
        high_priority_modules,
        medium_priority_modules,
        low_priority_modules
    ]

    response = []

    for group in priority_groups:
        sorted_by_eta = get_sorted_eta(group)

        for module in sorted_by_eta:
            response.append(module)
        #TODO: Adicionar comparação de combustível se necessário
    return response




waiting_modules = sort_modules(modules_data)
authorized_modules = []
landed_modules = []
alert_modules = []

for module in waiting_modules:
    if check_landing_authorization(module):
        authorized_modules.append(module)
    else:
        alert_modules.append(module)

print(f"Temos {len(authorized_modules)} modulos liberados para pouso e {len(alert_modules)} modulos em alerta.")

for module in alert_modules:
    print(f"Modulo {module['id']} bloqueado para pouso.")

input("Pressione enter para iniciar pousos de modulos liberados...")

for module in authorized_modules:
    print(f"Modulo {module['id']} liberado com sucesso! Preparando para pouso.")
    land_module(module)
    landed_modules.append(module)

print(f"Pousamos {len(landed_modules)} modulos!")





