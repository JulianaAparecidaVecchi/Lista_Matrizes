def gerar_matriz():
    nlinhas=10
    ncolunas=10
    matriz=[]
    for i in range(nlinhas):
        linha_matriz=[]
        for j in range(ncolunas):
          if i<j:
            elemento=2*i+7*j
            linha_matriz.append(elemento)
          if i==j:
            elemento=3*i**2
            linha_matriz.append(elemento)
          if i>j:
            elemento=(4*(i**3))+(5*(j**2))
            linha_matriz.append(elemento)
        matriz.append(linha_matriz)
    return matriz

def imprimir_matriz(matriz):
    for i in matriz:
        print(i)

matriz=gerar_matriz()
imprimir_matriz(matriz)
