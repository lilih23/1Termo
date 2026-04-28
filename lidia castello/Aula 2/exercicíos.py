#Exercicíos 1 
# Cálculo de Notas
# Somativa 1 e Somativo 2
# Valores de 0 a 100
# O valor deverá ser atribuido por duas notas e uma média final e ao final deverá ser apresentado o resultado

# print("Bem-Vindos a calculadora de Notas")
# print("Notas do SENAI")
# print("As notas serão por Somativos 1 e 2")

# nota1 = float(input("Digite a Somativa 1 "))
# nota2 = float(input("Digite a somativa 2 "))
# media = (nota1 + nota2) / 2
# print("Sua média final foi:", round(media,2))

#Exercicío 2
# Criar um algoritmo para simular uma calculadora
# Deverá conter os operadora + - / *
# Ao inserir o valor 1 e o valor 2 ela deve apresentar o resultado


# print("Calculadora de Operadora")
# print("Escolha uma das opções")
# print("Soma + ")
# print("Subtração -")
# print("Multiplicação * ")
# print("Divisão / ")

# valor1 = float(input("Digite o primeiro valor "))
# valor2 = float(input("Digite o segundo valor "))
# operador = input("Qual operador deseja? ")

# if operador == "+": 
#      soma = valor1 + valor2
#      print("A soma foi: " , soma)
# elif operador == "-":
#      subtracao = valor1 - valor2
#      print("A subtracao foi: ", subtracao)
# elif operador == "*":
#      multiplicacao = valor1 - valor2
#      print("A multiplicação foi: " , multiplicacao)
# elif operador == "/": 
#      divisao = valor1 / valor2
#      print("A divisao foi: " , divisao)
# else:
#      print("obrigada por usar nossa calculadora")

# Exercicío 3
# Lojas de Roupas, Sapatos e Perfumes
# Ao escolher uma das opçãoes você deverá perguntar o valor do produto, a quantidade e aplicar descontos
# Roupas = 10%
# Sapatos = 5%
# Perfumes = 2%

# print("Bem-vindo a loja da lilih")
# print("nós tabalhamos com Sapatos, Roupas e Perfumes")
# print("Escolha uma das opções para iniciar suas compras")
# print("Digite 1 para Roupas")
# print("Digite 2 para Sapatos")
# print("Digite 3 para Perfumes")

# opcao = int(input("Digite a opção desejada "))

# if opcao == 1:
#     print("Você escolheu o setor de Roupas")
#     prod = float(input("Digite o valor do produtos" :))
#     qtde = float(input("Digite a quantidade que deseja" :))
#     desconto = 10 / 100
#     total = (prod * qtde) - desconto
#     print("Sua compra no setor de Roupas foi de: ", total)
# elif opcao == 2:
#     print("Você escolheu o setor de Sapatos")
#     prod = float(input("Digite o valor do produtos" :))
#     qtde = float(input("Digite a quantidade que deseja" :))
#     desconto = 5 / 100
#     total = (prod * qtde) - desconto
#     print("Sua compra no setor de Sapatos foi de: ", total)
# elif opcao == 3:
#     print("Você escolheu o setor de Perfumes")
#     prod = float(input("Digite o valor do produtos" :))
#     qtde = float(input("Digite a quantidade que deseja" :))
#     desconto = 2 / 100
#     total = (prod * qtde) - desconto
#     print("Sua compra no setor de Perfumes foi de: ", total)
# else:
#     print("Obigada por sua perferencia de vim na loja da lilih")