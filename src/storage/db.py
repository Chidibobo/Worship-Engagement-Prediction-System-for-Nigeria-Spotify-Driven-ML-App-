import sqlite3
from pathlib import Path
from src.config.logger import get_logger
logger = get_logger(__name__)


# Define DB path at module level (consistent location)
DB_PATH = Path(__file__).resolve().parent.parent.parent / "data" / "spotify_data.db"


def get_connection():
    """
    Returns a SQLite connection to the project database.
    """
    try:
        # Ensure the data directory exists
        DB_PATH.parent.mkdir(parents=True, exist_ok=True)
        logger.info(f"Initializing DB connection at {DB_PATH}")    
        conn = sqlite3.connect(DB_PATH)
        logger.info(f"DB Connection Successful")
        return conn
    except Exception as e:
        logger.error(f"DB Connection Failed: {str(e)}")
        return None