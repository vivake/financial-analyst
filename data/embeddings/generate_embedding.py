"""
This script generates embeddings using FinBERT.

Functions:
    load_finbert_model(model_name: str) -> BertModel:
        Loads the FinBERT model specified by the model_name parameter.

    preprocess_text(text: str) -> List[str]:
        Preprocesses the input text by tokenizing and cleaning it.

    generate_embeddings(text: str, model: BertModel, tokenizer: BertTokenizer) -> torch.Tensor:
        Generates embeddings for the input text using the provided FinBERT model and tokenizer.

    main():
        Main function that loads the FinBERT model, preprocesses the input text, and generates embeddings.
"""