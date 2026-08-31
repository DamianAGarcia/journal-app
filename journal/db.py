import sqlite3
from datetime import date
from pathlib import Path

from .models import Entry

# Store the DB in the user's home directory so it never gets
# accidentally committed to the git repo along with your code.
DB_PATH = Path.home() / ".journal" / "journal.db"


def get_connection():
    DB_PATH.parent.mkdir(exist_ok=True)
    return sqlite3.connect(DB_PATH)


def init_db():
    conn = get_connection()
    try:
        with conn:
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
    finally:
        conn.close()


def insert_entry(entry: Entry) -> None:
    conn = get_connection()
    try:
        with conn:
            conn.execute("""
                INSERT OR REPLACE INTO entries (
                    entry_date, relationships_note, relationships_rating,
                    learning_note, learning_minutes, money_note, money_spent,
                    health_note, sleep_hours, exercised
                ) VALUES (
                    :entry_date, :relationships_note, :relationships_rating,
                    :learning_note, :learning_minutes, :money_note, :money_spent,
                    :health_note, :sleep_hours, :exercised
                )
            """, {
                "entry_date": entry.entry_date.isoformat(),
                "relationships_note": entry.relationships_note,
                "relationships_rating": entry.relationships_rating,
                "learning_note": entry.learning_note,
                "learning_minutes": entry.learning_minutes,
                "money_note": entry.money_note,
                "money_spent": entry.money_spent,
                "health_note": entry.health_note,
                "sleep_hours": entry.sleep_hours,
                "exercised": int(entry.exercised),
            })
    finally:
        conn.close()


def get_entries(limit: int = 7) -> list[Entry]:
    conn = get_connection()
    try:
        rows = conn.execute("""
            SELECT entry_date, relationships_note, relationships_rating,
                   learning_note, learning_minutes, money_note, money_spent,
                   health_note, sleep_hours, exercised
            FROM entries ORDER BY entry_date DESC LIMIT ?
        """, (limit,)).fetchall()
    finally:
        conn.close()

    return [
        Entry(
            entry_date=date.fromisoformat(row[0]),
            relationships_note=row[1],
            relationships_rating=row[2],
            learning_note=row[3],
            learning_minutes=row[4],
            money_note=row[5],
            money_spent=row[6],
            health_note=row[7],
            sleep_hours=row[8],
            exercised=bool(row[9]),
        )
        for row in rows
    ]
