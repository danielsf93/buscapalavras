#### Projeto Busca Palavras 
## Neste arquivo ficam as funcoes referentes ao desenvolvimento da ferramenta

class Textos:
    def __init__(self, texto1, texto2, textoBusca):
        self.texto1 = texto1
        self.texto2 = texto2

        def mensagemInicial(self, texto1):
            print("Olá, seja bem-vindo ao busca palavras")
        
        def solicitacaoArquivo(self, texto2):
            arquivo = input("Por favor insira o arquivo ao qual deseja realizar as buscas")
        
        def solicitaPalavra(self, textoBusca):
        palavra = input("Por favor, digite a palavra que você deseja buscar: ")
        if isinstance(palavra, str):
            self.textoBusca = palavra
        else:
        print("Erro: Por favor, digite uma palavra.")
