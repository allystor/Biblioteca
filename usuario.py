class Usuario():

    def __init__(self, nome, login, senha, tipo):
        self.__nome = nome
        self.__login = login
        self.__senha = senha

        if tipo.lower() == "usuario" or tipo.lower() == "bibliotecario":
            self.__tipo = tipo
        else:
            self.__tipo = None
            
    #=================================================#
   
    def get_nome(self):
        return self.__nome
    
    def get_login(self):
        return self.__login

    def get_senha(self):
        return self.__senha

    def get_tipo(self):
        return self.__tipo

    #=================================================#
    
    def logar(usuarios, login, senha):

        for usuario in usuarios:
            if login == usuario.get_login() and senha == usuario.get_senha():
                return True, usuario
        return False, None

listaUsuarios = [
    Usuario("UsuarioTeste", "teste", "teste", "teste"),
    Usuario("Luiz", "luiz002", "password", "usuario"),
    Usuario("Alvrin", "admin", "admin", "bibliotecario")
]