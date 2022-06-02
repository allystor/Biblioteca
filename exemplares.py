from livro import Livro, listaLivros
from categoria import Categoria, listaCategorias
class Exemplar(Livro):
    def __init__(self, titulo, autor, edicao, isbn, editora, ano, categoria, exemplares):
        super().__init__(titulo, autor, edicao, isbn, editora, ano, categoria)
        self.__exemplares = exemplares

    def get_exemplares(self):
        return self.__exemplares
    
    def set_exemplares(self, exemplares):
        self.__exemplares = exemplares

    def incluirExemplar(listaLivro, titulo, autor, edicao, isbn, editora, ano, categoria, exemplares):
        exemplar = Exemplar(titulo, autor, edicao, isbn, editora, ano, categoria, exemplares)
        exemplar.get_exemplares = int(input("Digite o numero de exemplares: "))
        if exemplar > 0:
            exemplar += exemplar
            print("Exemplar adicionado com sucesso!")
            return True
        elif exemplar == 0:
            print("Exemplar não adicionado!")
            return False
        
        
    def consultarExemplar(listaLivros):
        pesquisar = str(input("Digite o titulo do livro que deseja consultar: "))
        for livro in listaLivros:
            if pesquisar == Livro.get_titulo(listaLivros).lower():
                print(f"Titulo:{livro.get_titulo()}\nAutor:{livro.get_autor()}\nEdicao:{livro.get_edicao()}\nISBN:{livro.get_isbn()}\nEditora:{livro.get_editora()}\nAno:{livro.get_ano()}\nCategoria:{livro.get_categoria()}\nExemplares:{livro.get_exemplares()}")
                break
            
    def excluirExemplar(listaLivros):
        pesquisar = str(input("Digite o titulo do livro que deseja excluir: "))
        if pesquisar == Livro.get_titulo(listaLivros).lower():
            listaLivros.remove(Livro)
            print("Livro excluido com sucesso!")
            return True
                    
#zona de testes
Exemplar.incluirExemplar(listaLivros, "O Senhor dos Anéis", "J.R.R. Tolkien", "1ª Edição", "0-395-07477-5", "Minha Biblioteca", "1954", "Fantasia", "1")