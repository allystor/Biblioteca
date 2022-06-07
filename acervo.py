from ast import AugStore
from livro import *
from exemplar import *
from categoria import *

class Acervo():

    def __init__(self):
        self.listaCategorias = []
        self.listaLivros = []
        self.listaExemplares = []

    def consultarTudo(listaCategorias, listaLivros, listaExemplares):
        try:
            for categoria in listaCategorias:
                print(categoria.get_nome())
                for livro in listaLivros:
                    if livro.get_categoria() == categoria.get_nome():
                        print(livro.get_titulo())
                        for exemplar in listaExemplares:
                            if exemplar.get_livro() == livro:
                                print(exemplar.get_numero())
        except:
            return False
    def consultarTitulo(listaLivros, titulo):
        try:
            lista = []
            for livro in listaLivros:
                if livro.get_titulo() == titulo:
                    lista.append(livro)
            return lista
        except:
            return False

    def consultarAutor(listaLivros, autor):

        lista = []

        for livro in listaLivros:
            if livro.get_autor().lower() == autor.lower():
                lista.append(livro)

        return lista

    def consultarAssunto(listaLivros, assunto):

        lista = []

        for livro in listaLivros:
            if livro.get_assunto().lower() == assunto.lower():
                lista.append(livro)

        return lista

    
        
Acervo.consultarTudo(listaCategorias, listaLivros, listaExemplares)
