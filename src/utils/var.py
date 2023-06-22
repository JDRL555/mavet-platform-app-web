from dotenv import load_dotenv
from os import getenv

load_dotenv()

#cloudinary API
CLOUD_NAME    = getenv("CLOUD_NAME")
API_KEY_C     = getenv("API_KEY_C")
API_SECRET    = getenv("API_SECRET")

#app config
SECRET_KEY    = getenv("SECRET_KEY")
DATABASE_URL  = getenv("DATABASE_URL")