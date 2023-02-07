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

    df_exchange_rate    = fdr.DataReader(symbol = 'USD/KRW', start = before_standard)[['Close']]
    df_kospi            = fdr.DataReader(symbol = 'KS11', start = before_standard)[['Close']]
    df_samsung_elec     = fdr.DataReader(symbol = get_stock_code('삼성전자'), start = before_standard)[['Close']]
    df_samsung_pre_elec = fdr.DataReader(symbol = get_stock_code('삼성전자우'), start = before_standard)[['Close']]
    df_sk_hynix         = fdr.DataReader(symbol = get_stock_code('SK하이닉스'), start = before_standard)[['Close']]
    df_db_hitek         = fdr.DataReader(symbol = get_stock_code('DB하이텍'), start = before_standard)[['Close']]
    df_hanmi            = fdr.DataReader(symbol = get_stock_code('한미반도체'), start = before_standard)[['Close']]

    df = pd.concat([df_exchange_rate, df_kospi, df_samsung_elec, df_samsung_pre_elec, df_sk_hynix, df_db_hitek, df_hanmi], axis = 1, join = 'inner')
    df.columns = ['USD/KRW', 'KOSPI', 'SS_ELEC', 'SS_ELEC_PRE', 'SK_HINIX', 'DB_HITEK', 'HANMI']
    df.reset_index(inplace = True)

    df_2_year = df.copy()
    df_1_year = df.copy()
    df_9_month = df.copy()
    df_6_month = df.copy()
    df_3_month = df.copy()
    df_1_month = df.copy()

    df_1_year = df_1_year[df_1_year['Date'] > str(datetime.now() - relativedelta(years = 1))]
    df_9_month = df_9_month[df_9_month['Date'] > str(datetime.now() - relativedelta(months = 9))]
    df_6_month = df_6_month[df_6_month['Date'] > str(datetime.now() - relativedelta(months = 6))]
    df_3_month = df_3_month[df_3_month['Date'] > str(datetime.now() - relativedelta(months = 3))]
    df_1_month = df_1_month[df_1_month['Date'] > str(datetime.now() - relativedelta(months = 1))]

    stock_list = ['USD/KRW', 'KOSPI', 'SS_ELEC', 'SS_ELEC_PRE', 'SK_HINIX', 'DB_HITEK', 'HANMI']

    for stock in stock_list:
        df_2_year[stock] = round(df_2_year[stock] / df_2_year[stock].iloc[0], 3) * 100
        df_1_year[stock] = round(df_1_year[stock] / df_1_year[stock].iloc[0], 3) * 100
        df_9_month[stock] = round(df_9_month[stock] / df_9_month[stock].iloc[0], 3) * 100
        df_6_month[stock] = round(df_6_month[stock] / df_6_month[stock].iloc[0], 3) * 100
        df_3_month[stock] = round(df_3_month[stock] / df_3_month[stock].iloc[0], 3) * 100
        df_1_month[stock] = round(df_1_month[stock] / df_1_month[stock].iloc[0], 3) * 100

    plt.figure(figsize=(20, 10))

    plt.subplot(3,2,1)
    # plt.title('before 2 years')
    plt.plot(df_2_year['Date'], df_2_year['USD/KRW'].to_list(), label = 'USD/KRW', linewidth = '1')
    plt.plot(df_2_year['Date'], df_2_year['KOSPI'].to_list(), label = 'KOSPI', linewidth = '2')
    plt.plot(df_2_year['Date'], df_2_year['SS_ELEC'].to_list(), label = 'SS_ELEC', linewidth = '1')
    plt.plot(df_2_year['Date'], df_2_year['SS_ELEC_PRE'].to_list(), label = 'SS_ELEC_PRE', linewidth = '1')
    plt.plot(df_2_year['Date'], df_2_year['SK_HINIX'].to_list(), label = 'SK_HINIX', linewidth = '1')
    plt.plot(df_2_year['Date'], df_2_year['DB_HITEK'].to_list(), label = 'DB_HITEK', linewidth = '1')
    plt.plot(df_2_year['Date'], df_2_year['HANMI'].to_list(), label = 'HANMI', linewidth = '1')
    plt.grid(axis = 'x')
    plt.grid(axis = 'y')
    plt.legend(fontsize = 6)

    plt.subplot(3,2,2)
    # plt.title('before 1 years')
    plt.plot(df_1_year['Date'], df_1_year['USD/KRW'].to_list(), label = 'USD/KRW', linewidth = '1')
    plt.plot(df_1_year['Date'], df_1_year['KOSPI'].to_list(), label = 'KOSPI', linewidth = '2')
    plt.plot(df_1_year['Date'], df_1_year['SS_ELEC'].to_list(), label = 'SS_ELEC', linewidth = '1')
    plt.plot(df_1_year['Date'], df_1_year['SS_ELEC_PRE'].to_list(), label = 'SS_ELEC_PRE', linewidth = '1')
    plt.plot(df_1_year['Date'], df_1_year['SK_HINIX'].to_list(), label = 'SK_HINIX', linewidth = '1')
    plt.plot(df_1_year['Date'], df_1_year['DB_HITEK'].to_list(), label = 'DB_HITEK', linewidth = '1')
    plt.plot(df_1_year['Date'], df_1_year['HANMI'].to_list(), label = 'HANMI', linewidth = '1')
    plt.grid(axis = 'x')
    plt.grid(axis = 'y')
    plt.legend(fontsize = 6)

    plt.subplot(3,2,3)
    # plt.title('before 9 months')
    plt.plot(df_9_month['Date'], df_9_month['USD/KRW'].to_list(), label = 'USD/KRW', linewidth = '1')
    plt.plot(df_9_month['Date'], df_9_month['KOSPI'].to_list(), label = 'KOSPI', linewidth = '2')
    plt.plot(df_9_month['Date'], df_9_month['SS_ELEC'].to_list(), label = 'SS_ELEC', linewidth = '1')
    plt.plot(df_9_month['Date'], df_9_month['SS_ELEC_PRE'].to_list(), label = 'SS_ELEC_PRE', linewidth = '1')
    plt.plot(df_9_month['Date'], df_9_month['SK_HINIX'].to_list(), label = 'SK_HINIX', linewidth = '1')
    plt.plot(df_9_month['Date'], df_9_month['DB_HITEK'].to_list(), label = 'DB_HITEK', linewidth = '1')
    plt.plot(df_9_month['Date'], df_9_month['HANMI'].to_list(), label = 'HANMI', linewidth = '1')
    plt.grid(axis = 'x')
    plt.grid(axis = 'y')
    plt.legend(fontsize = 6)

    plt.subplot(3,2,4)
    # plt.title('before 6 months')
    plt.plot(df_6_month['Date'], df_6_month['USD/KRW'].to_list(), label = 'USD/KRW', linewidth = '1')
    plt.plot(df_6_month['Date'], df_6_month['KOSPI'].to_list(), label = 'KOSPI', linewidth = '2')
    plt.plot(df_6_month['Date'], df_6_month['SS_ELEC'].to_list(), label = 'SS_ELEC', linewidth = '1')
    plt.plot(df_6_month['Date'], df_6_month['SS_ELEC_PRE'].to_list(), label = 'SS_ELEC_PRE', linewidth = '1')
    plt.plot(df_6_month['Date'], df_6_month['SK_HINIX'].to_list(), label = 'SK_HINIX', linewidth = '1')
    plt.plot(df_6_month['Date'], df_6_month['DB_HITEK'].to_list(), label = 'DB_HITEK', linewidth = '1')
    plt.plot(df_6_month['Date'], df_6_month['HANMI'].to_list(), label = 'HANMI', linewidth = '1')
    plt.grid(axis = 'x')
    plt.grid(axis = 'y')
    plt.legend(fontsize = 6)

    plt.subplot(3,2,5)
    # plt.title('before 3 months')
    plt.plot(df_3_month['Date'], df_3_month['USD/KRW'].to_list(), label = 'USD/KRW', linewidth = '1')
    plt.plot(df_3_month['Date'], df_3_month['KOSPI'].to_list(), label = 'KOSPI', linewidth = '2')
    plt.plot(df_3_month['Date'], df_3_month['SS_ELEC'].to_list(), label = 'SS_ELEC', linewidth = '1')
    plt.plot(df_3_month['Date'], df_3_month['SS_ELEC_PRE'].to_list(), label = 'SS_ELEC_PRE', linewidth = '1')
    plt.plot(df_3_month['Date'], df_3_month['SK_HINIX'].to_list(), label = 'SK_HINIX', linewidth = '1')
    plt.plot(df_3_month['Date'], df_3_month['DB_HITEK'].to_list(), label = 'DB_HITEK', linewidth = '1')
    plt.plot(df_3_month['Date'], df_3_month['HANMI'].to_list(), label = 'HANMI', linewidth = '1')
    plt.grid(axis = 'x')
    plt.grid(axis = 'y')
    plt.legend(fontsize = 6)

    plt.subplot(3,2,6)
    # plt.title('before 1 months')
    plt.plot(df_1_month['Date'], df_1_month['USD/KRW'].to_list(), label = 'USD/KRW', linewidth = '1')
    plt.plot(df_1_month['Date'], df_1_month['KOSPI'].to_list(), label = 'KOSPI', linewidth = '2')
    plt.plot(df_1_month['Date'], df_1_month['SS_ELEC'].to_list(), label = 'SS_ELEC', linewidth = '1')
    plt.plot(df_1_month['Date'], df_1_month['SS_ELEC_PRE'].to_list(), label = 'SS_ELEC_PRE', linewidth = '1')
    plt.plot(df_1_month['Date'], df_1_month['SK_HINIX'].to_list(), label = 'SK_HINIX', linewidth = '1')
    plt.plot(df_1_month['Date'], df_1_month['DB_HITEK'].to_list(), label = 'DB_HITEK', linewidth = '1')
    plt.plot(df_1_month['Date'], df_1_month['HANMI'].to_list(), label = 'HANMI', linewidth = '1')
    plt.grid(axis = 'x')
    plt.grid(axis = 'y')
    plt.legend(fontsize = 6)

    plt.show()