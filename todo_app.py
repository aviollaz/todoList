import sqlite3


conn = sqlite3.connect("todos.db")

c = conn.cursor()

# c.execute("""CREATE TABLE tasks (
#         id INTEGER PRIMARY KEY, 
#         description TEXT,
#         completed BOOLEAN
# )

# """)

c.execute("SELECT * FROM tasks")
# c.fetchone()
# c.fetchmany()
print(c.fetchall())
conn.commit()

conn.close()
