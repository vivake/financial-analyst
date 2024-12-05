import os
from dotenv import load_dotenv
import logging
from astrapy import DataAPIClient
from sqlalchemy import create_engine

# Load environment variables from .env file
load_dotenv()

# Initialize logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class DbConnector:
    """
    Class for connecting to different types of databases.
    """

    def __init__(self, db_type):
        self.db_type = db_type
        self.db_host = os.getenv('DB_HOST')
        self.db_port = os.getenv('DB_PORT')
        self.db_name = os.getenv('DB_NAME')
        self.db_user = os.getenv('DB_USER')
        self.db_password = os.getenv('DB_PASSWORD')
        self.astra_db_application_token = os.getenv('ASTRA_DB_APPLICATION_TOKEN')
        self.astra_db_api_endpoint = os.getenv('ASTRA_DB_API_ENDPOINT')

        # Debug statements to check environment variables
        logger.info(f"DB_TYPE: {self.db_type}")
        logger.info(f"DB_HOST: {self.db_host}")
        logger.info(f"DB_PORT: {self.db_port}")
        logger.info(f"DB_NAME: {self.db_name}")
        logger.info(f"DB_USER: {self.db_user}")
        logger.info(f"ASTRA_DB_APPLICATION_TOKEN: {self.astra_db_application_token}")
        logger.info(f"ASTRA_DB_API_ENDPOINT: {self.astra_db_api_endpoint}")

        if self.db_type == 'postgresql':
            self.connection = self._connect_to_postgresql()
        elif self.db_type == 'vector_db':
            self.connection = self._connect_to_astra()
        else:
            raise ValueError("Unsupported database type")

    def _connect_to_postgresql(self):
        if not self.db_host or not self.db_port or not self.db_name or not self.db_user or not self.db_password:
            raise ValueError("Environment variables for PostgreSQL are missing")
        connection_string = f"postgresql://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}"
        engine = create_engine(connection_string)
        return engine.connect()

    def _connect_to_astra(self):
        if not self.astra_db_application_token or not self.astra_db_api_endpoint:
            raise ValueError("Environment variables for Astra DB are missing")
        client = DataAPIClient(self.astra_db_application_token)
        return client.get_database(self.astra_db_api_endpoint)

    def get_connection(self):
        return self.connection

# Usage example
if __name__ == "__main__":
    db_connector = DbConnector(db_type="postgresql")
    connection = db_connector.get_connection()
    logger.info(f"Connected to DB: {connection}")