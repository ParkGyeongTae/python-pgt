import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(os.path.dirname(__file__)))))

from main.ohlc_chart import OhlcChart

if __name__ == "__main__":
    chart_settings = OhlcChart(None, 3, "ohlcv", "KQ11")
    chart_settings.title_name = "코스닥 (3 Years)"
    chart_settings.data_name = "코스닥"
    chart_settings.get_chart_ohlcv()
