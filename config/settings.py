import os 
from dotenv import load_dotenv

load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_PORT = int(os.getenv("DB_PORT"))
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_NAME = os.getenv("DB_NAME")

DASH_HOST = os.getenv("DASH_HOST")
DASH_PORT = int(os.getenv("DASH_PORT"))
DEBUG = os.getenv("DEBUG").lower() == "true"