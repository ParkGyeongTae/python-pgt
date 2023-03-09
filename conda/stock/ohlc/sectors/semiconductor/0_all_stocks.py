import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from main.ohlc_chart import OhlcChart

if __name__ == "__main__":
    OhlcChart("삼성전자", 3, "ohlcv", None).get_chart_ohlcv()
    OhlcChart("SK하이닉스", 3, "ohlcv", None).get_chart_ohlcv()
    OhlcChart("삼성전자우", 3, "ohlcv", None).get_chart_ohlcv()
    OhlcChart("SK스퀘어", 3, "ohlcv", None).get_chart_ohlcv()
    OhlcChart("DB하이텍", 3, "ohlcv", None).get_chart_ohlcv()
    OhlcChart("한미반도체", 3, "ohlcv", None).get_chart_ohlcv()
