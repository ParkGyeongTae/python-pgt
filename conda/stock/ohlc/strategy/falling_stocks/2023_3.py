import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(os.path.dirname(__file__)))))

from main.ohlc_chart import OhlcChart

if __name__ == "__main__":

    # 2023-03-09
    OhlcChart("한국ANKOR유전", 3, "ohlcv", None).get_chart_ohlcv()
    OhlcChart("이수화학", 3, "ohlcv", None).get_chart_ohlcv()
    OhlcChart("DB하이텍1우", 3, "ohlcv", None).get_chart_ohlcv()
    OhlcChart("코스모화학", 3, "ohlcv", None).get_chart_ohlcv()
    OhlcChart("금양", 3, "ohlcv", None).get_chart_ohlcv()

    OhlcChart("라온텍", 3, "ohlcv", None).get_chart_ohlcv()
    OhlcChart("뉴지랩파마", 3, "ohlcv", None).get_chart_ohlcv()
    OhlcChart("국일제지", 3, "ohlcv", None).get_chart_ohlcv()
    OhlcChart("에스디생명공학", 3, "ohlcv", None).get_chart_ohlcv()
    OhlcChart("일야", 3, "ohlcv", None).get_chart_ohlcv()
