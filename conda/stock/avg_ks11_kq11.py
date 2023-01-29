'''
pip install pandas,beautifulsoup4,finance-datareader -y
'''

import FinanceDataReader as fdr

from datetime import datetime
from dateutil.relativedelta import relativedelta
import pandas as pd

if __name__ == '__main__':

    before_one_week = (datetime.now() - relativedelta(years = 3)).strftime('%Y-%m-%d')

    df_ks11 = fdr.DataReader(symbol = 'KS11', start = before_one_week)[['Close']]
    df_kq11 = fdr.DataReader(symbol = 'KQ11', start = before_one_week)[['Close']]

    moving_average_list = [1, 3, 5, 7, 10, 15, 20, 30, 40, 50, 60, 120, 240, 360, 480, 600, 720]

    result_dict = {}

    for day in moving_average_list:
        result_dict[f'avg_{day}'] = [int(df_ks11.tail(day).sum() / day), int(df_kq11.tail(day).sum() / day)]

    df_result = pd.DataFrame(result_dict).T
    df_result.columns = ['kospi', 'kodaq']

    print(df_result)
