import os
from tracemalloc import stop
from usuario import Usuario, listaUsuarios
from livro import Livro, livroDeLivros
from exemplares import Exemplar

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

#■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
#■            SISTEMA BIBLIOTECA                   ■
#■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■

# ⮞LOGIN =============================================

while True:
    while True:

        cls()

        print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
        print("|           Login            |")
        print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
        print("|                            |")
        print("| ⯈ Username:                ")
        print("|   Senha:                    ")
        print("|                            |")
        print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")

        login = input("Digite o username: ")
        cls()

        print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
        print("|           Login            |")
        print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
        print("|                            |")
        print(f"|   Username: {login}        ")
        print("| ⯈ Senha:                   ")
        print("|                            |")
        print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")

        senha = input("Digite a senha: ")

        login, usuario = Usuario.logar(listaUsuarios, login, senha)

        if login:
            break
        else:
            print("Username/Senha incorreto!")
            input("Aperte enter para continuar... ")

    # FIM LOGIN ============================================================

    # ⮞MENUS ==============================================================

    print(usuario.get_tipo())
    if usuario.get_tipo() == None:
        print("Esse usuário possui erro de cadastro!")
        quit()

    if usuario.get_tipo() == "usuario":
        print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
        print(f"   {usuario.get_nome()}           {usuario.get_tipo().capitalize()} ")
        print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
        #Esse inutil só pode ver acervo, mas eu n implementei esse lixo ainda

    if usuario.get_tipo() == "bibliotecario":
        while True:

            cls()

            print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
            print(f"   {usuario.get_nome()}           {usuario.get_tipo().capitalize()} ")
            print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
            print("|                                  |")
            print("| 1) Cadastrar Livro               |")
            print("| 2) Cadastrar Exemplar            |")
            print("| 3) Cadastrar Categoria           |")
            print("| 4) Consultar Acervo              |")
            print("| 5) Sair                          |")
            print("|                                  |")
            print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")

            escolha = int(input("Escolha uma opção: "))
            
            if escolha == 1:
                def menuLivro():
                    print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
                    print("|       Cadastro de livros         |")
                    print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
                    print("| 1) Lista de livros               |")
                    print("| 2) Cadastrar livro               |")
                    print("| 3) Excluir livro                 |")
                    print("| 4) Alterar livro                 |")
                    print("| 5) Voltar                        |")
                    print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
                    
                    opcao = int(input("Escolha uma opção: "))
                    
                    if opcao == 1:
                        Livro.listarLivros(livroDeLivros)
                    if opcao == 2:
                        Livro.incluirNovoLivro(livroDeLivros)
                    if opcao == 3:
                        Livro.excluirLivro(livroDeLivros)
                    if opcao == 4:
                        Livro.alterarLivro(livroDeLivros)
                    if opcao == 5:
                        return usuario.get_tipo()
                        
                menuLivro()
            if escolha == 2:
                def menuExemplar():
                    print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
                    print("|     Cadastro de exemplares      |")
                    print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
                    print("| 1) Lista de exemplares          |")
                    print("| 2) Cadastrar exemplar           |")
                    print("| 3) Excluir exemplar             |")
                    print("| 4) voltar                       |")
                    print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
                
                    opcao = int(input("Escolha uma opção: "))
                    if opcao == 1:
                        Exemplar.consultarExemplar(livroDeLivros)
                    if opcao == 2:
                        Exemplar.incluirExemplar(livroDeLivros)
                    if opcao == 3:
                        Exemplar.excluirExemplar(livroDeLivros)
                    if opcao == 4:
                        return usuario.get_tipo()
                menuExemplar()
        
                    
                    
            if escolha == 5:
                break