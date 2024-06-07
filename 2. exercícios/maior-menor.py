import os
os.system("cls || clear")

numeros = []

for i in range(5):
    numero = int(input("Digite os números: "))
    numeros.append(numero)

maior_valor = max(numeros)
menor_valor = min(numeros)

print("\nExibindo resultados. ")
print(f"{i+1}º número: {numero}")
print(f"Maior número: {maior_valor}")
print(f"Menor número: {menor_valor}")