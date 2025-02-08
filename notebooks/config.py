# from dotenv import dotenv_values
# config = dotenv_values(".env")

from dotenv import load_dotenv
import os

load_dotenv()

DB_HOST_CORSO = os.getenv('DB_HOST_CORSO')
DB_PASSWORD_CORSO = os.getenv('DB_PASSWORD_CORSO')
DB_PORT_CORSO = os.getenv('DB_PORT_CORSO')
DB_USER_CORSO = os.getenv('DB_USER_CORSO')

