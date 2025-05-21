import pymysql

from exceptions.StoreException import StoreException
from store.base.StoreBase import Store

from config.configuration import PDAgentMySqlConfiguration

class MySqlStore(Store):
    """ Specifica class for manage MySql operations """

    def _get_connection(self):
        """ Abtract method to get the connection """

        # We get the configuration
        config = PDAgentMySqlConfiguration()

        # Configuring the connection
        return  pymysql.connect(host=config.mysql_ip, port=config.mysql_port, user=config.mysql_user, passwd=config.mysql_pass, database=config.mysql_db)

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