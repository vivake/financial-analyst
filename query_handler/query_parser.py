import torch
from transformers import BertTokenizer, BertForSequenceClassification

#Class for parsing user queries (Class: `QueryParser`)
"""

Class for parsing user queries (Class: `QueryParser`)

This module contains the `QueryParser` class which is responsible for parsing user queries to extract and classify intent. The classification determines how `query_router.py` will route the query (either to SQL or vector DB).

Steps to achieve the function of this script:
1. Define the `QueryParser` class.
2. Implement a method to parse the user query.
3. Implement a method to classify the intent of the query.
4. Ensure the classification method can distinguish between SQL queries and vector DB queries.
5. Integrate with `query_router.py` to route the query based on the classified intent.
"""

#Parse query to extract and classify intent. Classification determines how query_router.py will route the query (SQL or vector DB).
#Get intent by using bert model to classify query.
class QueryParser:
    """
    QueryParser is a class that utilizes a pre-trained BERT model to parse and classify text queries.

    Attributes:
        tokenizer (BertTokenizer): Tokenizer for converting text into tokens suitable for BERT.
        model (BertForSequenceClassification): Pre-trained BERT model for sequence classification.

    Methods:
        __init__(model_path):
            Initializes the QueryParser with a tokenizer and model from the specified path.
            Args:
                model_path (str): Path to the pre-trained BERT model.

        parse_query(query):
            Tokenizes the input query and passes it through the BERT model to get the outputs.
            Args:
                query (str): The text query to be parsed.
            Returns:
                outputs (ModelOutput): The output from the BERT model containing logits and other information.

        classify_intent(query):
            Classifies the intent of the input query by parsing it and determining the predicted class.
            Args:
                query (str): The text query whose intent is to be classified.
            Returns:
                predicted_class_id (int): The ID of the predicted class for the input query.
    """
    def __init__(self, model_path):
        self.tokenizer = BertTokenizer.from_pretrained(model_path)
        self.model = BertForSequenceClassification.from_pretrained(model_path)

    def parse_query(self, query):
        inputs = self.tokenizer(query, return_tensors='pt')
        outputs = self.model(**inputs)
        return outputs

    def classify_intent(self, query):
        outputs = self.parse_query(query)
        logits = outputs.logits
        predicted_class_id = torch.argmax(logits, dim=1).item()
        return predicted_class_id
