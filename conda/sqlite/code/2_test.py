import sqlite3
import pandas as pd

con = sqlite3.connect(':memory:')

cur = con.cursor()

cur.execute("CREATE TABLE my_test_table(id int, name varchar, phone_number varchar);")
            
data = [
    (11, "Park", "010-1111-2222"), 
    (12, "Kim", "010-1234-5678"), 
    (13, "Oh", "010-8765-4321s"), 
    ]

cur.executemany("INSERT INTO my_test_table VALUES (?, ?, ?);", data)
query = cur.execute("SELECT * FROM my_test_table;")
cols = [column[0] for column in query.description]

df = pd.DataFrame.from_records(data = query.fetchall(), columns = cols)
print(df)

cur.close()
con.close()
