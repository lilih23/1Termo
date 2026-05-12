# Exercícios de Programação Python: "O Caça-Erros"
# 1. O Problema da Idade
# Erro
# idade = input("Digite sua idade:")
# if idade >= 18:
#     print("Você é maior de iade")

    #Corrigido
# idade = int(input("Digite sua idade:"))
# if idade >= 18:
#     print("Você é maior de iade")

    #Melhorado
# idade = int(input("Digite sua idade:"))
# if idade >= 18:
#     print("Você é maior de iade")
# else:
#     print("Você é menor de idade")

# 2. A Escrita Fiel
# Erro
# nome = "Mariana"
# print("Seja bem-vinda, nome!")

 #Corrigido
# nome = "Mariana"
# print(f"Seja bem-vinda, {nome}!")

# Melhorado
# nome = "Mariana"
# print("=" * 30)
# print(f"Seja muito bem-vinda, {nome}!")
# print("=" * 30)

# 3. Falta de Espaço
# Erro
# numero = 10
# if numero > 5:
# print("O número é maior que cinco.")
# else:
# print("O número é menor ou igual a cinco.")

#Corrigido
# numero = 10
# if numero > 5:
#     print("O número é maior que cinco.")
# else:
#     print("O número é menor ou igual a cinco.")

# melhorado
# numero = int(input("Digite um numero: "))
# if numero > 5:
#     print(f"O numero {numero} é maior que cinco.")
# else:
#     print(f"O numero {numero} é menor ou igual a cinco.")

# 4. Esquecimento Fatal
# Erro
# usuario = "aluno123"
# if usuario == "aluno123"
#    print("Login realizado com sucesso.")

#Corrigido
# usuario = "aluno123"
# if usuario == "aluno123":
#     print("Login realizado com sucesso.")

# melhorado
# usuario = input("Digite seu usuario: ")
# if usuario == "aluno123":
#     print("Login realizado com sucesso!")
# else:
#     print("Usario incorreto. Tente novamente")

# 5. Atribuição vs. Comparação
# Erro
# clima = "ensolarado"
# if clima = "chuvoso":
# print("Leve um guarda-chuva!")

# Corrigido
# clima = "ensolarado"
# if clima == "chuvoso":
#     print("Leve um guarda-chuva!")

# Melhorado
# clima = input("como esta o clima hoje? "). lower()
# if clima == "chuvoso":
#     print(" Leve um guarda-chuva! ")
# elif clima == "ensolarado":
#     print(" Esta ensolarado! aproveite o dia.")
# else:
#     print("Clima desconhecido")

# 6. Misturando Alhos com Bugalhos
# Erro
# pontos = 50
# print("Parabéns! Você fez " + pontos + " pontos.")

# Corrigido
# pontos = 50
# print("Parabéns! Você fez " + str(pontos) + " pontos.")

# Melhorado
# pontos = int(input("Digite a quantidade de pontos: "))
# print(f"Parabens! Você fez {pontos} pontos.")

# 7. A Ordem dos Fatores
# Erro
# O sistema deve dar "Excelente" para notas 9 ou 10.
# nota = 9.5
# if nota >= 7:
# print("Aprovado")
# elif nota >= 9:
# print("Excelente!")

# Corrigido
# nota = 9.5
# if nota >= 7:
#     print("Aprovado")
#     if nota >= 9:
#         print("Excelente")

# Melhorada
# nota = float(input("Digite a nota da aluna: "))
# if nota >= 7:
#     print("Aprovado!")
#     if nota >= 9:
#         print("Exelente!")
# elif nota >= 5:
#     print("Recuperação.")
# else:
#     print("Reprovado.")

# 8. O Contador de 1 a 5
# Erro
# Objetivo: Mostrar na tela os números 1, 2, 3, 4 e 5.
# for i in range(5):
# print(i)

# Corrigido
# for i in range(1, 6):
#     print(i)

# Melhorada
# print("Contando de 1 a 5:")
# for numero in range(1, 6):
#     print(numero)

# 9. O Loop Eterno
# Erro
# tentativas = 1
# while tentativas <= 3:
# print("Tentando conectar...")
# O código deveria parar após 3 tentativas

# Corrigido
# tentativas = 1 
# while tentativas <= 3:
#     print("Tentando conectar...")
#     tentativas = tentativas +1

# Melhorada
# tentativas = 1 
# while tentativas <=3:
#     print(f"tentativa {tentativas}: tentando conectar...")
#     tentativas+= 1
#     print("\n Numero maximo de tentativas atingido. Processo finalizado.")

# 10. A Senha Teimosa
# Erro
# O programa deve pedir a senha até que o usuário digite "python123"
# senha = ""
# while senha == "python123":
# senha = input("Digite a senha secreta: ")
# print("Acesso concedido!")

# Corrigido
# senha = ""
# while senha != "python123":
#     senha = input("Digite a senha secreta: ")
# print ("Acesso concedido!")

# Melhorada 
# senha = ""
# while senha != "python123":
#     senha = input("Digite a senha secreta: ")
#     if senha != "python123":
#         print("senha incorreta! tente novamente.")
# print("\n Acesso concedido! Bem-vindo ao sistema.")