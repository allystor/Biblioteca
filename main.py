from array import array
from bib import *

def main():
    cadastroLivro = []
    try:
        while True:
            print("------------Menu do bibliotecário----------------")
            menuBibliotecario = ["Opções do livros","Para cadastrar um exemplar","Para consultar o acervo","Para cadastrar categoria","Para sair"]
            print("bem vindo ao menu do bibliotecário!")
            print("Escolha uma das seguintes opções:")
            for contador, item in enumerate(menuBibliotecario):
                print(f'{contador + 1}-{item}')
            opcao = int(input("Digite a opção desejada: "))
            print("----------------------------------------------------")
            while opcao == 1:
                print("----------------Opções dos livros--------------")
                menulivro = ["Criar livro","Alterar livro","Remover livro", "Sair"]
                print("Escolha uma das seguintes opções:")
                print("----------------------------------------------------")
                for contador, item in enumerate(menulivro):
                    print(f'{contador + 1}-{item}')
                opcao = int(input("Digite a opção desejada: "))
                while opcao == 1:
                    print("Para cadastrar um novo livro, digite os seguintes dados:")
                    titulo = input("Digite o titulo do livro: ")
                    autor = input("Digite o autor do livro: ")
                    assunto =input("Digite o assunto do livro: ")
                    editora = input("Digite a editora do livro: ")
                    edicao = input("Digite a edição do livro: ")
                    isbn = int(input("Digite o ISBN do livro: "))
                    ano = int(input("Digite o ano do livro: "))
                    livro = Livro(titulo, autor, assunto, editora, edicao, isbn, ano)
                    print(livro.__str__())
                    cadastroLivro.append(livro)
                    prosseguir = int(input("Para criar um novo outro livro, digite 1. Para voltar ao menu anterior, digite 2: "))
                    if prosseguir == 2:
                        break
                while opcao == 2:
                    print("Para alterar um livro, digite os seguintes dados:")
                                  
    except:
        print("Ops, algo deu errado!")        
if __name__ == "__main__":
    main()
        
        