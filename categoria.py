class Categoria():

    def __init__(self, nome, descricao, assunto):

        self.__nome = nome
        self.__descricao = descricao
        self.__assunto = assunto

    #=================================================#

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

    def get_descricao(self):
        return self.__descricao

    def set_descricao(self, descricao):
        self.__descricao = descricao

    def get_assunto(self):
        return self.__assunto

    def set_assunto(self, assunto):
        self.__assunto = assunto

    #=================================================#

    def incluirCategoria(listaCategorias):
        pass

listaCategorias = [
    Categoria("Biografia", "Gênero no qual o autor narra sobre a vida de uma pessoa ou de várias pessoas.", None),
    Categoria("Ficção", "Narrativa imaginária, irreal, que se opõe à Não-Ficção. Ainda que possa ser baseada em fatos reais, contará sempre com elementos de conteúdo imaginário.", None),
    Categoria("Drama", "Obras que trazem conteúdos, centrais ou não, caracterizados por sofrimentos e/ou tragédias, todavia, podem ou não terem um desfecho triste.", None)
]