import os
os.system("cls || clear")

quantidade_notas = 3
notas = []

for i in range(quantidade_notas):
    nota = float(input("Digite uma nota: "))
    notas.append(nota)

media = sum(notas) / quantidade_notas

for i, nota in enumerate(notas):
    print(f"{i+1}ª nota: {nota}")

print(f"\média: {media}")