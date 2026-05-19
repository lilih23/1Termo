# Markdown
# 🐍 Plano de Aula: Lógica de Programação com Python & Clean Code

## 1. 📝 Introdução às Entradas e Saídas (I/O) e Tipos de Dados
<!-- Para iniciar na programação, precisamos entender como o nosso programa se comunica com o usuário e como ele armazena informações básicas.

### 📢 A Função `print()`
É a nossa saída padrão. Usada para exibir textos, números ou resultados de operações na tela.

```python
# Exemplo simples de saída
print("Olá, mundo! Bem-vindos à aula de Lógica.")
📥 A Função input()
Permite que o usuário interaja com o programa, inserindo dados através do teclado. Atenção: Por padrão, tudo o que o input() captura é tratado como texto (String).

Python
nome = input("Digite o seu nome: ")
print("Seja bem-vindo,", nome)
🔢 O Tipo de Dado int() (Conversão/Casting)
O int representa números inteiros (sem casas decimais). Quando precisamos fazer cálculos com um número digitado no input(), devemos converter esse texto em um número inteiro usando int().

Python
# Sem a conversão 'int()', o Python juntaria os textos (ex: "2" + "3" viraria "23")
idade = int(input("Digite sua idade: "))
anos_para_cem = 100 - idade
print("Faltam", anos_para_cem, "anos para você completar um século!")
2. 🔀 Estruturas Condicionais (if, else)
As estruturas condicionais permitem que o programa tome decisões e siga caminhos diferentes dependendo de uma condição (verdadeira ou falsa).

if (Se): Executa um bloco de código se a condição for verdadeira.

else (Senão): Executa um bloco alternativo caso a condição do if seja falsa.

Python
nota = int(input("Digite a nota do aluno (0 a 100): "))

if nota >= 60:
    print("🎉 Aluno Aprovado!")
else:
    print("📚 Aluno em Recuperação.")
3. 🔄 Estruturas de Repetição / Loops (while, for)
Loops são utilizados para executar o mesmo bloco de código várias vezes, evitando repetição desnecessária de linhas de código.

🔁 O Loop while (Enquanto)
Executa o código repetidamente enquanto uma condição específica continuar sendo verdadeira. É ideal para quando não sabemos exatamente quantas vezes o código vai rodar.

Python
# Contador simples
contador = 1

while contador <= 5:
    print("Contagem:", contador)
    contador += 1 # Incrementa o contador para não gerar um loop infinito
➰ O Loop for (Para)
Usado para iterar sobre uma sequência (como uma lista de elementos) ou dentro de um intervalo definido. Geralmente utiliza a função range() para gerar uma sequência de números.

Python
# Repete o código de 0 até 4 (o número 5 é exclusivo)
for i in range(5):
    print(f"Esta é a repetição número {i}")
🧼 4. Boas Práticas: Introdução ao Clean Code (Código Limpo)
Escrever código que funciona é apenas metade do trabalho. A outra metade é escrever um código que seja fácil de ler e manter por você ou por outros desenvolvedores.

📐 Regras Básicas de Clean Code para Iniciantes:
Nomes Significativos: Variáveis e funções devem dizer claramente o que fazem. Evite nomes como x, y, a1, temp.

❌ Ruim: v = 10

✅ Bom: velocidade_maxima = 10

Evite Comentários Óbvios: O código deve ser autoexplicativo. Use comentários apenas para explicar o porquê de algo complexo, não o o que a linha faz.

❌ Ruim: print("Oi") # Imprime Oi na tela

Mantenha a Simplicidade (KISS - Keep It Simple, Stupid): Não complique a lógica se houver uma maneira mais direta e legível de resolver o problema.

📊 Comparação Prática de Clean Code
Código Confuso (Bad Code):

Python
x = int(input())
if x > 18:
 print("pode")
else:
 print("nao")
Código Limpo (Clean Code):

Python
# Variável com nome claro, indentação correta e mensagens amigáveis
idade_usuario = int(input("Por favor, digite a sua idade: "))
MAIORIDADE_LEGAL = 18

if idade_usuario >= MAIORIDADE_LEGAL:
    print("Acesso autorizado: Usuário é maior de idade.")
else:
    print("Acesso negado: Usuário é menor de idade.")
🛠️ 5. Desafio Prático para os Alunos
Exercício: O Jogo da Adivinhação
Peça para os alunos criarem um script onde:

O programa define um número secreto fixo (ex: numero_secreto = 7).

Usando um loop while, o programa pede para o usuário tentar adivinhar o número (usando input e int).

Usando if e else, o programa parabeniza o usuário se ele acertar e encerra o loop. Se ele errar, diz que está incorreto e pede um novo palpite.

Regra de Ouro: O código do aluno deve seguir as regras de Clean Code (nomes de variáveis claros e organização). -->