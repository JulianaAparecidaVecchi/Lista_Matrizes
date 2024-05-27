import random
#Exercicício 01
def gera_matriz(nlinhas,ncolunas):
    matriz=[]
    for i in range(nlinhas):
        linha_matriz=[]
        for j in range(ncolunas):
            elemento=random.randint(0,20)
            print(f'O elemento {i+1},{j+1} da sua matriz é: {elemento}')
            linha_matriz.append(elemento)
        matriz.append(linha_matriz)
    return matriz

#Exercicício 02
def imprimir_matriz(matriz):
    for i in matriz:
        print(i)

#Exercicício 03
def soma_par_matriz(matriz):
    soma=0
    for i in matriz:
        for j in i:
            if j % 2 == 0:
                soma+=j
            else:
                soma=soma 
    return soma 

#Exercicício 04
def soma_coluna(coluna,ncoluna,matriz):
    soma=0
    coluna=coluna-1
    if coluna<= ncoluna and coluna>=0:
        for i in matriz:
                soma+=i[coluna]
    elif coluna>ncoluna or coluna<ncoluna:
        print('Essa coluna não existe')
    
    return soma

#Exercicício 05
def maior_linha(linha,nlinhas,matriz):
    maior=0
    linha=linha-1
    if linha<=nlinhas and linha>=0:
        for j in matriz[linha]:
            if j>maior:
                maior=j
    return maior


nlinhas=int(input('Digite o número de linhas da sua matriz: '))
ncolunas=int(input('Digite o número de colunas da sua matriz: '))
matriz=gera_matriz(nlinhas,ncolunas)
imprimir_matriz(matriz)
print(f'A soma dos elementos pares da sua matriz é: {soma_par_matriz(matriz)}')
coluna=int(input('Qual coluna deseja somar? '))
print(f'A soma da coluna {coluna} é: {soma_coluna(coluna,ncolunas,matriz)}')
linha=int(input('Qual linha deseja achar o maior elemento? '))
print(f'O maior elemento da linha {linha} é: {maior_linha(linha,nlinhas,matriz)}')