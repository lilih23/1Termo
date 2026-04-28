# Exercicio 1
# 1. Contador de Produção (for)
# Uma esteira processa 10 peças por ciclo. Crie um programa que use um for para contar de 1 a 10 e, para cada número, imprima: "Peça nº X processada com suceso".
# No final, exiba "Ciclo de produção concluído".

# for ciclo in range(1,11):
#     print(f"Peça nº {ciclo} processada com sucesso... :)")
# print("Ciclo de produção concluido... :)")

# Exercicio 2 
# Imagine a produção de frutas em uma feira. Desejo apresentar as frutas bananas, manga, melancia, abacaxi. Com uma quantidade de 10 bananas , 5 mangas , 10 melancia e 13 abacaxi.
# No fim  da produção gostaria de ter um total das produções


for  bananas in range(1,20):
    print(f"bananas Nº: {bananas}")

for  manga in range(1,5):
    print(f"manga Nº {manga} foi...")

for  melancia in range(1,10):
    print(f"melancia Nº {melancia} foi...")

for  abacaxi in range(1,13):
    print(f"abacaxi Nº {abacaxi} foi...")

Total = bananas + manga + melancia + abacaxi
print("a produção final foi:", Total)

