import os
from this import d
from categoria import *
from usuario import *
from livro import *

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

#■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
#■            SISTEMA BIBLIOTECA                   ■
#■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■

# ⮞LOGIN =============================================
try:
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
            while True:

                cls()

                print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
                print(f"   {usuario.get_nome()}    ■      {usuario.get_tipo().capitalize()} ")
                print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
                print("| 1) Consultar Acervo              |")
                print("| 2) Sair                          |")
                print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")

                #Esse inutil só pode ver acervo, mas eu n implementei esse lixo ainda

                escolha = int(input("Escolha uma opção: "))

                if escolha == 1:
                    print("FUNÇÃO NÃO IMPLEMENTADA!!")
                    input("Aperte enter para continuar... ")
                
                if escolha == 2:
                    break

        if usuario.get_tipo() == "bibliotecario":
            while True:

                #■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ MENU B ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■

                cls()

                print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
                print(f"   {usuario.get_nome()}     ■     {usuario.get_tipo().capitalize()} ")
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

                    #■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ LIVRO ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■#

                    while True:
                        cls()

                        print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
                        print(f"   {usuario.get_nome()}           {usuario.get_tipo().capitalize()} ")
                        print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
                        print("|             LIVRO                |")
                        print("|                                  |")
                        print("| 1) Incluir novo livro            |")
                        print("| 2) Alterar dados do livro        |")
                        print("| 3) Consultar dados do livro      |")
                        print("|                                  |")
                        print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")

                        escolha = int(input("Escolha uma opção: "))

                        if escolha == 1:

                            cls()

                            print("Incluindo novo livro...")

                            titulo = str(input("Digite o titulo do livro: "))
                            autor = str(input("Digite o autor do livro: "))
                            assunto = str(input("Digite o assunto do livro: "))
                            editora = str(input("Digite a editora do livro: "))
                            edicao = input("Digite a edição do livro: ")
                            isbn = input("Digite o ISBN do livro: ")
                            ano = input("Digite o ano do livro: ")
                            categoria = input("Digite a categoria do livro: ")

                            teste = Livro.incluirLivro(titulo, autor, assunto, editora, edicao, isbn, ano, categoria)

                            if teste:
                                print("")
                                print(f"Livro '{titulo}' Adiconado com sucesso!!")
                                input("Aperte enter para continuar... ")

                            else:
                                print("")
                                print("Algo deu errado no registro!")
                                print("")
                                print("Lembre-se, o isbn, edição e ano devem ser numeros inteiros!")
                                print("O livro deve pertencer a uma das categorias:")
                                for categoria in listaCategorias:
                                    print(categoria.get_nome())
                                print("")
                                input("Aperte enter para continuar... ")

                        if escolha == 2:
                            cls()
                            
                            print("Alterando dados do livro...")
                            
                            alterar = input("Digite o titulo do livro que deseja alterar: ")
                            nome = input("Digite o novo titulo do livro: ")
                            autor = input("Digite o novo autor do livro: ")
                            assunto = input("Digite o novo assunto do livro: ")
                            editora = input("Digite a nova editora do livro: ")
                            edicao = input("Digite a nova edição do livro: ")
                            isbn = input("Digite o novo ISBN do livro: ")
                            ano = input("Digite o novo ano do livro: ")
                            categoria = input("Digite a nova categoria do livro: ")
                            
                            testa = Livro.alterarLivro(alterar, nome, autor, assunto, editora, edicao, isbn, ano, categoria)
                            
                            if testa:
                                print("")
                                print("Livro alterado com sucesso!!")
                                input("Aperte enter para continuar... ")
                            
                            else:
                                print("")
                                print("Algo deu errado no registro!")
                                print("")
                                print("Lembre-se, o isbn, edição e ano devem ser numeros inteiros!")
                                print("O livro deve pertencer a uma das categorias:")
                                for categoria in listaCategorias:
                                    print(categoria.get_nome())
                                print("")
                                input("Aperte enter para continuar... ")

                        if escolha == 3:

                            cls()

                            print("Consultando livro...")

                            livro = input("Informe o livro que deseja consultar: ")

                            teste , titulo, autor, assunto, editora, edicao, isbn, ano, categoria = Livro.consultarLivro(listaLivros, livro)

                            if teste:

                                print("")
                                print(f"Titulo : {titulo}")
                                print(f"Autor : {autor}")
                                print(f"Assunto : {assunto}")
                                print(f"Editora : {editora}")
                                print(f"Isbn : {isbn}")
                                print(f"Ano : {ano}")
                                print(f"Categoria : {categoria}")
                                print("")
                                input("Aperte enter para continuar... ")

                            else: 

                                print(f"Livro '{livro}' Não encontrado")
                                input("Aperte enter para continuar... ")
                    #■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■

                if escolha == 2:
                    #■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ EXEMPLAR ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■#
                    while True:
                        
                        cls()
                        print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
                        print(f"   {usuario.get_nome()}     ■     {usuario.get_tipo().capitalize()} ")
                        print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
                        print("|             EXEMPLAR            |")
                        print("|                                 |")
                        print("| 1) Incluir novo exemplar        |")
                        print("| 2) Alterar dados do exemplar    |")
                        print("| 3) Consultar dados do exemplar  |")
                        print("| 4) deletar exemplar             |")
                        print("|                                 |")
                        print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
                        escolha = int(input("Escolha uma opção: "))
                        
                        if escolha == 1:
                            cls()
                            
                            print("Incluindo novo exemplar...")
                            disponibilidade = input("Informe a disponibilidade do exemplar: ")
                            livro = input("Informe o livro do exemplar: ")
                            
                            teste = Exemplar.incluirExemplar(disponibilidade, livro)
                            
                            if teste == True:
                                print("")
                                print("Exemplar adicionado com sucesso!!")
                                input("Aperte enter para continuar... ")
                            else:
                                print("")
                                print("Algo deu errado no registro!")
                                print("")
                                print("O exemplar deve pertencer a um livro que já existe!")
                                print("")
                                input("Aperte enter para continuar... ")
                                
                        if escolha == 2:
                            titulo = input("Informe o titulo do livro que deseja alterar: ")
                            disponibilidade = input("Informe a disponibilidade do exemplar: ")
                            
                            alterar = Exemplar.alterarExemplar(listaLivros, titulo, disponibilidade)
                            
                            if alterar == True:
                                print("")
                                print("Exemplar alterado com sucesso!!")
                                input("Aperte enter para continuar... ")
                            else:
                                print("")
                                print("Algo deu errado no registro!")
                                print("")
                                print("O exemplar deve pertencer a um livro que já existe!")
                                print("")
                                input("Aperte enter para continuar... ")
                        
                        if escolha == 3:
                            titulo = input("Informe o titulo do livro que deseja consultar: ")
                            
                            teste , disponibilidade, livro = Exemplar.consultarExemplar(listaLivros, titulo)
                            
                            if teste == True:
                                print("")
                                print(f"Disponibilidade : {disponibilidade}")
                                print(f"Livro : {livro}")
                                print("")
                                input("Aperte enter para continuar... ")
                            else: 
                                print(f"Exemplar '{titulo}' Não encontrado")
                                input("Aperte enter para continuar... ")
                    #■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
                if escolha == 3:

                    #■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ CATEGORIA ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■

                    while True:

                        cls()

                        print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
                        print(f"   {usuario.get_nome()}      ■    {usuario.get_tipo().capitalize()} ")
                        print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
                        print("|           CATEGORIA              |")
                        print("|                                  |")
                        print("| 1) Incluir nova categoria        |")
                        print("| 2) Alterar dados de categoria    |")
                        print("| 3) Consultar dados de categoria  |")
                        print("| 4) Excluir categoria             |")
                        print("| 5) Sair                          |")
                        print("|                                  |")
                        print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")

                        escolha = int(input("Escolha uma opção: "))

                        if escolha == 1:
                                                    
                            cls()

                            print("Incluindo nova categoria...")

                            nome = input("Informe o nome da nova categoria: ")
                            descricao = input("Informe a descrição da nova categoria: ")
                            assunto = input("Informe o assunto da nova categoria: ")

                            testa = Categoria.incluirCategoria(nome, descricao, assunto)

                            if testa:
                                print("Categoria adiconada com sucesso!")
                                print(f"'{listaCategorias[-1].get_nome()}'")
                                input("Aperte enter para continuar... ")

                            else:
                                print("Algo deu errado...")
                                input("Aperte enter para continuar... ")


                        if escolha == 2:

                            #ISSO AQUI PODE FICAR MUITO MELHOR!!!!!
                            #ATUALMENTE NÃO DA PRA ESCOLHER 1 COISA, TEM QUE MUDAR TUDO
                            
                            cls()

                            print("Alterando categoria...")

                            altera = input("Informe a categoria que deseja ALTERAR: ")
                            nome = input("Informe o novo nome: ")
                            descricao = input("Informe a nova descrição: ")
                            assunto = input("Informe o novo assunto: ")
                        
                        
                            testa = Categoria.alterarCategoria(altera, nome, descricao, assunto)

                            if testa:

                                print("Categoria alterada com sucesso!")
                                input("Aperte enter para continuar... ")

                            else:

                                print("Algo deu errado...")
                                input("Aperte enter para continuar... ")

                        if escolha == 3: 

                            cls()

                            print("Consultando categoria...")

                            categoria = input("Informe a categoria que deseja consultar: ")

                            teste, nome, descricao, assunto = Categoria.consultarCategoria(categoria)

                            if teste:

                                cls()

                                print(f"Nome: {nome}")
                                print(f"Descrição: {descricao}")
                                print(f"Assunto: {assunto}")

                                print("")
                                input("Aperte enter para continuar... ")

                            else:

                                print("Algo deu errado...")
                                input("Aperte enter para continuar... ")
                        
                        if escolha == 4:


                            cls()
                            
                            remover = input("Informe a categoria que deseja excluir: ")
                            
                            testa = Categoria.excluirCategoria(remover)
                            
                            if testa:
                                
                                cls()
                                
                                print("Categoria excluida com sucesso!")
                                input("Aperte enter para continuar... ")
                            
                            else:
                                print("Algo deu errado...")
                                input("Aperte enter para continuar... ")

                            print("Excluindo categoria...")

                    #■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■

    
                if escolha == 4:
                    break

                if escolha == 5:
                    break

                #■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
except:
    print("Algo deu errado...")