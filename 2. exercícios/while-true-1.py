import os
os.system("cls || clear")

nota1: float = -1
nota2: float = -2

while True:
    nota1 = float(input("Digite a primeira nota: "))

    if (nota1 < 0 or nota1 > 10):
        print("Nota inválida.")
    
    nota2 = float(input("Digite a segunda nota: "))

    if (nota2 < 0 or nota2 > 10):
        print('Nota inválida.')

    else:
        break
media = (nota1 + nota2) / 2

print(f"Média {media}")