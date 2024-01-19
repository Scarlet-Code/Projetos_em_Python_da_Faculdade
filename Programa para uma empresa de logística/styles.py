print('----------Bem-vindo a companhia de Logistica Yara Faria Godoy Bueno S.A----------')#Identificador Pessoal RU: 4384673
#--------------------Inicio da funcão dimensõesObjeto------------------------
def dimensoesObjeto(): 
  while True: #Laço de repetição para definir se o tamanho do objeto em cm³ é aceito
    try: #Caso o usúario digite um valor não inteiro ou não numérico sera informado através da função try/except
      comprimento = float(input('Digite o comprimento do objeto (em cm):'))
      largura = float(input('Digite a largura do objeto (em cm):'))
      altura = float(input('Digite a altura do objeto (em cm):'))
      volume = comprimento * largura * altura
      print('O volume do objeto é(em cm³): {}' .format(volume))
      if volume < 1000:
        return 10
      elif 1000 <= volume < 10000:
        return 20
      elif 10000 <= volume < 30000:
        return 30
      elif 30000 <= volume < 100000:
        return 50
      else:
        print('Não aceitamos objetos com dimensões tão grandes')
        print('Entre com as dimensões desejadas novamente')
        continue
    except ValueError:
      print('Você digitou alguma dimensão do objeto com valor não numérico')
      print('Por favor entre com as dimensões desejdas novamente')
      continue #retorna para a pergunta
#----------------------Fim da função dimensões objeto----------------------  

#------------------Inicio da função pesoObjeto-----------------------------
def pesoObjeto():
  while True:#Laço de repetição para definir se o peso do objeto é aceito
    try: #Caso o usúario digite um valor não númerico ou muito pesado, será informado através da função try\except
      peso = float(input('Digite o peso do objeto em (kg):'))
      if peso <= 0.1:
        return 1
      elif 0.1 < peso <=1:
        return 1.5
      elif 1 < peso < 10:
        return 2
      elif 10 <= peso < 30:
        return 30

      else:
        print('Não aceitamos objetos tão pesados:')

    except ValueError:
        print('Você digitou peso do objeto com valor não numérico')
        print('Por favor entre com o peso desejado novamente.')
        print('Entre com o peso desejado novamente:')
        print('Digite o peso do objeto em (kg):')
#--------------------Fim da função pesoObjeto---------------------      
        
#--------------------Inicio da função rotaObjeto-------------------        
def rotaObjeto():#Laço de repetição para definir se a rota do objeto em é aceita
  while True:
    rota = input('Selecione a rota:\nRS - De rio de Janeiro para são Paulo\nSR - De São Paulo até rio de Janeiro\nBS - De Brasilia até São Paulo\nSB - De'
    'São Paulo para Brasilia\nBR - De Brasilia ate Rio de Janeiro\nRB - De rio de Janeiro ate Brasilia\n>>')
    if rota == 'RS':
      return 1
    elif rota == 'SR' or 'sr':
      return 1
    elif rota == 'BS' or 'bs':
      return 1.2
    elif rota == 'SB' or 'sb':
      return 1.2
    elif rota == 'BR' or 'br':
      return 1.5
    elif rota == 'RB' or 'rb':
      return 1.5
    else:
      print('Você digitou uma rota que não existe')
      print('Por favor entre com a rota desejada novamente')
#------------------Fim da função RotaObjeto------------------
      
#-----------------------Inicio do main-----------------------
print('-----Bem-vindo a Companhia de Logistica Yara Faria Godoy Bueno S.A-----')
dimensoes = dimensoesObjeto()
peso = pesoObjeto()
rota = rotaObjeto()
total = dimensoes * peso * rota #Calculo do valor total a ser pago
print('O valortotal é R${:.2f}\n(Dimensões:{:.2f} * Peso:{:.2f} *Rota:{:.2f})' .format(total,dimensoes,peso,rota))




                
            
                
        