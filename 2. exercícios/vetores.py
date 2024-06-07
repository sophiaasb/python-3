import os
os.system("cls || clear")

numeros = []

# Preenchendo ovetor com 10 números reais
for i in range(10):
    numero = float(input("Digite um número real: "))
    numeros.append(numero)

# Inicializando variáveis para contar os números negativos e somar os positivos
quantidade_negativos = 0
soma_positivos = 0

# Iterando sobre os números no vetor
for numero in numeros:
    if numero < 0:
        quantidade_negativos += 1
    else:
        soma_positivos += numero

# Mostrando os resultados
print("\nResultados: ")
print(f"Quantidade de números negativos: {quantidade_negativos}")
print(f"Soma dos números positivos: {soma_positivos}")