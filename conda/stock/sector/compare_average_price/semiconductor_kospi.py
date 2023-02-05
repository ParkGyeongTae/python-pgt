'''
pip install pandas,beautifulsoup4,finance-datareader,matplotlib -y
'''

import pandas as pd
import matplotlib.pyplot as plt

import FinanceDataReader as fdr

from datetime import datetime
from dateutil.relativedelta import relativedelta

def get_stock_code(name):
    '''이름을 입력하면 코드를 리턴'''

    df = fdr.StockListing('KRX')
    stock_code = df[df['Name'] == name]['Code'].to_string(index = False)
    return stock_code

if __name__ == '__main__':

    before_standard = (datetime.now() - relativedelta(years = 3)).strftime('%Y-%m-%d')

    df_exchange_rate    = fdr.DataReader(symbol = 'USD/KRW', start = before_standard)[['Close']]
    df_kospi            = fdr.DataReader(symbol = 'KS11', start = before_standard)[['Close']]
    df_samsung_elec     = fdr.DataReader(symbol = get_stock_code('삼성전자'), start = before_standard)[['Close']]
    df_samsung_pre_elec = fdr.DataReader(symbol = get_stock_code('삼성전자우'), start = before_standard)[['Close']]
    df_sk_hynix         = fdr.DataReader(symbol = get_stock_code('SK하이닉스'), start = before_standard)[['Close']]

    df_result = pd.concat([df_exchange_rate, df_kospi, df_samsung_elec, df_samsung_pre_elec, df_sk_hynix], axis = 1, join = 'inner')
    df_result.columns = ['USD/KRW', 'KOSPI', 'SS_ELEC', 'SS_ELEC_PRE', 'SK_HINIX']
    df_result.reset_index(inplace = True)

    df_result['USD/KRW'] = round((df_result['USD/KRW'] - (df_result['USD/KRW'].sum() / df_result['Date'].count())) / df_result['USD/KRW'] * 100, 2)
    df_result['KOSPI'] = round((df_result['KOSPI'] - (df_result['KOSPI'].sum() / df_result['Date'].count())) / df_result['KOSPI'] * 100, 2)
    df_result['SS_ELEC'] = round((df_result['SS_ELEC'] - (df_result['SS_ELEC'].sum() / df_result['Date'].count())) / df_result['SS_ELEC'] * 100, 2)
    df_result['SS_ELEC_PRE'] = round((df_result['SS_ELEC_PRE'] - (df_result['SS_ELEC_PRE'].sum() / df_result['Date'].count())) / df_result['SS_ELEC_PRE'] * 100, 2)
    df_result['SK_HINIX'] = round((df_result['SK_HINIX'] - (df_result['SK_HINIX'].sum() / df_result['Date'].count())) / df_result['SK_HINIX'] * 100, 2)

    plt.figure(figsize=(12, 8))

    plt.plot(df_result['Date'], df_result['USD/KRW'].to_list(), label = 'USD/KRW')
    plt.plot(df_result['Date'], df_result['KOSPI'].to_list(), label = 'KOSPI')
    plt.plot(df_result['Date'], df_result['SS_ELEC'].to_list(), label = 'SS_ELEC')
    plt.plot(df_result['Date'], df_result['SS_ELEC_PRE'].to_list(), label = 'SS_ELEC_PRE')
    plt.plot(df_result['Date'], df_result['SK_HINIX'].to_list(), label = 'SK_HINIX')

    plt.grid(axis = 'x')
    plt.grid(axis = 'y')

    plt.legend()
    plt.show()
