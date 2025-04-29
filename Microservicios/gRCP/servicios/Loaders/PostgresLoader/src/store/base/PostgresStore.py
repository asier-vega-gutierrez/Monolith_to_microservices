from store.base.StoreBase import Store 
from exceptions.StorageException import StoreException
import psycopg2

from config.configuration import ApplicationConfiguration

class PostgresStore(Store):
    """ Class to manage postgres DBs"""

    def __init__(self):
        """ Default constructor of the Alarm Store """

        super().__init__()
    
    def _get_connection(self):
        """ AbStract method to get the connection """

        # We get the configuration
        config = ApplicationConfiguration()        

        # We get the connection
        return  psycopg2.connect(host=config.postgres_ip, port=config.postgres_port, user=config.postgres_user, password=config.postgres_pass, database=config.postgres_db)
    
    def disconnect(self):
        """ Abstract method to make disconnection"""
        if(self._conn):
            self._conn.close()
        else:
            raise StoreException('Disconection not posible. No connection available', None)

    def commit(self):
        """ Abtract method to make a commit in a transaction """
        if(self._conn):
            self._conn.commit()
        else:
            raise StoreException('Commit not possible. No connection available', None)


    def rollback(self):
        """ Abstract method to  make a rollback """
        if(self._conn):
            self._conn.commit()
        else:
            raise StoreException('Commit not possible. No connection available', None)