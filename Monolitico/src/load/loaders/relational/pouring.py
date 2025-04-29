from communication.distribution import DataCommunicationManager
from config.configuration import ApplicationConfiguration
from unit.unit_of_work import UnitOfWork
from observable.subscriber.base.observer import ObserverBase

from domain.Pouring import PouringDataRecData
from domain.Models import PouringArchiveModelsData

from datetime import datetime, timezone
from threading import Thread, Lock
from time import sleep 
from json import dumps 

import random
import json


class PouringDataRecWriter(ObserverBase):
    """ Class to manage the Pouring Data Load process into Relational storage """

    def __init__(self) -> None:
        """ Default constructor creating all needed elements """

        self._config = ApplicationConfiguration()
        self._communication_manager =  DataCommunicationManager()
        self._unit_of_work = UnitOfWork()
        self._run = False
        self._notify_lock = Lock() 
    
    def start_observe_and_load_data(self):
        """ Method to start to listen to new messages  """

        self._communication_manager.add_observer(f"{self._config.pouring_data_topic}", self)

    def stop_observe_and_load_data(self):
        """ Method to stop listen new messages  """
        
        self._communication_manager.remove_observer(f"{self._config.pouring_data_topic}", self)

    def notify(self, message):
        """ Method to be called when the message is received """

        # We check the sync between several calls. Enter the lock
        self._notify_lock.acquire()

        print(f"POURING OBSERVER: message received for pouring.")
        print(message)

        # We deserializae the JSON data
        decoded_data = PouringDataRecData(**json.loads(message))
        print(decoded_data)

        # We store the data
        model_json = json.dumps(decoded_data.archive_model_data)
        model = PouringArchiveModelsData(**json.loads(model_json))

        if not self._unit_of_work.output.pouring_archive_model_store.exists_archive_model(model.id):
            self._unit_of_work.pouring_archive_model_store.add_archive_model(model)
        
        self._unit_of_work.output.pouring_data_rec_store.add_pouring_data_rec(decoded_data, model.id)

        
        # Exiting the lock
        self._notify_lock.release();
    

