# 1. Perfil de Gamer: Peça o nick (nome) do jogador e o nível atual. Exiba: "O
# jogador [nick] está no nível [nível] e pronto para a partida!"

# print("Bem-vindos ao jogo da lilih")
# pergunta1 = input("Digite seu nome")
# pergunta2 = int(input("Digite o nivel"))
# print(f"o jogador" , pergunta1 , "está no nivel" , pergunta2 , "e pronto para a partida")

# 2. Calculadora de Mesada: Peça o valor que o aluno ganha por semana e
# multiplique por 4 para mostrar quanto ele terá no final do mês.

# valor = float(input("quanto você ganha de mesada toda semana"))
# print("no fim do mês você terá" , valor * 4)

# 3. Conversor de Internet: Peça um valor em Gigabytes (GB) e converta para
# Megabytes (MB) (multiplique por 1024). 

# print("peça um valor em gigabytes")
# gb = float(input("digite o valor gigabytes "))
# mb = gb * 1024
# print(f"{gb} GB equivalem a {mb} MB")

# 4. Média de Notas: Peça as notas de Matemática e Português. Calcule e mostre a
# média final.

# mat = float(input("digite a sua nota em português"))
# port = float(input("Digite sua nota em matemática"))
# media = (mat + port) /2
# print(f"a sua media final é {media}")

# 5. Seguidores: Peça a quantidade de seguidores atuais e quantos novos seguidores
# aluno ganhou hoje. Exiba o total atualizado.

# seguidores_atuais= int(input(" digite a quantidade de seguidores atuais"))
# novos_seguidores= int(input("quantos seguidores voce ganhou hoje"))
# soma= seguidores_atuais + novos_seguidores 
# print(f"eu tenho {seguidores_atuais+novos_seguidores}")

# 6. Idade em Dias: Peça a idade do aluno e calcule aproximadamente quantos dias
# ele já viveu (idade * 365).

# idade = int(input(" Digite a idade do aluno: "))
# dias_vividos = idade * 365
# print(f"o aluno vive aproximadamente {dias_vividos} dias")

# 7. Consumo de Lanche: Peça o preço do salgado e o preço do suco. Exiba o valor
# total da conta.

# preço_salgado = float(input("Digite o preço do salgado: "))
# preço_suco = float(input("Digite o peço do suco: "))
# total = preço_salgado + preço_suco 
# print(f"o valor total da conta é {total}")

# 8. Ano de Nascimento: Peça o ano atual e a idade do aluno. Calcule e exiba o ano
# em que ele nasceu.

# ano_atual = int(input("Digite o ano atual: "))
# idade = int(input("Digite a idade do aluno: "))
# ano_nascimento= ano_atual - idade 
# print(f"o aluno nasceu no ano de {ano_nascimento} ")

# 9. Filtro de Idade (TikTok): Peça a idade do usuário. Se for menor que 13, exiba
# "Acesso restrito". Se tiver entre 13 e 17, "Acesso moderado". Se for 18 ou
# mais, "Acesso liberado".

# idade = int(input("Digite a idade do usuario " ))
# if idade < 13: 
#      print("Acesso restrito")
# elif 13<= idade <= 17: 
#      print ("Acesso moderado")
# else:
#      print("Acesso liberado")

# 10.Bateria do Celular: Crie um while que começa com a bateria em 100. A cada
# repetição, subtraia 10 e mostre: "Bateria em [valor]%". O loop para quando
# chegar em 10 e exibe: "Por favor, conecte o carregador!".

# bateria = 100
# while bateria > 10:
#      print(f"Bateria em {bateria}% ")
#      bateria  -= 10 
# print (" por favor, conecte ao carregador!")

# 11. Contagem de Curtidas: Use um for para simular a contagem de curtidas em uma
# foto. Peça ao usuário o limite de curtidas (ex: 5). O programa deve contar de 1 até
# esse número, printando: "Curtida no [i] recebida!".

# limite = int(input("Digite o limete de curtidas: "))
# for i in range(1, limite + 1):
#      print(f"curtida no[{i}] recebida! ")

# 12.Carrinho de Compras Online: Use um while para pedir nomes de produtos que o
# aluno quer comprar. O loop só para quando ele digitar "sair". No final, mostre
# quantas vezes ele adiciona itens ao carrinho (use um contador).

# contador = 0 
# while True:
#     produto = input("Digite o nome do produto (ou 'sair' para encerrar): ")
#     if produto.lower() == "sair":
#         break
#     contador += 1
# print(f"foram adicionados {contador} itens no carrinho")