import os

os.system("cls || clear")

QUANTIDADE_ALUNOS = 2

class Aluno:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

alunos = []

for i in range(QUANTIDADE_ALUNOS):
    nome_aluno = input("Digite seu nome: ")
    idade_aluno = int(input("Digite sua idade: "))
    aluno = Aluno(nome = nome_aluno, idade = idade_aluno)
    alunos.append(aluno)

for dados_aluno in alunos:
    print(f"Nome: {dados_aluno.nome}")
    print(f"Idade: {dados_aluno.idade}")
