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

    before_one_week = (datetime.now() - relativedelta(years = 3)).strftime('%Y-%m-%d')

    df_exchange_rate    = fdr.DataReader(symbol = 'USD/KRW', start = before_one_week)[['Close']]
    df_kospi            = fdr.DataReader(symbol = 'KS11', start = before_one_week)[['Close']]
    df_samsung_elec     = fdr.DataReader(symbol = get_stock_code('삼성전자'), start = before_one_week)[['Close']]
    df_samsung_pre_elec = fdr.DataReader(symbol = get_stock_code('삼성전자우'), start = before_one_week)[['Close']]
    df_sk_hynix         = fdr.DataReader(symbol = get_stock_code('SK하이닉스'), start = before_one_week)[['Close']]

    moving_average_list = list(range(1, 61))
    # moving_average_list = list(range(1, 121))

    result_dict = {}

    for day in moving_average_list:
        result_dict[f'{day}'] = [
            int(df_exchange_rate.tail(day).sum() / day), 
            int(df_kospi.tail(day).sum() / day), 
            int(df_samsung_elec.tail(day).sum() / day), 
            int(df_samsung_pre_elec.tail(day).sum() / day), 
            int(df_sk_hynix.tail(day).sum() / day)]

    df_result = pd.DataFrame(result_dict).T
    df_result.columns = ['USD/KRW', 'KOSPI', 'SS_ELEC', 'SS_ELEC_PRE', 'SK_HINIX']

    for column_name in df_result.columns:
        df_result[f'{column_name}_per'] = round(df_result[column_name] / df_result[column_name].iloc[0], 3) * 100

    df_result.reset_index(inplace = True)
    df_result = df_result.astype({'index': 'int64'})

    df_result = df_result.sort_values(by = 'index', ascending = False)

    plt.plot(df_result['index'].to_list()[::-1], df_result['USD/KRW_per'].to_list(), label = 'USD/KRW')
    plt.plot(df_result['index'].to_list()[::-1], df_result['KOSPI_per'].to_list(), label = 'KOSPI')
    plt.plot(df_result['index'].to_list()[::-1], df_result['SS_ELEC_per'].to_list(), label = 'SS_ELEC')
    plt.plot(df_result['index'].to_list()[::-1], df_result['SS_ELEC_PRE_per'].to_list(), label = 'SS_ELEC_PRE')
    plt.plot(df_result['index'].to_list()[::-1], df_result['SK_HINIX_per'].to_list(), label = 'SK_HINIX')

    plt.grid(axis = 'x')
    plt.grid(axis = 'y')

    plt.legend()
    plt.show()
