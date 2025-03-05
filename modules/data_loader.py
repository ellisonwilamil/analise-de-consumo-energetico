# Carga e pré-processamento dos dados
import pandas as pd
from glob import glob

def carregar_dados():
    anos = ['2017', '2018', '2019','2020','2021']
    lista = []
    for ano in anos:
        files = sorted(glob(f'dados/campus_fpolis_{ano}/*.xlsx'))
        dados = pd.concat((pd.read_excel(file) for file in files), ignore_index=True)
        lista.append(dados[['p3','ta','tb','tc', 'fpa', 'fpb', 'fpc', 'q3', 'horario']])
        df = pd.concat(lista)
        df.set_index('horario', inplace=True)
    return df

