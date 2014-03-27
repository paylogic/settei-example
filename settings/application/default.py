"""Default settings."""

from settei.config import Config

def generate_config():
    config = Config()

    config['env'] = "This is a setting in the default environment."

    return config
