# pip install pandas,beautifulsoup4,finance-datareader,matplotlib,cufflinks,chart_studio -y

import FinanceDataReader as fdr
import cufflinks as cf
import plotly.offline as plyo

from datetime import datetime
from dateutil.relativedelta import relativedelta

class OhlcChart():

    def __init__(self, stock_name, period):
        self.stock_name = stock_name
        self.period = period

    def _get_stock_code(self):
        df = fdr.StockListing('KRX')
        stock_code = df[df['Name'] == self.stock_name]['Code'].to_string(index = False)
        return stock_code

    def get_chart_ohlcv(self):
        before_standard = (datetime.now() - relativedelta(years = self.period)).strftime('%Y-%m-%d')
        df = fdr.DataReader(symbol = self._get_stock_code(), start = before_standard)
        df = df[['Open', 'High', 'Low', 'Close', 'Volume']]
        qf = cf.QuantFig(
            df, 
            title = f'{self.stock_name}({self.period} Years)', 
            legend = 'top', 
            name = self.stock_name, 
            up_color = 'red', 
            down_color = 'blue')
        qf.add_volume()
        plyo.iplot(qf.iplot(asFigure = True))
