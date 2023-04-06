import sqlite3

con = sqlite3.connect(':memory:')

cur = con.cursor()
cur.execute("CREATE TABLE PhoneBook(Name text, PhoneNum text);")

# cur = con.cursor()
cur.execute("INSERT INTO PhoneBook Values('Derick', '010-1234-5678');")
cur.execute("INSERT INTO PhoneBook Values('Derick', '010-1234-5678');")
cur.execute("INSERT INTO PhoneBook Values('Derick', '010-1234-5678');")

# cur.execute('SELECT * FROM PhoneBook')

# for row in cur:
#     print(row)

cur.close()
con.close()
