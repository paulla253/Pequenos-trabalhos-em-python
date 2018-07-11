from Pessoa import Pessoa

class Aluno(Pessoa):
    def __init__(self,nome,idade,salario, matricula="",semetre=None,materia=None,nota1=0,nota2=0,nota3=0):
        self._matricula = matricula
        self._semetre = semetre
        self._materia = materia
        self._nota1 = nota1
        self._nota2 = nota2
        self._nota3 = nota3
        Pessoa.__init__(self,nome, idade, salario)

    @property
    def matricula(self):
        return self._matricula

    @matricula.setter
    def matricula(self, matricula):
        self._matricula = matricula

    @property
    def semestre(self):
        return self._semestre

    @semestre.setter
    def semestre(self, semestre):
        self._semestre = semestre

    @property
    def materia(self):
        return self._materia

    @materia.setter
    def materia(self, materia):
        self._materia = materia

    @property
    def nota1(self):
        # print('get do nome')
        return self._nota1

    @nota1.setter
    def nota1(self, nota1):
        # print('set do nome', nome)
        self._nota1 = nota1

    @property
    def nota2(self):
        # print('get do nome')
        return self._nota2

    @nota2.setter
    def nota2(self, nota2):
        # print('set do nome', nome)
        self._nota2 = nota2

    @property
    def nota3(self):
        # print('get do nome')
        return self._nota3

    @nota3.setter
    def nota3(self, nota3):
        # print('set do nome', nome)
        self._nota3 = nota3

    def Resultado(self):
        resul=self.nota1+self.nota2+self.nota3
        return resul

    #funcao para o print.
    def __repr__(self):
        return str(self.__dict__)