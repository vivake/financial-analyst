import pytest
from config.config import ConfigManager

@pytest.fixture
def config_manager():
    return ConfigManager()

def test_config_loading(config_manager):
    config = config_manager.load_config("config.yml")
    db_config = config_manager.load_config("db_config.yml")
    
    assert isinstance(config, dict)  # Ensure config is loaded as a dictionary
    assert "pipeline_config" in config  # Ensure certain keys exist in the config
    assert "database_url" in db_config  # Ensure that DB URL exists in the DB config
