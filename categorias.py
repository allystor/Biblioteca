class Categoria:
    def __init__(self, nome,descricao,assunto):
        self.nome = nome
        self.descricao = descricao
        self.assunto = assunto

    #------get-e-set-------->
    def get_nome(self):
        return self.__nome

    def get_descricao(self):
        return self.__descricao

    def get_assunto(self):
        return self.__assunto
    
    def set_nome(self, nome):
        self.__nome = nome

    def set_descricao(self, descricao):
        self.__descricao = descricao

    def set_assunto(self, assunto):
        self.__assunto = assunto
    #----------------------->    
    
    def cadastrarCategoria(categorias):
        nome = str(input("Digite o nome da categoria: "))
        descricao = str(input("Digite a descrição da categoria: "))
        assunto = str(input("Digite o assunto da categoria: "))
        categorias.append = Categoria(nome,descricao,assunto)
    def consultarCategoria(categorias):
        for categoria in categorias:
            print(f"Nome: {categoria.get_nome()}\n Descrição: {categoria.get_descricao()}\n Assunto: {categoria.get_assunto()}")

    def excluirCategoria(categorias):
        pesquisar = str(input("Digite o nome da categoria que deseja excluir: "))
        for categoria in categorias:
            if categoria.get_nome().lower() == pesquisar.lower():
                categorias.remove(categoria)
                print("Categoria excluida!")
                break
    def alterarCategoria(categorias):
        pesquisar = str(input("Digite o nome da categoria que deseja alterar: "))
        for categoria in categorias:
            if categoria.get_nome().lower() == pesquisar.lower():
                novo_nome = str(input("Digite o novo nome da categoria: "))
                nova_descricao = str(input("Digite a nova descrição da categoria: "))
                novo_assunto = str(input("Digite o novo assunto da categoria: "))
                categoria.set_nome(novo_nome)
                categoria.set_descricao(nova_descricao)
                categoria.set_assunto(novo_assunto)
                print("Categoria alterada!")
                break


categorias = [
    Categoria("Ciências da Natureza","Ciências da Natureza","Ciências da Natureza"),
    Categoria("Ciências Humanas","Ciências Humanas","Ciências Humanas"),
    Categoria("Ciências da Computação","Ciências da Computação","Ciências da Computação"),
]