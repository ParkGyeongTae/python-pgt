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
    df_samsung_elec_pre = fdr.DataReader(symbol = get_stock_code('삼성전자우'), start = before_standard)
    df_samsung_elec_pre = df_samsung_elec_pre[['Open', 'High', 'Low', 'Close']]

    # for i in df_samsung_elec_pre.columns:
    #     df_samsung_elec_pre[i] = round((df_samsung_elec_pre[i] - df_samsung_elec_pre[i].mean()) / df_samsung_elec_pre[i] * 100, 2)

    qf = cf.QuantFig(
        df_samsung_elec_pre,
        title = '삼성전자우(4 Years)',
        legend = 'top',
        name = '삼성전자우',
        up_color = 'red',
        down_color = 'blue'
    )

    plyo.iplot(qf.iplot(asFigure = True))
