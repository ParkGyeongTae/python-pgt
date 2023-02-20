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

    before_standard = (datetime.now() - relativedelta(years = 5)).strftime('%Y-%m-%d')
    df_kosdaq = fdr.DataReader(symbol = 'KQ11', start = before_standard)
    df_kosdaq = df_kosdaq[['Open', 'High', 'Low', 'Close']]

    qf = cf.QuantFig(
        df_kosdaq,
        title = 'KOSDAQ(5 Years)',
        legend = 'top',
        name = 'KOSDAQ',
        up_color = 'red',
        down_color = 'blue'
    )

    plyo.iplot(qf.iplot(asFigure = True))
