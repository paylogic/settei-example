"""Local settings."""

def generate_config(default):
    """Generate configuration settings for default environment.

    :param default: `settei.config.Config` to inherit settings from

    :returns: `settei.config.Config`

    """
    default["env"] = "This is a setting from the local environment."

    return default
