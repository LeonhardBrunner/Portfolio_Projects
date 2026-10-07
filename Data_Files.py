import os

from dotenv import load_dotenv

load_dotenv()

db_url = os.getenv("DATABASE_URL")
secret = os.getenv("SECRET_KEY")
