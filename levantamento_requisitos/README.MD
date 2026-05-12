# # 📋 Plano de Aula: Engenharia e Levantamento de Requisitos

## 1. 🧠 Fase de Descoberta: Design Thinking & Design Sprint
Antes de documentar o que o sistema deve fazer, precisamos entender a fundo o problema do usuário. Para isso, utilizamos abordagens centradas no ser humano.

### 👥 Design Thinking
É uma abordagem estruturada para gerar inovação e solucionar problemas complexos focada em empatia. Divide-se tradicionalmente em 5 etapas:

1. **Empatia (Empathize):** Entender as dores, necessidades e o contexto dos usuários reais.
2. **Definição (Define):** Filtrar as informações coletadas para definir claramente o problema central a ser resolvido.
3. **Ideação (Ideate):** Sessões de *brainstorming* para gerar o maior número possível de soluções criativas livres de julgamentos.
4. **Prototipagem (Prototype):** Construir versões baratas e de baixa fidelidade das ideias geradas (desenhos, wireframes, maquetes).
5. **Testes (Test):** Colocar o protótipo na mão dos usuários para coletar feedbacks rápidos antes do desenvolvimento real.

### ⏱️ Design Sprint
Criado pela *Google Ventures*, é um método ágil de **5 dias** para validar ideias e resolver grandes problemas de negócio através de design, prototipagem e teste com clientes, pulando o ciclo longo de desenvolvimento.

* **Segunda-feira (Mapear):** Compreender o desafio e escolher um foco.
* **Terça-feira (Esboçar):** Desenhar soluções concorrentes no papel.
* **Quarta-feira (Decidir):** Escolher a melhor solução por meio de votação.
* **Quinta-feira (Prototipar):** Construir um protótipo rápido e realista.
* **Sexta-feira (Testar):** Testar o protótipo com clientes reais.

---

## 2. 📑 Engenharia de Requisitos: Funcionais vs. Não Funcionais
Uma vez mapeado o problema, as necessidades são traduzidas em requisitos de software. Eles especificam o que o sistema deve fazer e sob quais restrições.

### 🟢 Requisitos Funcionais (RF)
Definem **o que o sistema deve fazer**. Representam as funcionalidades, ações e comportamentos diretos que o software deve oferecer ao usuário.

* *Exemplo 1:* O sistema deve permitir que o usuário recupere sua senha digitando o e-mail cadastrado.
* *Exemplo 2:* O sistema deve gerar um relatório mensal de vendas em formato PDF.

### 🔵 Requisitos Não Funcionais (RNF)
Definem **como o sistema deve funcionar**. Representam restrições de qualidade, atributos técnicos, segurança, desempenho, usabilidade ou conformidade regulatória.

* *Exemplo 1 (Desempenho):* O sistema deve processar as consultas de busca em menos de 2 segundos sob uma carga de 500 usuários simultâneos.
* *Exemplo 2 (Segurança):* Todas as senhas dos usuários armazenadas no banco de dados devem ser criptografadas usando o algoritmo SHA-256.

---

## 3. 🏃‍♂️ Metodologias Ágeis no Levantamento e Gestão
Em ambientes modernos, o levantamento de requisitos não acontece de forma engessada (Cascata), mas sim de maneira **iterativa e incremental**.

### 🧩 Escrita de Requisitos no Ágil: Histórias de Usuário (User Stories)
Os requisitos funcionais geralmente são documentados na forma de histórias simples sob a perspectiva de quem usará o recurso. O formato padrão é:

> **Como** [tipo de usuário],  
> **Eu quero** [alguma funcionalidade],  
> **Para que** [eu obtenha algum benefício ou valor].

* **Exemplo:** *"Como cliente do banco, eu quero ler o código de barras de um boleto usando a câmera do celular para que eu possa pagar minhas contas sem precisar digitar os números."*

### 🛠️ Frameworks Populares

#### Scrum
* **Product Backlog:** A lista viva e priorizada de todos os requisitos do sistema (gerenciada pelo *Product Owner*).
* **Sprint Backlog:** O conjunto de requisitos selecionados para serem desenvolvidos em um ciclo curto (geralmente de 2 a 4 semanas).
* **Mudança de Escopo:** O escopo é flexível entre as Sprints, permitindo reavaliar novos requisitos à medida que o mercado ou o cliente mudam de opinião.

#### Kanban
* **Foco em Fluxo:** Visualização das demandas por cartões em colunas (A Fazer, Em Desenvolvimento, Em Teste, Concluído).
* **Gestão de Requisitos:** O levantamento é feito de forma contínua (*Just-in-Time*). Assim que o time ganha capacidade, novos requisitos são puxados e refinados.

---

## 📊 4. Tabela Resumo da Aula

| Conceito | Foco Principal | Quando é Aplicado no Projeto? |
| :--- | :--- | :--- |
| **Design Thinking** | Entender o usuário e descobrir o problema real | Fase Inicial / Descoberta (*Discovery*) |
| **Design Sprint** | Validar uma ideia específica em 5 dias | Validação rápida de novos conceitos ou módulos |
| **Requisitos Funcionais** | Comportamento e funções diretas do software | Durante o refinamento técnico das tarefas |
| **Requisitos Não Funcionais** | Arquitetura, qualidade e restrições técnicas | Definição da arquitetura e critérios de aceitação |
| **Metodologias Ágeis** | Entregar valor rápido e aceitar mudanças de escopo | Durante todo o ciclo de desenvolvimento e entrega |

---

## 🛠️ 5. Atividade Prática Sugerida

**Desafio "Uber das Entregas de Drone":**
1. Divida a turma em grupos e peça para mapearem **3 Requisitos Funcionais** e **3 Requisitos Não Funcionais** essenciais para o aplicativo funcionar.
2. Peça para converterem um dos requisitos funcionais no formato padrão de **História de Usuário**.