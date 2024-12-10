import pytest
from ui.chatbot import ChatbotUI

@pytest.fixture
def sample_user_input():
    return "How does the market perform?"

def test_chatbot_response(sample_user_input):
    chatbot = ChatbotUI()
    
    # Mocking user input and response
    response = chatbot.handle_input(sample_user_input)
    
    # Check if the response is of expected type (string or dictionary)
    assert isinstance(response, str)
    assert "market" in response
