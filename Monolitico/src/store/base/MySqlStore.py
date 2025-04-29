import pymysql

from exceptions.StorageException import StoreException
from store.base.StoreBase import Store

from config.configuration import ApplicationConfiguration

class MySqlStore(Store):
    """ Specifica class for manage MySql operations """

    def _get_connection(self):
        """ Abtract method to get the connection """
        
        #conn = None
        #connected = False

        config = ApplicationConfiguration()
        db_params = {
            'database': config.mysql_db,
            'user': config.mysql_user,
            'password': config.mysql_pass,
            'host': config.mysql_ip,
            'port': config.mysql_port
        }

        #TODO: To be completed for conn creation (using config information)
        try:
            self._conn = pymysql.connect(**db_params)
            print("Connected to the database.(MySql)")
        except pymysql.Error as e:
            print(f"Error connecting to the database(MySql): {e}")
        return self._conn       

    def disconnect(self):
        """ Abstract method to make disconnection"""
        
        #TODO: To be compleated 
        if self._conn:
            self._conn.close()
        print("Disconnected from the database. (MySql)")

    def commit(self):
        """ Abtract method to make a commit in a transaction """
        
        #TODO: To be compleated
        try:
            self._conn.commit()
            print("Changes committed to the database.(MySql)")
        except pymysql.Error as e:
            print(f"Error committing changes(MySql): {e}")
            self._conn.rollback()


    def rollback(self):
        """ Abstract method to  make a rollback """
        
        #TODO: To be compleated 
        try:
            self._conn.rollback()
            print("Transaction rolled back.(MySql)")
        except pymysql.Error as e:
            print(f"Error rolling back transaction(MySql): {e}")