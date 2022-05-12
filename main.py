from livro import Livro, listaLivros

def menu():
    print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
    print("■              BIBLIOTECA                ■")
    print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
    print("■ 1 - Livros                             ■")
    print("■ 2 - Exemplares                         ■")
    print("■ 3 - Categorias                         ■")
    print("■ 4 - Acervos                            ■")
    print("■ 0 - Encerrar                           ■")
    print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
menu()

def livros():
    print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
    print("■              lIVROS                    ■")
    print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
    print("■ 1 - Listar titulos                     ■")
    print("■ 2 - Adicionar livro                    ■")
    print("■ 3 - Excluir livro                      ■")
    print("■ 4 - Alterar livro                      ■")
    print("■ 5 - Listar todas informações           ■")
    print("■ 0 - Voltar                             ■")
    print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")

def exemplares():
    print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
    print("■               EXEMPLARES               ■")
    print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
    print("■ 1 - Listar exemplares                  ■")
    print("■ 2 - Adicionar exemplar                 ■")
    print("■ 3 - Excluir exemplar                   ■")
    print("■ 4 - Alterar exemplar                   ■")
    print("■ 5 - Listar todas informações           ■")
    print("■ 0 - Voltar                             ■")
    print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")

def categorias():
    print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
    print("■              CATEGORIAS                ■")
    print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
    print("■ 1 - Listar categorias                  ■")
    print("■ 2 - Adicionar categoria                ■")
    print("■ 3 - Excluir categoria                  ■")
    print("■ 4 - Alterar categoria                  ■")
    print("■ 5 - Listar todas informações           ■")
    print("■ 0 - Voltar                             ■")
    print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")      

def acervos():
    print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
    print("■              ACERVO                   ■")
    print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
    print("■ 1 - Listar acervo                     ■")
    print("■ 2 - Adicionar acervo                  ■")
    print("■ 3 - Excluir acervo                    ■")
    print("■ 4 - Alterar acervo                    ■")
    print("■ 5 - Listar todas informações          ■")
    print("■ 0 - Voltar                            ■")
    print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")

escolha = int(input("Escolha uma opção: "))

while escolha != 0:
    if escolha == 1:
        livros()
    if escolha == 2:
        exemplares()
    if escolha == 3:
        categorias()
    if escolha == 4:
        acervos()
    if escolha == 0:
        print("Saindo...")
        break 
         
livro = int(input("Escolha uma opção: "))

while livro != 0:
    if livro == 1:
        print("batata")
        for i in listaLivros:
            print(i.get_titulo())

    if livro == 2:
        Livro.incluirLivro(listaLivros)
    
    if livro == 3:
        Livro.excluirLivro(listaLivros)

    if livro == 4:
        Livro.alterarLivro(listaLivros)
    
    if livro == 5:
        for i in listaLivros:
                print("\n")
                print(f"Titulo: {i.get_titulo()}\n Autor: {i.get_autor()}\n Assunto: {i.get_assunto()}\n Editora: {i.get_editora()}\n Edição: {i.get_edicao()}\n ISBN: {i.get_isbn()}\n Ano de publicação:{i.get_ano()}")
                print("\n")

    livros()
    if livro == 0:
        menu()
        
    livro = int(input("Escolha uma opção: "))


    


