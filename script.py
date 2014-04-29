from settei import get_config

# get config settings for 'application' and environment
# which was specified when running script.py
config = get_config('application')

print config['env']
