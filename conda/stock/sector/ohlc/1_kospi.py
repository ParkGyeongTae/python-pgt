'''
pip install pandas,beautifulsoup4,finance-datareader,matplotlib,cufflinks,chart_studio -y
'''

import FinanceDataReader as fdr
import cufflinks as cf
import plotly.offline as plyo

from datetime import datetime
from dateutil.relativedelta import relativedelta

if __name__ == '__main__':

    before_standard = (datetime.now() - relativedelta(years = 4)).strftime('%Y-%m-%d')
    df_kospi = fdr.DataReader(symbol = 'KS11', start = before_standard)
    df_kospi = df_kospi[['Open', 'High', 'Low', 'Close']]

    # for i in df_kospi.columns:
    #     df_kospi[i] = round((df_kospi[i] - df_kospi[i].mean()) / df_kospi[i] * 100, 2)

    qf = cf.QuantFig(
        df_kospi,
        title = 'KOSPI(4 Years)',
        legend = 'top',
        name = 'KOSPI',
        up_color = 'red',
        down_color = 'blue'
    )

    plyo.iplot(qf.iplot(asFigure = True))
