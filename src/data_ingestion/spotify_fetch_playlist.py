import requests
from src.config.setup import Config
from src.config.logger import get_logger
from src.data_ingestion.auth import system_auth
logger = get_logger(__name__)

def fetch_top_artist_playlists(artist_id:str, market:str):
    """
    Fetch artist top tracks information from Spotify API
    
    Args:
        artist_id (str): Spotify artist ID
        market(str): Current Spotify Engagement Market e.g "NG" for Nigeria
        
    Returns:
        dict: Artist data or None if failed
    """
    try:
        access_token = system_auth.get_access_token()

        logger.info(f"Fetching artist data for artist_id: {artist_id}")
        url = f"{system_auth.base_url}/{artist_id}/top-tracks?market={market}"
        headers = {
            "Authorization": f"Bearer {access_token}"
        }
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            logger.info(f"Successfully fetched top tracks data for {artist_id}")
            return response.json()
        else:
            logger.error(f"Failed to fetch top tracks for {artist_id}: {response.status_code} {response.text}")
            return None

    except requests.exceptions.RequestException as e:
        logger.error(f"Request exception while fetching top tracks for {artist_id}: {str(e)}")
        return None
    except Exception as e:
        logger.error(f"Unexpected error fetching top tracks for {artist_id}: {str(e)}", exc_info=True)
        return None