import pytest
from databases.sql_database import SQLDatabaseManager
from databases.vector_database import VectorDBManager

@pytest.fixture
def mock_sql_connection():
    # Mock a database connection (use unittest.mock or pytest-mock for actual mock)
    return SQLDatabaseManager(connection_string="mock_connection_string")

def test_sql_query(mock_sql_connection):
    sql_manager = mock_sql_connection
    result = sql_manager.query("SELECT * FROM users")
    assert isinstance(result, list)  # Check if the result is a list (or the expected type)
    assert len(result) > 0  # Ensure some data is returned
import pytest
from databases.vector_database import VectorDBManager

@pytest.fixture
def mock_vector_db():
    return VectorDBManager(connection_string="mock_vector_db_connection")

def test_vector_db_insert(mock_vector_db):
    db_manager = mock_vector_db
    result = db_manager.insert_embedding("mock_embedding_id", [0.1, 0.2, 0.3])
    
    assert result is True  # Assuming that the insert function returns a success boolean