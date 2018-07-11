from Pessoa import Pessoa
from Aluno import Aluno

aluno= Aluno("Ana",20,500, "123", 1, "asdf", 10, 10, 20)

print(aluno)

aluno.nome="AnaP"
aluno.idade = 15
aluno.salario = 400

print(aluno)
aluno.apresetacao() #funcao pertecente a pessoa.

print("Minha nota foi "+str(aluno.Resultado()))