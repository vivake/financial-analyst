financial_analyst_project/
├── .gitignore             		   # Specifies files and directories to be ignored by Git
├── environment.yml          		 # Conda environment configuration file
├── main.py                 		  # Main script for the project
├── README.md             		    # Project documentation
├── data/                		     # Directory for data-related files
│   ├── embeddings/       		    # Directory for embedding-related files
│   │   └── generate_embedding.py  		# Script to generate embeddings
│   ├── sec_filings/       		   # Directory for SEC filings-related files
│   │   ├── get_sec_filings.py  		# Script to fetch SEC filings using the EDGAR API
│   │   ├── preprocessing/    		# Directory for preprocessing scripts
│   │   │   └── clean_filing_data.py 		 # Script to clean and preprocess SEC filings data
│   │   └── raw_filings/     		 # Directory for raw SEC filings data
├── models/                   		# Directory for model-related files
│   ├── bert/                		 # Directory for BERT model-related files
│   │   └── load_bert.py    		  # Script to load the BERT model
│   ├── finbert/             		 # Directory for FinBERT model-related files
│   │   └── load_finbert.py 		  # Script to load the FinBERT model
├── src/              		        # Directory for source code
│   ├── cashing/          		    # Directory for caching-related files (purpose unclear)
│   ├── databases/        		    # Directory for database-related files
│   │   ├── sec_filings_sql_db/  		# Directory for SQL database-related files
│   │   │   ├── connect_to_sql_db.py		  # Script to connect to the SQL database
│   │   │   ├── load_filings_to_sql_db.py  		# Script to load SEC filings into the SQL database
│   │   │   ├── retrieve_filings_sql_db.py 		 # Script to retrieve SEC filings from the SQL database
│   │   │   └── test_connection.py 		 # Script to test the SQL database connection
│   │   ├── sec_filings_vector_db/  		# Directory for vector database-related files
│   │   │   ├── connect_to_vector_db.py 		 # Script to connect to the vector database
│   │   │   ├── load_filings_to_vector_db.py  		# Script to load SEC filings into the vector database
│   │   │   └── retrieve_filings_vector_db.py 		 # Script to retrieve SEC filings from the vector database
│   ├── query_handler/       		 # Directory for query handling-related files
│   │   ├── context_augmentation.py  		# Script to augment context for queries
│   │   ├── query_intent_classifier.py  		# Script to classify query intents
│   │   └── query_router.py  		 # Script to route queries to appropriate handlers
├── tests/                  			  # Directory for test cases
├── utils/                    # Directory for utility functions
│   └── helpers.py            # Script for helper functions






1. **Environment Setup:**
    - **Description:** Load environment variables from the .env file to access necessary configurations and secrets.
    - **Script:** main.py
    - **Function:** load_dotenv()

2. **Fetch SEC Filings:**
    - **Description:** Fetch SEC filings using the EDGAR API.
    - **Script:** src/data/sec_filings/get_sec_filings.py
    - **Function:** fetch_sec_filings()

3. **Connect to SQL Database:**
    - **Description:** Establish a connection to the SQL database to store and retrieve SEC filings.
    - **Script:** connect_to_sql_db.py
    - **Function:** connect_to_sql_db()

4. **Store Raw SEC Filings in SQL Database:**
    - **Description:** Store the fetched raw SEC filings in the SQL database.
    - **Script:** load_filings_to_sql_db.py
    - **Function:** store_raw_filings()

5. **Retrieve SEC Filings from SQL Database:**
    - **Description:** Retrieve SEC filings from the SQL database for preprocessing.
    - **Script:** retrieve_filings_sql_db.py
    - **Function:** retrieve_filings()

6. **Preprocess SEC Filings Data:**
    - **Description:** Clean and preprocess the retrieved SEC filings data to prepare it for embedding generation.
    - **Script:** src/data/sec_filings/preprocessing/clean_filing_data.py
    - **Function:** clean_filing_data()

7. **Load FinBERT Model:**
    - **Description:** Load the FinBERT model to generate embeddings for the cleaned SEC filings data.
    - **Script:** src/data/models/finbert/load_finbert.py
    - **Function:** load_finbert()

8. **Generate Embeddings for SEC Filings:**
    - **Description:** Use the FinBERT model to generate embeddings for the cleaned SEC filings data.
    - **Script:** src/data/embeddings/generate_embeddings.py
    - **Function:** generate_embeddings()

9. **Connect to Vector Database:**
    - **Description:** Establish a connection to the vector database to store the generated embeddings.
    - **Script:** connect_to_vector_db.py
    - **Function:** connect_to_vector_db()

10. **Store Embeddings in Vector Database:**
     - **Description:** Store the generated embeddings in the vector database for future retrieval and analysis.
     - **Script:** load_filings_to_vector_db.py
     - **Function:** store_embeddings()

11. **Handle Queries:**
     - **Description:** Set up query handling to process user queries, classify intents, and route them to the appropriate handlers.
     - **Script:** query_router.py
     - **Function:** route_query()

12. **Augment Context for Queries:**
     - **Description:** Augment the context for user queries to provide more accurate and relevant responses.
     - **Script:** context_augmentation.py
     - **Function:** augment_context()

13. **Utility Functions:**
     - **Description:** Utilize any necessary utility functions to support the above steps.
     - **Script:** src/utils/helpers.py
     - **Function:** some_utility_function()

**Summary:**
By modularizing the tasks and organizing them in a logical order, you can ensure that each step of your project is clearly defined and executed. This approach enhances the maintainability and scalability of your project. Each task is described with its purpose and the corresponding script and function, providing a comprehensive overview of the project's workflow.
