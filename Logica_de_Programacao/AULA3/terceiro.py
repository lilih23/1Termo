# 1. O laço 'for'(Repetições Determinadas)
# Use o 'for' quando você sabe exatamente quantas vezes algo deve acontecer (como ler 10 sensorres ou processar ma lista de peças).
# Exemplo: Relatório de Produção Diária 
# Imagine que você tem uma meta de prodizir 5 lotes e quer numerar cada um:

# Exemplo 1
# for lote in range(1, 6):
#     print(f"Processando lote número (lote)...")
#     print("Quantidade verificado.[OK]")
#     print("Podução do dia finalizada!")

# Exemplo 2
# for b in range(10):
#     print(f"Quantidade total {b} foi...")

# Exemplo 3
# Imagine o seguinte cenáro, iremos produzir 20 discos de vinil.

# Exemplo 5 
# Imagine a seguinte situação gostaria de ter um menu pudesse perguntar qual opção você desejo e a partir da seleção ele listar os produtos

# print("Bem-vindos a loja da lilih")
# print("Opção 1- pefumes")
# print("Opção 2- maquiagem")
# menu = int(input("Escolha uma opção"))

# perfumes = ["doce", "amadeirado", "citrico"]
# maquiagem = ["cilios", "rimel", "batom"]

# if menu ==1:
#      for item1 in perfumes:
#           print(f"Sua lista de item de perfumes {perfumes} são...")

# elif menu == 2:
#      for item1 in maquiagem:
#           print(f"Sua lista de maquiagem {maquiagem} são...")
# else:
#      print("Opção inválida: Encerrando o sistema")