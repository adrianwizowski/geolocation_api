# Configuration from environment variables or '.env' file.
import databases
from starlette.config import Config

config = Config('.env')

TESTING = config('TESTING', cast=bool, default=False)
DATABASE_URL = config('DATABASE_URL', cast=databases.DatabaseURL)
TEST_DATABASE_URL = DATABASE_URL.replace(database='test_' + DATABASE_URL.database)
