class StoreException(Exception):
    """ Class to define an exception for storage """
    def __init__(self, message, *errors):
        Exception.__init__(self, message)
        self.errors = errors