from datetime import datetime

str_1 = "2023-01-07 13:54:39"
print(str_1, type(str_1))

dt_1 = datetime.strptime(str_1, "%Y-%m-%d %H:%M:%S")
print(dt_1, type(dt_1))