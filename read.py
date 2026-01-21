import sqlite3

conn = sqlite3.connect('banco.db')
cursor = conn.cursor()

cursor.execute('SELECT * FROM users ')
usuarios = cursor.fetchall()
for usuario in usuarios:
   print(f"name:{usuario[0]}|age:{usuario[1]}|texto:{usuario[2]}")
conn.close()