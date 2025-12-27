import requests
from config.logger import get_logger

logger = get_logger(__name__)


def fetch_artist(artist_id, access_token):
    """
    Fetch artist information from Spotify API
    
    Args:
        artist_id (str): Spotify artist ID
        access_token (str): Valid Spotify access token
        
    Returns:
        dict: Artist data or None if failed
    """
    try:
        logger.info(f"Fetching artist data for artist_id: {artist_id}")
        url = f"{base_url}/{artist_id}"
        headers = {
            "Authorization": f"Bearer {access_token}"
        }
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            logger.info(f"Successfully fetched artist data for {artist_id}")
            return response.json()
        else:
            logger.error(f"Failed to fetch artist {artist_id}: {response.status_code} {response.text}")
            return None

    except requests.exceptions.RequestException as e:
        logger.error(f"Request exception while fetching artist {artist_id}: {str(e)}")
        return None
    except Exception as e:
        logger.error(f"Unexpected error fetching artist {artist_id}: {str(e)}", exc_info=True)
        return None