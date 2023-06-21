from busca import ManipuladorValoress
import pandas as pd
from datetime import datetime, time


def executar_busca():
    manipulador = ManipuladorValoress()
    mensagem = manipulador.mensagemInicial()
    print(mensagem)

    valor = manipulador.solicitaValor()
    if valor is not None:
        # Faça algo com o valor retornado, se necessário
        print(f"Valor digitado: {valor}")

# Exemplo de uso
#executar_busca()

import pandas as pd
from datetime import time

base = pd.read_csv('sked-a23.csv')
def converteHora(base):
    base = base[['horaInício', 'horaFim']] = base['Time(UTC):93'].str.split('-', expand=True)
    base = base.rename(columns={0: 'col1', 1: 'col2'})
    base = base.drop(['col1', 'col2'], axis=1)
    base['horaFim'] = base['horaFim'].str.replace('2400', '0000')
    base['horaInício'] = base['horaInício'].str.slice(0, 2) + ':' + base['horaInício'].str.slice(2, 4)
    base['horaFim'] = base['horaFim'].str.slice(0, 2) + ':' + base['horaFim'].str.slice(2, 4)
    base['horaInício'] = pd.to_datetime(base['horaInício'], format='%H:%M').dt.time
    base['horaFim'] = pd.to_datetime(base['horaFim'], format='%H:%M').dt.time
    return base

print(converteHora(base))

