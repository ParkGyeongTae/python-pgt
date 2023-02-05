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

if __name__ == '__main__':

    before_one_week = (datetime.now() - relativedelta(years = 3)).strftime('%Y-%m-%d')

    df_exchange_rate    = fdr.DataReader(symbol = 'USD/KRW', start = before_one_week)[['Close']]
    df_kospi            = fdr.DataReader(symbol = 'KS11', start = before_one_week)[['Close']]
    df_lg_energy        = fdr.DataReader(symbol = get_stock_code('LG에너지솔루션'), start = before_one_week)[['Close']]
    df_samsung_sdi      = fdr.DataReader(symbol = get_stock_code('삼성SDI'), start = before_one_week)[['Close']]
    df_echoprobm        = fdr.DataReader(symbol = get_stock_code('에코프로비엠'), start = before_one_week)[['Close']]
    df_lnf              = fdr.DataReader(symbol = get_stock_code('엘앤에프'), start = before_one_week)[['Close']]
    df_ski_tech         = fdr.DataReader(symbol = get_stock_code('SK아이이테크놀로지'), start = before_one_week)[['Close']]

    moving_average_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 25, 30, 35, 40, 45, 50, 60, 120, 200]

    result_dict = {}

    for day in moving_average_list:
        result_dict[f'avg_{day}'] = [
            int(df_exchange_rate.tail(day).sum() / day), 
            int(df_kospi.tail(day).sum() / day), 
            int(df_lg_energy.tail(day).sum() / day), 
            int(df_samsung_sdi.tail(day).sum() / day), 
            int(df_echoprobm.tail(day).sum() / day),
            int(df_lnf.tail(day).sum() / day),
            int(df_ski_tech.tail(day).sum() / day)]

    df_result = pd.DataFrame(result_dict).T
    df_result.columns = ['USD/KRW', 'KOSPI', 'LG_ENSOL', 'SS_SDI', 'ECHOPROBM', 'LNF', 'SKI_TECH']

    for column_name in df_result.columns:
        df_result[f'{column_name}_per'] = round(df_result[column_name] / df_result[column_name].iloc[0], 3) * 100

    print(df_result)
