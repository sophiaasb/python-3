import os
os.system("cls || clear")

def calcular_media(notas):
    return sum(notas) / len(notas)

def main():
    notas = []
    for i in range(4):
        nota = float(input("Digite a {}ª nota: ".format(i + 1)))
        notas.append(nota)

    media = calcular_media(notas)
    print("A média das notas é:", media)

if __name__ == "__main__":
    main()