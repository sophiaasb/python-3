import os
os.system("cls || clear")

def cabecalho():
    os.system("cls || clear")
    print("----------------------")
    print(" === SENAI | FIEB === ")
    print("----------------------")

quantidade_numeros = 5
numeros = []

for i in range(quantidade_numeros):
    cabecalho()
    numero = int(input("\nDigite o {i+1}º número: "))
    if numero < 0:
        numero = 0
    numeros.append(numero)

for i, numero in enumerate(numeros):
    print(f"{i+1}º número: {numero}")