from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
import MySQLdb

#funcao sera realizada ao clicar no botao.
def click():

    # Conecao com o banco de dados
    db = MySQLdb.connect(host="localhost", user="root", passwd="root", db="Book")
    # Posiciona o cursor no banco
    cursor = db.cursor()

    #pegando os valores nos edits
    nome = ed1.text
    autor = ed2.text
    valor = ed3.text
    ano = ed4.text

    try:
        # tenta inserir no banco.
        cursor.execute("INSERT INTO Book.Livro (Nome, Autor, Valor,Ano) VALUES (%s, %s,%s,%s)",
                       (nome, autor, valor, ano))
        db.commit()
        print("Inserido novo livro com sucesso")
    except:

        # se ocorreu algum erro,desfaz.
        db.rollback()
        print("Nao conseguiu inserir novo livro,tente mais tarde")

#construindo os componentes
def build():

    layout=GridLayout()
    #duas colunas.
    layout.cols = 2

    #labels
    lb1=Label()
    lb1.text="Nome"
    lb1.font_size=15

    lb2=Label()
    lb2.text="Autor"
    lb2.font_size=15

    lb3=Label()
    lb3.text="Valor"
    lb3.font_size=15

    lb4=Label()
    lb4.text="Ano"
    lb4.font_size=15

    #edits globais:
    ed1=TextInput(text="",multiline=False)
    global ed1

    ed2=TextInput(text="",multiline=False)
    global ed2

    ed3=TextInput(text="",multiline=False)
    global ed3

    ed4=TextInput(text="",multiline=False)
    global ed4

    #botao com sua funcao
    bt = Button(text="Cadastrar")
    bt.on_press=click

    #Adicionando ao layout
    layout.add_widget(lb1)
    layout.add_widget(ed1)

    layout.add_widget(lb2)
    layout.add_widget(ed2)

    layout.add_widget(lb3)
    layout.add_widget(ed3)

    layout.add_widget(lb4)
    layout.add_widget(ed4)

    layout.add_widget(bt)

    return layout

janela=App()
#titulo para APP
janela.title="Exemplo de APP"

from kivy.core.window import Window

#tamanho da janela.
Window.size=300,300

#trocando o build
janela.build=build

#rodando a aplicacao.
janela.run()