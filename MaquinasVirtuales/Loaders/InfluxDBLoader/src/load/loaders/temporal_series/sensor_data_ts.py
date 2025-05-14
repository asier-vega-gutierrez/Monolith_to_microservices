from config.configuration import ApplicationConfiguration
from unit.unit_of_work import UnitOfWork

from communication.base.subscriber_base import SubscriberBase
from communication.consumer import Consumer

from domain.Sensor import SensorData

from datetime import datetime, timezone
from threading import Thread, Lock
from time import sleep 
from json import dumps 
import logging

import random
import json


class SensorDataTemporalSeriesWriter(SubscriberBase):
    """ Class to manage the Sensor Data Load process into Temporal Series storage """

    def __init__(self, line:int) -> None:
        """ Default constructor creating all needed elements """

        self._config = ApplicationConfiguration()
        '''self._communication_manager =  DataCommunicationManager()'''
        self._communication_manager = Consumer()
        self._unit_of_work = UnitOfWork()
        self._run = False
        self._line = line
        self._notify_lock = Lock() 
    
    def start_observe_and_load_data(self):
        """ Method to start to listen to new messages  """

        self._communication_manager.add_subscriber(f"{self._config.sensor_data_topic}_l{self._line}", self)

    def stop_observe_and_load_data(self):
        """ Method to stop listen new messages  """
        
        self._communication_manager.remove_subscriber(f"{self._config.sensor_data_topic}_l{self._line}", self)

    def log_info(self, message):
        # Configure the logging system (you can customize this based on your needs)
        logging.basicConfig(filename='logs/InfluxDBLoader.txt', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

        # Log the provided message at the INFO level
        logging.info(message)

    def notify(self, message):
        """ Method to be called when the message is received """

        # We check the sync between several calls. Enter the lock
        self._notify_lock.acquire()


        print(f"SENSORS OBSERVER (Temporal Series): message received for line {self._line}")
        print(message)
        self.log_info(f"SENSORS OBSERVER (Temporal Series): message received for line {self._line}")
        self.log_info(message)

        # We deserializae the JSON data
        decoded_sensor_data = SensorData(**json.loads(message))
        print(decoded_sensor_data)

        # We store the data into the temporal series sensor store 
        data = self._unit_of_work.output.sensor_store_ts.add_sensor(decoded_sensor_data)
        
        # Exiting the lock
        self._notify_lock.release();
    

