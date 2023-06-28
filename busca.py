"""
O projeto palavras tem o objetivo de servir como uma ferramenta de buscas, onde o usuario/visitante
ao entrar na plataforma, pode realizar a busca pela sua estacao de interesse, e obter as informacoes
referentes aos programas que estao em transmissao em um contexto da America Latina, com horarios e 
informacoes. 
"""

import pandas as pd
from datetime import datetime, timedelta

class ManipuladorValores:
    """
    Essa classe tem por objetivo desenvolver as funcoes que realizam a solicitacao do valor base das
    buscas, de modo a englobar desde a mensagem de boas-vindas, ate o resultado na busca, que se
    refere as informacoes de horario, pais e programas em exibicao durante a hora atual de busca. 
    """
    # Mensagem de boas vindas ao usuario.
    def mensagemInicial(self):
        boasVindas = "Olá, seja bem-vindo ao busca palavras"
        return boasVindas
    
    def processarBase(self, base):
        """
        Esta funcao recebe o arquivo csv que possui a base de dados que sera processado durante 
        a busca, contendo os horarios dos programas da radio, e as informacoes acerca. 
        """
        base[['horaInicio', 'horaFim']] = base['Time(UTC):93'].str.split('-', expand=True)
        base['horaFim'] = base['horaFim'].str.replace('2400', '0000')
        base['horaInicio'] = base['horaInicio'].str.slice(0, 2) + ':' + base['horaInicio'].str.slice(2, 4)
        base['horaFim'] = base['horaFim'].str.slice(0, 2) + ':' + base['horaFim'].str.slice(2, 4)
        base['horaInicio'] = pd.to_datetime(base['horaInicio'], format='%H:%M').dt.time
        base['horaFim'] = pd.to_datetime(base['horaFim'], format='%H:%M').dt.time
        return base

    def solicitaValor(self:float):
        """
        Essa funcao solicita ao usuario o numero da estacao ao qual a busca sera realizada,
        o paramentro exigido trata-se de uma varial float, caso a funcao receba uma string 
        ou outro tipo de dado o programa apresentara uma mensagem de erro.
        
        A funcao retorna as informacoes referentes a estacao, pais, e horarios.
        """
        valor = input("Por favor, digite o valor que você deseja buscar: ") 
        try:    #Tenta converter o valor para float.
            valor = float(valor)  #Converter para float.
        except ValueError: #Caso nao consiga apresenta uma mensagem de erro. 
            raise ValueError("Erro: Por favor, digite um valor numérico.")

        hora_atual = datetime.now() #Para obter a hora atual em que o usuario realiza a busca
        hora_atual_formatada = hora_atual.strftime('%H:%M')
        hora_futura = hora_atual + timedelta(hours=1) # adicao de 1 hora ao intervalo
        hora_futura_formatada = hora_futura.strftime('%H:%M')


        # Arquivo csv base das pequisas
        base = pd.read_csv('sked-a23.csv')
        base = self.processarBase(base)

        # Especificacao da coluna base onde o valor da estacao sera a base da busca.
        valores_filtrados = base[base['kHz:75'] == valor]

        # Verificar se a linha foi encontrada
        if not valores_filtrados.empty:
            # Filtro nas colunas horaInicio e horaFim
            valores_filtrados[(valores_filtrados['horaInicio'] >= hora_atual_formatada) & (valores_filtrados['horaFim'] < hora_futura_formatada)]

            if not valores_filtrados.empty:
                infoFiltrada = ['kHz:75', 'ITU:49', 'Station:201', 'Lng:49', 'horaInicio', 'horaFim']
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