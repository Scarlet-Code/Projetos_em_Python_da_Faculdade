print('Bem-vindo a loja da Yara Faria Godoy Bueno') # Identificador pessoal RU: 4384673

# Variaveis Globais
valor_produto = float(input('Entre com o valor do produto: ')) 
qtd_produto = int(input('Entre com o valor da quantidade: '))
desconto = 0 

if qtd_produto <= 10: 
  desconto = 0.0 
elif 10 <= qtd_produto < 100:
  desconto = 0.5
elif 100 <= qtd_produto < 1000:
  desconto = 0.1
else:
  desconto = 0.15

sem_desconto = valor_produto * qtd_produto # Mostra o valor do produto sem desconto a partir da multiplicação valor-produto * qtd_produto
print('O valor sem desconto foi: R${:.2f}'.format(sem_desconto)) 
com_desconto = sem_desconto - sem_desconto * desconto #Mostra o valor do produto com a subitração sem_desconto multiplicado por esconto
print('O valor com deconto foi: R${:.2f}'.format(com_desconto))