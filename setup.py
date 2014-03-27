from setuptools import setup, find_packages

setup(
    name='settei-example',
    version='1.0',
    packages = find_packages(),
    entry_points = {
        'settings_application': [
            'default = settings.application.default:generate_config',
            'local = settings.application.local:generate_config',
        ]
    },
)
