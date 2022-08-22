import FinanceDataReader as fdr

df_krx = fdr.StockListing('KRX')

df_kospi = fdr.StockListing('KOSPI')
df_kosdoq = fdr.StockListing('KOSDAQ')
df_konex = fdr.StockListing('KONEX')

print(df_krx.head())
print(df_kospi.head())
print(df_kosdoq.head())
print(df_konex.head())

exit()