from livro import Livro, listaLivros

def menu():

    print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
    print("■              BIBLIOTECA                ■")
    print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
    print("■ 1 - Listar titulos                     ■")
    print("■ 2 - Adicionar livro                    ■")
    print("■ 3 - Excluir livro                      ■")
    print("■ 4 - Alterar livro                      ■")
    print("■ 5 - Listar todas informações           ■")
    print("■ 0 - Sair                               ■")
    print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")

menu()
escolha = int(input("Escolha uma opção: "))

while escolha != 0:
    if escolha == 1:
        print("batata")
        for i in listaLivros:
            print(i.get_titulo())

    if escolha == 2:
        Livro.incluirLivro(listaLivros)
    
    if escolha == 3:
        Livro.excluirLivro(listaLivros)

    if escolha == 4:
        Livro.alterarLivro(listaLivros)
    
    if escolha == 5:
        for i in listaLivros:
                print("\n")
                print(f"Titulo: {i.get_titulo()}\n Autor: {i.get_autor()}\n Assunto: {i.get_assunto()}\n Editora: {i.get_editora()}\n Edição: {i.get_edicao()}\n ISBN: {i.get_isbn()}\n Ano de publicação:{i.get_ano()}")
                print("\n")

    menu()
    escolha = int(input("Escolha uma opção: "))


