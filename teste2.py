import pandas as pd
from datetime import datetime, timedelta

base = pd.read_csv('sked-a23.csv')


base[['horaInicio', 'horaFim']] = base['Time(UTC):93'].str.split('-', expand=True)
base['horaFim'] = base['horaFim'].str.replace('2400', '0000')
base['horaInicio'] = base['horaInicio'].str.slice(0, 2) + ':' + base['horaInicio'].str.slice(2, 4) + ':00'
base['horaFim'] = base['horaFim'].str.slice(0, 2) + ':' + base['horaFim'].str.slice(2, 4) + ':00'
#print(base)

def solicitaValor(base):
        valor = input("Por favor, digite o valor que você deseja buscar: ") 
        try:    #Tenta converter o valor para float.
            valor = float(valor)  #Converter para float.
        except ValueError: #Caso nao consiga apresenta uma mensagem de erro. 
            raise ValueError("Erro: Por favor, digite um valor numérico.")

        hora_atual = datetime.now()
        hora_atual_formatada = hora_atual.strftime('%H:%M:%S')

        hora_futura = hora_atual + timedelta(hours=1)
        hora_futura_formatada = hora_futura.strftime('%H:%M:%S')

        # Arquivo csv base das pequisas

        # Especificacao da coluna base onde o valor da estacao sera a base da busca.
        valores_filtrados = base[base['kHz:75'] == valor]

        # Verificar se a linha foi encontrada
        if not valores_filtrados.empty:
            # Filtro nas colunas horaInicio e horaFim
            valores_filtrados = valores_filtrados[(valores_filtrados['horaInicio'] <= hora_atual_formatada) & (valores_filtrados['horaFim'] >= hora_futura_formatada)]

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

#solicitaValor(base)

hora_atual = datetime.now()
hora_atual_formatada = hora_atual.strftime('%H:%M:%S')
hora_futura = hora_atual + timedelta(hours=1)
hora_futura_formatada = hora_futura.strftime('%H:%M:%S')
valores_filtrados = base

#valores_filtrados = valores_filtrados[(valores_filtrados['horaInicio'] >= hora_atual_formatada) & (valores_filtrados['horaFim'] <= 'hora_futura_formatada')]
valores_filtrados['horaInicio'] = pd.to_datetime(valores_filtrados['horaInicio'], format='%H:%M:%S').dt.time
valores_filtrados['horaFim'] = pd.to_datetime(valores_filtrados['horaFim'], format='%H:%M:%S').dt.time

hora_atual_formatada = pd.to_datetime(hora_atual_formatada, format='%H:%M:%S').time()
hora_futura_formatada = pd.to_datetime(hora_futura_formatada, format='%H:%M:%S').time()

valores_filtrados = valores_filtrados[(valores_filtrados['horaInicio'] >= hora_atual_formatada) & (valores_filtrados['horaFim'] <= hora_futura_formatada)]


print('hora atual', hora_atual_formatada, 'hora futura', hora_futura_formatada)
print(valores_filtrados[['horaInicio', 'horaFim']])
#print(teste)

##print(teste[['horaInicio', 'horaFim']])

##print('hora atual', hora_atual_formatada, 'hora futura', hora_futura_formatada)