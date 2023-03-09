import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))))

from main.ohlc_chart import OhlcChart

if __name__ == "__main__":

    # 2023-03-09
    OhlcChart("덕양산업", 3, "ohlcv", None).get_chart_ohlcv()
    OhlcChart("금비", 3, "ohlcv", None).get_chart_ohlcv()
    OhlcChart("이아이디", 3, "ohlcv", None).get_chart_ohlcv()
    OhlcChart("평화홀딩스", 3, "ohlcv", None).get_chart_ohlcv()
    OhlcChart("화신", 3, "ohlcv", None).get_chart_ohlcv()
    OhlcChart("엘브이엠씨홀딩스", 3, "ohlcv", None).get_chart_ohlcv()
    OhlcChart("디아이씨", 3, "ohlcv", None).get_chart_ohlcv()
    OhlcChart("코오롱플라스틱", 3, "ohlcv", None).get_chart_ohlcv()
    OhlcChart("한미사이언스", 3, "ohlcv", None).get_chart_ohlcv()
    OhlcChart("에쓰씨엔지니어링", 3, "ohlcv", None).get_chart_ohlcv()
