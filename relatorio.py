from usuario import *
from exemplar import Exemplar
from livro import *
from datetime import date

class Emprestimo:
    def __init__(self,usuario,livro, data_emprestimo, data_devolucao):
        self.__usuario = usuario
        self.__livro = livro
        self.__data_emprestimo = data_emprestimo
        self.__data_devolucao = data_devolucao
    
    def get_usuario(self):
        return self.__usuario
    
    def set_usuario(self, usuario):
        self.__usuario = usuario
    
    def get_livro(self):
        return self.__livro
    
    def set_livro(self, livro):
        self.__livro = livro

    def get_data_emprestimo(self):
        d= date.day(self.__data_emprestimo)
        m =  date.month(self.__data_emprestimo)
        a = date.year(self.__data_emprestimo)
        self.__data_emprestimo = str(d) + "/" + str(m) + "/" + str(a)
        return self.__data_emprestimo
    
    def set_data_emprestimo(self, data_emprestimo):
        self.__data_emprestimo = data_emprestimo
        
    def get_data_devolucao(self):
        d = date.day(self.__data_devolucao)
        m = date.month(self.__data_devolucao)
        a = date.year(self.__data_devolucao)
        self.__data_devolucao = str(d) + "/" + str(m) + "/" + str(a)
        return self.__data_devolucao
    
    def set_data_devolucao(self, data_devolucao):
        self.__data_devolucao = data_devolucao
        
    def criarEmprestimo(usuario,livro,data_emprestimo,data_devolucao):
        try:
            for usuario in listaUsuarios:
                if (usuario == usuario.get_login()):
                    for livro in listaLivros:
                        if (livro == livro.get_titulo()):
                            listaEmprestimos.append(Emprestimo(usuario,livro,data_emprestimo,data_devolucao))
                            return True, Emprestimo
                        elif (livro != livro.get_titulo()):
                            return False, None
        except:
            return False, None
        
    def listarEmprestimos():
        try:
            for emprestimo in listaEmprestimos:
                print("Usuario: ", emprestimo.get_usuario())
                print("Livro: ", emprestimo.get_livro())
                print("Data de emprestimo: ", emprestimo.get_data_emprestimo())
                print("Data de devolucao: ", emprestimo.get_data_devolucao())
        except:
            return None
    
    def consultarEmprestimo(usuario, livro):
        try:
            for emprestimo in listaEmprestimos:
                if (usuario == emprestimo.get_usuario() and livro == emprestimo.get_livro()):
                    return True, emprestimo
                elif (usuario != emprestimo.get_usuario() or livro != emprestimo.get_livro()):
                    return False, None
        except:
            return False, None
    def efetuarDevolucao(verificar): 
        try:
            for data in listaEmprestimos:
                if (verificar == data.get_data_devolucao()):
                    return True, Emprestimo
                elif (verificar > data.get_data_devolucao()):
                    return False, None
        except:
            return False, None
listaEmprestimos = [
    Emprestimo("João", "O Senhor dos Aneis", "01/01/2020", "01/02/2020"),
    Emprestimo("Maria", "O Senhor dos Aneis", "01/01/2020", "01/02/2020"),
    Emprestimo("Pedro", "O Senhor dos Aneis", "01/01/2020", "01/02/2020"),
    
]
        

    
    