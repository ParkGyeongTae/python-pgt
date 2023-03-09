import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from main.ohlc_chart import OhlcChart

if __name__ == "__main__":
    OhlcChart("LG에너지솔루션", 3, "ohlcv", None).get_chart_ohlcv()
    OhlcChart("삼성SDI", 3, "ohlcv", None).get_chart_ohlcv()
    OhlcChart("에코프로비엠", 3, "ohlcv", None).get_chart_ohlcv()
    OhlcChart("엘앤에프", 3, "ohlcv", None).get_chart_ohlcv()
    OhlcChart("SK아이이테크놀로지", 3, "ohlcv", None).get_chart_ohlcv()
