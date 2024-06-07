import os
os.system("cls || clear")

nota = float(input("Digite a sua nota: "))

while (nota < 0 or nota > 10):
    nota = float(input("Digite sua nota: "))

print(f"Nota: {nota}")

print("=== Fim ===")