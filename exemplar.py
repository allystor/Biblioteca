from random import randint
from livro import *

class Exemplar():

    def __init__(self, status, livro):
        self.__id = randint(0, 99999)
        self.__status = status
        self.__livro = livro

    #=================================================#

    def get_id(self):
        return self.__id

    def set_id(self, novoId):
        self.__id = novoId

    def get_status(self):
        return self.__status

    def set_status(self, novoStatus):
        self.__status = eval(novoStatus)

    def get_livro(self):
        return self.__livro

    def set_livro(self, novoLivro):
        self.__id = novoLivro
    #=================================================#

    def incluirExemplar(listaExemplares, listaLivros, status, livro):

        for livroTeste in listaLivros:
            if livro.lower() == livroTeste.get_titulo().lower():
                listaExemplares.append(Exemplar(eval(status), livro))
                return True

        return False

    def alteraExemplar(listaExemplares, id, novoStatus):

        for exemplar in listaExemplares:
            if exemplar.get_id() == id:
                exemplar.set_status(novoStatus)
                print("cERTO")
                return True
        
        return False

    def consultarExemplar(listaExemplares, id):
        
        for exemplar in listaExemplares:
            if exemplar.get_id() == id:
                return True, exemplar

        return False, None

    def excluirExemplar(listaExemplares, id):
        pass


listaExemplares = [
    Exemplar(True, "Pipo o sapo"),
    Exemplar(True, "Pipo o sapo"),
    Exemplar(False, "Pipo o sapo"),
    Exemplar(False, "A Metamorfose"),
]

