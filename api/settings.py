# Configuration from environment variables or '.env' file.
from starlette.config import Config

config = Config('.env')
DATABASE_URL = config('DATABASE_URL')
