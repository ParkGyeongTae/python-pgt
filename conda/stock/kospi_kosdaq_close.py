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
    df_kosdaq           = fdr.DataReader(symbol = 'KQ11', start = before_one_week)[['Close']]

    df_result = pd.concat([df_exchange_rate, df_kospi, df_kosdaq], axis = 1, join = 'inner')
    df_result.columns = ['USD/KRW', 'KOSPI', 'KOSDAQ']

    df_result.reset_index(inplace = True)
    # # df_result = df_result.sort_values(by = 'index', ascending = False)

    plt.plot(df_result['Date'].to_list(), df_result['USD/KRW'].to_list(), label = 'USD/KRW')
    plt.plot(df_result['Date'].to_list(), df_result['KOSPI'].to_list(), label = 'KOSPI')
    plt.plot(df_result['Date'].to_list(), df_result['KOSDAQ'].to_list(), label = 'KOSDAQ')

    plt.grid(axis = 'x')
    plt.grid(axis = 'y')

    plt.legend()
    plt.show()

    # print(df_result)
    exit()

    result_dict = {}

    for day in moving_average_list:

        result_dict[f'{day}'] = [
            int(df_exchange_rate.tail(day).sum() / day), 
            int(df_kospi.tail(day).sum() / day), 
            int(df_kosdaq.tail(day).sum() / day)]

    # print(result_dict)
    exit()

    df_result = pd.DataFrame(result_dict).T
    df_result.columns = ['USD/KRW', 'KOSPI', 'KOSDAQ']

    for column_name in df_result.columns:
        df_result[f'{column_name}_per'] = round(df_result[column_name] / df_result[column_name].iloc[0], 3) * 100

    df_result.reset_index(inplace = True)
    df_result = df_result.astype({'index': 'int64'})

    df_result = df_result.sort_values(by = 'index', ascending = False)

    plt.plot(df_result['index'].to_list()[::-1], df_result['USD/KRW_per'].to_list(), label = 'USD/KRW')
    plt.plot(df_result['index'].to_list()[::-1], df_result['KOSPI_per'].to_list(), label = 'KOSPI')
    plt.plot(df_result['index'].to_list()[::-1], df_result['KOSDAQ_per'].to_list(), label = 'KOSDAQ')

    plt.grid(axis = 'x')
    plt.grid(axis = 'y')

    plt.legend()
    plt.show()
