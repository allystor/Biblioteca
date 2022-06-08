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

    def alterarLivro(listaLivros, listaCategorias, alteracao, titulo, autor, assunto, editora, edicao, isbn, ano, categoria):
            
            try:

                for livro in listaLivros:

                    if alteracao.lower() == livro.get_titulo().lower():
                        alteracao = livro
            

                alteracao.set_titulo(titulo)
                alteracao.set_autor(autor)
                alteracao.set_assunto(assunto)
                alteracao.set_editora(editora)
                alteracao.set_edicao(edicao)
                alteracao.set_isbn(isbn)
                alteracao.set_ano(ano)

                for categoriaTeste in listaCategorias:
                    if categoria.lower() == categoriaTeste.get_nome().lower():
                        alteracao.set_categoria(categoria.capitalize())
                        return True
                
        
                return False

            except:
                print("Merda ali")
                return False



    def consultarLivro(listaLivros, titulo):

        for livro in listaLivros:
            if titulo.lower() == livro.get_titulo().lower():
                
                return True , livro.get_titulo() , livro.get_autor(), livro.get_assunto(), livro.get_editora(), livro.get_edicao(), livro.get_isbn(), livro.get_ano(), livro.get_categoria()

        return False, None, None, None, None, None, None, None, None,

    def excluirLivro(listaLivros, listaExemplares, livro):

        for exemplar in listaExemplares:
            if exemplar.get_livro().lower() == livro.lower():
                print("Possui Exemplar")
                return False
        
        contador = 0

        for item in listaLivros:
            if item.get_titulo().lower() == livro.lower():
                listaLivros.pop(contador)
                print("Sucesso")
                print(contador)
                return True
            contador = contador + 1

        print("Livro errado")
        return False


listaLivros = [
    Livro("A Metamorfose", "Franz Kafka", "Isso é um livro de vdd de um cara que vira inseto ou alguma coisa assim", "Editora alemã aleatória", 3, 420420420420, 1915, "Ficção"),
    Livro("O Senhor dos Anéis", "J. R. R. Tolkien", " história narra o conflito contra o mal que se alastra pela Terra-média, através da luta de várias raças - Humanos, Anãos, Elfos, Ents e Hobbits - contra Orques, para evitar que o Anel do Poder volte às mãos de seu criador Sauron, o Senhor Sombrio.", "Editora alemã aleatória", 1, 99999999999, 1954, "Ficção"),
    Livro("Harry Potter e a Pedra Filosofal", "J. K. Rowling", " A série narra as aventuras de um jovem chamado Harry James Potter, que descobre aos 11 anos de idade que é um bruxo ao ser convidado para estudar na Escola de Magia e Bruxaria de Hogwarts.", "Editora alemã aleatória", 1, 99999999999, 1997, "Ficção"),
]
