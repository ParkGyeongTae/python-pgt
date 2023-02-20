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

    before_standard = (datetime.now() - relativedelta(years = 2)).strftime('%Y-%m-%d')
    df_kospi = fdr.DataReader(symbol = 'KS11', start = before_standard)
    df_kospi = df_kospi[['Open', 'High', 'Low', 'Close']]
    df_kospi.reset_index(inplace = True)

    qf = cf.QuantFig(
        df_kospi,
        title = 'Kospi 2 years',
        legend = 'top',
        name = 'Kospi',
        up_color = 'red',
        down_color = 'blue'
    )

    plyo.iplot(qf.iplot(asFigure = True))
