import os
from dotenv import load_dotenv
import logging
from astrapy import DataAPIClient

# Load environment variables from .env file
load_dotenv()

# Initialize logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class VectorDBConnection:   # Class for Astra DB connection setup
 

    def __init__(self, keyspace):  # Constrcuter to initialize the class
        self.keyspace = keyspace    # Initialize the keyspace attribute
        self.astra_db_application_token = os.getenv('ASTRA_DB_TOKEN')   # Get the Astra DB application token from the environment
        self.astra_db_api_endpoint = os.getenv('ASTRA_DB_ENDPOINT')    # Get the Astra DB API endpoint from the environment 
        
        # Debug statements to check environment variables
        logger.info(f"ASTRA_DB_APPLICATION_TOKEN: {self.astra_db_application_token}")
        logger.info(f"ASTRA_DB_API_ENDPOINT: {self.astra_db_api_endpoint}")
        
        if not self.astra_db_application_token or not self.astra_db_api_endpoint:
            raise ValueError("Environment variables for Astra DB are missing")
        
        self.client = self._initialize_client()
        self.db = self._connect_to_db()

    def _initialize_client(self):
        """Initialize the DataAPIClient."""
        return DataAPIClient(self.astra_db_application_token)

    def _connect_to_db(self):
        """Connect to the vector database."""
        return self.client.get_database(self.astra_db_api_endpoint)

    def get_db(self):
        """Return the connected database object."""
        return self.db

    def confirm_connection(self):
        """Confirm the database connection."""
        if self.db:
            print("Successfully connected to the Astra DB.")
        else:
            print("Failed to connect to the Astra DB.")

# Usage example
if __name__ == "__main__":
    keyspace = "financial_data"
    vector_db_connection = VectorDBConnection(keyspace)
    db = vector_db_connection.get_db()
    logger.info(f"Connected to Astra DB: {db}")
    vector_db_connection.confirm_connection()