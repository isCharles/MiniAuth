from sqlite3 import connect

DATABASE_URL= "miniauth.db"

def get_db():
    conn = connect(DATABASE_URL)
    conn.row_factory = lambda cursor, row: {col[0]: row[idx] for idx, col in enumerate(cursor.description)}
    return conn