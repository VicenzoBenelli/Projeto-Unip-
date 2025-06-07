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

