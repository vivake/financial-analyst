# Class for SQL database connection setup

#Create and connect to sql db for sec filings. 

from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Access environment variables
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_host = os.getenv('DB_HOST')
db_port = os.getenv('DB_PORT')
db_name = os.getenv('DB_NAME')

# Create the database connection string
connection_string = f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
engine = create_engine(connection_string)

# Test the connection
try:
    with engine.connect() as connection:
        print("Connection to the database was successful!")
except Exception as e:
    print(f"An error occurred: {e}")