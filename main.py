from utils import carregar_dados
from MGPEB import executar_mgpeb


def main():
    print("=== Simulador MGPEB ===")
    arquivo = escolher_cenario()
    modulos = carregar_dados(arquivo)

    print(f"\nCarregando cenário: {arquivo}")
    print(f"Total de módulos: {len(modulos)}\n")

    executar_mgpeb(modulos)


def escolher_cenario() -> str:
    opcao = ""
    dado_escolhido = ""

    print("Escolha um cenário:")
    print("1 - Cenário Crítico")
    print("2 - Cenário Positivo")
    print("3 - Cenário Aleatório")

    while opcao not in ["1", "2", "3"]:
        opcao = input("Digite o número do cenário: ")
        if opcao == "1":
            dado_escolhido = "data/data_critico.csv"
        elif opcao == "2":
            dado_escolhido = "data/data_positivo.csv"
        elif opcao == "3":
            dado_escolhido = "data/data_aleatorio.csv"
        else:
            print("Opção inválida.")
    return dado_escolhido


if __name__ == "__main__":
    main()
