from os import system
from dataclasses import dataclass

QUANTIDADE_PETS = 2

def limpar():
    system('clear')

@dataclass
class Pet():
    nome: str
    idade: int
    raca: str
    porte: str
    alimentacao: str

pets = []

for i in range(QUANTIDADE_PETS):
    limpar()
    nome_pet = input("Nome do pet: ")
    idade_pet = int(input("Idade do pet: "))
    raca_pet = input("Raça do pet: ")
    porte_pet = input("Porte do pet: ")
    alimentacao_pet = input("Alimentação do pet: ")
    pet = Pet(nome = nome_pet, idade = idade_pet, raca = raca_pet, porte = porte_pet, alimentacao = alimentacao_pet)
    pets.append(pet)
    
for dados_pet in pets:
    limpar()
    print(f"Nome do pet: {dados_pet.nome}")
    print(f"Idade do pet: {dados_pet.idade}")
    print(f"Raça do pet: {dados_pet.raca}")
    print(f"Porte do pet: {dados_pet.porte}")
    print(f"Alimentação do pet: {dados_pet.alimentacao}")