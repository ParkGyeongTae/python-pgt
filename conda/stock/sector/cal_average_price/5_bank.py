'''
pip install pandas,beautifulsoup4,finance-datareader,matplotlib -y
'''

import pandas as pd
import matplotlib.pyplot as plt

import FinanceDataReader as fdr

from datetime import datetime
from dateutil.relativedelta import relativedelta

def get_stock_code(name):
    '''이름을 입력하면 코드를 리턴'''

    df = fdr.StockListing('KRX')
    stock_code = df[df['Name'] == name]['Code'].to_string(index = False)
    return stock_code

if __name__ == '__main__':

    before_standard = (datetime.now() - relativedelta(years = 2)).strftime('%Y-%m-%d')

    df_exchange_rate = fdr.DataReader(symbol = 'USD/KRW', start = before_standard)[['Close']]
    df_kospi = fdr.DataReader(symbol = 'KS11', start = before_standard)[['Close']]
    df_kb = fdr.DataReader(symbol = get_stock_code('KB금융'), start = before_standard)[['Close']]
    df_shinhan = fdr.DataReader(symbol = get_stock_code('신한지주'), start = before_standard)[['Close']]
    df_hana = fdr.DataReader(symbol = get_stock_code('하나금융지주'), start = before_standard)[['Close']]
    df_kabang = fdr.DataReader(symbol = get_stock_code('카카오뱅크'), start = before_standard)[['Close']]
    df_ibk = fdr.DataReader(symbol = get_stock_code('기업은행'), start = before_standard)[['Close']]

    df = pd.concat([df_exchange_rate, df_kospi, df_kb, df_shinhan, df_hana, df_kabang, df_ibk], axis = 1, join = 'inner')
    stock_list = ['USD/KRW', 'KOSPI', 'KB', 'SHINHAN', 'HANA', 'KABANG', 'IBK']
    df.columns = stock_list
    df.reset_index(inplace = True)

    df_2_year, df_1_year, df_9_month, df_6_month, df_3_month, df_1_month = df.copy(), df.copy(), df.copy(), df.copy(), df.copy(), df.copy()

    df_1_year = df_1_year[df_1_year['Date'] > str(datetime.now() - relativedelta(years = 1))]
    df_9_month = df_9_month[df_9_month['Date'] > str(datetime.now() - relativedelta(months = 9))]
    df_6_month = df_6_month[df_6_month['Date'] > str(datetime.now() - relativedelta(months = 6))]
    df_3_month = df_3_month[df_3_month['Date'] > str(datetime.now() - relativedelta(months = 3))]
    df_1_month = df_1_month[df_1_month['Date'] > str(datetime.now() - relativedelta(months = 1))]

    for stock in stock_list:
        df_2_year[stock] = round((df_2_year[stock] - (df_2_year[stock].sum() / df_2_year['Date'].count())) / df_2_year[stock] * 100, 2)
        df_1_year[stock] = round((df_1_year[stock] - (df_1_year[stock].sum() / df_1_year['Date'].count())) / df_1_year[stock] * 100, 2)
        df_9_month[stock] = round((df_9_month[stock] - (df_9_month[stock].sum() / df_9_month['Date'].count())) / df_9_month[stock] * 100, 2)
        df_6_month[stock] = round((df_6_month[stock] - (df_6_month[stock].sum() / df_6_month['Date'].count())) / df_6_month[stock] * 100, 2)
        df_3_month[stock] = round((df_3_month[stock] - (df_3_month[stock].sum() / df_3_month['Date'].count())) / df_3_month[stock] * 100, 2)
        df_1_month[stock] = round((df_1_month[stock] - (df_1_month[stock].sum() / df_1_month['Date'].count())) / df_1_month[stock] * 100, 2)

    plt.figure(figsize=(20, 10))

    plt.subplot(3,2,1)
    for stock in stock_list:
        plt.plot(df_2_year['Date'], df_2_year[stock].to_list(), label = stock, linewidth = '1')
    plt.title('2 Years')
    plt.grid(True)
    plt.legend(fontsize = 6)

    plt.subplot(3,2,2)
    for stock in stock_list:
        plt.plot(df_1_year['Date'], df_1_year[stock].to_list(), label = stock, linewidth = '1')
    plt.title('1 Years')
    plt.grid(True)
    plt.legend(fontsize = 6)

    plt.subplot(3,2,3)
    for stock in stock_list:
        plt.plot(df_9_month['Date'], df_9_month[stock].to_list(), label = stock, linewidth = '1')
    plt.title('9 Months')
    plt.grid(True)
    plt.legend(fontsize = 6)

    plt.subplot(3,2,4)
    for stock in stock_list:
        plt.plot(df_6_month['Date'], df_6_month[stock].to_list(), label = stock, linewidth = '1')
    plt.title('6 Months')
    plt.grid(True)
    plt.legend(fontsize = 6)

    plt.subplot(3,2,5)
    for stock in stock_list:
        plt.plot(df_3_month['Date'], df_3_month[stock].to_list(), label = stock, linewidth = '1')
    plt.title('3 Months')
    plt.grid(True)
    plt.legend(fontsize = 6)

    plt.subplot(3,2,6)
    for stock in stock_list:
        plt.plot(df_1_month['Date'], df_1_month[stock].to_list(), label = stock, linewidth = '1')
    plt.title('1 Months')
    plt.grid(True)
    plt.legend(fontsize = 6)

    plt.show()
