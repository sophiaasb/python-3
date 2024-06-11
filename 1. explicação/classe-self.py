import os

os.system("cls || clear")

QUANTIDADE_ALUNOS = 2

class Aluno:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

alunos = []

for i in range(QUANTIDADE_ALUNOS):
    nome_aluno = input("Digite seu nome: ")
    idade_aluno = int(input("Digite sua idade: "))
    peso_aluno = float(input("Digite seu peso: "))
    altura_aluno = float(input("Digite sua altura: "))
    aluno = Aluno(nome = nome_aluno, idade = idade_aluno, peso = peso_aluno, altura = altura_aluno)
    alunos.append(aluno)

for dados_aluno in alunos:
    print(f"Nome: {dados_aluno.nome}")
    print(f"Idade: {dados_aluno.idade}")
    print(f"Peso: {dados_aluno.peso}")
    print(f"Altura: {dados_aluno.altura}")
