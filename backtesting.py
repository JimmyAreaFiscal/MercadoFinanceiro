import pandas as pd 
import numpy as np 
import math
from datetime import datetime, timedelta 

class Cruzamentos:
    """ Classe de funções para cruzamentos entre indicadores e/ou preços """

    def cruzar_acima(series_1, series_2, confirmacao = False):
        """ Função para retornar True ou False se houver cruzamento para cima """
        cond_cruz_acima = (series_1.shift(1) > series_2.shift(1)) & (series_1.shift(2) < series_2.shift(2))
        if confirmacao:
            cond_cruz_acima = cond_cruz_acima & (series_1 > series_2)

        return cond_cruz_acima 


    def cruzar_abaixo(series_1, series_2, confirmacao = False):
        """ Função para retornar True ou False se houver cruzamento para baixo """
        cond_cruz_acima = (series_1.shift(1) < series_2.shift(1)) & (series_1.shift(2) > series_2.shift(2))
        if confirmacao:
            cond_cruz_acima = cond_cruz_acima & (series_1 < series_2)

        return cond_cruz_acima 
    
   