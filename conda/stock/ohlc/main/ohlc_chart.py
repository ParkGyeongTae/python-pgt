# pip install pandas,beautifulsoup4,finance-datareader,matplotlib,cufflinks,chart_studio -y

import FinanceDataReader as fdr
import cufflinks as cf
import plotly.offline as plyo

from datetime import datetime
from dateutil.relativedelta import relativedelta

class OhlcChart():

    def __init__(self, stock_name, period, graph_type, symbol_name):
        self.stock_name = stock_name
        self.period = period
        self.graph_type = graph_type
        self.symbol_name = symbol_name
        self.data_name = stock_name
        self.title_name = f"{self.stock_name} ({self.period} Years)"
        self.ohlc_type = ["Open", "High", "Low", "Close"]
        self.ohlcv_type = ["Open", "High", "Low", "Close", "Volume"]

    def _get_stock_code(self):
        df = fdr.StockListing("KRX")
        stock_code = df[df["Name"] == self.stock_name]["Code"].to_string(index = False)
        return stock_code

    def _get_df_preprocessing(self, df):
        for item in self.ohlc_type:
            df = df[df[item] != 0]
        return df

    def get_chart_ohlcv(self):
        before_standard = (datetime.now() - relativedelta(years = self.period)).strftime("%Y-%m-%d")

        if self.stock_name is not None:
            df = fdr.DataReader(symbol = self._get_stock_code(), start = before_standard)
        elif self.stock_name is None:
            df = fdr.DataReader(symbol = self.symbol_name, start = before_standard)
        else:
            pass

        if self.graph_type == "ohlcv":
            df = self._get_df_preprocessing(df[self.ohlcv_type])
            qf = cf.QuantFig(
                df, 
                title = self.title_name, 
                legend = "top", 
                name = self.data_name, 
                up_color = "red", 
                down_color = "blue")
            qf.add_volume()
            plyo.iplot(qf.iplot(asFigure = True))
        elif self.graph_type == "ohlc":
            df = df = self._get_df_preprocessing(df[self.ohlc_type])
            qf = cf.QuantFig(
                df, 
                title = self.title_name, 
                legend = "top", 
                name = self.data_name, 
                up_color = "red", 
                down_color = "blue")
            plyo.iplot(qf.iplot(asFigure = True))
        else:
            pass
