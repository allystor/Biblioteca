class Categoria():

    def __init__(self, nome, descricao, assunto):
        self.__nome = nome
        self.__descricao = descricao
        self.__assunto = assunto
        pass

    #-------------------------------------------

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

    #--------------------------------------------

    def incluirCategoria(listaCategorias):

        print("Incluindo nova categoria.....")

        nome = str(input("Informe o nome da categoria: "))

        for categoria in listaCategorias:
            if nome.lower() == categoria.get_nome().lower():
                print("Essa categoria já existe!")
                return
 
        descricao = str(input("Informe a descrição da categoria: "))
        assunto = str(input("Informe o assunto da categoria: "))

        listaCategorias.append(Categoria(nome, descricao, assunto))

    def alterarCategoria(listaCategorias):

        print("Alterando categoria...")
        
        busca = str(input("Informe a categoria que deseja alterar: "))
        
        categoriaEncontrada = False

        for categoria in listaCategorias:
            if busca.lower() == categoria.get_nome().lower():
                categoria = categoria
                categoriaEncontrada = True

        if categoriaEncontrada:

            while True:

                print(f"Alterando categoria '{categoria.get_nome()}'")
                print("Digite 'sair' para sair")
                print("Opções = nome, descricao, assunto")
                escolha = input("Oque deseja alterar na categoria?: ")

                if escolha == "sair":
                    break

                elif escolha == "nome":
                    categoria.set_nome(input("Digite o novo nome: "))
                
                elif escolha == "descricao":
                    categoria.set_descricao(input("Digite a nova descrição: "))

                elif escolha == "assunto":
                    categoria.set_assunto(input("Digite o novo assunto: "))
          
                else:
                    print("Escolha invalida...")

        else:
            print("Essa categoria não foi encontrada, verifique a escrita e tente novamente!")
            



listaCategorias = [
    Categoria("Biografia", "Gênero no qual o autor narra sobre a vida de uma pessoa ou de várias pessoas.", None),
    Categoria("Ficção", "Narrativa imaginária, irreal, que se opõe à Não-Ficção. Ainda que possa ser baseada em fatos reais, contará sempre com elementos de conteúdo imaginário.", None),
    Categoria("Drama", "Obras que trazem conteúdos, centrais ou não, caracterizados por sofrimentos e/ou tragédias, todavia, podem ou não terem um desfecho triste.", None)
]