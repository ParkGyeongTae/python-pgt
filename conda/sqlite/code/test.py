import sqlite3

con = sqlite3.connect(':memory:')

cur = con.cursor()
cur.execute("CREATE TABLE PhoneBook(Name text, PhoneNum text);")
cur.execute("INSERT INTO PhoneBook Values('Derick', '010-1234-5678');")
cur.execute("SELECT * FROM PhoneBook;")

for row in cur:
    print(row)

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
