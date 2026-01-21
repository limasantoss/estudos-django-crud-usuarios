import sqlite3

conn = sqlite3.connect('bd.db')
cursor = conn.cursor()
cursor.execute('CREATE TABLE users (name TEXT, age INTEGER)')
name = "Igor"
age = 27
cursor.execute("INSERT INTO users VALUES(?,?)",(name,age))
conn.commit()
