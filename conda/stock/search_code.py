'''
pip install pandas,beautifulsoup4,finance-datareader -y
'''

import FinanceDataReader as fdr

def search_code(name):
    df = fdr.StockListing('KRX')
    code = df[df['Name'] == name]['Code'][0]
    return code

if __name__ == '__main__':
    samsung_electronics_code = search_code('삼성전자')
    print(samsung_electronics_code)




# df_krx = fdr.StockListing('KRX')
# print(df_krx.head())

# df = fdr.DataReader('005930', '2023')
# print(df)