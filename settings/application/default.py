"""Default settings."""

from settei.config import Config

def generate_config():
    """Generate configuration settings for default environment.

    :returns: `settei.config.Config`

    """
    config = Config()

    config["env"] = "This is a setting in the default environment."

    return config
