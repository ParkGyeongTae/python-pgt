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
    df_kosdaq           = fdr.DataReader(symbol = 'KQ11', start = before_standard)[['Close']]

    df_result = pd.concat([df_exchange_rate, df_kospi, df_kosdaq], axis = 1, join = 'inner')
    df_result.columns = ['USD/KRW', 'KOSPI', 'KOSDAQ']
    df_result.reset_index(inplace = True)

    df_result['USD/KRW'] = round((df_result['USD/KRW'] - (df_result['USD/KRW'].sum() / df_result['Date'].count())) / df_result['USD/KRW'] * 100, 2)
    df_result['KOSPI']   = round((df_result['KOSPI'] - (df_result['KOSPI'].sum() / df_result['Date'].count())) / df_result['KOSPI'] * 100, 2)
    df_result['KOSDAQ']  = round((df_result['KOSDAQ'] - (df_result['KOSDAQ'].sum() / df_result['Date'].count())) / df_result['KOSDAQ'] * 100, 2)

    plt.figure(figsize=(20, 8))

    plt.plot(df_result['Date'].to_list(), df_result['USD/KRW'].to_list(), label = 'USD/KRW')
    plt.plot(df_result['Date'].to_list(), df_result['KOSPI'].to_list(), label = 'KOSPI')
    plt.plot(df_result['Date'].to_list(), df_result['KOSDAQ'].to_list(), label = 'KOSDAQ')

    plt.grid(axis = 'x')
    plt.grid(axis = 'y')

    plt.legend()
    plt.show()
