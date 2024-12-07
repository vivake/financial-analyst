# Import the necessary libraries

# Model imports
from transformers import BertTokenizer, BertModel   #  FinBERT model and tokenizer from the Hugging Face Transformers library
import torch    # PyTorch library for gradient removal and tensor operations

# Text processing imports
from langchain_text_splitters import RecursiveCharacterTextSplitter # Recursive text splitter for splitting text into sentences

# Document imports
import pymupdf  # PyMuPDF document text extraction of PDFs
from langchain.docstore.document import Document    # Document class for storing document text and metadata
import uuid # UUID for generating unique document IDs

# Database loader and vector store imports
from astrapy.client import DataAPIClient
# Environment variable loader imports
import os   # OS library for environment variable access
from dotenv import load_dotenv  # Load environment variables from a .env file

# JSON library for parsing JSON strings
import json 

class PDFPreprocessor:
    def __init__(self):
        # Load environment variables
        load_dotenv()
        self.astra_db_endpoint = os.getenv('ASTRA_DB_ENDPOINT')
        self.astra_db_token = os.getenv('ASTRA_DB_TOKEN')
        self.astra_db_id = os.getenv('ASTRA_DB_ID')
        self.keyspace = os.getenv('ASTRA_DB_KEYSPACE')
        self.collection = os.getenv('ASTRA_DB_COLLECTION_NAME')
        
        # Print the environment variables to verify they are loaded correctly
        print("Astra DB API Endpoint:", self.astra_db_endpoint)
        print("Astra DB Application Token:", self.astra_db_token)
        print("Astra API Key:", self.astra_api_key)
        print("Astra DB ID:", self.astra_db_id)
        print("Keyspace:", self.keyspace)
        print("Collection Name:", self.collection_name)
        print("\n")
        
        
         # Step 1: Connect to Astra DB and initialize the FinBERT model and tokenizer
    
         # Initialize the DataAPIClient with the application token
        client = DataAPIClient(self.astra_db_token)

        # Connect to the database using the API endpoint
        db=client.get_database_by_api_endpoint(
            api_endpoint=self.astra_db_endpoint,
            keyspace=self.keyspace,
        )
        print(f"Connected to Astra DB: {db.list_collection_names()}")
        print("\n")
        
        self.tokenizer = BertTokenizer.from_pretrained("ProsusAI/finbert")
        self.model = BertModel.from_pretrained("ProsusAI/finbert")
        print(self.model)

    # Function to generate embeddings using FinBERT
    def generate_embedding(self, text):
        """
        Generates an embedding for the given text using a pre-trained transformer model.
        Args:
            text (str): The input text to be embedded.
        Returns:
            numpy.ndarray: The embedding of the input text as a numpy array.
        """
        
        # Tokenize the input text
        inputs = self.tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=512)
                
        # Get the model's outputs (hidden states)
        with torch.no_grad():   # Disable gradient calculation for faster processing
            outputs = self.model(**inputs)
        
        # Access generated embedding from the [CLS] token (last hidden state of the first token of the sequence)
        embedding = outputs.last_hidden_state[:, 0, :].squeeze().numpy()    
        return embedding
    
# Step 2: Function to extract text and metadata from PDF using PyMuPDF
def extract_text_and_metadata_from_pdf(pdf_path):
    """
    Extracts text and metadata from a PDF file.
    Args:
        pdf_path (str): The file path to the PDF document.
    Returns:
        tuple: A tuple containing:
            - text (str): The extracted text from the PDF.
            - metadata (dict): The metadata of the PDF, which may include information such as:
                - title (str): The title of the document.
                - author (str): The author of the document.
                - subject (str): The subject of the document.
                - keywords (str): Keywords associated with the document.
                - creator (str): The software used to create the document.
                - producer (str): The software used to produce the document.
                - creationDate (str): The date the document was created.
                - modDate (str): The date the document was last modified.
    # doc: A list of PyMuPDF Document object representing the PDF file.
    #      It contains methods and attributes to interact with the PDF, such as:
    #      - get_text(): Extracts text from a page.
    #      - metadata: A dictionary containing the PDF's metadata.
    """

    doc = pymupdf.open(pdf_path)  # Open the PDF document and load it into a doc
    
    text = ""
    
    # Extract text from each page
    for page in doc:
        text += page.get_text()
    
    # Extract metadata from the PDF
    metadata = doc.metadata
    
    print(f"metadata: {metadata},")
    print(f"text: {text}")
    
    return text, metadata   # Return the extracted text and metadata as a tuple

# Step 3: Initialize the RecursiveCharacterTextSplitter
def get_recursive_text_splitter(chunk_size=500):
    """
    This function creates a RecursiveCharacterTextSplitter with a specified chunk size, 
    chunk overlap, and length function. The splitter is used to divide text into smaller 
    chunks while preserving context by overlapping chunks.
    Parameters:
    chunk_size (int): The maximum size of each chunk in tokens. Default is 500.
    Returns:
    RecursiveCharacterTextSplitter: An initialized RecursiveCharacterTextSplitter object.
    """    
    # Initialize the RecursiveTextSplitter
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,  # Max chunk size in tokens
        chunk_overlap=50,       # Overlap between chunks to preserve context
        length_function=len     # Length function to determine chunk size
    )
    return splitter # Return the initialized RecursiveTextSplitter object

# Step 4: Use RecursiveCharacterTextSplitter to chunk the text
def chunk_text(text, splitter):
    """
Chunks the given text using the specified splitter.
This function takes a text string and a splitter object, then uses the splitter's
split_text method to divide the text into smaller chunks.
Args:
    text (str): The text to be chunked.
    splitter (object): An object with a split_text method that handles the chunking.
Returns:
    list: A list of text chunks.
"""
   # Chunk the text using the splitter
    chunks = splitter.split_text(text)  
    return chunks  # Return a list of text chunks 

# Function to split the documents into batches
def batch(documents, batch_size):
    for i in range(0, len(documents), batch_size):
        yield documents[i : i + batch_size]
        
# Step 5: Create a function to prepare the documents with id, text, embeddings and, metadata
def create_astra_db_document(self, text, metadata):
    """
    Prepare a JSON-serializable document for insertion into an Astra database collection. 
    Args:
        text (str): The text content of the document.
        metadata (dict): The metadata associated with the document.
    Returns:
        dict: A dictionary representation of the document containing the text, metadata, and embedding.
    """
    
    # Generate the embedding for the document chunk
    embedding = self.generate_embedding(text)
    
    # Create the document dictionary with Astra DB required fields (Id, text, metadata, and embedding)
    doc = {
        "id": str(uuid.uuid4()),  # Generate a unique ID for the document
        "text": text,
        "metadata": metadata,
        "vector": embedding.tolist()  # Convert the embedding to a list
    }
    return doc  # Return the dictionary representation of the document        

# Step 6: Define the Astra DB insertion function
# Function to insert documents into Astra DB in batches
def insert_documents_into_astra_db(self, documents):
    """
    Inserts a list of documents (metadata, text, embedding) into an Astra DB collection in batches.
    Args:
        documents (list): A list of document dictionaries to be inserted into the Astra DB.
    """
    # Define the collection in the database
    collection = self.db.get_collection(self.collection_name)
    
    # Insert the documents in batches
    for batch_documents in batch(documents, 50):
        # Insert the batch of documents into the collection
        res = collection.insert_many(batch_documents)
        print(f"Inserted batch with response: {res}")
        
# Main Workflow

# Step 7: Process the PDF, extract metadata, and insert documents into Astra DB collection
def process_pdf_to_astra(self, pdf_path):
    """
    Processes a PDF file and inserts its content into Astra DB.
    This function performs the following steps:
    1. Extracts text and metadata from the given PDF file.
    2. Initializes a RecursiveTextSplitter with a specified chunk size.
    3. Splits the extracted text into chunks using the splitter.
    4. Enhances the extracted metadata with additional information.
    5. Creates Document objects for each text chunk with the associated metadata.
    6. Inserts the Document objects into Astra DB.
    7. Logs the number of documents inserted.
    Args:
        pdf_path (str): The file path to the PDF document to be processed.
    Returns:
        None
    """
    
    # Extract text and metadata from the PDF
    pdf_text, pdf_metadata = extract_text_and_metadata_from_pdf(pdf_path)
    print("Extracted PDF Metadata:", pdf_metadata) # Print the extracted metadata to indicate successful extraction
    
    # Initialize RecursiveTextSplitter
    splitter = get_recursive_text_splitter(chunk_size=500)
    print("RecursiveTextSplitter Initialized") # Print a message to indicate initialization
    
    # Use the splitter to chunk the extracted text
    chunks = chunk_text(pdf_text, splitter)
    print(f"Chunked PDF into {len(chunks)} text chunks.") # Print the number of chunks
    
    # Enhance metadata with additional info (you could add more info based on use case)
    metadata = {
        "source": pdf_path,
        "title": pdf_metadata.get('title', 'Unknown Title'),
        "author": pdf_metadata.get('author', 'Unknown Author'),
        "subject": pdf_metadata.get('subject', 'Unknown Subject'),
        "created": pdf_metadata.get('created', 'Unknown Date'),
        "modified": pdf_metadata.get('modified', 'Unknown Date'),
    }
    
    # Create Document objects with text chunks and metadata
    documents = []
    for chunk in chunks:    # loop to create a Document object for each chunk
        doc = create_astra_db_document(chunk, metadata)
        documents.append(doc)  
    print(f"Generated {len(documents)} Document objects.") # Print the number of Document objects generated
          
    # Insert documents into Astra DB
    insert_documents_into_astra_db(documents)
    
    # Print or log the number of documents inserted (optional)
    print(f"Processed PDF '{pdf_path}'. Inserted {len(documents)} documents into Astra DB.")