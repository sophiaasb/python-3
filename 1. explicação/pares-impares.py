import os
os.system("cls || clear")

pares = 0 
impares = 0 
media = 0

for i in range(5):
    valor = int(input(f"Digit o {i+1}º valor: "))

    if valor % 2 == 0:
        pares += 1
    else:
        impares += 1

media = (pares + impares) / 5

print(f"Números pares: {pares}")
print(f"Números ímpares: {impares}")
print(f"Média: {media}")