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

    before_standard = (datetime.now() - relativedelta(months = 6)).strftime('%Y-%m-%d')

    df_exchange_rate    = fdr.DataReader(symbol = 'USD/KRW', start = before_standard)[['Close']]
    df_kospi            = fdr.DataReader(symbol = 'KS11', start = before_standard)[['Close']]
    df_samsung_elec     = fdr.DataReader(symbol = get_stock_code('삼성전자'), start = before_standard)[['Close']]
    df_samsung_pre_elec = fdr.DataReader(symbol = get_stock_code('삼성전자우'), start = before_standard)[['Close']]
    df_sk_hynix         = fdr.DataReader(symbol = get_stock_code('SK하이닉스'), start = before_standard)[['Close']]
    df_db_hitek         = fdr.DataReader(symbol = get_stock_code('DB하이텍'), start = before_standard)[['Close']]
    df_hanmi            = fdr.DataReader(symbol = get_stock_code('한미반도체'), start = before_standard)[['Close']]

    df = pd.concat([df_exchange_rate, df_kospi, df_samsung_elec, df_samsung_pre_elec, df_sk_hynix, df_db_hitek, df_hanmi], axis = 1, join = 'inner')
    stock_list = ['USD/KRW', 'KOSPI', 'SS_ELEC', 'SS_ELEC_PRE', 'SK_HINIX', 'DB_HITEK', 'HANMI']
    df.columns = stock_list
    df.reset_index(inplace = True)

    df_4_week, df_3_week, df_2_week, df_1_week = df.copy(), df.copy(), df.copy(), df.copy()

    df_4_week = df_4_week[df_4_week['Date'] > str(datetime.now() - relativedelta(weeks = 4))]
    df_3_week = df_3_week[df_3_week['Date'] > str(datetime.now() - relativedelta(weeks = 3))]
    df_2_week = df_2_week[df_2_week['Date'] > str(datetime.now() - relativedelta(weeks = 2))]
    df_1_week = df_1_week[df_1_week['Date'] > str(datetime.now() - relativedelta(weeks = 1))]

    for stock in stock_list:
        df_4_week[stock] = round((df_4_week[stock] - (df_4_week[stock].sum() / df_4_week['Date'].count())) / df_4_week[stock] * 100, 2)
        df_3_week[stock] = round((df_3_week[stock] - (df_3_week[stock].sum() / df_3_week['Date'].count())) / df_3_week[stock] * 100, 2)
        df_2_week[stock] = round((df_2_week[stock] - (df_2_week[stock].sum() / df_2_week['Date'].count())) / df_2_week[stock] * 100, 2)
        df_1_week[stock] = round((df_1_week[stock] - (df_1_week[stock].sum() / df_1_week['Date'].count())) / df_1_week[stock] * 100, 2)

    print(df_4_week)

    # plt.figure(figsize=(20, 10))

    # plt.subplot(2,2,1)
    # for stock in stock_list:
    #     plt.plot(df_4_week['Date'], df_4_week[stock].to_list(), label = stock, linewidth = '1')
    # plt.title('4 Weeks')
    # plt.grid(True)
    # plt.legend(fontsize = 6)

    # plt.subplot(2,2,2)
    # for stock in stock_list:
    #     plt.plot(df_3_week['Date'], df_3_week[stock].to_list(), label = stock, linewidth = '1')
    # plt.title('3 Weeks')
    # plt.grid(True)
    # plt.legend(fontsize = 6)

    # plt.subplot(2,2,3)
    # for stock in stock_list:
    #     plt.plot(df_2_week['Date'], df_2_week[stock].to_list(), label = stock, linewidth = '1')
    # plt.title('2 Weeks')
    # plt.grid(True)
    # plt.legend(fontsize = 6)

    # plt.subplot(2,2,4)
    # for stock in stock_list:
    #     plt.plot(df_1_week['Date'], df_1_week[stock].to_list(), label = stock, linewidth = '1')
    # plt.title('1 Weeks')
    # plt.grid(True)
    # plt.legend(fontsize = 6)

    # plt.show()
