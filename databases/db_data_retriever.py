import logging

# Initialize logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class DataRetriever:
    """
    Class for retrieving data from different types of databases.
    """

    def __init__(self, db_connector):
        self.db_connector = db_connector
        self.connection = db_connector.get_connection()

    def retrieve_data(self, query):
        """
        Retrieve data from the database based on the query.

        Parameters:
        query (str): The query to execute.

        Returns:
        result: The result of the query.
        """
        if self.db_connector.db_type == 'postgresql':
            return self._retrieve_from_postgresql(query)
        elif self.db_connector.db_type == 'vector_db':
            return self._retrieve_from_astra(query)
        else:
            raise ValueError("Unsupported database type")

    def _retrieve_from_postgresql(self, query):
        result = self.connection.execute(query)
        return result.fetchall()

    def _retrieve_from_astra(self, query):
        result = self.connection.execute(query)
        return result

# Usage example
if __name__ == "__main__":
    from db_connector import DbConnector

    # Example for PostgreSQL
    db_connector = DbConnector(db_type="postgresql")
    data_retriever = DataRetriever(db_connector)
    query = "SELECT * FROM your_table"
    result = data_retriever.retrieve_data(query)
    logger.info(f"Retrieved Data: {result}")

    # Example for Astra DB
    db_connector = DbConnector(db_type="vector_db")
    data_retriever = DataRetriever(db_connector)
    query = "SELECT * FROM your_table"
    result = data_retriever.retrieve_data(query)
    logger.info(f"Retrieved Data: {result}")