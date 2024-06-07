import os
os.system("cls || clear")

resultado = 0

a = int(input("Digite o primeiro número: "))
opcao = input("Digite a opção desejada: ")
b = int(input("Digite o segundo número: "))

match(opcao):
    case '+':
        resultado = a + b
    case '-':
        resultado = a - b
    case '*':
        resultado = a * b
    case '/':
        resultado = a / b
    case _:
        print("Opção inválida.")

print(f"Resultado: {resultado}")