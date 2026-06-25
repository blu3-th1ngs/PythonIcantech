import hashlib
from database import conn, cursor


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def register(username, password):
    try:
        cursor.execute(
            "INSERT INTO users(username,password) VALUES (?,?)",
            (username, hash_password(password))
        )
        conn.commit()
        return True
    except:
        return False


def login(username, password):
    cursor.execute(
        "SELECT * FROM users WHERE username=? AND password=?",
        (username, hash_password(password))
    )

    return cursor.fetchone()