import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(os.path.dirname(__file__)))))

from main.ohlc_chart import OhlcChart

if __name__ == "__main__":
    OhlcChart("하이브", 3, "ohlcv", None).get_chart_ohlcv()
    OhlcChart("에스엠", 3, "ohlcv", None).get_chart_ohlcv()
    OhlcChart("JYP Ent.", 3, "ohlcv", None).get_chart_ohlcv()
    OhlcChart("와이지엔터테인먼트", 3, "ohlcv", None).get_chart_ohlcv()
