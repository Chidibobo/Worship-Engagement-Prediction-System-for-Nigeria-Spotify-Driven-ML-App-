from dotenv import load_dotenv
load_dotenv(override=True)
import os

class Config:
    CLIENT_ID = os.getenv("CLIENT_ID")
    CLIENT_SECRET = os.getenv("CLIENT_SECRET")
    TOKEN_URL = os.getenv("TOKEN_URL")
    BASE_URL = os.getenv("BASE_URL")