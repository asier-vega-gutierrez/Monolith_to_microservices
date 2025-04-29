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
        """ Abtract method to get the connection """
        
        #conn = None
        #connected = False

        #TODO: To be completed for conn creation (using config information)
        config = ApplicationConfiguration()
        db_params = {
            'database': config.postgres_db,
            'user': config.postgres_user,
            'password': config.postgres_pass,
            'host': config.postgres_ip,
            'port': config.postgres_port
        }
        try:
            self._conn = psycopg2.connect(**db_params)
            print("Connected to the database.(Postgress)")
        except psycopg2.Error as e:
            print(f"Error connecting to the database(Postgress): {e}") 
        return self._conn

    def disconnect(self):
        """ Abstract method to make disconnection"""
        
        #TODO: To be compleated 
        if self._conn:
            self._conn.close()  
        print("Disconnected from the database.(Postgress)")

    def commit(self):
        """ Abtract method to make a commit in a transaction """
        
        #TODO: To be compleated 
        try:
            self._conn.commit()
            print("Changes committed to the database.(Postgress)")
        except psycopg2.Error as e:
            print(f"Error committing changes(Postgress): {e}")
            self._conn.rollback()


    def rollback(self):
        """ Abstract method to  make a rollback """
        
        #TODO: To be compleated 
        try:
            self._conn.rollback()
            print("Transaction rolled back.(Postgress)")
        except psycopg2.Error as e:
            print(f"Error rolling back transaction(Postgress): {e}")