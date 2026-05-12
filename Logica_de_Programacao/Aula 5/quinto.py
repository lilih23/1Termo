# # Pergunta1 
# nick = input("Qual é o nome do jogador?...")
# nivel = int(input("Qual é o nível?..."))
# print(f"O jogador {nick} está no nivel {nick} e pronto para a partida!")

# # Pergunta2
# print("Calculadora de mesada")
# valor_semana = float(input("Quando você ganha por semana?..."))
# total = valor_semana * 4
# print(f"Sua mesada no fim do mês foi de... {total}")

# # Pergunta3
# print("Conversor de internet")
# gigi = float("Digite o valor em gigabytes...")
# meg = gigi * 1024
# print(f"O valor convertido em megabytes seria de... {meg}")

# Pergunta4
# print("Média das notas")
# mat = float(input("Digite sua nota de Matemática"))
# port = float(input("Digite sua note de portugues"))
# media = (mat + port) / 2
# print(f"Sua média de matematica e portugues...{media}")

# Pergunta5
# seg_atual = int(input("Quantos seguidores você possui?"))
# seg_novos = int(input("Quantos novos você ganhou?"))
# seg_atualizado = seg_atual + seg_novos
# print(f"Você possui {seg_atualizado} um total atualizado de seguidores")

# Pergunta6 
# print("idade e dias")
# idade = int(input("Digite sua idade"))
# idade_dias = idade * 365
# print(f"A quantidade de dias vividos são {idade_dias}")

# Pergunta7
# print("consumo do lanche")
# salgado = float(input("Qual o valor do salgado...?"))
# suco = float(input("Qual o valor do suco...?")) 
# total = salgado + suco 
# print(f"sua compra ficou no valor de ... {total:.2f}")
# print("sua compra foi im total de R$..." ,round(total,2))

# Pergunta8
# print("Ano de nascimento")
# ano_atual = int(input("Digite o ano do seu ano atual"))
# idade = int(input("Quantos você irá fazer esse ano?"))
# ano_nasc = ano_atual - idade 
# print(f"O ano que você nasceu {ano_nasc}")

# Pergunta9 
# print("Filtro de idade (tiktok)")
# idade = int(input("Qual é sua idade...?"))

# if idade < 13: 
#     print("Acesso Restrito!")
# elif 13 < idade < 17: #entre esse intervalo
#     print("Acesso Moderado")
# elif idade >= 18: 
#     print("Acesso liberado")
# else: 
#     print("idade invalida")


# Pergunta10
# print("Bateria de calcular... Carregamento")
# import time 
# bateria = 100 

# while bateria > 10:
#     print(f"Bateria em {bateria}%")
#     bateria =- 10 
#     time.sheep(1)
# print("Por favor conecte o carregador!")

# Pergunta11
# print("Contagem de curtidas ")
# import time
# limite = int(input("Digite a quantidade de curtidas"))
# for curtidas in range(1, limite + 1):
#     print(f"Curtida nº {curtidas} recebida!")
#     time.sheep(0.5)

# Pergunta12
# print("carrinho de compras Online")
# print("Digite Sair para encerrar o sistema")
# contador = 0 
# produto = 0

# while produto.lower() != "sair":
#     produto = input("Digite o nome do produto")
#     contador += 1 
#     if produto.lower() != "sair"
#     print(f"Produto '{produto}' adicionado ao carrinho!")
#           print(f"Compra finalizada você dicionou {contador-1} itens ao seu carrinho!")
# print("obrigado por comprar conosco")

# print("Carrinho de compras online - vesao 2.0")
#  contador = 0
#  produto = 0 
#  while produto


# 1. Registro de Veículo: Peça o modelo do veículo e a placa. ○ Exiba: "Veículo [Modelo] de placa [Placa] registrado no sistema. Boa viagem!" 

# def registrar_veiculo() -> None:
#     """Solicita dados do usuário e confirma o registro do veículo."""
    
#     modelo = input("Digite o modelo do veículo: ").strip()
#     placa = input("Digite a placa do veículo: ").strip()

    # O uso de f-strings torna a leitura muito mais clara e direta
    # print(f"\nVeículo {modelo} de placa {placa} registrado no sistema. Boa viagem!")

# if __name__ == "__main__":
    # registrar_veiculo()