import subprocess as sub

#python2

flag_continue=True
nome=""

while (flag_continue):

    print("\n\n=======================")
    print("1- Olhar conteudo na pasta")
    print("2- Hora do sistema")
    print("3- Criar novo arquivo")
    print("4- Conteudo de um arquivo")
    print("5- Criar nova pasta")
    print("6- Deletar arquivo/pasta")
    print("7- Sair")
    print("=======================")
    op = int(input("Opcao:  "))


    if(op==1):

        p = sub.Popen(['ls', '-al'], stdout=sub.PIPE, stderr=sub.PIPE)
        output, errors = p.communicate()
        print(output)


    elif(op==2):

        p=sub.Popen(['date'], stdout=sub.PIPE, stderr=sub.PIPE)
        output, errors = p.communicate()
        print(output)
    #
    elif(op==3):

        nome = raw_input('Nome do arquivo: ')
        p=sub.Popen(['touch',nome], stdout=sub.PIPE, stderr=sub.PIPE)
        output, errors = p.communicate()

    elif (op == 4):

        nome = raw_input('Nome do arquivo: ')
        p=sub.Popen(['cat',nome], stdout=sub.PIPE, stderr=sub.PIPE)
        output, errors = p.communicate()

    elif (op == 5):

        nome = raw_input('Nome da pasta/arquivo: ')
        p=sub.Popen(['rm','-R',nome], stdout=sub.PIPE, stderr=sub.PIPE)
        output, errors = p.communicate()

    elif (op == 6):

        nome = raw_input('Nome da pasta/arquivo: ')
        p=sub.Popen(['rm','-R',nome], stdout=sub.PIPE, stderr=sub.PIPE)
        output, errors = p.communicate()

    else:
            print(op)
            print("\n\n\nPrograma Finalizado  \n")
            flag_continue=False