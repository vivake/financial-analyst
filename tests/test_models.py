import pytest
from models.finbert import FinBERTModel

@pytest.fixture
def sample_text():
    return "The stock price of Tesla increased by 5% in Q4 2023."

def test_finbert_embedding(sample_text):
    model = FinBERTModel()
    embedding = model.get_embedding(sample_text)
    
    # Asserting that the embedding is returned as a list or array
    assert isinstance(embedding, list)
    assert len(embedding) > 0  # Ensure that embedding is non-empty
