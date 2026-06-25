import sqlite3

conn = sqlite3.connect(
    "cyberguard.db",
    check_same_thread=False
)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    password TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS vulnerabilities(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    severity TEXT,
    status TEXT,
    description TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS assets(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    hostname TEXT,
    ip TEXT,
    os TEXT,
    owner TEXT
)
""")

conn.commit()