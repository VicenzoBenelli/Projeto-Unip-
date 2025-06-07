# Projeto-Unipê

- Projeto Pratico Avaliativo ministrado pelo professor Jeofton Costa Melo

- ALUNOS: Vicenzo Benelli e Rafael Reginatto

# Descrição do projeto:

Este projeto é um sistema interativo desenvolvido em Python para gerenciar um pequeno acervo de livros em uma livraria fictícia chamada "Livraria do Vicenzo Benelli". O sistema segue o paradigma procedural e é totalmente baseado em terminal, utilizando entradas do usuário para realizar as operações.

Ao iniciar o programa, o usuário é saudado com uma mensagem de boas-vindas e, em seguida, acessa um menu principal com quatro opções: Cadastrar Livro, Consultar Livro(s), Remover Livro, ou Sair do sistema.

# Cadastro de Livros
A funcionalidade de cadastro permite ao usuário inserir informações de um novo livro, incluindo:

 - Nome do livro

 - Autor

 - Editora

Cada livro recebe um ID único incremental (id_global), que é controlado fora da função de cadastro. Os livros são armazenados como dicionários dentro de uma lista global (lista_livro), que atua como um pequeno banco de dados em memória.

# Consulta de Livros
O sistema de consulta oferece ao usuário três opções:

 1- Listar todos os livros cadastrados

 2- Consultar um livro específico por ID

 3- Consultar todos os livros de um determinado autor

A busca é realizada por meio de iteração sobre a lista de livros. Para garantir maior flexibilidade, a busca por autor é case-insensitive.

# Remoção de Livros
O sistema também permite que livros sejam removidos com base em seu ID. O usuário fornece o ID desejado e, se encontrado, o livro correspondente é excluído da lista. Caso contrário, o sistema informa que o ID é inválido. A entrada é protegida com tratamento de exceções para garantir que apenas números válidos sejam aceitos.

# Estrutura do Programa
O código é organizado com funções separadas para cada operação principal:

 - cadastrar_livro(id)

 - consultar_livro()

 - remover_livro()

A execução é controlada por um laço principal (while True) que exibe o menu e delega as ações conforme a escolha do usuário. A execução continua até que o usuário escolha explicitamente a opção de sair.

# Características Técnicas
 - Linguagem: Python

 - Paradigma: Procedural

 - Entrada/Saída: Interativa via terminal

 - Armazenamento: Volátil (em memória, sem persistência em disco)

 - Estrutura de dados: Lista de dicionários