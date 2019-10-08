from classes import Aluno, Evento
import sqlite3 

connection = sqlite3.connect('table.db')
cursor = connection.cursor()

'''
cursor.execute(CREATE TABLE BCEventos(
    id INTEGER PRIMARY KEY,
    nome STR NOT NULL,
    evento STR NOT NULL,
    data STR
    ))
'''
#cursor.execute('ALTER TABLE BCEventos ADD local STR')

x = input("qual o seu nome, aluno?")
nome = x
x = Aluno(70654, 123456, 10, 'eng', 53321)

evento = input("nome do evento")
local = input("local")
data = input("data")
evento = x.CriarEvento(evento, local, data)

cursor.execute('INSERT INTO BCEventos(nome, evento, local, data) VALUES(?,?,?,?)', (nome, evento.nome, evento.local, evento.data))
connection.commit()
