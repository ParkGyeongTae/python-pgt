import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from main.ohlc_chart import OhlcChart

if __name__ == "__main__":
    OhlcChart("이마트", 3, "ohlcv", None).get_chart_ohlcv()
    OhlcChart("BGF리테일", 3, "ohlcv", None).get_chart_ohlcv()
    OhlcChart("GS리테일", 3, "ohlcv", None).get_chart_ohlcv()
    OhlcChart("롯데쇼핑", 3, "ohlcv", None).get_chart_ohlcv()
    OhlcChart("신세계", 3, "ohlcv", None).get_chart_ohlcv()
    OhlcChart("현대백화점", 3, "ohlcv", None).get_chart_ohlcv()
