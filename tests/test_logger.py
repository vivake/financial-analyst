import pytest
from utils.logger import Logger

def test_logger():
    logger = Logger()
    
    # Assuming your logger has a method log
    logger.log("Test message")
    
    # Check if the log file contains the expected message (you may want to check the file content)
    with open("logfile.log", "r") as f:
        logs = f.read()
    
    assert "Test message" in logs  # Ensure the test message is logged
