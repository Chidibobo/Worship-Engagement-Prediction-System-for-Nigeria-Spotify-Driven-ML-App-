from config.setup import Config
from config.logger import get_logger

import requests

logger = get_logger(__name__)

class Auth:
    def __init__(self):
        self.client_id = Config.CLIENT_ID
        self.client_secret = Config.CLIENT_SECRET
        self.token_url = Config.TOKEN_URL

    def get_access_token(self):
        logger.info("Attempting to get Spotify access token")
        url = self.token_url
        headers = {
            "Authorization": f"Basic {self.client_id}:{self.client_secret}"
        }
        data = {
            "grant_type": "client_credentials"
        }
        
        try:
            response = requests.post(url, headers=headers, data=data)
            if response.status_code == 200:
                logger.info("Successfully obtained access token")
                return response.json()["access_token"]
            else:
                logger.error(f"Failed to get access token: {response.status_code} {response.text}")
                raise Exception(f"Failed to get access token: {response.status_code} {response.text}")
        except requests.exceptions.RequestException as e:
            logger.error(f"Request exception while getting access token: {str(e)}")
            raise