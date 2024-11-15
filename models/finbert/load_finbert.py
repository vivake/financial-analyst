from transformers import AutoTokenizer, AutoModel
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access the Hugging Face token from the environment variables
finbert_huggingface_token = os.getenv('FINBERT_HUGGINGFACE_TOKEN')

def load_finbert():
    """
    Load the FinBERT tokenizer and model.

    Returns:
    tokenizer, model: The loaded FinBERT tokenizer and model.
    """
    # Load the FinBERT tokenizer and model using the Hugging Face token
    tokenizer = AutoTokenizer.from_pretrained("ProsusAI/finbert", token=finbert_huggingface_token)
    model = AutoModel.from_pretrained("ProsusAI/finbert", token=finbert_huggingface_token)
    return tokenizer, model

# Example usage
if __name__ == "__main__":
    tokenizer, model = load_finbert()
    print("FinBERT model and tokenizer loaded successfully.")