import os
os.system("cls || clear")

nota1: float = -1
nota2: float = -1
nota3: float = -1
nota4: float = 0

while True:
    nota1 = float(input("Digite a primeira nota: "))

    if (nota1 < 0 or nota1 > 10):
        print("Nota inválida.")
    
    nota2 = float(input("Digite a segunda nota: "))

    if (nota2 < 0 or nota2 > 10):
        print('Nota inválida.')

    nota3 = float(input("Digite a terceira nota: "))

    if (nota3 < 0 or nota3 > 10):
        print('Nota inválida.')

media = (nota1 + nota2 + nota3) / 3

print(f"Média {media}")

def verificar_status(media):
        if media >= 7:
            return "Aprovado."
        elif media >= 4:
            return "Recuperação."
        else: 
            return "Reprovado."