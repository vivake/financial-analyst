import pytest
from nlp.tokenization import Tokenizer

@pytest.fixture
def sample_text():
    return "This is a test sentence."

def test_tokenization(sample_text):
    tokenizer = Tokenizer()
    
    # Tokenize the sample text
    tokens = tokenizer.tokenize(sample_text)
    
    # Assert that the tokens are as expected
    assert len(tokens) == 5  # Example: 'This', 'is', 'a', 'test', 'sentence'
    assert "test" in tokens
    assert isinstance(tokens, list)
