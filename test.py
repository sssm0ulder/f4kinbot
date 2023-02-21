import sqlite3

# создаем базу данных и таблицу
conn = sqlite3.connect('example.db')
cur = conn.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS users
               (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')
cur.execute('''INSERT INTO users (name, age) VALUES (?, ?)''', ('Alice', 25))
cur.execute('''INSERT INTO users (name, age) VALUES (?, ?)''', ('Bob', 30))
conn.commit()

# получаем результат запроса в виде списка кортежей
cur.execute('SELECT * FROM users')
rows = cur.fetchall()

# преобразуем кортежи в словари
result = []
for row in rows:
    result.append({'id': row[0], 'name': row[1], 'age': row[2]})

# выводим результат
print(result)

# закрываем курсор и соединение с базой данных
cur.close()
conn.close()