class Livro:

    def __init__(self, titulo, autor, assunto, editora, edicao, isbn, ano, categoria):
        self.__titulo = titulo
        self.__autor = autor
        self.__assunto = assunto
        self.__editora = editora
        self.__edicao = edicao
        self.__isbn = isbn
        self.__ano = ano
        self.__categoria = categoria

    # GET E SET ================================================================

    def get_titulo(self):
        return self.__titulo
    
    def set_titulo(self, titulo):
        self.__titulo = titulo
    
    def get_autor(self):
        return self.__autor
    
    def set_autor(self, autor):
        self.__autor = autor

    def get_assunto(self):
        return self.__assunto

    def set_assunto(self, assunto):
        self.__assunto = assunto
    
    def get_editora(self):
        return self.__editora

    def set_editora(self, editora):
        self.__editora = editora
    
    def get_edicao(self):
        return self.__edicao
    
    def set_edicao(self, edicao):
        self.__edicao = edicao
    
    def get_isbn(self):
        return self.__isbn

    def set_isbn(self, isbn):
        self.__isbn = isbn
    
    def get_ano(self):
        return self.__ano 

    def set_ano(self, ano):
        self.__ano = ano

    def get_cattegoria(self):
        return self.__categoria

    def set_categoria(self, categoria):
        self.__categoria = categoria

    #================================================================

    def incluirLivro(listaLivro):

        print("Incluindo novo livro.....")

        titulo = str(input("Digite o titulo do livro: "))
        autor = str(input("Digite o autor do livro: "))
        assunto = str(input("Digite o assunto do livro: "))
        editora = str(input("Digite a editora do livro: "))
        edicao = input("Digite a edição do livro: ")
        isbn = int(int(input("Digite o ISBN do livro: ")))
        ano = int(input("Digite o ano do livro: "))
        categoria = str(input("Digite a categoria do livro: "))

        listaLivro.append(Livro(titulo, autor, assunto, editora, edicao, isbn, ano))

    #Isso aqui ta um lixo
    def excluirLivro(listaLivro):

        print("Excluindo livro...")
        
        busca = str(input("Informe o titulo do livro que deseja excluir: "))
        posicao = 0

        for livro in listaLivro:
            if busca.lower() == livro.get_titulo().lower():
                listaLivro.pop(posicao)

            posicao += 1
                
    def alterarLivro(listaLivro):

        print("Alterando dados do livro...")
        
        busca = str(input("Informe o titulo do livro que deseja alterar: "))
        contador = 0
        listaAlterar = []

        for livro in listaLivro:
            if busca.lower() == livro.get_titulo().lower():
                contador += 1
                listaAlterar.append(livro)

        if contador == 0:
            print("Não foi encontrado nenhum livro com esse titulo")

        elif contador == 1:
            livro = listaAlterar[0]

        elif contador > 1:
            print("Mais de um livro encontrado com esse titulo, informe qual deseja alterar:")
            contador = 1

            for i in listaAlterar:
                print("\n")
                print(f"{contador})")
                print(f"Titulo: {i.get_titulo()}\n Autor: {i.get_autor()}\n Assunto: {i.get_assunto()}\n Editora: {i.get_editora()}\n Edição: {i.get_edicao()}\n ISBN: {i.get_isbn()}\n Ano de publicação:{i.get_ano()}")
                print("\n")
                contador += 1

            escolha = int(input("Qual desses livros deseja alterar?: "))
            livro = listaAlterar[escolha - 1]

        while True:

            print(f"Alterando livro '{livro.get_titulo()}'")
            print("Digite 'sair' para sair")
            print("Opções = titulo, autor, assunto, editora, edicao, isbn, ano")
            escolha = input("Oque deseja alterar no livro?: ")

            if escolha == "sair":
                break

            elif escolha == "titulo":
                livro.set_titulo(input("Digite o novo titulo: "))
            
            elif escolha == "autor":
                livro.set_autor(input("Digite o novo autor: "))

            elif escolha == "assunto":
                livro.set_assunto(input("Digite o novo assunto: "))

            elif escolha == "editora":
                livro.set_editora(input("Digite a nova editora: "))

            elif escolha == "edicao":
                livro.set_edicao(input("Digite a nova edição: "))

            elif escolha == "isbn":
                livro.set_isbn(input("Digite o novo isbn: "))

            elif escolha == "ano":
                livro.set_ano(input("Digite o novo ano: "))

            else:
                print("Escolha invalida...")

     
    
    






listaLivros = [ 
    Livro("livro Teste", "Autor Ruim", "Um monte de merda", "Editora Burra", "1º Edição", 5974800454590, 2022),
    Livro("livro Ruim", "Autor Burro", "Umas parada ai", "Editora Péssima", "69º Edição", 1424080386011, 1987),
    Livro("livro Feio", "Autor Ruim", "Umas parada ai", "Editora Burra", "96º Edição", 6188234457778, 1111),
    Livro("livro Maneiro", "Autor Competente", "Esse vale a pena", "Editora Sangue Bom", "24º Edição", 7212696729254, 2002),
    Livro("livro Ruim", "Autor Competente", "Um monte de merda", "Editora Repetida", "0º Edição", 1424080386011, 1937),  
]