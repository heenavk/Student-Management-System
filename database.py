import sqlite3

def connect_db():
    conn = sqlite3.connect("students.db")
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS student (
            roll INTEGER PRIMARY KEY,
            name TEXT,
            marks INTEGER,
            grade TEXT
        )
    """)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    connect_db()
    print("Database created successfully")
