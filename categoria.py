from os import remove


class Categoria:

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

    def incluirCategoria(listaCategorias ,nome, descricao, assunto):

        try:

            listaCategorias.append(Categoria(nome, descricao, assunto))
            return True

        except:

            return False
        
    def alterarCategoria(listasCategorias,alteracao, nome, descricao, assunto):

        try:

            for categoria in listaCategorias:
                if alteracao == categoria.get_nome():
                    alteracao = categoria
                                
            alteracao.set_nome(nome)
            alteracao.set_descricao(descricao)
            alteracao.set_assunto(assunto)

            return True

        except:

            return False

    def consultarCategoria(listaCategoria, consulta):
        try:
            for categoria in listaCategorias:
                if consulta.lower() == categoria.get_nome().lower():
                    return True, categoria.get_nome(), categoria.get_descricao(), categoria.get_assunto()
        except:
            return False, None, None, None

    def excluirCategoria(listaCategoria, remover):
        try:
            for categoria in listaCategorias:
                if remover == categoria.get_nome():
                    listaCategorias.remove(categoria)
                    return True
        except:
            return False


        

listaCategorias = [
    Categoria("Biografia", "G??nero no qual o autor narra sobre a vida de uma pessoa ou de v??rias pessoas.", None),
    Categoria("Fic????o", "Narrativa imagin??ria, irreal, que se op??e ?? N??o-Fic????o. Ainda que possa ser baseada em fatos reais, contar?? sempre com elementos de conte??do imagin??rio.", None),
    Categoria("Drama", "Obras que trazem conte??dos, centrais ou n??o, caracterizados por sofrimentos e/ou trag??dias, todavia, podem ou n??o terem um desfecho triste.", None),
    Categoria("Romance", "Narrativas de amor, que se op??em ??s N??o-Fic????o, mas tamb??m podem ser baseadas em fatos reais.", None)
    
]
