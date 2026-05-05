# Clean Code - Aula 6
# Para que usar?
# Como usar?
# print("clean code - Aula 6")
# aula = 6 
# print(f"Estamos na aula {aula} de clean code")

# # Manipulação de arquivo e Texto
# texto = "  Python é Muito legal!  "
# print(texto.strip().upper()) # "PYTHON"
# print(texto.strip().lower()) # "python"
# print(texto.strip().capitalize()) # "Python"
# print(texto.strip().title()) # "Python"
# print(texto.strip().replace(" ", "_" )) # "Python"
# print(texto.strip().split()) # ["Python"]

# Escevendo
# with open("notas.txt", "w") as arquivo:
#     arquivo.write("Estudar Python hoje!")
#     arquivo.write("\nler sobre Clean Code.")

# # Lendo
# with open("notas.txt", "r") as arquivo:
#     conteudo = arquivo.read()
#     print(conteudo)

# Exercicio 1:
# Crie um programa que peça ao asuárioa para inserir uma frase e, em seguida, exiba a frase com as seguintes transformações:
# - Remova os espaços extras no início e no final da frase.

# frase = input("Digite sua frase")
# print(frase.strip().upper()) # "PYTHON"

# jeito do professor 
# frase = input("Digite uma frase: ")
# print(frase.strip())

# # - Converta a frase para letras maiúsculas.
# print(frase.strip().upper())

# Exemplo 1:
# Crie um programa que leia o conteúdo de um arquivo de texto e conte quantas vezes a palavras "Python" aparece no arquivo. Exiba o resultado para o usuário.

# print("Contagem de palavras em arquivo")
# with open("notas.txt", "r") as arquivo:
#     conteudo = arquivo.read()
#     contagem = conteudo.count("Python")
#     print(f"A contagem de palavras {contagem} é de...")

# Execução de comandos do sistema 
import os # importa o módulo os para interagir com o sistema operacional
# Onde estou?
# print(os.getcwd())
# Lista arquivos da pasta 
# print(os.listdir())
# print(os.listdir("..")) # Lista arquivo da pasta pai
# print(os.listdir("..\\..")) # Lista arquivo da pasta avô
# print(os.listdir("C:\\")) # Lista arquivo da raiz do C
# print(os.listdir("C:\\Users")) # Lista arquivo da pasta Users
# print(os.listdir("C:\\Users\\Public")) # Lista de arquivo da pasta Public

# Outros comandos úteis
# # Criar pasta 
# os.mkdir("nova_pasta")
# # Renomear pasta
# os.rename("nova_pasta", "pasta_renomeada")
# # # Excluir pasta
# os.rmdir("pasta_renomeada")

# Exercicio 2: 
# Crie um script que mostre o caminho da pasta atual.
# print(os.getcwd())

# # Exercicio 3:
# # Lista os arquivos da pasta atual.
# print(os.listdir())

# # Exercicio 4:
# # Crie uma pasta chamada "projetos" e depois renome para "meus_projeos". Por fim, esclua a pasta 
# os.mkdir("projetos")
# os.rename("projetos", "meus_projetos")
# os.rmdir("meus_projetos")

# # Exercicio 5: 
# Crie um arquivo chamado "log.txt" e escreva a mensagem "Log de atividade". Depois, leia o conteúdo do arquivo e exiba a tela.
# with open("log.txt", "w") as arquivo:
#     arquivo.write("Log de atividade")
# with open("log.txt","r") as arquivo:
#     conteudo = arquivo.read()
#     print(conteudo)

# Exemlo de dicionário:
# Crie um dicionário com informações sobre uma pessoa e acesse um valor usando uma chave.

# pessoa = {
#     "nome": "Alice",
#     "idade": 30,
#     "cidade": "São Paulo", 
#     "profissão": "Engenheira"
# }
# pessoa2 = {
#     "nome": "Bruno",
#     "idade": 25,
#     "cidade": "SP",
#     "profissão": "Designer"
# }
# print(pessoa["profissão"])
# print(pessoa2["nome"], pessoa["idade"])

# comida = {
#     "nome": "strogonoff",
#     "ingrediente":"frango" "Creme de leite" ,
#     "sabor": "frango",
# }

# Exemplo2  2: Deligar o PC (comando para Windows)
with open("desliga.bat", "w") as desligar:
    desligar.write("shutdown -s -t 0 -c \"Desliamento programado para daqui a 1 hora. Salve seu trabalho!\"")

#     # -s comando para desligar 
#     # -t tempo definir 
#     # -a cancelar desligamento