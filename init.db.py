import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('Primeiro Post', 'Esta é minha primeira postagem!!')
            )

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('Segundo Post', 'Esta é minha segunda postagem!!')
            )


connection.commit()
connection.close()