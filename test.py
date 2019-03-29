import sqlite3

db = sqlite3.connect('mydb.db')
cursor = db.cursor()

#value to insert
nam = "Joe"

def createDB():
  #create a database
  cursor.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, name TEXT)")
  db.commit()

def insertName(nam, cursor):
  #insert a name from the 'nam' var into database
  cursor.execute("INSERT INTO users(name) VALUES(?)", [nam,])
  print("data insterted")
  db.commit()

def showContent(cursor):
  #show all content in the database
  foo = cursor.execute("SELECT name FROM users")
  for row in foo:
    print(row)

def closeConnection(cursor):
  #close the connection
  cursor.close()
