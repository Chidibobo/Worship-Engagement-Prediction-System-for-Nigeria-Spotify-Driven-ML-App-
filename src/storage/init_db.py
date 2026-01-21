import sqlite3
from pathlib import Path
from src.config.logger import get_logger
logger = get_logger(__name__)

# Import DB_PATH from db.py to ensure consistency
from src.storage.db import DB_PATH

def init_db():
    try:
        logger.info(f"Attempting to create DB at {DB_PATH}")
        
        # Ensure the data directory exists
        DB_PATH.parent.mkdir(parents=True, exist_ok=True)

        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        # Artists table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS artists (
                artist_id TEXT PRIMARY KEY,
                name TEXT,
                genres TEXT,
                source TEXT
        )
        """)

        # Tracks table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS tracks (
                    track_id TEXT PRIMARY KEY,
                    artist_id TEXT,
                    name TEXT,
                    duration_ms INTEGER,
                    explicit INTEGER,
                    release_date TEXT
        )
        """)

        #Artist weekly metrics table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS artist_weekly_metrics(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                artist_id TEXT NOT NULL,
                week_start DATE NOT NULL,
                followers INTEGER,
                popularity INTEGER,
                collected_at TEXT,

                UNIQUE (artist_id, week_start),
                FOREIGN KEY (artist_id) REFERENCES artists (artist_id)
        )
        """)

        conn.commit()
        conn.close()
        logger.info(f"Created DB successfully at {DB_PATH}")
    except Exception as e:
        logger.error(f"Error creating DB: {str(e)}")


if __name__ == "__main__":
    init_db()