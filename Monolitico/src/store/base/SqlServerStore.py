from multiprocessing import connection
import pymssql
from time import sleep  

from exceptions.StorageException import StoreException
from store.base.StoreBase import Store

from config.configuration import ApplicationConfiguration

class SqlServerStore(Store):
    """ Specifica class for manage MySql operations """

    def __init__(self, db_name):
        """ Constructor of the class  """
        super().__init__()
        
        self.db_name = db_name

    def _get_connection(self):
        """ Abtract method to get the connection """
        
        #conn = None
        #connected = False

        #TODO: To be completed for conn creation (using config information)
        config = ApplicationConfiguration()
        db_params = {
            'database': config.sql_server_mould_db,
            'user': config.sql_server_user,
            'password': config.sql_server_pass,
            'host': config.sql_server_ip,
            'port': config.sql_server_port
        }
        try:
            self._conn = pymssql.connect(**db_params)
            print("Connected to the database.(SqlServer)")
        except pymssql.Error as e:
            print(f"Error connecting to the database(SqlServer): {e}")
        return self._conn       

    def disconnect(self):
        """ Abstract method to make disconnection"""

        #TODO: To be compleated 
        if self._conn:
            self._conn.close()
        print("Disconnected from the database.(SqlServer)")

    def commit(self):
        """ Abtract method to make a commit in a transaction """
        
        #TODO: To be compleated 
        try:
            self._conn.commit()
            print("Changes committed to the database.(SqlServer)")
        except pymssql.Error as e:
            print(f"Error committing changes: {e}")
            self.conn.rollback()

    def rollback(self):
        """ Abstract method to  make a rollback """
        
        #TODO: To be compleated 
        try:
            self.conn.rollback()
            print("Transaction rolled back.(SqlServer)")
        except pymssql.Error as e:
            print(f"Error rolling back transaction(SqlServer): {e}")