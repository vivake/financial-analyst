# Reddit Business Analysis Pipeline

This project aims to build an end-to-end pipeline for extracting, processing, analyzing, and querying complex financial and business data for Reddit's revenue growth and scalability. The pipeline integrates various NLP models like FinBERT for financial text analysis, data extraction from multiple formats (PDF, Excel), embedding generation, and advanced query handling to assist in decision-making.
The project incorporates a multi-modal pipeline that handles different stages of data processing, from document extraction to metadata generation and querying, using tools like spaCy, FinBERT, and vector databases for embeddings.

## Project Overview

This project provides an end-to-end solution for analyzing key business questions related to Reddit's revenue growth, including identifying important KPIs, understanding the scalability of its ad business, and exploring new revenue opportunities. The pipeline utilizes multiple technologies and steps, including:

## Features

- **Text Extraction**:
  - Handles different types of data sources (PDF, Excel, etc.)
- **NLP Processing**:
  - Includes tokenization, Named Entity Recognition (NER), and domain-specific financial entity extraction.
- **Embedding Generation**:
  - Converts raw data into meaningful embeddings for advanced querying and analysis.
- **Query Handling**:
  - Routes user queries to appropriate data sources and generates insightful responses.
- **Real-time Chatbot UI**:
  - Allows interaction with users via a chatbot interface, providing answers based on financial data.

## Table of Contents

- [Project Structure] (#project-overview)
- [Setup and Installation] (#setup-and-installation)
- [Requirements] (#software-requirements)
- [Pipelines] (#pipelines)
- [Configuration] (#configuration)
- [Database] (#database)
- [Model Integration] (#model-integration)
- [Querying] (#querying)
- [Testing] (#testing)
- [GitHub Workflows] (#github-workflows)
- [Future Enhancements] (#future-enhancements)

sec_analyst_project/
│
├── main.py                     # Main entry point to orchestrate pipelines and workflows
│
├── config/
|     ├── config.yml               # Central configuration for all modules
|     ├── db_config.yml            # Shared database configuration (SQL and Vector DB)
|     ├── pipeline_config.yml      # Pipeline settings (e.g., workflows, dependencies)
|     ├── config.py                # Class: `ConfigManager` to handle configurations
|-- preprocessors/
|     |-- preprocessor.py          # Centralized interface combining all preprocessing steps
|     ├── text_preprocessor.py     # Specialized class for text preprocessing
|     ├── table_preprocessor.py    # Specialized class for table preprocessing
|     ├── pdf_preprocessor.py      # Specialized class for PDF preprocessing
├── data/
|     ├── raw/                     # Raw input data (PDFs, Excel)
|     ├── processed/               # Processed data after extraction and NLP tasks
|     ├── preprocessed/            # Preprocessed and cleaned data
|     ├── embeddings/              # Generated embeddings linked to Astra DB
|     ├── sql_data.py/             # Class: SqlData linked to PostgreSQL
|
├── pipelines/
|    ├── extraction_pipeline.py    # Class: `ExtractionPipeline` for end-to-end extraction
|    ├── nlp_pipeline.py           # Class: `NLPPipeline` for tokenization, NER
|    ├── embedding_pipeline.py     # Class: `EmbeddingPipeline` for FinBERT and vector DB
|    ├── retrieval_pipeline.py     # Class: `RetrievalPipeline` for query responses
|    ├── automation.py             # Automated pipeline orchestration with Airflow/Prefect
│
├── extractors/
│   ├── pdf_extractor.py           # Class: `PDFExtractor` for text extraction
│   ├── excel_extractor.py         # Class: `ExcelExtractor` for table extraction
│
├── nlp/
│   ├── tokenization.py            # Class: `Tokenizer`
│   ├── basic_ner.py               # Class: `BasicNERProcessor` (pre-trained spaCy)
│   ├── custom_ner.py              # Class: `CustomNERProcessor` (fine-tuned spaCy)
│   ├── financial_entity.py        # Class: `FinancialEntityProcessor` for financial NER
│
├── models/
│   ├── finbert.py                 # Class: `FinBERTModel` for domain-specific embeddings
│   ├── gpt4.py                    # Class: `GPT4Model` for advanced metadata extraction
│
├── databases/
│   ├── sql_database.py            # Class: `SQLDatabaseManager` for managing SQL interactions
│   ├── vector_database.py         # Class: `VectorDBManager` for managing vector DB
│
├── query/
│   ├── query_router.py            # Class: `QueryRouter` for routing queries
│   ├── response_generator.py      # Class: `ResponseGenerator` for GPT-4 responses
│
├── ui/
│   ├── chatbot.py                 # Class: `ChatbotUI` for user interface
│   ├── handlers.py                # Query handler logic for the UI
│
├── utils/
│   ├── logger.py                  # Class: `Logger`
│   ├── file_manager.py            # Utility: File management operations
│   ├── helpers.py                 # Utility: Shared helper functions
│
├── tests/
│   ├── test_pipelines.py          # Test cases for pipelines
│   ├── test_extractors.py         # Test cases for text extraction
│   ├── test_nlp.py                # Test cases for NLP tasks
│   ├── test_databases.py          # Test cases for databases
│   ├── test_query.py              # Test cases for query routing and responses
│   ├── test_ui.py                 # Test cases for UI interface
│
├── logs/                       # Directory for log files
│   ├── app.log                 # Log file for application-wide events
│   ├── pipeline.log            # Log file for pipeline-specific events
|
├── workflows/
│   ├── github/
│       ├── workflows/
│           ├── ci.yml             # GitHub Actions for CI/CD
│           ├── pipeline_test.yml  # Automated pipeline testing
│
├── .env                           # Environment variables (secrets)
├── .gitignore                     # Files to ignore
├── environment.yml                # Conda environment configuration
├── environment.yml                # Conda environment configuration
└── README.md                      # Project overview and instructions

Setup and Installation

    **Software Requirements**
      - Python 3.8+
        - Ensure that Python 3.8 or a later version is installed in your environment.
      - PostgreSQL 12+
        - Used for storing and managing structured data.
        - Ensure PostgreSQL is installed and a database is set up for use.
      - Conda (optional for environment management)
        - If you are using Conda to manage environments, make sure Conda is installed.
      - Required Python Libraries
        - List of dependencies required to run the project (included in requirements.txt).
    - **Hardware Requirements**
      - Memory: At least 8 GB of RAM is recommended for NLP tasks.
      - CPU: Multi-core processors are recommended for parallel execution of pipelines.
      - Storage: Sufficient storage for large PDF and Excel documents, and embeddings (may require several GBs depending on data).

Pipelines

- The project utilizes several pipelines for different stages of processing. Each pipeline is independent, but they work together to produce the desired results.

  1. Extraction Pipeline (extraction_pipeline.py)
     - Extracts text from raw input files (PDF, Excel).
     - Tools: pdf_extractor.py, excel_extractor.py
     - Steps:
       - PDF or Excel file input.
       - Extract text using appropriate extraction classes.
       - Output raw text in a structured format.
  2. NLP Pipeline (nlp_pipeline.py)
     - Tokenizes text formatted from extraction pipeline text, applies Named Entity Recognition (NER), and prepares text for embedding generation.
     - Tools: basic_ner.py, custom_ner.py, financial_entity.py
     - Steps:
       - Tokenize text into meaningful chunks.
       - Apply NER to detect important financial entities (e.g., companies, dates, financial terms).
       - Return preprocessed data ready for embedding generation.
  3. Embedding Pipeline (embedding_pipeline.py)
     - Converts processed data into embeddings using FinBERT.
     - Tools: finbert.py
     - Steps:
       - Load tokenized text.
       - Generate embeddings using FinBERT.
       - Store embeddings into the vector database (handled by vector_db.py).
  4. Query Pipeline (query_pipeline.py)
     - Handles queries from users, processes them, and retrieves data from the database.
     - Tools: query_processor.py, response_generator.py
     - Steps:
       - Receive and process the user query.
       - Route the query to the relevant data source (SQL database, vector database).
       - Return insights or text summaries based on the query.
  5. UI Pipeline (ui_pipeline.py)
     - Handles user interactions through a chatbot interface.
     - Tools: chatbot_ui.py, query_handler.py
     - Steps:
       - Show the chatbot interface to the user.
       - Collect user input and forward queries to the Query Pipeline.
       - Return answers from the Query Pipeline to the user.

Configuration

- Configuration Files
  - config.yml: Central configuration file for general settings.
  - db_config.yml: Stores PostgreSQL database connection details.
  - pipeline_config.yml: Defines the pipeline configurations, including parameters like batch sizes or execution modes.
  - config.py: Contains the ConfigManager class to load configuration settings dynamically.
- Environment Variables
  - .env: Contains sensitive data like API keys, database credentials, etc.

Example:

    OPENAI_API_KEY=your_api_key
    POSTGRES_DB=your_database_name

Database

- PostgreSQL Integration
  - postgresql_db.py: Integrates PostgreSQL for managing structured financial data (reports, transaction data).
  - Stores data such as earnings calls, financial reports, and business metrics.
- Vector Database
  - vector_db.py: Handles storage and retrieval of embeddings.
  - Optimized for storing vectorized data from models like FinBERT.

Model Integration
    - FinBERT Model
    - finbert.py: A class for handling FinBERT-based embeddings.
    - The class will load a pre-trained FinBERT model and perform embedding generation for business-related text.
    - GPT-4 Model
    - gpt4.py: A class to interact with GPT-4, leveraging OpenAI's API for generating responses to complex queries.
    - Uses GPT-4 to generate text-based insights, summaries, and answers to business questions.

Querying
  Query Processing
        - query_processor.py: Responsible for receiving, interpreting, and processing user queries.
        - Determines whether the query is about structured data (SQL database) or textual data (vector DB).
  Response Generation
        - response_generator.py: Generates a response based on the processed query.
        - Retrieves relevant data from databases or uses NLP models to create a meaningful response.

Testing
    - Unit Tests
    - The following tests ensure each component works as expected:
    - test_extraction.py: Tests the extraction pipeline, including text extraction from PDF/Excel.
    - test_nlp.py: Verifies the NLP pipeline, ensuring tokenization and entity recognition works.
    - test_embeddings.py: Validates that embeddings are generated correctly from text.
    - test_query.py: Ensures the query pipeline returns correct responses from the database.

GitHub Workflows
    - Continuous Integration (CI) with GitHub Actions
    - ci.yml: Runs unit tests on every commit to ensure code quality.
    - pipeline_test.yml: Automatically tests the entire pipeline to validate end-to-end processing.

Future Enhancements
    - Real-time Data Ingestion:
          - Integrate real-time data feeds for dynamic analysis of financial reports and earnings calls.
Advanced Query Features:
    -Expand the query functionality to support multi-source queries and complex question answering.
UI Improvements:
     -Enhance the chatbot UI for better user experience and interactivity.
