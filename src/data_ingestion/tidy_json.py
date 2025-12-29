from src.config.logger import get_logger
from datetime import datetime, timezone, timedelta
import json
logger = get_logger(__name__)

timestamp_cal = datetime.now(timezone.utc)
week_start = timestamp_cal - timedelta(days=timestamp_cal.weekday())
week_start = week_start.date()

timestamp = datetime.now(timezone.utc).isoformat()

def tidy_artist_data(artist_data, source:str):
    try:
        logger.info(f"Attempting to tidy Spotify Json  Artist data")
        record = {
            "artist_id": artist_data["id"],
            "name":artist_data["name"],
            "genres": json.dumps(artist_data["genres"]),
            "source": source
        }
        logger.info(f"Successfully Spotify Artist Json tidy up")
        return record
    except Exception as e:
        logger.error(f"Failed to tidy up Spotify Artist Json. Error here:{str(e)}") 
        return None


def tidy_tracks_data(tracks_data,artist_id:str):
    try:
        logger.info(f"Attempting to tidy Spotify Json tracks data")
        tracks = []
        for track in tracks_data:
            record={
                "track_id":track['id'],
                "artist_id":artist_id,
                "name":track['name'],
                "duration_ms":track['duration_ms'],
                "explicit":track['explicit'],
                "release_date":track['album']['release_date']
            }
            tracks.append(record)
        logger.info(f"Successfully tidied Spotify tracks data")
        return tracks
    except Exception as e:
        logger.error(f"Failed to tidy up Spotify tracks data: {str(e)}")
        return None


def tidy_metrics(artist_data):
    try:
        logger.info(f"Attempting to tidy relevant metrics data")
        record= {
            "artist_id": artist_data["id"],
            "week_start": week_start,
            "followers":artist_data["followers"]["total"],
            "popularity":artist_data["popularity"],
            "collected_at": timestamp
        }
        logger.info(f"Succeccfully tidied relevant metrics")
        return record
    except Exception as e:
        logger.error(f"Failed to tidy up relevant metrics: {str(e)}")    
        return None