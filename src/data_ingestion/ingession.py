from src.storage.db import get_connection
from src.config.logger import get_logger
logger = get_logger(__name__)


def save_artist(record):
    try:
        logger.info("Attempting to save records to DB")
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT OR IGNORE INTO artists (
                artist_id, name, genres, source
            )
            VALUES (?, ?, ?, ?)
        """, (
            record["artist_id"],
            record["name"],
            record["genres"],
            record["source"]  
        ))

        conn.commit()
        logger.info("Successfully saved record to DB")

    except Exception as e:
        logger.error(f"Error saving to DB: {e}")

    finally:
        conn.close()

        

def save_artist_tracks(record,):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT OR IGNORE INTO tracks (
            track_id, artist_id, name, duration_ms, explicit, release_date
        )
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        record["track_id"],
        record["artist_id"],
        record["name"],
        record["duration_ms"],
        record["explicit"],
        record["release_date"]
    ))

    conn.commit()
    conn.close()

def save_artist_metrics(record):
    try:
        logger.info("Attempting to save records to DB")
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT OR IGNORE INTO artist_weekly_metrics (
                artist_id, week_start, followers, popularity, collected_at
            )
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            record["artist_id"],
            record["week_start"],
            record["followers"],
            record["popularity"],
            record["collected_at"]
        ))

        conn.commit()
        logger.info("Successfully saved record to DB")

    except Exception as e:
        logger.error(f"Error saving to DB: {e}")

    finally:
        conn.close()