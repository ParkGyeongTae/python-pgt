'''
pip install pandas,beautifulsoup4,finance-datareader,matplotlib,cufflinks,chart_studio -y
'''

import FinanceDataReader as fdr
import cufflinks as cf
import plotly.offline as plyo
import pandas as pd
# import matplotlib.pyplot as plt

from datetime import datetime
from dateutil.relativedelta import relativedelta

def get_stock_code(name):
    df = fdr.StockListing('KRX')
    stock_code = df[df['Name'] == name]['Code'].to_string(index = False)
    return stock_code

if __name__ == '__main__':

    before_standard = (datetime.now() - relativedelta(years = 4)).strftime('%Y-%m-%d')
    df_db_hitek = fdr.DataReader(symbol = get_stock_code('DB하이텍'), start = before_standard)
    df_db_hitek = df_db_hitek[['Open', 'High', 'Low', 'Close']]

    # for i in df_db_hitek.columns:
    #     df_db_hitek[i] = round((df_db_hitek[i] - (df_db_hitek[i].sum() / len(df_db_hitek))) / df_db_hitek[i] * 100, 2)

    qf = cf.QuantFig(
        df_db_hitek,
        title = 'DB하이텍(4 Years)',
        legend = 'top',
        name = 'DB하이텍',
        up_color = 'red',
        down_color = 'blue')

    plyo.iplot(qf.iplot(asFigure = True))
