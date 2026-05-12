#Atividade 1: Mensagem de Boas-Vindas
#Crie um script que use a função print() para exibir a mensagem "Bem-vindo ao mundo da
#programação em Python!".

# print("Bem-vindo ao mundo da progamação em Python!")

# Atividade 2: Informações Pessoais
# Escreva um programa que imprima seu nome completo em uma linha e sua idade em outra linha.
# Exemplo de saída:
# Fulano de Tal
# 30

# pergunta1 = input("Digite seu nome")
# pergunta2 = int(input("Digite sua idade"))

# print ("Seu nome e sua idade são: " ,pergunta1, pergunta2) 

# Atividade 3: Calculadora de Soma e Subtração
# Crie um script que exiba o resultado da soma de 135 com 246 e o resultado da subtração de 512
# por 128. Cada resultado deve ser exibido em uma linha separada.
# ● Dica: Use o print() diretamente com os operadores (print(135 + 246)).
# ● Obs: Realize também a mesma situação com variáveis

# (print(135 + 246))

# Atividade 4: Multiplicação e Divisão
# Escreva um programa que mostre o resultado da multiplicação de 15 por 8 e o resultado da
# divisão de 78 por 3.

# print("Multiplicação * ")
# print("Divisão / ")

# valor1 = float(input("Digite o primeiro valor "))
# valor2 = float(input("Digite o segundo valor "))
# operador = input("Qual operador deseja? ")

# if operador == "*":
#       multiplicacao = valor1 *valor2
#       print("A multiplicação foi: " , multiplicacao)
# elif operador == "/": 
#       divisao = valor1 / valor2
#       print("A divisao foi: " , divisao)

# print("5 elevado a 3 é: ")
# print(5**3)

# Atividade 6: Concatenando Palavras
# Crie um script que declare o seu primeiro nome em uma string e seu sobrenome em outra. Use
# o operador + para concatenar (juntar) as duas strings e exibir seu nome completo.
# ● Exemplo: print("Maria" + " " + "Silva")

# print("lidia" + " " + " eliana")

# Atividade 7: Cálculo de Eficiência (OEE)
# ● Peça a quantidade de peças produzidas e a quantidade de peças defeituosas. Calcule
# e exiba a taxa de aproveitamento (peças boas / total).

# qtd = int(input("Digite sua qtd"))
# defeituosa = int(input("Digite a quantidade de defeituosa"))
# print("qtd total foi", qtd / defeituosa )

# Atividade 8: Descrição com Cálculos
# Crie um script que exiba a seguinte frase, substituindo os cálculos pelos seus resultados:
# "Eu tenho 25 anos e, em 10 anos, terei 35 anos."
# ● Dica: Use a vírgula dentro do print() para combinar strings e cálculos.
# ● Ex: print("Texto", 25 + 10).

# print("Eu tenho 16 anos e, em 10 anos terei", 16 + 10)

# Atividade 9: Orçamento de Viagem (Cálculo com float)
# Imagine que você está planejando uma viagem. O custo do hotel é de R$ 250.50 por noite e
#  o custo da passagem é R$ 412.00. Calcule e exiba o custo total para uma viagem por noites.
#  ● Ex: Fórmula: (custo_hotel * 3) + custo_passagem

# custoH = float(input("custo da noite "))
# custoP = float(input("custo da passagem "))
# dias = float(input("quantos dia "))

# print("total da viagem foi" , (custoH * dias) + custoP )

# Atividade 10: Desafio - Mini Relatório
# Crie um script que imprima um pequeno relatório. Use print() várias vezes para formatar a
# saída de forma organizada.
# ● Exemplo de saída:

# ==========================
# Relatório de Vendas
# ==========================
# Produto: Notebook Gamer
# Quantidade vendida: 15
# Preço unitário: R$ 5499.50
# Total de vendas: R$ 82492.50
# ==========================

# print("Bem-vindos a loja da Lilih")
# produto = input("Digite o produto que deseja?")
# qtde = int(input("Digite a quantidade desejada?"))
# preco = float(input("Dgite o valor do produto"))


# print("Relatorio de venda" )
# print("nome do produto vendido" , produto )
# print("quantidade do produto vendido" , qtde )
# print("Preço unitario das peça" , preco )
# print("o valor total das vendas foi: " , preco * qtde )


