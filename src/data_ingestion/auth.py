from src.config.setup import Config
from src.config.logger import get_logger
import base64
import requests

logger = get_logger(__name__)

class Auth:
    def __init__(self):
        self.client_id = Config.CLIENT_ID
        self.client_secret = Config.CLIENT_SECRET
        self.token_url = Config.TOKEN_URL
        self.base_url = Config.BASE_URL

    def get_access_token(self):
        logger.info("Attempting to get Spotify access token")
        url = self.token_url

        # Create base64 encoded authorization string
        auth_string = f"{self.client_id}:{self.client_secret}"
        auth_bytes = auth_string.encode('utf-8')
        auth_base64 = base64.b64encode(auth_bytes).decode('utf-8')
        
        headers = {
            "Authorization": f"Basic {auth_base64}",
            "Content-Type": "application/x-www-form-urlencoded"
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



system_auth = Auth()