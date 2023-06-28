#### Projeto Busca Palavras 
## Neste arquivo ficam as funcoes referentes ao desenvolvimento da ferramenta
import pandas as pd
from datetime import datetime

class ManipuladorValores:
    def mensagemInicial(self):
        boasVindas = "Olá, seja bem-vindo ao busca palavras"
        return boasVindas
    
    def processarBase(self, base):
        base[['horaInicio', 'horaFim']] = base['Time(UTC):93'].str.split('-', expand=True)
        base['horaFim'] = base['horaFim'].str.replace('2400', '0000')
        base['horaInicio'] = base['horaInicio'].str.slice(0, 2) + ':' + base['horaInicio'].str.slice(2, 4)
        base['horaFim'] = base['horaFim'].str.slice(0, 2) + ':' + base['horaFim'].str.slice(2, 4)
        base['horaInicio'] = pd.to_datetime(base['horaInicio'], format='%H:%M').dt.time
        base['horaFim'] = pd.to_datetime(base['horaFim'], format='%H:%M').dt.time
        return base

    def solicitaValor(self):
        valor = input("Por favor, digite o valor que você deseja buscar: ")
        try:
            valor = float(valor)  # Converter para float
        except ValueError:
            raise ValueError("Erro: Por favor, digite um valor numérico.")

        hora = datetime.now().strftime("%H:%M")
        hora = datetime.strptime(hora, "%H:%M").time()

        # Arquivo csv base das pequisas
        base = pd.read_csv('sked-a23.csv', parse_dates=['Time(UTC):93'])
        base = self.processarBase(base)

        # Especificacao da coluna base
        valores_filtrados = base[base['kHz:75'] == valor]

        # Verificar se a linha foi encontrada
        if not valores_filtrados.empty:
            # Filtro nas colunas horaInicio e horaFim
            valores_filtrados = valores_filtrados[
                (valores_filtrados['horaInicio'] <= hora) & (valores_filtrados['horaFim'] >= hora)
            ]

            if not valores_filtrados.empty:
                infoFiltrada = ['ITU:49', 'Station:201', 'Lng:49', 'horaInicio', 'horaFim']
                resultado = valores_filtrados[infoFiltrada]
                resultadoBusca = f"As informações encontradas que correspondem a sua busca são: {resultado}"
                return resultadoBusca
            else:
                print(f"Nenhum valor correspondente à '{valor}' foi encontrado no horário atual.")
                return None
        else:
            print(f"Nenhum valor correspondente à '{valor}' foi encontrado.")
            return None

manipulador = ManipuladorValores()
resultado = manipulador.solicitaValor()
print(resultado)
