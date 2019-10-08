class Evento():
    def __init__(self, nome, local, data):    
        self.nome = nome
        self.local = local
        self.data = data


'''x = input("qual o seu nome, aluno?")
x = Aluno(70654, 123456, 10, 'eng', 53321)

nome = input("nome do evento")
local = input("local")
data = input("data")
festinha = x.CriarEvento(nome, local, data)

print(festinha.local)
'''
class Aluno():
    def __init__(self, cpf, senha, periodo, curso, dre):
        self.cpf = cpf
        self.senha = senha
        self.periodo = periodo
        self.curso = curso 
        self.dre = 10

    def CriarEvento(self, nome, local, data):
        nome = Evento(nome, local, data)
        return nome
