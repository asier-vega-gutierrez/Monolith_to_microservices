from config.configuration import ApplicationConfiguration
from unit.unit_of_work import UnitOfWork

from communication.base.subscriber_base import SubscriberBase
from communication.consumer import Consumer

from domain.Alarm import Alarm

from datetime import datetime, timezone
from threading import Thread, Lock
from time import sleep 
from json import dumps 
import logging

import random
import json


class PouringAlarmDataWriter(SubscriberBase):
    """ Class to manage the Pouring Alarm Load process into Relational storage """

    def __init__(self) -> None:
        """ Default constructor creating all needed elements """

        self._config = ApplicationConfiguration()
        '''self._communication_manager =  DataCommunicationManager()'''
        self._communication_manager = Consumer()
        self._unit_of_work = UnitOfWork()
        self._run = False
        self._notify_lock = Lock()        
    
    def start_observe_and_load_data(self):
        """ Method to start to listen to new messages  """

        self._communication_manager.add_subscriber(f"{self._config.pouring_alarm_topic}", self)

    def stop_observe_and_load_data(self):
        """ Method to stop listen new messages  """
        
        self._communication_manager.remove_subscriber(f"{self._config.pouring_alarm_topic}", self)

    def log_info(self, message):
        # Configure the logging system (you can customize this based on your needs)
        logging.basicConfig(filename='logs/PostgresLoader.txt', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

        # Log the provided message at the INFO level
        logging.info(message)

    def notify(self, message):
        """ Method to be called when the message is received """

        # We check the sync between several calls. Enter the lock
        self._notify_lock.acquire()

        print(f"POURING ALARM OBSERVER: message received for pouring.")
        print(message)
        self.log_info(f"POURING ALARM OBSERVER: message received for pouring.")
        self.log_info(message)

        # We deserializae the JSON data
        decoded_data = Alarm(**json.loads(message))
        print(decoded_data)

        # We store the data        
        id = self._unit_of_work.output.pouring_data_rec_store.last_data_rec_id()
        if id is not None:
            self._unit_of_work.output.pouring_alarm_store.add_alarm(decoded_data, id)
        
        # Exiting the lock
        self._notify_lock.release();
    

