# ['Symbol', 'Market', 'Name', 'Sector', 'Industry', 'ListingDate', 'SettleMonth', 'Representative', 'HomePage', 'Region']

import FinanceDataReader as fdr

# df_krx    = fdr.StockListing('KRX')
df_kospi  = fdr.StockListing('KOSPI')
# df_kosdoq = fdr.StockListing('KOSDAQ')
# df_konex  = fdr.StockListing('KONEX')

search_names = ['삼성전자', 'LG에너지솔루션']
target_names = []

for search_name in search_names:
    target_names.extend(df_kospi[df_kospi['Name'] == search_name]['Symbol'].tolist())

for stock_code in target_names:
    df = fdr.DataReader(stock_code, '2022-08-16', '2022-08-23')
    print(df)


# print(df)

# exit()

# search_name = '삼성전자'

# if (df_krx['Name'] == search_name).any(): print('KRX')
# if (df_kospi['Name'] == search_name).any(): print('KOSPI')
# if (df_kosdoq['Name'] == search_name).any(): print('KOSDAQ')
# if (df_konex['Name'] == search_name).any(): print('KONEX')

# print('krx count    :', df_krx['Symbol'].count())
# print('kospi count  :', df_kospi['Symbol'].count())
# print('kosdoq count :', df_kosdoq['Symbol'].count())
# print('konex count  :', df_konex['Symbol'].count())

# print('----------------------------')

# print('krx columns    :', df_krx.columns)
# print('kospi columns  :', df_kospi.columns)
# print('kosdoq columns :', df_kosdoq.columns)
# print('konex columns  :', df_konex.columns)