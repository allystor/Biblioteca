"""
Projeto: Sistema de Biblioteca
1. Introdução
Este documento apresenta a especificação de requisitos para a construção de um sistema
de bibliotecas. Essa atividade será conduzida usando a técnica de Modelagem de Casos
de Uso e, portanto, este documento contém uma descrição do propósito do sistema,
associados às descrições dos casos de uso.
2. Descrição do Propósito do Sistema
O sistema de biblioteca visa informatizar as atividades de gestão de um repositório de
arquivos, a saber: gestão de livros a usuários e reserva de livros. Para que essas atividades
sejam apoiadas, é necessário controlar as informações acerca de livros, exemplares e
usuários. Além disso, devem ser fornecidas facilidades de consulta ao acervo, permitindo
consultas por assunto, autor e título.
3. Modelo de Casos de Uso
No contexto do presente projeto, foram identificados dois subsistemas: Controle de
Acervo e Atendimento a Usuário, figuras 1 e 2. Assim, a seguir, são apresentados dois
diagramas de casos de uso, bem como as descrições dos casos de uso de cada uma delas.
"""
class cadastrarLivro:
    def __init__(self, titulo, autor, assunto, editora, edicao, isbn, ano):
        self.titulo = titulo
        self.autor = autor
        self.assunto = assunto
        self.editora = editora
        self.edicao = edicao
        self.isbn = isbn
        self.ano = ano
        
    def get_titulo(self):
        return self.titulo
    
    def get_autor(self):
        return self.autor

    def get_assunto(self):
        return self.assunto
    
    def get_editora(self):
        return self.editora
    
    def get_edicao(self):
        return self.edicao
    
    def get_isbn(self):
        return self.isbn
    
    def get_ano(self):
        return self.ano
    
    def AlterarLivro(self, titulo, autor, assunto, editora, edicao, isbn, ano):
        alterar = cadastrarLivro(titulo, autor, assunto, editora, edicao, isbn, ano)
        if alterar.get_titulo() != self.get_titulo():
            print("Título alterado com sucesso!")
        elif alterar.get_autor() != self.get_autor():
            print("Autor alterado com sucesso!")
        elif alterar.get_assunto() != self.get_assunto():
            print("Assunto alterado com sucesso!")
        elif alterar.get_editora() != self.get_editora():
            print("Editora alterada com sucesso!")
        elif alterar.get_edicao() != self.get_edicao():
            print("Edição alterada com sucesso!")
        elif alterar.get_isbn() != self.get_isbn():
            print("ISBN alterado com sucesso!")
        elif alterar.get_ano() != self.get_ano():
            print("Ano alterado com sucesso!")
        else:
            print("Nenhuma informação pode ser alterada!")
        
class cadastrarExemplar:
    def __init__(self,novoexemplar, alteracao, consulta):
        self.novoexemplar = novoexemplar
        self.alteracao = alteracao
        self.consulta = consulta
        
    def get_novoexemplar(self):
        return self.novoexemplar
    
    def get_alteracao(self):
        return self.alteracao
    
    def get_consulta(self):
        return self.consulta
    
class cadastrarCategoria:
    def __init__(self, categoria, alteracao, consulta, excluir):
        self.categoria = categoria
        self.alteracao = alteracao
        self.consulta = consulta
        self.excluir = excluir
        
    def get_categoria(self):
        return self.categoria
    
    def get_alteracao(self):
        return self.alteracao
    
    def get_consulta(self):
        return self.consulta
    
    def get_excluir(self):
        return self.excluir
    

        