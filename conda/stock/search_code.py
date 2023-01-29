'''
pip install pandas,beautifulsoup4,finance-datareader -y
'''

import FinanceDataReader as fdr

def get_stock_code(name):
    '''이름을 입력하면 코드를 리턴'''
    df = fdr.StockListing('KRX')
    stock_code = df[df['Name'] == name]['Code'].to_string(index = False)
    return stock_code

def get_kospi_dataframe():
    '''코스피를 리턴'''
    df = fdr.StockListing('KRX')
    df = df[df['Market'] == 'KOSPI']
    return df

def get_kosdaq_dataframe():
    '''코스닥을 리턴'''
    df = fdr.StockListing('KRX')
    df = df[df['Market'] == 'KOSDAQ']
    return df

if __name__ == '__main__':

    code = get_stock_code('삼성전자')
    print(code)
    code = get_stock_code('LG에너지솔루션')
    print(code)

    df = get_kospi_dataframe()
    print(df)

    df = get_kosdaq_dataframe()
    print(df)