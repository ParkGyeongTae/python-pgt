'''
pip install pandas,beautifulsoup4,finance-datareader -y
'''

# - 각종 지수 : KS11(코스피 지수), KQ11(코스닥 지수), DJI(다우 지수), IXIC(나스닥 지수), US500(S&P5000)
# - 환율 데이터 : USD/KRX(원달러 환율), USD/EUR(달러당 유로화 환율), CNY/KRX(위완화 원화 환율)

import FinanceDataReader as fdr

def get_stock_code(name):
    df = fdr.StockListing('KRX')
    stock_code = df[df['Name'] == name]['Code'].to_string(index = False)
    return stock_code

def get_kospi_dataframe():
    df = fdr.StockListing('KRX')
    df = df[df['Market'] == 'KOSPI']
    return df

def get_kosdaq_dataframe():
    df = fdr.StockListing('KRX')
    df = df[df['Market'] == 'KOSDAQ']
    return df

if __name__ == '__main__':
    # df_kosdaq = get_kosdaq_dataframe()
    # print(df_kosdaq.head(20))
    df = fdr.DataReader('KS11')
    print(df)
    # code = get_stock_code('LG에너지솔루션')
    # df = fdr.DataReader(symbol = code, start = '2023-01-10', end = '2023-01-20')
    # print(df)
    # print(fdr.StockListing('KRX'))

# df_krx = fdr.StockListing('KRX')
# print(df_krx.head())

# df = fdr.DataReader('005930', '2023')
# print(df)