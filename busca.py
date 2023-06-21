#### Projeto Busca Palavras 
## Neste arquivo ficam as funcoes referentes ao desenvolvimento da ferramenta
import pandas as pd
import datetime

class ManipuladorValoress:
    def __init__(self):
        pass

    def mensagemInicial(self):
        boasVindas = "Olá, seja bem-vindo ao busca palavras"
        return boasVindas
    
    def solicitaValor(self):
        valor = input("Por favor, digite o valor que você deseja buscar: ")
        try:
            valor = float(valor)  # Converter para float
        except ValueError:
            print("Erro: Por favor, digite um valor numérico.")
            return None

        # Arquivo csv base das pequisas
        base = pd.read_csv('sked-a23.csv', parse_dates=['Time(UTC)'])

        hora = datetime.now().strftime("%H:%M")

        # Especificacao da coluna base
        valores_filtrados = base[base['kHz:75'] == valor]

        # Verificar se a linha foi encontrada
        if not valores_filtrados.empty:
            infoFiltrada = ['ITU:49', 'Station:201', 'Lng:49']
            resultado = valores_filtrados[infoFiltrada]
            resultadoBusca = f"As informações encontradas que correspondem a sua busca são: {resultado}"
            return resultadoBusca
        # Caso nao sejam encontrados valores correspondentes 
        else:
            print(f"Nenhum valor correspondente à '{valor}' foi encontrado.")
            return None