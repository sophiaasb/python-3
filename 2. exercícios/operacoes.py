import os
os.system("cls || clear")

def cabecalho():
    os.system("cls || clear")
    print("----------------------")
    print(" === SENAI | FIEB === ")
    print("----------------------")

def som(n1, n2):
    resultado = n1 + n2
    return resultado

def sub(n1, n2):
    resultado = n1 - n2
    return resultado

def mult(n1, n2):
    resultado = n1 * n2
    return resultado

def div(n1, n2):
    resultado = n1 / n2
    return resultado

cabecalho()
primeiro_num = int(input(f"\nDigite o primeiro número: "))
segundo_num = int(input(f"Digite o segundo número: "))

soma = som(primeiro_num, segundo_num)
subtração = sub(primeiro_num, segundo_num)
multiplicação = mult(primeiro_num, segundo_num)
divisão = div(primeiro_num, segundo_num)

cabecalho()
print(f"Soma: {soma}")
print(f"Subtração: {subtração}")
print(f"Multiplição: {multiplicação}")
print(f"Divisão: {divisão}")