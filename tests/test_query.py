import pytest
from query.query_router import QueryRouter

@pytest.fixture
def query_router():
    return QueryRouter()

def test_route_query(query_router):
    response = query_router.route_query("What is the revenue for Tesla?")
    
    assert "Tesla" in response  # Ensure that the response contains information about Tesla
    assert isinstance(response, str)  # Response should be a string
