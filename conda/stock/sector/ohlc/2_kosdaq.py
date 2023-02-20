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

if __name__ == '__main__':

    before_standard = (datetime.now() - relativedelta(years = 4)).strftime('%Y-%m-%d')
    df_kosdaq = fdr.DataReader(symbol = 'KQ11', start = before_standard)
    df_kosdaq = df_kosdaq[['Open', 'High', 'Low', 'Close']]

    # for i in df_kosdaq.columns:
    #     df_kosdaq[i] = round((df_kosdaq[i] - df_kosdaq[i].mean()) / df_kosdaq[i] * 100, 2)

    qf = cf.QuantFig(
        df_kosdaq,
        title = 'KOSDAQ(4 Years)',
        legend = 'top',
        name = 'KOSDAQ',
        up_color = 'red',
        down_color = 'blue'
    )

    plyo.iplot(qf.iplot(asFigure = True))
