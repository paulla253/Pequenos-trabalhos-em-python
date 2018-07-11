import MySQLdb

# Conexão com o banco de dados
db = MySQLdb.connect(host="localhost", user="root", passwd="root", db="Book")
# Posiciona o cursor no banco
cursor = db.cursor()

flag_continue=True
while (flag_continue):

    print("\n\n=======================")
    print("1- Select na tabela")
    print("2- Inserir novo livro")
    print("3- Deletar por id")
    print("4- Editar pelo id")
    print("5- Sair")
    print("=======================")
    op = input("Opcao:  ")

    if(op=="1"):

        print("\n\n\n Consulta na tabela : \n")
        # Executa a consulta na tabela Livro
        cursor.execute("SELECT * FROM Book.Livro;")
        # # Laço for para retornar os valores, ex.: row[0] primeira coluna, row[1] segunda coluna.
        for row in cursor.fetchall():
            print(" ", row[0], " ", row[1])

    elif(op=="2"):

        print("\n\n\nInserir novo livro : \n")
        nome = input("Nome do livro:  ")
        autor = input("Autor do livro:  ")
        valor = input("Valor do livro:  ")
        ano = input("Ano do livro:  ")

        try:
            #tenta inserir no banco.
            cursor.execute("INSERT INTO Book.Livro (Nome, Autor, Valor,Ano) VALUES (%s, %s,%s,%s)", (nome, autor, valor, ano))
            db.commit()
            print("Inserido novo livro")
        except:

            # se ocorreu algum erro,desfaz.
            db.rollback()
            print("Não conseguiu inserir novo livro,tente mais tarde")

    elif(op=="3"):

        print("\n\n\n Deletar o livro : \n")
        id = input("Digite o id:  ")

        try:
            #tenta inserir no banco.
            cursor.execute("DELETE FROM `Book`.`Livro` WHERE `id`='%s';" %(id))
            db.commit()
            print("Livro Deletado com sucesso")
        except:

            # se ocorreu algum erro,desfaz.
            db.rollback()
            print("Não foi possivel deletar o livro,tente mais tarde")

    elif (op == "4"):
        print("\n\n\nEditar livro : \n")

        id = input("Id do livro para ser editado:  ")

        nome = input("Nome do livro:  ")
        autor = input("Autor do livro:  ")
        valor = input("Valor do livro:  ")
        ano = input("Ano do livro:  ")

        try:
            # atualizada a tabela
            cursor.execute("UPDATE Livro SET Nome=%s,Autor=%s,Valor=%s,Ano=%s WHERE ID=%s ", (nome,autor,valor,ano, id))
            # Efetua a modificação na tabela
            print("Livro editado com sucesso")
            db.commit()
        except:
            # se ocorreu algum erro,desfaz.
            db.rollback()
            print("Não foi possivel editar o livro,tente mais tarde")
    else:
            print("\n\n\nPrograma Finalizado : \n")
            flag_continue=False