 ## Projeto Busca Palavras 
import pandas as pd

class Palavra:
    def __init__(self, palavra, valor):
        self.palavra = palavra
        self.valor = valor
    
    def definePalavra(self, palavra):
        if isinstance(palavra, str):
            self.palavra = palavra
        else:
            print("Erro: Por favor digite uma palavra.")

    def defineValor(self, valor):
        if isinstance(valor, (int, float)):
            self.valor = valor
        else:
            print("Erro: Por favor digite um número.")

    def buscaPalavra(self, nome_arquivo):
        try:
            with open(nome_arquivo, 'r') as arquivo:
                conteudo = arquivo.read()
                if self.palavra.lower() in conteudo.lower():
                    return self.palavra
                else:
                    return None
        except FileNotFoundError:
            print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")

    def buscaValor(self, nome_arquivo):
        try:
            with open(nome_arquivo, 'r') as arquivo:
                conteudo = arquivo.read()
                numeros = [float(num) for num in conteudo.split() if num.replace('.', '', 1).isdigit()]
                if self.valor in numeros:
                    return self.valor
                else:
                    return None
        except FileNotFoundError:
            print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")


# Exemplo de uso
nome_arquivo = 'arquivo.txt'

# Criar objeto Palavra
palavra = Palavra('', 0)

# Solicitar a palavra-chave
palavra_chave = input("Digite a palavra-chave: ")
palavra.definePalavra(palavra_chave)

# Buscar a palavra-chave no arquivo
resultado_palavra = palavra.buscaPalavra(nome_arquivo)
if resultado_palavra:
    print(f"A palavra '{resultado_palavra}' foi encontrada no arquivo.")
else:
    print("A palavra-chave não foi encontrada no arquivo.")

# Solicitar o valor numérico
valor_numerico = input("Digite o valor numérico: ")
palavra.defineValor(float(valor_numerico))

# Buscar o valor numérico no arquivo
resultado_valor = palavra.buscaValor(nome_arquivo)
if resultado_valor:
    print(f"O valor numérico '{resultado_valor}' foi encontrado no arquivo.")
else:
    print("O valor numérico não foi encontrado no arquivo.")
