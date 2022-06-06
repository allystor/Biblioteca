from ast import AugStore
from livro import *
from exemplar import *
from categoria import *

class Acervo():

    def __init__(self) -> None:
        pass

    def consultarTudo(listaCategorias, listaLivros, listaExemplares):
        for categoria in listaCategorias:
            print(f"{categoria.get_nome()}---------------------")
            for livro in listaLivros:
                if livro.get_categoria() == categoria.get_nome():
                    print("   ↳  ", end='')
                    print(livro.get_titulo())
                    for exemplar in listaExemplares:
                        if exemplar.get_livro() == livro.get_titulo():
                            print("           ↳  ", end='')
                            if exemplar.get_status() == True:
                                print(f"{exemplar.get_id()}  ✔")
                            else:
                                print(f"{exemplar.get_id()}  ✖")
                    print("")
            
            print("")

    def consultarTitulo(listaLivros, titulo):

        lista = []

        for livro in listaLivros:
            if livro.get_titulo().lower() == titulo.lower():
                lista.append(livro)

        return lista

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
