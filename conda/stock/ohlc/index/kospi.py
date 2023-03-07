'''
pip install pandas,beautifulsoup4,finance-datareader,matplotlib,cufflinks,chart_studio -y
'''

import FinanceDataReader as fdr
import cufflinks as cf
import plotly.offline as plyo

from datetime import datetime
from dateutil.relativedelta import relativedelta

if __name__ == '__main__':

    before_standard = (datetime.now() - relativedelta(years = 3)).strftime('%Y-%m-%d')
    df = fdr.DataReader(symbol = 'KS11', start = before_standard)
    df = df[['Open', 'High', 'Low', 'Close', 'Volume']]

    qf = cf.QuantFig(
        df, 
        title = 'KOSPI(3 Years)', 
        legend = 'top', 
        name = 'KOSPI', 
        up_color = 'red', 
        down_color = 'blue')
    qf.add_volume()

    plyo.iplot(qf.iplot(asFigure = True))
