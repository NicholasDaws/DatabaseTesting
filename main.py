#test code

import sqlite3
db = sqlite3.connect('mydb.db')

cursor = db.cursor()

#create table
cursor.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, name TEXT)")

#insert a name
#insert via command line
#nam = str(input("Enter a name: "))
nam = "Joe"

cursor.execute("INSERT INTO users(name) VALUES(?)", [nam,]) #could be a tuple

print("Data entered to database")

db.commit()

#show all data in the database
print("print data")
cursor.execute("SELECT * FROM users")
data = cursor.fetchall()
for row in data:
  print(row)

db.close()
