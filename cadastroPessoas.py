def cadastrar_pessoa():
    Pessoa=[]
    nome=str(input('Digite seu nome: '))
    Pessoa.insert(0,nome)
    cpf=int(input('Digite seu cpf: '))
    Pessoa.insert(1,cpf)
    idade=float(input('Digite sua idade: '))
    Pessoa.insert(2,idade)
    renda=float(input('Digite sua renda mensal: '))
    Pessoa.insert(3,renda)
    return Pessoa

def imprimir_matriz(matriz):
    for i in matriz:
        print(i)
    
def calcular_media_idade(matriz,contador):
    soma=0
    for i in matriz:
            soma+=i[2]
    media=soma/contador
    return media  

def calcular_media_renda(matriz,contador):
    soma=0
    for i in matriz:
            soma+=i[3]
    media=soma/contador     
    return media

matriz=[]
cont=0
while True:
    print('[1]-Sim\n[2]-Não')
    resposta=int(input('Deseja cadatrar uma pessoa? '))
    if resposta==1:
        pessoa=cadastrar_pessoa()
        matriz.append(pessoa)
        print('Pessoa cadatrada!')
        cont+=1
    else:
        print('Aqui está a tabela de pessoas cadastradas: ')
        imprimir_matriz(matriz)
        print(f'A média das idades de pessoas cadatradas é: {calcular_media_idade(matriz,cont)}')
        print(f'A média das rendas das pessoas cadatradas é: {calcular_media_renda(matriz,cont)}')
        break