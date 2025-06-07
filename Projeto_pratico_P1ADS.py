# Saudação de boas-vindas ao sistema
print("\nBem-vindo à Livraria do Vicenzo Benelli & Rafael Reginatto\n")

lista_livro = []
id_global = 0

# Função para cadastrar livro
def cadastrar_livro(id):
    print("\n" + "-" * 38)
    print("-" * 8 + " MENU CADASTRAR LIVRO " + "-" * 8)
    print("-" * 38)
    print(f"Id do livro: {id}")
    nome = input("Por favor entre com o nome do livro: ")
    autor = input("Por favor entre com o autor do livro: ")
    editora = input("Por favor entre com a editora do livro: ")

    livro = {
        "id": id,
        "nome": nome,
        "autor": autor,
        "editora": editora
    }

    lista_livro.append(livro)
    print("\nLivro cadastrado com sucesso!\n")

# Função para consultar livros
def consultar_livro():
    while True:
        print("\n" + "-" * 40)
        print("-" * 9 + " MENU CONSULTAR LIVRO " + "-" * 9)
        print("-" * 40)
        print("1 - Consultar Todos os Livros")
        print("2 - Consultar Livro por ID")
        print("3 - Consultar Livro(s) por Autor")
        print("4 - Retornar")
        opcao = input(">> ")

        if opcao == "1":
            print("\nLista de todos os livros:")
            for livro in lista_livro:
                print("-" * 14)
                print(f"id: {livro['id']}")
                print(f"nome: {livro['nome']}")
                print(f"autor: {livro['autor']}")
                print(f"editora: {livro['editora']}")
            print("--------------\n")

        elif opcao == "2":
            try:
                id_consulta = int(input("\nDigite o ID do livro: "))
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
                    print("\nLivro não encontrado.\n")
            except ValueError:
                print("\nDigite um número válido.\n")

        elif opcao == "3":
            autor_consulta = input("\nDigite o autor do(s) livro(s): ")
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
                print("\nAutor não encontrado.\n")
            print("--------------\n")

        elif opcao == "4":
            break
        else:
            print("\nOpção inválida.\n")

# Função para remover livro
def remover_livro():
    print("\n" + "-" * 40)
    print("-" * 10 + " MENU REMOVER LIVRO " + "-" * 10)
    print("-" * 40)

    while True:
        try:
            id_remover = int(input("\nDigite o ID do livro a ser removido: "))
            for livro in lista_livro:
                if livro["id"] == id_remover:
                    lista_livro.remove(livro)
                    print("\nLivro removido com sucesso!\n")
                    return
            print("\nID inválido.\n")
        except ValueError:
            print("\nDigite um número válido.\n")

# Menu principal
while True:
    print("\n" + "-" * 46)
    print("-" * 15 + " MENU PRINCIPAL " + "-" * 15)
    print("\nEscolha a opção desejada:")
    print("1 - Cadastrar Livro")
    print("2 - Consultar Livro(s)")
    print("3 - Remover Livro")
    print("4 - Sair")
    opcao_principal = input(">> ")

    if opcao_principal == "1":
        id_global += 1
        cadastrar_livro(id_global)
    elif opcao_principal == "2":
        consultar_livro()
    elif opcao_principal == "3":
        remover_livro()
    elif opcao_principal == "4":
        print("\nSaindo do sistema...\n")
        break
    else:
        print("\nOpção inválida.\n")
