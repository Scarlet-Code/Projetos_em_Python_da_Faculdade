print('-----Bem-vindo a Lanchonete da Yara Faria Godoy Bueno------')#Identificador pessoal RU: 4384673

print('********************Cardápio*******************')
print('| CÓDIGO |        DESCRIÇAO        |   VALOR  |')
print('|   100  |     Cachorro-Quente     |    9,00  |')
print('|   101  |  Cachorro Quente Duplo  |   11,00  |')
print('|   102  |           X-Egg         |   12,00  |')
print('|   103  |          X-Salada       |   12,00  |')
print('|   104  |          X-Bacon        |   14,00  |')
print('|   105  |          X-Tudo         |   17,00  |')
print('|   200  |    Refrigerante Lata    |    5,00  |')
print('|   205  |       Chá Gelado        |    4,00  |')
print('***********************************************')

#Variavel x sera utilizada para somar os valores dos itens adicionados a lista de pedidos
x = 0

while True: #Cria uma repetição do programa usando While. O uso do "True" indica que a repetição será infinita ate que ache um "break"
    cod_produto = input('Digite o codigo desejado: ') 

    if cod_produto == '100':
        print('Você escolheu Cachorro-Quente no valor de R$ 9,00')
        valor = 9
        x += valor # Adiciona e retornando o resultado ao operando esquerdo
    elif cod_produto == '101':
        print('Você escolheu Cachorro-Quente Duplo no valor de R$ 11,00')
        valor = 11
        x += valor # Adiciona e retornando o resultado ao operando esquerdo
    elif cod_produto == "102":
        print('Você escolheu X-Eggs no valor de R$ 12,00')
        valor = 12
        x += valor # Adiciona e retornando o resultado ao operando esquerdo
    elif cod_produto == '103':
        print('Você escolheu X-Salada no valor de R$ 13,00')
        valor = 13
        x += valor # Adiciona e retornando o resultado ao operando esquerdo
    elif cod_produto == '104':
        print('Você escolheu X-Bacon no valor de R$ 14,00')
        valor = 14
        x += valor # Adiciona e retornando o resultado ao operando esquerdo
    elif cod_produto == '105':
        print('Você escolheu X-Tudo no valor de R$ 17,00')
        valor = 17
        x += valor # Adiciona e retornando o resultado ao operando esquerdo
    elif cod_produto == '200':
        print('Você escolheu Refrgerante de Lata no valor de R$ 5,00')  
        valor = 5
        x += valor # Adiciona e retornando o resultado ao operando esquerdo
    elif cod_produto == '201':
        print('Você escolheu Chá Gelado no valor de R$ 4,00')
        valor = 4
        x += valor # Adiciona e retornando o resultado ao operando esquerdo
    else: 
        print('Opção inválida! Digite Novamente')
        continue #Após exibir a mensagem de opção invalida, a repetição será reiniciada graças ao uso do "continue" para o 'While True'

#Programa pergunta para o usuario se ele desejar continuar pondo mais itens em sua lista de pedido 
    print('Deseja fazer um novo pedido?')
    print ('1 - Sim')
    print ('0 - Não')
    novo_pedido = input('')
    #Cria uma condição, caso o usúario deseje fazer mais pedidos
    if novo_pedido== '1'or novo_pedido== 'sim':
        continue #Após escolher a opção 'sim'a repetição será reiniciada graças ao uso do "continue" para 'novo_pedido'
    else:
        print('Valor total a ser pago é de {:.2f} Reais'.format(x))
        print('Obrigada por compra na lachonete da Yara Godoy. Volte sempre!')
        break # Interrompe o loop

    

        
