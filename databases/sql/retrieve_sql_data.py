import sqlite3
"""
Module for retrieving data from an SQLite database.

This module contains a class `SQLDataRetriever` that provides methods to connect to an SQLite database,
execute SQL queries, and retrieve data. It also includes error handling for database operations.

Classes:
    SQLDataRetriever: A class to handle SQLite database connections and data retrieval.

Methods:
    __init__(self, database_path):
        Initializes the SQLDataRetriever with the path to the SQLite database.

    connect(self):
        Establishes a connection to the SQLite database and creates a cursor object.
        Prints a message indicating the connection status.

    retrieve_data(self, query):
        Executes the given SQL query and retrieves all results.
        Returns the fetched data or None if an error occurs.

    close_connection(self):
        Closes the connection to the SQLite database.
        Prints a message indicating the connection closure status.
"""

# Class for SQL data retrieval logic
class SQLDataRetriever:
    def __init__(self, database_path):
        self.database_path = database_path

    def connect(self):
        try:
            self.connection = sqlite3.connect(self.database_path)
            self.cursor = self.connection.cursor()
            print("Connection to database established.")
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")

    def retrieve_data(self, query):
        try:
            self.cursor.execute(query)
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
            return None

    def close_connection(self):
        if self.connection:
            self.connection.close()
            print("Connection to database closed.")