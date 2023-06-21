import pandas as pd
from datetime import datetime, time



base = pd.read_csv('sked-a23.csv', parse_dates=['Time(UTC):93'])
base[['horaInicio', 'horaFim']] = base['Time(UTC):93'].str.split('-', expand=True)
base['horaFim'] = base['horaFim'].str.replace('2400', '0000')
base['horaInicio'] = base['horaInicio'].str.slice(0, 2) + ':' + base['horaInicio'].str.slice(2, 4)
base['horaFim'] = base['horaFim'].str.slice(0, 2) + ':' + base['horaFim'].str.slice(2, 4)
base['horaInicio'] = pd.to_datetime(base['horaInicio'], format='%H:%M').dt.time
base['horaFim'] = pd.to_datetime(base['horaFim'], format='%H:%M').dt.time
print(base)

hora = datetime.now().strftime("%H:%M")
hora = datetime.strptime(hora, "%H:%M").time()

valores_filtrados = base.loc[(base['horaInicio'] <= hora) & (base['horaFim'] >= hora)]

print(f"veja aqui: {valores_filtrados}")