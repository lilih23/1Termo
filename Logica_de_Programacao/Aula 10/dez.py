# Projeto de cancela


print("Bem-vindo ao shopping da lilih")
print("Escolha as opções")
print("1 - ticket \n 2 - Tag \n 3 - interfone")
metodo_entrada = input(" Ticket / Tag / interfone")

try:

    if metodo_entrada == "ticket":
        print("Bem-vindo ao shopping da lilih")
        
        hora_entrada = float(input("digite a hora de entrada"))
        valor_estacionamento = float(input("digite o valor a cobrar"))
        hora_saida = float(input("digite o hora da saida"))
        total_permanencia = hora_entrada - hora_saida
        print(f"Seu tempo de permanencia {total_permanencia} em horas")
        total_estacionamento = total_permanencia * valor_estacionamento
        print(f"O valor a ser cobrado foi de R${total_estacionamento:.2f}")
        print("Devolver Ticket")

    elif metodo_entrada == "Tag":
        print("Bem-Vindo ao Shopping da lilih")
        
        print("Sua permanência no Shopping será cobrada na sua fatura")


    elif metodo_entrada == "Interfone":
        print("Bem-Vindo ao Shopping da lilih")
        print("Liberando acesso pelo Interfone")
        print("Sua saída deverá ser feita também pelo Interfone")

    else:
        print("Obrigado pela visita, volte sempre para gastar seu dinheiro no shopping da lilih, para mim ficar rica")

except ValueError:
    print("Erro")