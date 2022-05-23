from categoria import Categoria
from livro import Livro
from exemplares import Exemplar

class Acervo:

    def __init__(self, id, titulo, autor, assunto, editora, edicao, isbn, ano):
        super().__init__(id, titulo, autor, assunto, editora, edicao, isbn, ano)
        self.__
        
    def get_listaLivros(self):
        return self.__listaLivros
    
    def get_listaExemplares(self):
        return self.__listaExemplares
    
    def get_listaCategorias(self):
        return self.__listaCategorias
    
    def set_listaLivros(self, listaLivros):
        self.__listaLivros = listaLivros
    
    def set_listaExemplares(self, listaExemplares):
        self.__listaExemplares = listaExemplares
    
    def set_listaCategorias(self, listaCategorias):
        self.__listaCategorias = listaCategorias
    
    def listarLivros(self):
        if self.get_listaLivros() == []:
            print("Não há livros cadastrados")
        else:
            print("Livros cadastrados:")
            for livro in self.get_listaLivros():
                print(f"Titulo: {livro.get_titulo()}\n Autor: {livro.get_autor()}\n Assunto: {livro.get_assunto()}\n Editora: {livro.get_editora()}\n Edição: {livro.get_edicao()}\n ISBN: {livro.get_isbn()}\n Ano de publicação:{livro.get_ano()}")
        