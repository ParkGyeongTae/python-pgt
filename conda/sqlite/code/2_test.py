import sqlite3

con = sqlite3.connect(':memory:')

cur = con.cursor()

cur.execute("""
CREATE TABLE my_test_table(id int, name varchar, phone_number varchar);
""")
            
data = ((11, 'Park', '010-1111-2222'), (12, 'Kim', '010-1234-5678'))

cur.executemany("INSERT INTO my_test_table VALUES(?, ?, ?);", data)

cur.execute("""
SELECT * FROM my_test_table;
""")

for row in cur:
    print(row)


# dataList = (('Tom', '010-543-5432'), ('DSP', '010-123-1234'))
# cur = con.cursor()
# cur.executemany("INSERT INTO PhoneBook VALUES(?, ?);", dataList)


# print([row for row in cur])

# for row in cur:
#     print(row)


# cur.execute("""
# SELECT name
# FROM sqlite_schema
# WHERE type = 'table' AND name NOT LIKE 'sqlite_%';
# """)
# 

# SELECT name
# FROM sqlite_schema
# WHERE type = 'table' AND name NOT LIKE 'sqlite_%';

# cur = con.cursor()
# cur.execute("INSERT INTO PhoneBook Values('Derick', '010-1234-5678');")
# cur.execute("INSERT INTO PhoneBook Values('Derick', '010-1234-5678');")
# cur.execute("INSERT INTO PhoneBook Values('Derick', '010-1234-5678');")

# cur.execute('SELECT * FROM PhoneBook')

# for row in cur:
#     print(row)

cur.close()
con.close()
