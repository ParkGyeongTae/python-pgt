'''
pip install pandas,beautifulsoup4,finance-datareader -y
'''

import FinanceDataReader as fdr

from datetime import datetime
from dateutil.relativedelta import relativedelta
import pandas as pd

if __name__ == '__main__':

    before_one_week = (datetime.now() - relativedelta(years = 3)).strftime('%Y-%m-%d')

    df_ks11 = fdr.DataReader(symbol = 'KQ11', start = before_one_week)
    df_ks11_close = df_ks11[['Close']]

    moving_average_list = [1, 3, 5, 10, 20, 30, 40, 50, 60, 120, 240, 360, 480, 600]
    result_dict = {}

    for day in moving_average_list:
        result_dict[f'MA_{day}'] = int(df_ks11_close.tail(day).sum() / day)

    df = pd.DataFrame.from_dict([result_dict], index = ['dd'])
    print(df)
