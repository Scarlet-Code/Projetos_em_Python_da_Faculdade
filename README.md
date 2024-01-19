# Projetos_em_Python_da_Faculdade

Esse repositório tem como objetivo mostrar 4 projetos feito para a faculdade.

- [App de Vendas com desconto](https://github.com/Scarlet-Code/Projetos_em_Python_da_Faculdade/tree/main/App%20de%20vendas%20com%20desconto)
- [App de Vendas para uma lanchonete](https://github.com/Scarlet-Code/Projetos_em_Python_da_Faculdade/tree/main/App%20de%20vendas%20para%20uma%20lanchonete)
- [Programa para uma empresa de logística](https://github.com/Scarlet-Code/Projetos_em_Python_da_Faculdade/tree/main/Programa%20para%20uma%20empresa%20de%20log%C3%ADstica)
- [Software de controle](https://github.com/Scarlet-Code/Projetos_em_Python_da_Faculdade/tree/main/Software%20de%20Controle)

 ### 1. App de Vendas com desconto

SITUAÇÃO: Imagina-se que você é um dos programadores responsáveis pela construção de app de vendas para uma determinada empresa X que vende em atacado. Uma das estratégias de vendas dessa empresa X é dar desconto maiores por unidade conforme a tabela abaixo:
 
|   Quantidades      |	   Desconto    |
|--------------------|-----------------|
|      Até 9         | 0% na unidade   |
|  Entre 10 e 99     |	5% na unidade  |
|  Entre 100 e 999   |	10% na unidade |
|  De 1000 para mais | 15% na unidade  |

### 2. App de Vendas para uma lachonete

SITUAÇÃO: Você e sua equipe de programadores foram contratados para desenvolver um app de vendas para uma lanchonete. Você ficou com a parte de desenvolver a interface do cliente para retirada do produto.
A lanchonete possui seguinte tabela de produtos listados com sua descrição, códigos e valores:

| Código |       Descrição           |  Valor |
|--------|---------------------------|--------|
|  100	 |       Cachorro-Quente	   |  9,00  |
|  101   |	   Cachorro-Quente Duplo |  11,00 |
|  102	 |         X-Egg	           |  12,00 |
|  103	 |         X-Salada	         |  13,00 |
|  104	 |         X-Bacon	         |  14,00 |
|  105	 |         X-Tudo	           |  17,00 |
|  200	 |     Refrigerante Lata	   |  5,00  |
|  201	 |        Chá Gelado	       |  4,00  |

### 3. Programa para uma empresa de logística

SITUAÇÃO: Imagina-se que você e sua equipe foram contratados por uma empresa de logística que acabou de entrar no ramo. Essa empresa trabalha com encomendas de pequeno e médio porte e opera somente entre 3 cidades.
O valor que a empresa cobra por objeto é dado pela seguinte equação:
|total=dimensões*peso*rota que você e sua equipe|
|-----------------------------------------------|

Em que cada uma das variáveis que compõe o preço total é quantizada da seguinte maneira:

 #### Quadro 1: Dimensões versus Valor                                                
|       Dimensões (cm³)	       |   Valor (R$) |
|------------------------------|------------- |
|        volume < 1000 	       |      10      |
|     1000   <= volume < 10000 |	    20      |
|     10000 <= volume < 30000  |	    30      |
|     30000 <= volume < 100000 |	    50      |
|         volume >= 100000     | Não é aceito |

 #### Quadro 2: Peso versus multiplicador
|      Peso(kg)	    |   Multiplicador |
|-------------------|-----------------|
|    peso <= 0.1	  |        1        |
|   0.1 <= peso < 1 |	      1.5       |
|   1 <= peso < 10  |	       2        |
|   10 <= peso < 30	|        3        |
|   peso =>   30	  |   Não é aceito  |

 #### Quadro 3: Rota versus multiplicador
|                  Rota	              | Multiplicador |
|-------------------------------------|---------------|
|RS - De Rio de Janeiro até São Paulo	|       1       |
|SR - De São Paulo até Rio de Janeiro	|       1       |
|BS - De Brasília até São Paulo	      |      1.2      |
|SB - De São Paulo até Brasília	      |      1.2      |
|BR - De Brasília até Rio de Janeiro	|      1.5      |
|RB - Rio de Janeiro até Brasília	    |      1.5      |

### 4. Software de Controle

SITUAÇÃO: Imagina-se que você está desenvolvendo um software de controle de estoque para uma bicicletaria. Este software deve ter o seguinte menu e opções:
1.	Cadastrar Peça
2.	Consultar Peça
    1)	Consultar Todas as Peças
    2)	Consulta Peças por Código
    3)	Consulta Peças por Fabricante
    4)	Retornar 
3.	Remover Peça
4.	Sair







 
