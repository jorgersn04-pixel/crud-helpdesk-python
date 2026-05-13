# Sistema de Triagem de Chamados (CRUD)

Um sistema simples de linha de comando desenvolvido em Python para gerenciar chamados de suporte técnico. 

Fiz este projeto para treinar a base da linguagem, aplicar a lógica de programação na prática e entender como funciona o fluxo de um sistema real, sem depender de interfaces gráficas complexas por enquanto.

## Como funciona
A ideia principal do sistema é focar na triagem: os chamados entram em uma fila, e o operador tem a responsabilidade de ler o problema e decidir manualmente para qual técnico aquele chamado será encaminhado.

## O que o sistema faz
*   **Abrir chamado:** Registra o problema e a descrição.
*   **Listar:** Mostra todos os chamados abertos de forma organizada.
*   **Encaminhar:** O operador escolhe o chamado pelo número e define o técnico responsável.
*   **Fechar:** Deleta o chamado da fila quando resolvido.

## O que aprendi e apliquei neste código
*   **Python puro:** Uso de listas e dicionários para guardar os dados na memória.
*   **Lógica e repetição:** Uso de laços `while` e `for`, além de condicionais `if/else` para construir os menus.
*   **Tratamento de erros:** Uso de `try/except` para impedir que o programa quebre caso o usuário digite uma letra no lugar de um número.
*   **Validações simples:** Travas para impedir que o usuário crie um chamado vazio ou coloque números no nome do técnico.

## Como testar o código
1. Tenha o Python instalado no seu computador.
2. Baixe o arquivo `main.py`.
3. Abra o terminal (ou prompt de comando) na pasta do arquivo.
4. Rode o comando: `python main.py`
