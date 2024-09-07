import pandas as pd 
import MetaTrader5 as mt5 
from datetime import datetime
from dateutil.relativedelta import relativedelta 



def importar_dados_historicos(ticker, start, end, timeframe = mt5.TIMEFRAME_M1):
        
    dados_brutos = pd.DataFrame() 

    start_loop = start
    while start_loop <= end:
        end_loop = start_loop + relativedelta(months=1) - relativedelta(days=1)
        dados_looping = mt5.copy_rates_range(ticker, timeframe, start_loop, end_loop)
        
        if dados_looping is not None:
            dados_looping = pd.DataFrame(dados_looping)
            dados_looping['ticker'] = str(ticker)
            dados_looping.index = pd.to_datetime(dados_looping['time'], unit='s')
            dados_looping['data'] = dados_looping.index.date
            dados_looping['horario'] = dados_looping.index.time 

            dados_brutos = pd.concat([dados_brutos, dados_looping])
        
        start_loop += relativedelta(months=1)

    return dados_brutos 
