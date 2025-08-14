import sqlite3

conn = sqlite3.connect('Simple_API/database.db')
connection = conn.cursor()

# Create users table
connection.execute('''
CREATE TABLE IF NOT EXISTS todo (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    task TEXT NOT NULL,
    is_done INT
)
''')

conn.commit()
conn.close()

print("Database initialized.")