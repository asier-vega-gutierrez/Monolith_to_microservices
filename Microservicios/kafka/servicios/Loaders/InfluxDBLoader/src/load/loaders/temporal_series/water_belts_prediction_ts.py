from config.configuration import ApplicationConfiguration
from unit.unit_of_work import UnitOfWork

from communication.base.subscriber_base import SubscriberBase
from communication.consumer import Consumer

from domain.Addition import WaterAdditionData

from datetime import datetime, timezone
from threading import Thread, Lock
from time import sleep 
from json import dumps 
import logging

import random
import json


class WaterBeltsPredictionTemporalSeriesWriter(SubscriberBase):
    """ Class to manage the Water Prediction for Belts Load process into Tempral Series storage """

    def __init__(self) -> None:
        """ Defaul contructor creating all needed elements """

        self._config = ApplicationConfiguration()
        '''self._communication_manager =  DataCommunicationManager()'''
        self._communication_manager = Consumer()
        self._unit_of_work = UnitOfWork()
        self._run = False
        self._notify_lock = Lock() 
    
    def start_observe_and_load_data(self):
        """ Method to start to listen to new messages  """

        self._communication_manager.add_subscriber(f"{self._config.water_prediction_unified_belts_topic}", self)

    def stop_observe_and_load_data(self):
        """ Method to stop listen new messages  """
        
        self._communication_manager.remove_subscriber(f"{self._config.water_prediction_unified_belts_topic}", self)

    def log_info(self, message):
        # Configure the logging system (you can customize this based on your needs)
        logging.basicConfig(filename='logs/InfluxDBLoader.txt', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

        # Log the provided message at the INFO level
        logging.info(message)

    def notify(self, message):
        """ Method to be called when the message is received """

        # We check the sync between several calls. Enter the lock
        self._notify_lock.acquire()

        print(f"PREDICTION OBSERVER (Temporal Series): message received for belts.")
        print(message)
        self.log_info(f"PREDICTION OBSERVER (Temporal Series): message received for belts.")
        self.log_info(message)

        # We deserializae the JSON data
        decoded_data = WaterAdditionData(**json.loads(message))
        print(decoded_data)

        # We store the data        
        data = self._unit_of_work.output.prediction_store_ts.add_prediction(decoded_data)
        
        # Exiting the lock
        self._notify_lock.release();
    

