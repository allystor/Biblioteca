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




class Bibliotecario:
    def __init__(self, nome, idade, telefone, email):
        self.nome = nome
        self.idade = idade
        self.telefone = telefone
        self.email = email
        
    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome
        
    def get_idade(self):
        return self.idade
    
    def set_idade(self, idade):
        self.idade = idade
        
    def get_telefone(self):
        return self.telefone
    
    def set_telefone(self, telefone):
        self.telefone = telefone
    
    def get_email(self):
        return self.email
    
    def set_email(self, email):
        self.email = email

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
    
    def alterarLivro(self, alterar):
        self.titulo = alterar.get_titulo()
        
        
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
    

        