class Pessoa(object):
    def __init__(self, nome=None, idade=0, salario=0):
        self._nome = nome
        self._idade = idade
        self._salario = salario

    @property
    def nome(self):
        # print('get do nome')
        return self._nome

    @nome.setter
    def nome(self, nome):
        # print('set do nome', nome)
        self._nome = nome

    @property
    def idade(self):
        # print('get da idade')
        return self._idade

    @idade.setter
    def idade(self, idade):
        # print('set da idade', idade)
        self._idade = idade

    @property
    def salario(self):
        # print('get do salario')
        return self._salario

    @salario.setter
    def salario(self, salario):
        # print('set do salario', salario)
        self._salario = salario

    def apresetacao(self):

        print("Hello meu nome é "+self._nome)