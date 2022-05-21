from categoria import Categoria

class Livro:
    def __init__(self, titulo, autor, edicao, isbn, editora, ano,categoria, exemplares):
        self.__titulo = titulo
        self.__autor = autor
        self.__edicao = edicao
        self.__isbn = isbn
        self.__editora = editora
        self.__ano = ano
        self.__categoria = categoria
        self.__exemplares = exemplares
        
    #============MELANCOLIA============================
    def get_titulo(self):
        return self.__titulo
    
    def set_titulo(self, titulo):
        self.__titulo = titulo
        
    def get_autor(self):
        return self.__autor
    
    def set_autor(self, autor):
        self.__autor = autor
    
    def get_edicao(self):
        return self.__edicao
    
    def set_edicao(self, edicao):
        self.__edicao = edicao
        
    def get_isbn(self):
        return self.__isbn
    
    def set_isbn(self, isbn):
        self.__isbn = isbn
        
    def get_editora(self):
        return self.__editora

    def set_editora(self, editora):
        return self.__editora
    
    def get_ano(self):
        return self.__ano
    
    def set_ano(self, ano):
        self.__ano = ano
    
    def get_categoria(self):
        return self.__categoria
    
    def set_categoria(self, categoria):
        self.__categoria = categoria
    
    def get_exemplares(self,):
        return self.__exemplares
    
    def set_exemplares(self, exemplares):
        self.__exemplares = exemplares
    
    #================================================
    
    def incluirNovoLivro(livroDeLivros):
        titulo = str(input("Digite o titulo do livro: "))
        autor = str(input("Digite o autor do livro: "))
        edicao = int(input("Digite a edicao do livro: "))
        isbn = int(input("Digite o isbn do livro: "))
        editora = str(input("Digite a editora do livro: "))
        ano = int(input("Digite o ano do livro: "))
        categoria = str(input("Digite a categoria do livro: "))
        exemplares = int(input("Digite o numero de exemplares do livro: "))
        livroDeLivros.append(Livro(titulo, autor, edicao, isbn, editora, ano, categoria, exemplares))
    
    def excluirLivro(livroDeLivros):
        titulo = str(input("Digite o titulo do livro: "))
        for livro in livroDeLivros:
            if livro.get_titulo() == titulo:
                livro.pop(livro)
                print("Livro excluido com sucesso!")
                break
            
    def listarLivros(livroDeLivros):
        print("Livros disponíveis:")
        for livro in livroDeLivros:
            print(f"Titulo:{livro.get_titulo()}\nAutor:{livro.get_autor()}\nEdicao:{livro.get_edicao()}\nISBN:{livro.get_isbn()}\nEditora:{livro.get_editora()}\nAno:{livro.get_ano()}\nCategoria:{livro.get_categoria()}\nExemplares:{livro.get_exemplares()}")
            print("\n")
                        
    def alterarLivro(livroDeLivros):
        print("Alterando livro")
        
        buscarLivro = str(input("Digite o titulo do livro: "))
        alterar = []
        contador = 0
        for livro in livroDeLivros:
            if livro.get_titulo() == buscarLivro:
                alterar.append(livro)
                contador += 1
        if contador == 0:
            print("Não foi encontrado nenhum livro com esse titulo!")
        
        elif contador == 1:
            livro = alterar[0]
            
        elif contador > 1:
            print("Há mais de um livro com esse titulo!")
            
            contador = 1
           
            for livro in alterar:
                print(f"{contador}:")
                print(f"Titulo:{livro.get_titulo()}\nAutor:{livro.get_autor()}\nEdicao:{livro.get_edicao()}\nISBN:{livro.get_isbn()}\nEditora:{livro.get_editora()}\nAno:{livro.get_ano()}\nCategoria:{livro.get_categoria()}\nExemplares:{livro.get_exemplares()}")
            contador += 1
            opcao = int(input("Digite o numero do livro que deseja alterar: "))
            livro = alterar[opcao-1]
        while True:
            opcao = int(input("Digite a opcao que deseja alterar:\n1 - Titulo\n2 - Autor\n3 - Edicao\n4 - ISBN\n5 - Editora\n6 - Ano\n7 - Categoria\n8 - Exemplares\n9 - Sair\n"))
            if opcao == 1:
                titulo = str(input("Digite o titulo do livro: "))
                livro.set_titulo(titulo)
                print("Titulo alterado com sucesso!")
            elif opcao == 2:
                autor = str(input("Digite o autor do livro: "))
                livro.set_autor(autor)
                print("Autor alterado com sucesso!")
            elif opcao == 3:
                edicao = int(input("Digite a edicao do livro: "))
                livro.set_edicao(edicao)
                print("Edicao alterado com sucesso!")
            elif opcao == 4:
                isbn = int(input("Digite o isbn do livro: "))
                livro.set_isbn(isbn)
                print("ISBN alterado com sucesso!")
            elif opcao == 5:
                editora = str(input("Digite a editora do livro: "))
                livro.set_editora(editora)
                print("Editora alterado com sucesso!")
            elif opcao == 6:
                ano = int(input("Digite o ano do livro: "))
                livro.set_ano(ano)
                print("Ano alterado com sucesso!")
            elif opcao == 7:
                categoria = str(input("Digite a categoria do livro: "))
                livro.set_categoria(categoria)
                print("Categoria alterado com sucesso!")
            elif opcao == 8:
                exemplares = int(input("Digite o numero de exemplares do livro: "))
                livro.set_exemplares(exemplares)
                print("Exemplares alterado com sucesso!")
            elif opcao == 9:
                break
            
livroDeLivros = [
    Livro("Titulo 1", "Autor 1", 1, 1, "Editora 1", 1, "Categoria 1", 1),
    Livro("Titulo 2", "Autor 2", 2, 2, "Editora 2", 2, "Categoria 2", 2),
    Livro("Titulo 3", "Autor 3", 3, 3, "Editora 3", 3, "Categoria 3", 3),
]        

#zona de testes
#Livro.incluirNovoLivro(livroDeLivros)
#Livro.excluirLivro(livroDeLivros)