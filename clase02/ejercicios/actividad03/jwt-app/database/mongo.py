import logging
import sys
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

# --- Logging ---
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


def get_env_variable(var_name):
    try:
        return os.environ[var_name]
    except KeyError:
        logging.error(f"La variable de entorno '{var_name}' no está definida.")
        sys.exit(1)

client = MongoClient(os.getenv("MONGO_URI"))
db = client["fastapi_jwt_db"]
user_collection = db["users"]