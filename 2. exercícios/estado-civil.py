import os
os.system("cls || clear")

nome = str(input("Digite o seu nome: "))
sexo = str(input("Digite o seu sexo (M ou F): "))
estado_civil = str(input("Digite o seu estado civil: "))

sexo = sexo.lower()
estado_civil = estado_civil.lower()

if sexo == 'f' and estado_civil == "casada":
    tempo_de_casamento = input("Digite o tempo de casada (em anos): ")

print("\n=== Exibindo dados ===")
print(f"Nome: {nome}")

if sexo == 'f':
    print(f"Sexo: Feminino")

else: 
    print(f"Sexo: Masculino")