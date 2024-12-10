import pytest
from nlp.basic_ner import BasicNERProcessor

@pytest.fixture
def sample_text():
    return "Tesla stock price increased by 10% in Q4 2023."

def test_basic_ner(sample_text):
    ner_processor = BasicNERProcessor()
    entities = ner_processor.extract_entities(sample_text)
    
    assert isinstance(entities, dict)  # Entities should be returned as a dictionary
    assert "Tesla" in entities  # Company name should be identified
    assert "Q4 2023" in entities  # Date or time period should be identified
    assert entities["Tesla"] == "ORG"  # Tesla should be classified as Organization
