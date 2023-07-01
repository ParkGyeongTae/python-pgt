import sqlite3

con = sqlite3.connect(":memory:")

cur = con.cursor()

cur.execute("CREATE TABLE my_test_table (id int, name varchar, phone_number varchar);")

cur.execute("INSERT INTO my_test_table VALUES (1, 'Park', '010-0000-0000');")
cur.execute("INSERT INTO my_test_table VALUES (2, 'Kim', '010-1234-5678');")

result = cur.execute("SELECT * FROM my_test_table;")

for row in result:
    print(row)

cur.close()
con.close()
