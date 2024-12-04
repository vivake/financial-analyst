import os
from dotenv import load_dotenv
import logging
from sqlalchemy import create_engine

# Load environment variables from .env file
load_dotenv()

# Initialize logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class SQLDBConnection:
    """
    Class for connecting to the SQL database.
    """

    def __init__(self):
        self.db_host = os.getenv('DB_HOST')
        self.db_port = os.getenv('DB_PORT')
        self.db_name = os.getenv('DB_NAME')
        self.db_user = os.getenv('DB_USER')
        self.db_password = os.getenv('DB_PASSWORD')
        
        # Debug statements to check environment variables
        logger.info(f"DB_HOST: {self.db_host}")
        logger.info(f"DB_PORT: {self.db_port}")
        logger.info(f"DB_NAME: {self.db_name}")
        logger.info(f"DB_USER: {self.db_user}")
        
        if not self.db_host or not self.db_port or not self.db_name or not self.db_user or not self.db_password:
            raise ValueError("Environment variables for SQL DB are missing")
        
        self.engine = self._initialize_engine()
        self.connection = self._connect_to_db()

    def _initialize_engine(self):
        connection_string = f"postgresql://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}"
        return create_engine(connection_string)

    def _connect_to_db(self):
        return self.engine.connect()

    def get_connection(self):
        return self.connection

# Usage example
if __name__ == "__main__":
    sql_db_connection = SQLDBConnection()
    connection = sql_db_connection.get_connection()
    logger.info(f"Connected to SQL DB: {connection}")