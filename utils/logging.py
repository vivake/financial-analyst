import logging  # Importing the logging module to handle logging
import os       # Importing the os module to work with file system operations

# Ensure that the 'logs' directory exists. If not, it will be created.
log_dir = 'logs'  # Directory where log files will be saved
os.makedirs(log_dir, exist_ok=True)  # Creates the logs directory if it doesn't exist

# Function to setup logging configuration
def setup_logger():
    """
    This function sets up the logger for the application, configuring it to log to both a file
    and the console, with detailed formatting and appropriate log levels.
    """
    
    # Create a logger instance. This will be used to write log messages
    logger = logging.getLogger('sec_analyst_project')  # Logger name can be any string, it's often the app name
    logger.setLevel(logging.DEBUG)  # Set the log level to DEBUG, meaning all logs from DEBUG level and higher are captured

    # File handler for logging messages to a file
    # All logs will be saved in the 'logs/app.log' file
    file_handler = logging.FileHandler(os.path.join(log_dir, 'app.log'))  # Creating the file handler
    file_handler.setLevel(logging.DEBUG)  # Set the minimum log level to DEBUG for the file handler (captures all messages)

    # Console handler for logging messages to the console (terminal)
    console_handler = logging.StreamHandler()  # Creating the console handler
    console_handler.setLevel(logging.INFO)  # Set the minimum log level to INFO for the console handler

    # Log format specifies how each log message will appear in the logs
    # The format includes the timestamp, logger name, log level, and the actual message
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    
    # Set the formatter for both the file handler and console handler
    file_handler.setFormatter(formatter)  # Applying formatter to file handler
    console_handler.setFormatter(formatter)  # Applying formatter to console handler

    # Add both handlers to the logger
    logger.addHandler(file_handler)  # Attach the file handler to the logger
    logger.addHandler(console_handler)  # Attach the console handler to the logger

    return logger  # Return the configured logger instance

# Initialize the logger by calling the setup_logger function
logger = setup_logger()

# Example usage of the logger:
logger.debug("This is a debug message")  # This log will appear in both the file and the console (if log level is DEBUG or higher)
logger.info("This is an info message")  # This log will appear in both the file and the console (if log level is INFO or higher)
logger.warning("This is a warning message")  # This log will appear in both the file and the console (if log level is WARNING or higher)
