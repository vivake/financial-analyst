# Initialize Document loader
from langchain_community.document_loaders import PyMuPDFLoader
file_path="/Users/vivakepandey/Python Projects/financial_analyst"
loader=PyMuPDFLoader(file_path)

# Load the document
docs=loader.load()

# import os
# import logging
# import json
# import pandas as pd
# import fitz  # PyMuPDF
# from langchain.text_splitter import CharacterTextSplitter

# # Initialize logger
# logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# logger = logging.getLogger(__name__)

# class Preprocessing:
#     """
#     Class for performing various preprocessing tasks.
#     """

#     def __init__(self):
#         pass

#     def clean_data(self, data_path, data_type):
#         """
#         General data cleaning method.

#         Parameters:
#         data_path (str): The path to the data file.
#         data_type (str): The type of data ('pdf', 'excel').

#         Returns:
#         cleaned_data (any): The cleaned data.
#         """
#         if data_type == 'pdf':
#             cleaned_data = self._pdf_cleaner(data_path)
#         elif data_type == 'excel':
#             cleaned_data = self._excel_cleaner(data_path)
#         else:
#             raise ValueError("Unsupported data type")
        
#         logger.info("Data cleaned successfully.")
#         return cleaned_data

#     def _pdf_cleaner(self, pdf_path):
#         """
#         Clean PDF data.

#         Parameters:
#         pdf_path (str): The path to the PDF file.

#         Returns:
#         cleaned_data (str): The cleaned text extracted from the PDF.
#         """
#         # Extract text from the PDF
#         document = fitz.open(pdf_path)  # Open the PDF file
#         text = ""  # Initialize an empty string to store the text
#         for page_num in range(len(document)):  # Iterate over each page
#             page = document.load_page(page_num)
#             text += page.get_text("text")

#         # Split text into sentences
#         sentences = text.split('. ')  # Split text by sentence

#         # Preprocess the text
#         sentences = [sentence.strip().lower() for sentence in sentences]  # Remove leading/trailing whitespace and convert to lowercase

#         # Combine sentences back into a single string (optional)
#         cleaned_data = ". ".join(sentences)

#         return cleaned_data

#     def _excel_cleaner(self, excel_path):
#         """
#         Clean Excel data.

#         Parameters:
#         excel_path (str): The path to the Excel file.

#         Returns:
#         cleaned_data (pd.DataFrame): The cleaned DataFrame.
#         """
#         df = pd.read_excel(excel_path)
#         # Additional cleaning logic can be added here
#         df.dropna(inplace=True)  # Example: Drop rows with missing values
#         return df

#     def transform_data(self, data, data_type):
#         """
#         General data transformation method.

#         Parameters:
#         data (any): The data to be transformed.
#         data_type (str): The type of data ('pdf', 'excel', 'text').

#         Returns:
#         transformed_data (any): The transformed data.
#         """
#         if data_type == 'pdf':
#             transformed_data = self._transform_pdf_data(data)
#         elif data_type == 'excel':
#             transformed_data = self._transform_excel_data(data)
#         elif data_type == 'text':
#             transformed_data = self._transform_text_data(data)
#         else:
#             raise ValueError("Unsupported data type")
        
#         logger.info("Data transformed successfully.")
#         return transformed_data

#     def _transform_pdf_data(self, text):
#         """
#         Transform PDF data.

#         Parameters:
#         text (str): The cleaned text extracted from the PDF.

#         Returns:
#         transformed_data (str): The transformed text.
#         """
#         # Additional transformation logic can be added here
#         transformed_data = text.lower()  # Example: Convert text to lowercase
#         return transformed_data

#     def _transform_excel_data(self, df):
#         """
#         Transform Excel data.

#         Parameters:
#         df (pd.DataFrame): The cleaned DataFrame.

#         Returns:
#         transformed_data (pd.DataFrame): The transformed DataFrame.
#         """
#         # Additional transformation logic can be added here
#         df.columns = df.columns.str.lower()  # Example: Convert column names to lowercase
#         return df

#     def _transform_text_data(self, text):
#         """
#         Transform text data.

#         Parameters:
#         text (str): The cleaned text data.

#         Returns:
#         transformed_text (str): The transformed text.
#         """
#         # Additional transformation logic can be added here
#         transformed_text = text.lower()  # Example: Convert text to lowercase
#         return transformed_text

#     def generate_embeddings(self, model, data, destination_path):
#         """
#         Generate embeddings for the given data using the specified model and save to a file.

#         Parameters:
#         model (any): The embedding model.
#         data (any): The data to generate embeddings for.
#         destination_path (str): The path where the embeddings should be saved.

#         Returns:
#         embeddings (dict): The generated embeddings.
#         """
#         embeddings = {}
#         # Add code to generate embeddings using the model
#         logger.info("Generating embeddings")

#         # Ensure the directory exists
#         os.makedirs(os.path.dirname(destination_path), exist_ok=True)

#         # Save the embeddings to the destination_path
#         logger.info(f"Saving embeddings to {destination_path}")
#         with open(destination_path, 'w') as f:
#             json.dump(embeddings, f)

#         return embeddings

#     def load_embeddings(self, model_path):
#         """
#         Load the embedding model from the specified path.

#         Parameters:
#         model_path (str): The path to the embedding model.

#         Returns:
#         model: The loaded embedding model.
#         """
#         # Add code to load the embedding model
#         logger.info(f"Loading model from {model_path}")
#         model = None  # Replace with actual model loading code
#         return model

#     def preprocess_embeddings(self, embeddings):
#         """
#         Preprocess the embeddings.

#         Parameters:
#         embeddings (dict): The dictionary of loaded embeddings.

#         Returns:
#         processed_embeddings (dict): The dictionary of processed embeddings.
#         """
#         processed_embeddings = {}
#         # Add code to preprocess the embeddings
#         # This could involve normalization, filtering out unwanted embeddings, etc.
#         logger.info("Preprocessing embeddings")
#         return processed_embeddings

#     def save_embeddings(self, embeddings, destination_path):
#         """
#         Saves the embeddings to a specified destination path.

#         Parameters:
#         embeddings (dict): The dictionary of embeddings to save.
#         destination_path (str): The path where the embeddings should be saved.
#         """
#         # Ensure the directory exists
#         os.makedirs(os.path.dirname(destination_path), exist_ok=True)
        
#         # Save the embeddings to the destination_path
#         logger.info(f"Saving embeddings to {destination_path}")
#         with open(destination_path, 'w') as f:
#             json.dump(embeddings, f)

# # Usage example
# if __name__ == "__main__":
#     preprocessing = Preprocessing()
    
#     # Example usage for data cleaning
#     pdf_path = "path/to/your/file.pdf"
#     cleaned_pdf_data = preprocessing.clean_data(pdf_path, 'pdf')  # Clean PDF data
#     logger.info(f"Cleaned PDF Data: {cleaned_pdf_data}")
    
#     excel_path = "path/to/your/file.xlsx"
#     cleaned_excel_data = preprocessing.clean_data(excel_path, 'excel')  # Clean Excel data
#     logger.info(f"Cleaned Excel Data: {cleaned_excel_data}")
    
#     raw_text = " Example raw text data "
#     cleaned_text_data = preprocessing.clean_data(raw_text, 'text')  # Clean text data
#     logger.info(f"Cleaned Text Data: {cleaned_text_data}")
    
#     # Example usage for data transformation
#     transformed_pdf_data = preprocessing.transform_data(cleaned_pdf_data, 'pdf')  # Transform PDF data
#     logger.info(f"Transformed PDF Data: {transformed_pdf_data}")
    
#     transformed_excel_data = preprocessing.transform_data(cleaned_excel_data, 'excel')  # Transform Excel data
#     logger.info(f"Transformed Excel Data: {transformed_excel_data}")
    
#     transformed_text_data = preprocessing.transform_data(cleaned_text_data, 'text')  # Transform text data
#     logger.info(f"Transformed Text Data: {transformed_text_data}")
    
#     # Example usage for loading and preprocessing embeddings
#     model_path = "path/to/your/model"
#     model = preprocessing.load_embeddings(model_path)
#     embeddings = {"example": [0.1, 0.2, 0.3]}  # Example embeddings
#     processed_embeddings = preprocessing.preprocess_embeddings(embeddings)
#     preprocessing.save_embeddings(processed_embeddings, "data/embeddings/processed_embeddings.json")
    
#     # Example usage for generating embeddings and saving to a file
#     generated_embeddings = preprocessing.generate_embeddings(model, raw_text, "data/embeddings/generated_embeddings.json")
#     logger.info(f"Generated Embeddings: {generated_embeddings}")