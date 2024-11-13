
from dotenv import load_dotenv
import logging

# Configure logger
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

# Description: Helper functions for the application.
def load_env_vars():
    """
    Load environment variables from .env file.
    """
    load_dotenv()
    logger.info("Environment variables loaded.")