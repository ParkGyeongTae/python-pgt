import FinanceDataReader as fdr

df_krx = fdr.StockListing('KRX')
print(df_krx.head())

# df = fdr.DataReader('005930', '2023')
# print(df)