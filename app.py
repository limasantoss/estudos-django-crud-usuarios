import sqlite3

conn = sqlite3.connect('banco.db')
cursor = conn.cursor()
cursor.execute('CREATE TABLE users (name TEXT, age INTEGER,texto TEXT)')
name = "Igor"
age = 27
texto = "ops kskskskksksksksk"
cursor.execute("INSERT INTO users VALUES(?,?,?)",(name , age , texto))
conn.commit()
