def input_informacao(entrada):
    resposta = int(input(f'Qual {entrada} você quer adicionar seu símbolo? '))
    return resposta

def gerar_matriz_nula():
    matriz = []
    for i in range(3):
        linha = []
        for j in range(3):
            linha.append(" ")
        matriz.append(linha)    
    return matriz

def imprimir_matriz(matriz):
    for linha in matriz:
        print(f'{"|".join(linha)}')  

def adicionar_matriz(matriz, linha, coluna, simbolo):
    if 0 <= linha <= len(matriz) and 0 <= coluna <= len(matriz[0]):
        matriz[linha-1][coluna-1] = simbolo
        return matriz
    else:
        print("Posição fora dos limites da matriz.")
        return matriz
    
def linha():
     print(60*'-')

def verificar_vitoria(matriz, simbolo):
    # Verificar linhas
    for linha in matriz:
        linha_igual = True
        for elemento in linha:
            if elemento != simbolo:
                linha_igual = False
                break
        if linha_igual:
            return True

    # Verificar colunas
    for coluna in range(len(matriz[0])):
        coluna_igual = True
        for linha in range(len(matriz)):
            if matriz[linha][coluna] != simbolo:
                coluna_igual = False
                break
        if coluna_igual:
            return True

    # Verificar diagonal principal
    diagonal_principal_igual = True
    for i in range(len(matriz)):
        if matriz[i][i] != simbolo:
            diagonal_principal_igual = False
            break
    if diagonal_principal_igual:
        return True

    # Verificar diagonal secundária
    diagonal_secundaria_igual = True
    for i in range(len(matriz)):
        if matriz[i][len(matriz) - i - 1] != simbolo:
            diagonal_secundaria_igual = False
            break
    if diagonal_secundaria_igual:
        return True

    return False

jogador1=0
jogador2=0
postosx = 0
pontoso = 0
while True:
    matriz_inicial = gerar_matriz_nula() 
    print('|---JOGO DA VELHA---|')
    print('Jogador [1] - X\nJogador [2] - O')
    print(60*'=')
    print(f'Os pontos do jogador 1 são: {jogador1}\nOs pontos do jogador 2 são: {jogador2}')
    print(60*'=')
    print('1-SIM\n2-NÃO')
    resposta=int(input('Quer jogar uma partida? '))
    if resposta==1:
        while True:
            linha()
            print('Jogador 1')
            linha()
            linhax = input_informacao('linha')
            colunax = input_informacao('coluna')
            matriz_jogo = adicionar_matriz(matriz_inicial, linhax, colunax, 'X')
            imprimir_matriz(matriz_jogo)

            if verificar_vitoria(matriz_jogo, 'X'):
                print("O jogador 1 venceu!")
                jogador1+=1
                break
            elif verificar_vitoria(matriz_jogo, 'O'):
                jogador2+=1
                print("O jogador 2 venceu!")
                break
            elif all(' ' != elemento for linha in matriz_jogo for elemento in linha):
                print("Empate!")
                break

            linha()
            print('Jogador 2')
            linha()
            linhao = input_informacao('linha')
            colunao = input_informacao('coluna')
            matriz_jogo = adicionar_matriz(matriz_jogo, linhao, colunao, 'O')
            imprimir_matriz(matriz_jogo)

            if verificar_vitoria(matriz_jogo, 'X'):
                linha()
                print("O jogador 1 venceu!")
                linha()
                break
            elif verificar_vitoria(matriz_jogo, 'O'):
                linha()
                print("O jogador 2 venceu!")
                linha()
                break
            elif all(' ' != elemento for linha in matriz_jogo for elemento in linha):
                print("Empate!")
                break
    elif resposta==2:
        print('Encerrando...')
        break
    else:
        print('Resposta inválida!')
        continue
