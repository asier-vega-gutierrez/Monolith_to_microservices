from communication.distribution import DataCommunicationManager
from config.configuration import ApplicationConfiguration
from unit.unit_of_work import UnitOfWork
from observable.subscriber.base.observer import ObserverBase

from domain.Alarm import Alarm

from datetime import datetime, timezone
from threading import Thread, Lock
from time import sleep 
from json import dumps 

import random
import json


class PouringAlarmDataWriter(ObserverBase):
    """ Class to manage the Pouring Alarm Load process into Relational storage """

    def __init__(self) -> None:
        """ Default constructor creating all needed elements """

        self._config = ApplicationConfiguration()
        self._communication_manager =  DataCommunicationManager()
        self._unit_of_work = UnitOfWork()
        self._run = False
        self._notify_lock = Lock()        
    
    def start_observe_and_load_data(self):
        """ Method to start to listen to new messages  """

        self._communication_manager.add_observer(f"{self._config.pouring_alarm_topic}", self)

    def stop_observe_and_load_data(self):
        """ Method to stop listen new messages  """
        
        self._communication_manager.remove_observer(f"{self._config.pouring_alarm_topic}", self)

    def notify(self, message):
        """ Method to be called when the message is received """

        # We check the sync between several calls. Enter the lock
        self._notify_lock.acquire()

        print(f"POURING ALARM OBSERVER: message received for pouring.")
        print(message)

        # We deserializae the JSON data
        decoded_data = Alarm(**json.loads(message))
        print(decoded_data)

        # We store the data        
        id = self._unit_of_work.output.pouring_data_rec_store.last_data_rec_id()
        if id is not None:
            self._unit_of_work.output.pouring_alarm_store.add_alarm(decoded_data, id)
        
        # Exiting the lock
        self._notify_lock.release();
    

