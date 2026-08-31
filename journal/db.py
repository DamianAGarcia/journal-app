import sqlite3
from pathlib import Path

# Store the DB in the user's home directory so it never gets
# accidentally committed to the git repo along with your code.
DB_PATH = Path.home() / ".journal" / "journal.db"


def get_connection():
    DB_PATH.parent.mkdir(exist_ok=True)
    return sqlite3.connect(DB_PATH)


def init_db():
    conn = get_connection()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS entries (
            entry_date TEXT PRIMARY KEY,
            relationships_note TEXT,
            relationships_rating INTEGER,
            learning_note TEXT,
            learning_minutes INTEGER,
            money_note TEXT,
            money_spent REAL,
            health_note TEXT,
            sleep_hours REAL,
            exercised INTEGER
        )
    """)
    conn.commit()
    conn.close()
