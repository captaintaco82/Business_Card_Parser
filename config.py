import json

class Config:
    """
    Handles retrieval of configuration files
    """
    
    def __init__(self):
        # Read config.json as dictionary and store as "config" property
        try:
            with open('config.json', 'r') as config_file:
                self.config = json.loads(config_file.read())
        except Exception as e:
            self.config = None
            print("Configuration file could not be initialized: %s" % e)
    
    def get_value(self, key):
        """
        Returns the value for a key in the configuration file.
        # input: key, a string representing a key in the configuration file.
        # returns: value for the corresponding configuration key.
        """
        try:
            return self.config[key]
        except KeyError as e:
            print("Error, config key '%s' does not exist" % e)