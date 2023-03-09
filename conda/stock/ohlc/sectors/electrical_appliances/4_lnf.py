import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(os.path.dirname(__file__)))))

from main.ohlc_chart import OhlcChart

if __name__ == "__main__":
    OhlcChart("엘앤에프", 3, "ohlcv", None).get_chart_ohlcv()
