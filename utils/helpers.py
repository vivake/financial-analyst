
from dotenv import load_dotenv
import logging
import os

# Configure logger
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

def load_env_vars(env_file="/Users/vivakepandey/Python Projects/financial_analyst/.env"):
    """
    Load environment variables from a specified .env file and return them as a dictionary.

    Parameters:
    env_file (str): The path to the .env file. Default is '.env'.

    Returns:
    dict: A dictionary containing the loaded environment variables.
    """
    load_dotenv(env_file)
    logger.info(f"Environment variables loaded from {env_file}")

    env_vars = {
        'ASTRA_DB_ENDPOINT': os.getenv('ASTRA_DB_API_ENDPOINT'),
        'ASTRA_DB_TOKEN': os.getenv('ASTRA_DB_APPLICATION_TOKEN'),
        'ASTRA_API_KEY': os.getenv('ASTRA_API_KEY'),
        'ASTRA_DB_ID': os.getenv('ASTRA_DB_ID'),
        'ASTRA_DB_KEYSPACE': os.getenv('ASTRA_DB_KEYSPACE'),
        'ASTRA_DB_COLLECTION_NAME': os.getenv('ASTRA_DB_COLLECTION_NAME')
    }

    return env_vars