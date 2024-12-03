# Class for vector database connection setup

import os
from dotenv import load_dotenv
import logging
from astrapy import DataAPIClient

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def connect_to_vector_db(keyspace):
    """
    Connect to the Astra vector database.

    Parameters:
    keyspace (str): The keyspace to connect to.

    Returns:
    db: The connected database object.
    """
    # Load environment variables from .env file
    load_dotenv()
    logger.info("Environment variables loaded.")

    # Access environment variables
    astra_db_application_token = os.getenv('ASTRA_DB_APPLICATION_TOKEN')
    astra_db_api_endpoint = os.getenv('ASTRA_DB_API_ENDPOINT')

    # Validate environment variables
    if not all([astra_db_application_token, astra_db_api_endpoint]):
        logger.error("One or more required environment variables are missing.")
        raise EnvironmentError("Missing required environment variables.")

    logger.info("Environment variables accessed.")

    try:
        # Initialize the client
        client = DataAPIClient(astra_db_application_token)
        logger.info("DataAPIClient initialized.")

        # Connect to vector_db
        db = client.get_database_by_api_endpoint(astra_db_api_endpoint, keyspace=keyspace)
        logger.info(f"Connected to vector_db with keyspace '{keyspace}'.")

        return db
    except Exception as e:
        logger.error(f"Failed to connect to vector_db: {e}")
        raise

# Example usage
if __name__ == "__main__":
    keyspace = "financial_data"  # Replace with your actual keyspace
    db = connect_to_vector_db(keyspace)
    logger.info(f"Connected to Astra DB: {db.list_collection_names()}")