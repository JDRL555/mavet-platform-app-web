from dotenv import load_dotenv
from os import getenv

load_dotenv()

#imgbb API
API_KEY       = getenv("API_KEY") 
API_URL       = getenv("API_URL")

#cloudinary
CLOUD_NAME    = getenv("CLOUD_NAME")
API_KEY_C     = getenv("API_KEY_C")
API_SECRET    = getenv("API_SECRET")

#app config
SECRET_KEY    = getenv("SECRET_KEY")
DATABASE_URL  = getenv("DATABASE_URL")