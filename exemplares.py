from livro import Livro, livroDeLivros

class Exemplar(Livro):
    def __init__(self, titulo, autor, edicao, isbn, editora, ano, categoria, numero):
        super().__init__(titulo, autor, edicao, isbn, editora, ano, categoria)
        self.__numero = numero
    def get_numero(self):
        return self.__numero
    
    def set_numero(self, numero):
        self.__numero = numero

    def incluirExemplar(livroDeLivros):
        qntd = Livro.get_exemplares()
        Exemplar = int(input("Digite a quantidade de exemplares: "))
        if qntd > 0:
            for i in range(qntd):
                livroDeLivros.append(Exemplar("Titulo", "Autor", 1, 1, "Editora", 1, "Categoria", qntd))
                print("Exemplar incluido com sucesso!")
            
    def consultarExemplar(livroDeLivros):
        pesquisar = str(input("Digite o titulo do livro que deseja consultar: "))
        for livro in livroDeLivros:
            if pesquisar == Livro.get_titulo(livroDeLivros).lower():
                print(f"Titulo:{livro.get_titulo()}\nAutor:{livro.get_autor()}\nEdicao:{livro.get_edicao()}\nISBN:{livro.get_isbn()}\nEditora:{livro.get_editora()}\nAno:{livro.get_ano()}\nCategoria:{livro.get_categoria()}\nExemplares:{livro.get_exemplares()}")
                break
            
    def excluirExemplar(livroDeLivros):
        pesquisar = str(input("Digite o titulo do livro que deseja excluir: "))
        for livro in livroDeLivros:
            if pesquisar == Livro.get_titulo(livroDeLivros).lower():
                livro.set_exemplares(livro.get_exemplares() - 1)
                print("Exemplar excluido!")
                break        
#zona de testes
Exemplar.incluirExemplar(livroDeLivros)