import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from main.ohlc_chart import OhlcChart

if __name__ == '__main__':
    OhlcChart('LG에너지솔루션', 3).get_chart_ohlcv()