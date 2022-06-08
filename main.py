import os
from categoria import *
from usuario import *
from livro import *
from exemplar import *
from acervo import *
from relatorio import *
from datetime import datetime

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
                print(f"   {usuario.get_nome()}           {usuario.get_tipo().capitalize()} ")
                print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
                print("| 1) Consultar Acervo              |")
                print("| 2) realizar empréstimo de livro  |")
                print("| 3) Sair                          |")
                print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")

                escolha = int(input("Escolha uma opção: "))

                if escolha == 1:

                    while True:

                        cls()

                        print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
                        print(f"   {usuario.get_nome()}           {usuario.get_tipo().capitalize()} ")
                        print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
                        print("|             ACERVO               |")
                        print("|                                  |")
                        print("| 1) Consultar Tudo                |")
                        print("| 2) Consultar por titulo          |")
                        print("| 3) Consultar por autor           |")
                        print("| 4) Consultar por assunto         |")
                        print("| 5) Voltar                        |")
                        print("|                                  |")
                        print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")

                        escolha = int(input("Escolha uma opção: "))

                        if escolha == 1:
                            cls()

                            print("")
                            Acervo.consultarTudo(listaCategorias, listaLivros, listaExemplares)
                            input("Aperte enter para continuar... ")

                        if escolha == 2:
                            cls()

                            print("Consultando por titulo...")

                            titulo = input("Informe o titulo que deseja buscar: ")

                            testa = Acervo.consultarTitulo(listaLivros, titulo)

                            if len(testa) > 0:

                                cls()

                                print("Livros encontrados:")
                                print("")

                                for item in testa:
                                    
                                    print(item.get_titulo())
                                    
                                print("")
                                input("Aperte enter para continuar... ")
                            
                            else:
                                cls()

                                print("Nenhum livro encontrado...")
                                input("Aperte enter para continuar... ")
            

                        if escolha == 3:

                            cls()

                            print("Consultando por autor...")

                            autor = input("Informe o autor que deseja buscar: ")

                            testa = Acervo.consultarAutor(listaLivros, autor)

                            if len(testa) > 0:

                                cls()

                                print("Livros encontrados:")
                                print("")

                                for item in testa:
                                    
                                    print(item.get_titulo())

                                print("")
                                input("Aperte enter para continuar... ")
                            
                            else:
                                cls()

                                print("Nenhum livro encontrado...")
                                input("Aperte enter para continuar... ")

                        if escolha == 4:

                            cls()

                            print("Consultando por assunto...")

                            assunto = input("Informe o assunto que deseja buscar: ")

                            testa = Acervo.consultarAutor(listaLivros, assunto)

                            if len(testa) > 0:

                                cls()

                                print("Livros encontrados:")
                                print("")

                                for item in testa:
                                    
                                    print(item.get_titulo())

                                print("")
                                input("Aperte enter para continuar... ")
                            
                            else:
                                cls()

                                print("Nenhum livro encontrado...")
                                input("Aperte enter para continuar... ")


                        if escolha == 5:
                            break

                
                if escolha == 2:
                    while True:

                        cls()

                        print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
                        print(f"   {usuario.get_nome()}           {usuario.get_tipo().capitalize()} ")
                        print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
                        print("|         EMPRÉSTIMO               |")
                        print("|                                  |")
                        print("| 1) Consultar por titulo          |")
                        print("| 2) Voltar                        |")
                        print("|                                  |")
                        print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
                        
                        escolha = int(input("Escolha uma opção: "))
                        
                        if escolha == 1:
                            cls()

                            print("Consultando por titulo...")

                            titulo = input("Informe o titulo que deseja buscar: ")

                            testa = Acervo.consultarTitulo(listaLivros, titulo)

                            if len(testa) > 0:

                                cls()

                                print("Livros encontrados:")
                                print("")

                                for item in testa:
                                    
                                    print(item.get_titulo())
                                    
                                print("")
                                escolha = int(input("Deseja adiquirir livro emprestado? (1) Sim (2) Não: "))
                                
                                if escolha == 1:
                                    usuario = str(input("Informe o nome do seu usuário: "))
                                    livro = str(input("Informe o titulo do livro: "))
                                    data = (input("Informe a data de empréstimo (dd/mm/aaaa): "))
                                    devolucao = input("Informe a data de devolução (dd/mm/aaaa): ")
                                
                                    Emprestimo.criarEmprestimo(usuario, livro, data, devolucao)
                                    
                                    print("Empréstimo realizado com sucesso!")
                                    input("Aperte enter para continuar... ")
                                    break
                                
                                if escolha == 2:
                                    break
                            
                            else:
                                cls()

                                print("Nenhum livro encontrado...")
                                input("Aperte enter para continuar... ")
                                
                        if escolha == 2:
                            break
                        
        if usuario.get_tipo() == "bibliotecario":
            
                #■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ MENU B ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■

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

                    #■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ LIVRO ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■

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
                        print("| 4) Excluir livro                 |")
                        print("| 5) Voltar                        |")
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

                            teste = Livro.incluirLivro(listaLivros, listaCategorias, titulo, autor, assunto, editora, edicao, isbn, ano, categoria)

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
                                                        
                            testa = Livro.alterarLivro(listaLivros, listaCategorias, alterar, nome, autor, assunto, editora, edicao, isbn, ano, categoria)
                                
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

                        if escolha == 4:

                            cls()
                                
                            print("Excluindo livro...")

                            livro = input("Informe o livro que deseja excluir: ")
                            
                            teste = Livro.excluirLivro(listaLivros, listaExemplares, livro)
                            
                            if teste:
                                cls()

                                print(f"Livro : {livro} Excluido con sucesso!")
                                input("Aperte enter para continuar... ")

                            else: 
                                cls()

                                print("Algo deu errado!")
                                print("Você pode ter escrito o titulo do livro errado, ou ele pode possuir algum exemplar")
                                input("Aperte enter para continuar... ")
                            




                        if escolha == 5:
                            escolha = None
                            break



                    #■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■

                    #■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ EXEMPLAR ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■

                if escolha == 2:

                    while True:
                
                        cls()

                        print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
                        print(f"   {usuario.get_nome()}           {usuario.get_tipo().capitalize()} ")
                        print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
                        print("|           EXEMPLAR               |")
                        print("|                                  |")
                        print("| 1) Incluir novo exemplar         |")
                        print("| 2) Alterar dados de exemplar     |")
                        print("| 3) Consultar dados de exemplar   |")
                        print("| 4) Excluir exemplar              |")
                        print("| 5) Voltar                        |")
                        print("|                                  |")
                        print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")

                        escolha = int(input("Escolha uma opção: "))

                        if escolha == 1:

                            cls()

                            print("Incluindo novo exemplar...")

                            livro = input("Para qual livro deseja incluir o exemplar?: ")
                            status = input("Esse exemplar pode circular? (True ou False) : ")

                            teste = Exemplar.incluirExemplar(listaExemplares, listaLivros, status, livro)

                            if teste:
                                cls()

                                print("Exemplar incluido com sucesso!")
                                print(f"Id gerado = {listaExemplares[-1].get_id()}")
                                input("Aperte enter para continuar... ")

                            else:
                                cls()

                                print("Algo deu errado...")
                                input("Aperte enter para continuar... ")

                        
                        if escolha == 2:

                            cls()

                            print("Alterando exemplar...")

                            id = input("Insira o id do exemplar que deseja alterar: ")
                            status = input("Esse exemplar pode circular? (True ou False) : ")

                            teste = Exemplar.incluirExemplar(listaExemplares, id , status)

                            if teste :
                                cls()

                                print(f"Exemplar {id} Alterado com sucesso!")
                                print(f"Sua circulação agora é {status}")
                                input("Aperte enter para continuar... ")
                            
                            else:
                                cls()

                                print("Algo deu errado...")
                                input("Aperte enter para continuar... ")


                        if escolha == 3:
                            
                            cls()

                            print("Consultando exemplar...")

                            id = int(input("Insira o id do exemplar que deseja consultar: "))

                            teste, exemplar = Exemplar.consultarExemplar(listaExemplares, id)

                            if teste:

                                cls()

                                print(f"Consulta de Exemplar")
                                print(f"Pertence ao livro: {exemplar.get_livro()}")
                                print(f"id: {exemplar.get_id()}")
                                if exemplar.get_status() == True:
                                    print(f"Pode circular?: Sim")
                                else:
                                    print(f"Pode circular?: Não")
                                input("Aperte enter para continuar... ")
                            
                            else:
                                cls()

                                print("Algo deu errado...")
                                input("Aperte enter para continuar... ")
                                                        
                        if escolha == 4:
                            pass

                        if escolha == 5:
                            escolha = None
                            break

                    #■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
                if escolha == 3:



                    #■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ CATEGORIA ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■

                    while True:

                        cls()

                        print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
                        print(f"   {usuario.get_nome()}           {usuario.get_tipo().capitalize()} ")
                        print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
                        print("|           CATEGORIA              |")
                        print("|                                  |")
                        print("| 1) Incluir nova categoria        |")
                        print("| 2) Alterar dados de categoria    |")
                        print("| 3) Consultar dados de categoria  |")
                        print("| 4) Excluir categoria             |")
                        print("| 5) Voltar                        |")
                        print("|                                  |")
                        print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")

                        escolha = int(input("Escolha uma opção: "))
                        
                        if escolha == 1:

                            cls()

                            print("Incluindo nova categoria...")

                            nome = input("Informe o nome da nova categoria: ")
                            descricao = input("Informe a descrição da nova categoria: ")
                            assunto = input("Informe o assunto da nova categoria: ")

                            testa = Categoria.incluirCategoria(listaCategorias, nome, descricao, assunto)

                            if testa:
                                print("Categoria adiconada com sucesso!")
                                print(f"'{listaCategorias[-1].get_nome()}'")
                                input("Aperte enter para continuar... ")

                            else:
                                print("Algo deu errado...")
                                input("Aperte enter para continuar... ")


                        if escolha == 2:
                            
                            cls()

                            print("Alterando categoria...")

                            altera = input("Informe a categoria que deseja ALTERAR: ")
                            nome = input("Informe o novo nome: ")
                            descricao = input("Informe a nova descrição: ")
                            assunto = input("Informe o novo assunto: ")
                        
                        
                            testa = Categoria.alterarCategoria(listaCategorias, altera, nome, descricao, assunto)

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

                            teste, nome, descricao, assunto = Categoria.consultarCategoria(listaCategorias, categoria)

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

                            print("Excluindo categoria...")
                        
                            categoria = input("Informe a categoria que deseja excluir: ")
                            
                            teste = Categoria.excluirCategoria(listaCategorias, categoria)
                            
                            if teste:
                                cls()

                                print(f"Categoria : {categoria} Excluido com sucesso!")
                                input("Aperte enter para continuar... ")

                            else: 

                                print("Algo deu errado!")
                                print("Você pode ter escrito o nome da categoria errado, ou ela pode estar atribuida em algum livro")
                                input("Aperte enter para continuar... ")
                            
                            

                        if escolha == 5:
                            escolha = None
                            break

                    #■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■

    
                if escolha == 4:
                                    
                    Acervo.consultarTudo(listaCategorias, listaLivros, listaExemplares)

                    print("")
                    

                if escolha == 5:
                    break

                #■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
                
        if usuario.get_tipo() == "funcionario":
            
            #■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ MENU C ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
            
            cls()
            
            print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
            print(f"   {usuario.get_nome()}     {usuario.get_tipo().capitalize()}")
            print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
            print("|1)Consultar usuário             |")
            print("|2)Consultar empréstimos         |")
            print("|3)Sair                          |")
            print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
            
            escolha = int(input("Informe a opção desejada: "))

            if escolha == 1:
                cls()
                
                print("Estes são os usuários cadastrados no sistema: ")
                print("")
                for usuario in listaEmprestimos:
                    print(f"Nome: {usuario.get_usuario()}")
                input("Aperte enter para continuar... ")    
                                
            if escolha == 2:
                while True:
                    cls()
                    
                    print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
                    print("        EMPRÉSTIMOS              ")
                    print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
                    print("|1)Consultar empréstimos        |")
                    print("|2)Solicitar devolução          |")
                    print("|3)Sair                         |")
                    print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
                    
                    escolha = int(input("Informe a opção desejada: "))
                    
                    if escolha == 1:
                
                        cls()
                        
                        print("Estes são os empréstimos atuais: ")
                        Emprestimo.listarEmprestimos(listaEmprestimos)
                        for emprestimo in listaEmprestimos:
                            print(f"Usuário: {emprestimo.get_usuario()}\nLivro: {emprestimo.get_livro()}\nData de empréstimo: {emprestimo.get_data_emprestimo()}\nPrevisão de devolução: {emprestimo.get_data_devolucao()}")
                            print("")
                        input("Aperte enter para voltar... ")
                    if escolha == 2:
                        usuario = input("Informe o usuário que deseja solicitar a devolução: ")
                        for emprestimo in listaEmprestimos:
                            if emprestimo.get_usuario() == usuario:
                                emprestimo.set_data_devolucao(datetime.now())
                                print("Devolução solicitada com sucesso!")
                                input("Aperte enter para continuar... ")
                                break
                                
                            print("Enviamos um aviso para o usuário que solicitou a devolução!")
                            input("Aperte enter para continuar... ")      
                    
                    if escolha == 3:
                        break
                    
                    
except:
    print("Algo deu errado...")
    input("Aperte enter para continuar... ")
    pass
