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
        nome = input("Digite o nome da categoria: ")
        descricao = input("Digite a descricao da categoria: ")
        assunto = input("Digite o assunto da categoria: ")
        categoria = Categoria(nome, descricao, assunto)
        listaCategorias.append(categoria)
    
    def excluirCategoria(listaCategorias):
        nome = input("Digite o nome da categoria: ")
        for categoria in listaCategorias:
            if categoria.get_nome() == nome:
                listaCategorias.remove(categoria)
                print("Categoria excluida com sucesso!")
                break
            
    def listarCategorias(listaCategorias):
        for categoria in listaCategorias:
            print(f"{categoria.get_nome()}")
            
    def alterarCategoria(listaCategorias):
        print("Alterando categorias")
        
        busca = str(input("Informe o nome da categoria que deseja alterar: "))
        alterar = []
        contador = 0

        for categoria in listaCategorias:
            if busca.lower() == categoria.get_nome().lower():
                contador += 1
                alterar.append(categoria)

        if contador == 0:
            print("Não foi encontrado nenhuma categoria com esse nome!")

        elif contador == 1:
            categoria = alterar[0]

        elif contador > 1:
            print("Foram encontrados mais de uma categoria com esse nome!")
            contador = 1

            for i in listaCategorias:
                print(f"{contador} - {i.get_nome()}")
                print(f"{contador} - {i.get_descricao()}")
                print(f"{contador} - {i.get_assunto()}")
                contador += 1

            opcao = int(input("Qual dessas categorias deseja alterar?: "))
            categoria = alterar[opcao - 1]

        while True:

            print(f"Alterando livro '{categoria.get_nome()}'")
            print("Opções disponíveis: para alterar:\n1 - Nome\n2 - Descrição\n3 - Assunto")
            print("Digite 'sair' para sair")
            escolha = input("O que deseja alterar na categoria? ")

            if opcao == "sair":
                break

            elif opcao == "nome":
                categoria.set_nome(input("Digite o novo nome: "))
            
            elif escolha == "descricao":
                categoria.set_descricao(input("Digite o nova descrição: "))

            elif escolha == "assunto":
                categoria.set_assunto(input("Digite o novo assunto: "))

            else:
                print("Escolha invalida...")
                
    #ta rentável?

listaCategorias = [
    Categoria("Biografia", "Gênero no qual o autor narra sobre a vida de uma pessoa ou de várias pessoas.", None),
    Categoria("Ficção", "Narrativa imaginária, irreal, que se opõe à Não-Ficção. Ainda que possa ser baseada em fatos reais, contará sempre com elementos de conteúdo imaginário.", None),
    Categoria("Drama", "Obras que trazem conteúdos, centrais ou não, caracterizados por sofrimentos e/ou tragédias, todavia, podem ou não terem um desfecho triste.", None)
]