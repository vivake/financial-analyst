import os
from dotenv import load_dotenv
import yaml

class Config:
    """
    Class for managing the configuration.
    """

    def __init__(self, config_files):
        """
        Initialize the Config class with a list of configuration files.

        Parameters:
        config_files (list): A list of paths to configuration files.
        """
        self.config_files = config_files  # Store the list of configuration files
        self.config = {}  # Initialize an empty dictionary to hold the configuration
        load_dotenv()  # Load environment variables from .env file
        self.load_all_configs()  # Load all configuration files

    def load_all_configs(self):
        """
        Load all configuration files.
        """
        for config_file in self.config_files:  # Iterate over each configuration file
            self.load_config(config_file)  # Load the configuration from the file

    def load_config(self, config_file):
        """
        Load the configuration from a YAML file and substitute environment variables.

        Parameters:
        config_file (str): The path to the configuration file.
        """
        with open(config_file, 'r') as file:  # Open the configuration file
            config = yaml.safe_load(file)  # Load the YAML content
            for section, settings in config.items():  # Iterate over each section in the configuration
                if section not in self.config:  # If the section is not already in the config
                    self.config[section] = {}  # Initialize the section in the config
                for key, value in settings.items():  # Iterate over each key-value pair in the section
                    if isinstance(value, str) and value.startswith("${") and value.endswith("}"):  # Check if the value is an environment variable
                        env_var = value[2:-1]  # Extract the environment variable name
                        self.config[section][key] = os.getenv(env_var)  # Substitute the environment variable value
                    else:
                        self.config[section][key] = value  # Otherwise, use the value from the file

    def get(self, section, key, default=None, secure=False):
        """
        Retrieve a configuration value.

        Parameters:
        section (str): The section of the configuration.
        key (str): The key within the section to retrieve the value.
        default: The default value to return if the key is not found (default is None).
        secure (bool): Whether to restrict access to sensitive information (default is False).

        Returns:
        The configuration value associated with the key, or the default value if the key is not found.
        """
        sensitive_keys = [
            ('api_keys', 'huggingface'), 
            ('api_keys', 'openai'), 
            ('postgresql_db', 'password'), 
            ('vector_data_db', 'api_endpoint'), 
            ('vector_data_db', 'application_token')
        ]
        if secure and (section, key) in sensitive_keys:  # Check if access to sensitive information is restricted
            raise PermissionError("Access to sensitive information is restricted.")  # Raise a PermissionError if access is restricted
        return self.config.get(section, {}).get(key, default)  # Retrieve the configuration value or return the default value

# Example usage
if __name__ == "__main__":
    config_files = ['config/config.yml', 'config/sql_db.yml', 'config/vector_db.yml']  # List of configuration files
    config = Config(config_files)  # Create a Config object with the list of configuration files
    try:
        db_host = config.get('postgresql_db', 'host')  # Retrieve the database host from the configuration
        db_name = config.get('postgresql_db', 'name')  # Retrieve the database name from the configuration
        api_key = config.get('api_keys', 'huggingface', secure=True)  # Retrieve the Hugging Face API key from the configuration
        api_endpoint = config.get('vector_data_db', 'api_endpoint', secure=True)  # Retrieve the AstraDB API endpoint from the configuration
        print(f"Database Host: {db_host}")  # Print the database host
        print(f"Database Name: {db_name}")  # Print the database name
        print(f"Hugging Face API Key: {api_key}")  # Print the Hugging Face API key
        print(f"AstraDB API Endpoint: {api_endpoint}")  # Print the AstraDB API endpoint
    except PermissionError as e:  # Catch any PermissionError exceptions
        print(e)  # Print the error message