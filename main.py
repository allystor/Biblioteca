from timeit import repeat
from bib import *

def main():
    try:
        while True:
            menuBibliotecario = ["Ir ao cadastro de um novo livro","Para cadastrar um exemplar","Para consultar o acervo","Para cadastrar categoria","Para sair"]
            print("bem vindo ao menu do bibliotecário!")
            print("Escolha uma das seguintes opções:")
            for contador, item in enumerate(menuBibliotecario):
                print(f'{contador}-{item}')
            opcao = int(input("Digite a opção desejada: "))
            while opcao == 0:
                print("Para cadastrar um novo livro, digite os seguintes dados:")
                titulo = input("Digite o titulo do livro: ")
                autor = input("Digite o autor do livro: ")
                assunto =input("Digite o assunto do livro: ")
                editora = input("Digite a editora do livro: ")
                edicao = input("Digite a edição do livro: ")
                isbn = int(input("Digite o ISBN do livro: "))
                ano = int(input("Digite o ano do livro: "))
                livro = cadastrarLivro(titulo, autor, assunto, editora, edicao, isbn, ano)
                print(f"O livro foi cadastrado com os seguintes dados:\n Titulo: {livro.get_titulo()}\n Autor: {livro.get_autor()}\n Assunto: {livro.get_assunto()}\n Editora: {livro.get_editora()}\n Edição: {livro.get_edicao()}\n ISBN: {livro.get_isbn()}\n Ano de publicação:{livro.get_ano()}")
                cadastroLivro = []
                cadastroLivro.append(livro)
                break    
    except:
        print("Ops, algo deu errado!")        
if __name__ == "__main__":
    main()
        
        