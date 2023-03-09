import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(os.path.dirname(__file__)))))

from main.ohlc_chart import OhlcChart

if __name__ == "__main__":

    # 2023-03-09
    OhlcChart("덕양산업", 3, "ohlcv", None).get_chart_ohlcv()
    OhlcChart("금비", 3, "ohlcv", None).get_chart_ohlcv()
    OhlcChart("이아이디", 3, "ohlcv", None).get_chart_ohlcv()
    OhlcChart("평화홀딩스", 3, "ohlcv", None).get_chart_ohlcv()
    OhlcChart("화신", 3, "ohlcv", None).get_chart_ohlcv()

    OhlcChart("석경에이티", 3, "ohlcv", None).get_chart_ohlcv()
    OhlcChart("자이글", 3, "ohlcv", None).get_chart_ohlcv()
    OhlcChart("케이씨에스", 3, "ohlcv", None).get_chart_ohlcv()
    OhlcChart("에코플라스틱", 3, "ohlcv", None).get_chart_ohlcv()
    OhlcChart("에스피지", 3, "ohlcv", None).get_chart_ohlcv()
