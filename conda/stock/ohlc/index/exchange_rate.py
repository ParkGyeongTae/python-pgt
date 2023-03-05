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
    df = fdr.DataReader(symbol = 'USD/KRW', start = before_standard)
    df = df[['Open', 'High', 'Low', 'Close']]

    qf = cf.QuantFig(
        df, 
        title = '환율(4 Years)', 
        legend = 'top', 
        name = '환율', 
        up_color = 'red', 
        down_color = 'blue')

    plyo.iplot(qf.iplot(asFigure = True))
