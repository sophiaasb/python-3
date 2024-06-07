import os
os.system("clear")

def inserir_nota(notas):
    nota = float(input("Digite a nota: "))
    notas.append(nota)

def mostrar_quantidade_notas(notas):
    print("Foram inseridas:", len(notas), "notas.")

def calcular_media(notas):
    if len(notas) == 0:
        print("nenhuma nota foi inserida ainda.")
    else:
        media = sum(notas) / len(notas)
        print("A média das notas é: ", media)

def main():
    notas = []
    continuar = True

    while continuar:
        print("\nMenu:")
        print("S - Inserir mais uma nota")
        print("P - Ver quantas notas foram inseridas")
        print("N - Calcular a média aritmética das notas")
        print("Q - Sair")

        opcao = input("Escolha uma opção: ").upper()

        if opcao == "S":
            inserir_nota(notas)
        elif opcao == "P":
            mostrar_quantidade_notas(notas)
        elif opcao == "N":
            calcular_media(notas)
        elif opcao == "Q":
            continuar = False
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

    print("Programa encerrado.")

if __name__ == "__main__":
    main()