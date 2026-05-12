# # 📚 Resumo Geral dos Planos de Aula Estruturados

Este documento consolida os objetivos, ementas e abordagens práticas desenvolvidas para as disciplinas de **Arquitetura IoT**, **Sistemas Operacionais**, **Levantamento de Requisitos** e **Lógica de Programação**.

---

## 1. 🌐 Arquitetura IoT
* **Foco:** Compreensão das camadas de uma solução de Internet das Coisas e a integração entre hardware e software.
* **Tópicos Abordados:**
  * **As 4 Camadas da IoT:** Percepção (Edge), Rede/Transmissão, Processamento (Nuvem) e Aplicação.
  * **Arduino:** O papel dos microcontroladores na camada de percepção para leitura de sensores e controle de atuadores.
  * **Ecossistema de Linguagens:** Uso do **C++** para a criação de firmwares eficientes na IDE do Arduino e do **Python** para a recepção de dados via comunicação Serial.

---

## 2. 🖥️ Sistemas Operacionais (SO)
* **Foco:** Analisar como o software gerencia os recursos de hardware, contrastando sistemas embarcados puros com sistemas operacionais completos.
* **Tópicos Abordados:**
  * **Abordagem Bare-Metal (Arduino/C++):** Execução de código diretamente no hardware, características de sistemas monotarefa estritos e previsibilidade (determinismo).
  * **Abordagem com SO Completo (Python/Linux):** O papel do Kernel, escalonamento preemptivo de processos, gerenciamento de memória e concorrência nativa (*Multithreading*).
  * **Conceito Chave:** A diferença prática entre a "espera ocupada" (`delay()` no C++) e o "estado bloqueado" que libera a CPU (`time.sleep()` no Python).

---

## 3. 📋 Levantamento de Requisitos
* **Foco:** Engenharia de software focada em entender o problema do cliente, documentar necessidades do produto e gerenciar o escopo de forma ágel.
* **Tópicos Abordados:**
  * **Fase de Descoberta:** Aplicação do **Design Thinking** (Empatia, Definição, Ideação, Prototipagem e Testes) e as etapas de 5 dias do **Design Sprint**.
  * **Especificação de Requisitos:** Diferenciação clara entre **Requisitos Funcionais** (o que o sistema faz) e **Requisitos Não Funcionais** (atributos de qualidade, desempenho e segurança).
  * **Gestão Ágil:** Escrita de Histórias de Usuário (*User Stories*) e dinâmica de requisitos nos frameworks **Scrum** (Product Backlog e Sprints) e **Kanban** (gestão visual do fluxo).

---

## 🐍 4. Lógica de Programação
* **Foco:** Construção dos fundamentos de algoritmos utilizando a linguagem Python, integrada a conceitos de código limpo.
* **Tópicos Abordados:**
  * **Entrada e Saída (I/O):** Interação com usuário usando `print()`, `input()` e conversão de tipos com `int()`.
  * **Estruturas Condicionais:** Tomada de decisão no código através dos blocos `if` e `else`.
  * **Estruturas de Repetição:** Controle de loops baseados em condições com `while` e baseados em intervalos/iterações com `for`.
  * **Clean Code (Código Limpo):** Boas práticas iniciais como o uso de nomes significativos para variáveis, eliminação de comentários óbvios e a aplicação do princípio KISS (*Keep It Simple, Stupid*).