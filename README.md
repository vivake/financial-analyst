# Financial Analyst Project

## Overview

The Financial Analyst Project is designed to provide tools and functionalities for financial data analysis, including data preprocessing, database interactions, embedding generation, and query handling. The project is organized into modular components to ensure maintainability, scalability, and ease of use.

## Project Structure
financial_analyst/
├── .env
├── .gitignore
├── config/
│   ├── __init__.py
│   ├── config_loader.py
├── data/
│   ├── embeddings/
│   │   ├── # This directory will store generated embeddings
│   ├── raw_data/
│   │   ├── # This directory will store raw data files
│   ├── preprocessing.py
├── databases/
│   ├── __init__.py
│   ├── db_connector.py
│   ├── db_data_retriever.py
├── environment.yml
├── main.py
├── models/
│   ├── bert/
│   │   ├── load_bert.py
│   ├── finbert/
│   │   ├── load_finbert.py
├── query_handler/
│   ├── __init__.py
│   ├── query_handler.py
├── README.md
├── tests/
│   ├── __init__.py
│   ├── test_databases.py
├── utils/
│   ├── # This directory will store utility scripts


## Components

### Configuration

- **config/**: Contains configuration-related scripts.
  - `config_loader.py`: Loads configuration settings from files.

### Data

- **data/**: Contains data-related scripts and directories.
  - **embeddings/**: Stores generated embeddings.
  - **raw_data/**: Stores raw data files.
  - `preprocessing.py`: Contains the `Preprocessing` class for various preprocessing tasks.

### Databases

- **databases/**: Contains database-related scripts.
  - `db_connector.py`: Contains the `DbConnector` class for connecting to different types of databases.
  - `db_data_retriever.py`: Contains the `DataRetriever` class for retrieving data from databases.

### Models

- **models/**: Stores trained machine learning models.

### Query Handling

- **query_handler/**: Contains query handling scripts.
  - `query_handler.py`: Contains the `QueryHandler` class for routing, parsing, and handling queries.

### Tests

- **tests/**: Contains test scripts.
  - `test_databases.py`: Contains tests for database-related functionality.

### Utilities

- **utils/**: Stores utility scripts.

## Usage

### Setting Up the Environment

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/financial-analyst.git
   cd financial-analyst

2. Create and activate the Conda environment:
    conda env create -f environment.yml
    conda activate financial_analyst_env


3. Set up environment variables:

Create a .env file in the root directory and add the necessary environment variables.


Running the Application

1. Main Entry Point:
   - The main entry point of the application is main.py. Run it using:
        python main.py

Preprocessing Data
    -The Preprocessing class in data/preprocessing.py provides methods for cleaning, transforming, and generating embeddings for data.

Database Interactions
    -The DbConnector class in databases/db_connector.py handles connections to different types of databases.
    -The DataRetriever class in databases/db_data_retriever.py retrieves data from databases.

Query Handling
    -The QueryHandler class in query_handler/query_handler.py routes, parses, and handles queries.
