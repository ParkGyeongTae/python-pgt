'''
pip install pandas,beautifulsoup4,finance-datareader -y
'''

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
    df_kosdaq = get_kosdaq_dataframe()
    print(df_kosdaq.head(20))

    # code = get_stock_code('LG에너지솔루션')
    # df = fdr.DataReader(symbol = code, start = '2023-01-10', end = '2023-01-20')
    # print(df)
    # print(fdr.StockListing('KRX'))

# df_krx = fdr.StockListing('KRX')
# print(df_krx.head())

# df = fdr.DataReader('005930', '2023')
# print(df)