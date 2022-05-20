from livro import Livro, livroDeLivros

class Exemplar(Livro):
    def __init__(self, id, titulo, autor, assunto, editora, edicao, isbn, ano,numero):
        super().__init__(id, titulo, autor, assunto, editora, edicao, isbn, ano)
        self.__id = id
        self.__numero = numero

    def get_id(self):
        return self.__id
    
    def set_id(self):
        self.__id = self.__id
    
    def get_numero(self):
        return self.__numero
    
    def set_numero(self, numero):
        self.__numero = numero

    def incluirExemplar(livroDeLivros):
        livro = livroDeLivros[0]
        if livro.set_exemplares(livroDeLivros) == 0:
            print("Não há livros cadastrados")
        elif livro.set_exemplares(livroDeLivros) >= 1:
            print("Livros cadastrados:")
            for livro in livroDeLivros:
                print(f"Titulo:{livro.get_titulo()}\nAutor:{livro.get_autor()}\nEdicao:{livro.get_edicao()}\nISBN:{livro.get_isbn()}\nEditora:{livro.get_editora()}\nAno:{livro.get_ano()}\nCategoria:{livro.get_categoria()}\nExemplares:{livro.get_exemplares()}")
            titulo = str(input("Digite o titulo do livro que deseja incluir: "))
            numero = int(input("Digite o número do exemplar: "))
            for livro in livroDeLivros:
                if livro.get_titulo().lower() == titulo.lower():
                    livro.set_numero(numero)
                    print("Exemplar incluido!")
                    break

    def consultarExemplar(livroDeLivros):
        pesquisar = str(input("Digite o titulo do livro que deseja consultar: "))
        
        for livro in livroDeLivros:
            if livro.get_titulo().lower() == pesquisar.lower():
                livro.set_exemplares(livroDeLivros)
                print(f"Titulo:{livro.get_titulo()}\nAutor:{livro.get_autor()}\nEdicao:{livro.get_edicao()}\nISBN:{livro.get_isbn()}\nEditora:{livro.get_editora()}\nAno:{livro.get_ano()}\nCategoria:{livro.get_categoria()}\nExemplares:{livro.get_exemplares()}")
                break
    def excluirExemplar(livroDeLivros):
        pesquisar = str(input("Digite o titulo do livro que deseja excluir: "))
        for livro in livroDeLivros:
            if livro.get_titulo().lower() == pesquisar.lower():
                livro.set_exemplares(livroDeLivros)
                print(f"Titulo:{livro.get_titulo()}\nAutor:{livro.get_autor()}\nEdicao:{livro.get_edicao()}\nISBN:{livro.get_isbn()}\nEditora:{livro.get_editora()}\nAno:{livro.get_ano()}\nCategoria:{livro.get_categoria()}\nExemplares:{livro.get_exemplares()}")
                numero = int(input("Digite o número do exemplar que deseja excluir: "))
                for livro in livroDeLivros:
                    if livro.get_numero() == numero:
                        livroDeLivros.pop(livro)
                        print("Exemplar excluido!")
                        break
                    
#zona de testes
Exemplar.incluirExemplar(livroDeLivros)