from categoria import Categoria, listaCategorias

class Livro:

    def __init__(self, titulo, autor, assunto, editora, edicao, isbn, ano, categoria):

        self.__titulo = titulo
        self.__autor = autor
        self.__assunto = assunto
        self.__editora = editora
        self.__edicao = int(edicao)
        self.__isbn = int(isbn)
        self.__ano = int(ano)
        self.__categoria = categoria

    # GET E SET ================================================================

    def get_titulo(self):
        return self.__titulo
    
    def set_titulo(self, titulo):
        self.__titulo = titulo
    
    def get_autor(self):
        return self.__autor
    
    def set_autor(self, autor):
        self.__autor = autor

    def get_assunto(self):
        return self.__assunto

    def set_assunto(self, assunto):
        self.__assunto = assunto
    
    def get_editora(self):
        return self.__editora

    def set_editora(self, editora):
        self.__editora = editora
    
    def get_edicao(self):
        return self.__edicao
    
    def set_edicao(self, edicao):
        self.__edicao = edicao
    
    def get_isbn(self):
        return self.__isbn

    def set_isbn(self, isbn):
        self.__isbn = isbn
    
    def get_ano(self):
        return self.__ano 

    def set_ano(self, ano):
        self.__ano = ano

    def get_categoria(self):
        return self.__categoria

    def set_categoria(self, categoria):
        self.__categoria = categoria

    #================================================================

    def incluirLivro(listaLivros, listaCategorias,  titulo, autor, assunto, editora, edicao, isbn, ano, categoria):
        
        for categoriaValida in listaCategorias:
            if categoria == categoriaValida.get_nome():
                try:
                    listaLivros.append(Livro(titulo, autor, assunto, editora, edicao, isbn, ano, categoria))
                    return True
                except:
                    return False
            
        return False

    def alterarLivro(listaLivros):
        pass



    def consultarLivro(listaLivros, titulo):

        for livro in listaLivros:
            if titulo.lower() == livro.get_titulo().lower():
                
                return True , livro.get_titulo() , livro.get_autor(), livro.get_assunto(), livro.get_editora(), livro.get_edicao(), livro.get_isbn(), livro.get_ano(), livro.get_categoria()

        return False, None, None, None, None, None, None, None, None,


#SÃO 5 DA MANHÃ, NÃO ME JULGUE PELO OQ EU ESCREVER AQUI
listaLivros = [
    Livro("Pipo o sapo", "Meu Tio", "Um sapo chamado pipo", "Jardim", 1, 696969696969, 2076, "Biografia"),
    Livro("A Metamorfose", "Franz Kafka", "Isso é um livro de vdd de um cara que vira inseto ou alguma coisa assim", "Editora alemã aleatória", 3, 420420420420, 1915, "Ficção"),
    Livro("Biblia", "Deus", "To sem ideia de livro e esse é o mais famoso que eu lembrei", "Heaven", 0, 0000000000, 0, "Drama")
]

Livro.consultarLivro(listaLivros, "pipo o sapo")
