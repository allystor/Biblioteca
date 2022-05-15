from webbrowser import get
from livro import Livro, listaLivros

class Exemplar(Livro):
    def __init__(self, id, titulo, autor, assunto, editora, edicao, isbn, ano):
        super().__init__(id, titulo, autor, assunto, editora, edicao, isbn, ano)
    
    def consultarExemplar(listaLivro):
        livro = listaLivro[0]
        
        if livro.set_id(listaLivro) == 0:
            print("Não há livros cadastrados")
        elif livro.set_id(listaLivro) > 0:
            print("Livros cadastrados:")
            for livro in listaLivro:
                print(f"Titulo: {livro.get_titulo()}\n Autor: {livro.get_autor()}\n Assunto: {livro.get_assunto()}\n Editora: {livro.get_editora()}\n Edição: {livro.get_edicao()}\n ISBN: {livro.get_isbn()}\n Ano de publicação:{livro.get_ano()}")
    
    def excluirExemplar(listaLivro):
        
        pesquisar = str(input("Digite o titulo do livro que deseja excluir: "))
        
        for livro in listaLivro:
            if livro.get_titulo().lower() == pesquisar.lower():
                livro.set_id(listaLivro)
                print("Exemplar excluido!")
                break