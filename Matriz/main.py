import numpy as np

#Referencia : https://gist.github.com/bencz/5180766
#Codigo estava em c, foi passado para python

tam = int(input("Tamanho da matriz"))

#declarando um vetor inicializadas com 0
matriz = np.zeros((tam,  tam))

#digitar os elementos da matriz.
for i in range(tam):
    for j in range(tam):

        matriz[i][j]=int(input("Matriz ["+str(i)+"]["+str(j)+"] : "))

#mostrar a matriz
print(matriz)

#convertendo para o tipo raiz.
matriz=np.matrix(matriz)

#utilizando a função de calcular determinante
print("Resultado pela funcao :np.linalg.det(matriz) ")
print(np.linalg.det(matriz))

count=0
temp=0.0
factor=0.0
#calculando o determinante:
for i in range(tam-1):
    if (matriz[i, i] == 0):
        for k in range(i, tam):

            if (matriz[k, i] != 0):

                for j in range(tam):

                    temp = matriz[i, j]
                    matriz[i, j] = matriz[k, j]
                    matriz[k, j] = temp
                break
        count=count+1
    if (matriz[i, i] != 0):
        for k in range(i+1, tam):

            factor = -1.0 * matriz[k, i] / matriz[i, i]
            for j in range(i,  tam):
                matriz[k, j] = matriz[k, j] + (factor * matriz[i, j])

temp=1.0
#calcular o determinante:
for i in range(tam):
    temp =temp * matriz[i, i]

print("Determinante : ")
if(count % 2 == 0):
        print(temp)
else:
    print(-1.0 * temp)

print("Matriz modoficada pelo codigo")
print(matriz)

#pegar coluna :
print("1 Coluna: ")
print(matriz[0:tam,0])
#pegar linha
print("1 linha: ")
print(matriz[0])
