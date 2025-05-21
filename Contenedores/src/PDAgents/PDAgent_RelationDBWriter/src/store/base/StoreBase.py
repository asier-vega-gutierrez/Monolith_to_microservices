from exceptions.store_exception import StoreException

import threading

class Store():
    """ Class that defines the base of storage connections and so on """

    def __init__(self):
        """ Constructor of the base class """
        self._conn = None
        
    def __enter__(self):
        """ Enter method """
        return self

    def __exit__(self, type_, value, traceback):
        """ Exit method """
        # can test for type and handle different situations
        self.close()

    def _get_connection(self):
        """ Abtract method to get the connection """
        pass

    def connect(self):
        """ Abstract method to get the connection """
        try:
            self._conn = self._get_connection()
        except Exception as e:
            raise StoreException(*e.args, **e.kwargs)
        self._complete = False

    def disconnect(self):
        """ Abstract method to make disconnection"""
        pass

    def commit(self):
        """ Abtract method to make a commit in a transaction """
        pass

    def rollback(self):
        """ Abstract method to  make a rollback """
        pass

    def complete(self):
        """ Mehod to complete """
        self._complete = True

    def close(self):
        """ method to close the connecion """
        if self._conn:
            try:
                if self._complete:
                    self.commit()
                else:
                    self.rollback()
            except Exception as e:
                raise StoreException(*e.args)
            finally:
                try:
                    self.disconnect()
                except Exception as e:
                    raise StoreException(*e.args)