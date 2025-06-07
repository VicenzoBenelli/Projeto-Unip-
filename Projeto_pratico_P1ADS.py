# Saudação de boas-vindas ao sistema
print("Bem-vindo à Livraria  do Vicenzo Benelli & Rafael Reginatto\n")

lista_livro = []
id_global = 0

# Função para cadastrar livro

def cadastrar_livro(id):
    print("-" * 38)
    print("-" * 8 + " MENU CADASTRAR LIVRO " + "-" * 8)
    print("-" * 38)
    print(f"Id do livro: {id_global}")
    nome = input("Por favor entre com o nome do livro: ")
    autor = input("Por favor entre com o autor do livro: ")
    editora = input("Por favor entre com a editora do livro: ")

    # Dicionário que armazena as variáveis dos ids, nomes, autores e editoras dos livros
    livro = {
        "id": id,
        "nome": nome,
        "autor": autor,
        "editora": editora
    }

    lista_livro.append(livro)
    print("----------------------------------------\n")

# Função para consultar livros

def consultar_livro():
    while True:
        print("-" * 40)
        print("-" * 9 + " MENU CONSULTAR LIVRO " + "-" * 9)
        print("-" * 40)
        print("1 - Consultar Todos os Livros")
        print("2 - Consultar Livro por ID")
        print("3 - Consultar Livro(s) por Autor")
        print("4 - Retornar")
        opcao = input(">> ")

        if opcao == "1":  # Consulta de todos os livros
            for livro in lista_livro:
                print("-" * 14)
                print(f"id: {livro['id']}")
                print(f"nome: {livro['nome']}")
                print(f"autor: {livro['autor']}")
                print(f"editora: {livro['editora']}")
            print("--------------\n")

        elif opcao == "2":  # Consulta por id do livro
            try:
                id_consulta = int(input("Digite o ID do livro: "))
                for livro in lista_livro:
                    if livro["id"] == id_consulta:
                        print("-" * 14)
                        print(f"id: {livro['id']}")
                        print(f"nome: {livro['nome']}")
                        print(f"autor: {livro['autor']}")
                        print(f"editora: {livro['editora']}")
                        print("--------------\n")
                        break
                else:
                    print("Livro não encontrado.\n")
            except ValueError:
                print("Digite um número válido.\n")

        elif opcao == "3":  # Consulta por autor do(s) livro(s)
            autor_consulta = input("Digite o autor do(s) livro(s): ")
            encontrou = False
            for livro in lista_livro:
                if livro["autor"].lower() == autor_consulta.lower():
                    encontrou = True
                    print("-" * 14)
                    print(f"id: {livro['id']}")
                    print(f"nome: {livro['nome']}")
                    print(f"autor: {livro['autor']}")
                    print(f"editora: {livro['editora']}")
            if not encontrou:
                print("Autor não encontrado.\n")
            print("--------------\n")

        elif opcao == "4":  # Quebra do loop interno da função
            break
        else:
            print("Opção inválida.\n")

# Função para remover livro

def remover_livro():
    print("-" * 40)
    print("-" * 10 + " MENU REMOVER LIVRO " + "-" * 10)
    print("-" * 40)

    # Loop responsável pela identificação do ID do livro que será removido
    while True:
        try:
            id_remover = int(input("Digite o ID do livro a ser removido: "))
            for livro in lista_livro:
                if livro["id"] == id_remover:
                    lista_livro.remove(livro)
                    print("Livro removido com sucesso!\n")
                    return
            print("ID inválido.\n")
        except ValueError:
            print("Digite um número válido.\n")

            # Menu principal com as opções de cadastrar, consultar, remover e sair do sistema
while True:
    print("-" * 46)
    print("-" * 15 + " MENU PRINCIPAL " + "-" * 15)
    print("Escolha a opção desejada:")
    print("1 - Cadastrar Livro")
    print("2 - Consultar Livro(s)")
    print("3 - Remover Livro")
    print("4 - Sair")
    opcao_principal = input(">> ")

    # Condicionais responsáveis por chamar as funções
    if opcao_principal == "1":
        id_global += 1
        cadastrar_livro(id_global)
    elif opcao_principal == "2":
        consultar_livro()
    elif opcao_principal == "3":
        remover_livro()
    elif opcao_principal == "4":
        break
    else:
        print("Opção inválida.\n")