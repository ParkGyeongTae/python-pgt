'''
pip install pandas,beautifulsoup4,finance-datareader,matplotlib -y
'''

import pandas as pd
import FinanceDataReader as fdr

from datetime import datetime
from dateutil.relativedelta import relativedelta

def get_stock_code(name):
    '''이름을 입력하면 코드를 리턴'''
    df = fdr.StockListing('KRX')
    stock_code = df[df['Name'] == name]['Code'].to_string(index = False)
    return stock_code

def get_kospi_dataframe():
    '''코스피를 리턴'''
    df = fdr.StockListing('KRX')
    df = df[df['Market'] == 'KOSPI']
    return df

if __name__ == '__main__':

    before_one_week = (datetime.now() - relativedelta(years = 3)).strftime('%Y-%m-%d')

    df_ks11 = fdr.DataReader(symbol = 'KS11', start = before_one_week)[['Close']]
    df_samsung = fdr.DataReader(symbol = get_stock_code('삼성전자'), start = before_one_week)[['Close']]

    moving_average_list = [1, 3, 5, 7, 10, 15, 20, 30, 40, 50, 60, 120, 200, 240, 360, 400, 480, 600, 720]

    result_dict = {}

    for day in moving_average_list:
        result_dict[f'avg_{day}'] = [int(df_ks11.tail(day).sum() / day), int(df_samsung.tail(day).sum() / day)]

    df_result = pd.DataFrame(result_dict).T
    df_result.columns = ['kospi', 'samsung']

    df_result['kospi_per'] = round(df_result['kospi'] / df_result['kospi'].iloc[0], 2)
    df_result['samsung_per'] = round(df_result['samsung'] / df_result['samsung'].iloc[0], 2)

    print(df_result)
