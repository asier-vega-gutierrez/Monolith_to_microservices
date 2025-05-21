from multiprocessing import connection
import pymssql
from time import sleep  

from exceptions.StoreException import StoreException
from store.base.StoreBase import Store

from config.configuration import PDAgentSqlServerReaderConfig

class SqlServerStore(Store):
    """ Specifica class for manage MySql operations """

    def __init__(self, db_name):
        """ Constructor of the class  """
        super().__init__()
        
        self.db_name = db_name

    def _get_connection(self):
        """ Abtract method to get the connection """
        
        conn = None
        connected = False
        while not connected:
            try:
                print('Trying to connecto to the SQL Server DB {}'.format(self.db_name))

                config = PDAgentSqlServerReaderConfig()

                # Connection to be used inside docker container
                conn = pymssql.connect(server=f'{config.sql_server_ip}:{config.sql_server_port}', 
                                       user=config.sql_server_user, 
                                       password=config.sql_server_pass, 
                                       database=self.db_name)

                # Connection to be done from outside docker container
                #conn = pymssql.connect(server='localhost:1433', user='sa', password='MUCSI_Deusto2022', database=self.db_name)  
                connected = True
            except:
                print('ERROR: Waiting 5 seconds to retry')
                sleep(5)

        return conn       

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