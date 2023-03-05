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
    df = fdr.DataReader(symbol = get_stock_code('KB금융'), start = before_standard)
    df = df[['Open', 'High', 'Low', 'Close']]

    qf = cf.QuantFig(
        df, 
        title = 'KB금융(4 Years)', 
        legend = 'top', 
        name = 'KB금융', 
        up_color = 'red', 
        down_color = 'blue')

    plyo.iplot(qf.iplot(asFigure = True))
