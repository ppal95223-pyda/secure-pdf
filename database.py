import sqlite3

connection = sqlite3.connect("database/notes.db")

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS notes(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    subject TEXT,
    unit TEXT,
    price INTEGER,
    pages INTEGER,
    description TEXT,
    pdf_name TEXT
)
""")

connection.commit()

connection.close()

print("Database Created Successfully!")

import sqlite3

connection = sqlite3.connect("database/notes.db")
cursor = connection.cursor()

cursor.execute("""
INSERT INTO notes
(subject, unit, price, pages, description, pdf_name)
VALUES (?, ?, ?, ?, ?, ?)
""", (
    "Web Technology",
    "Unit 1",
    49,
    120,
    "Complete Unit 1 Notes",
    "unit1.pdf"
))

connection.commit()
connection.close()

print("Data Inserted Successfully!")

connection = sqlite3.connect("database/notes.db")
cursor = connection.cursor()

cursor.execute("SELECT * FROM notes")
rows = cursor.fetchall()

for row in rows:
    print(row)

connection.close()