from config.configuration import ApplicationConfiguration
from unit.unit_of_work import UnitOfWork
from communication.publisher import data_distribution

from datetime import datetime, timezone
from threading import Thread
from time import sleep 
from json import dumps 

import random
import json
import logging


class SensorDataExtractor():
    """ Class to manage the Sensor Data extraction """

    def __init__(self) -> None:
        """ Defaul contructor creating all needed elements """

        self._config = ApplicationConfiguration()
        '''self._communication_manager =  DataCommunicationManager()'''
        self._unit_of_work = UnitOfWork()
        self._run = False
    
    def start_extract_and_inject_data(self):
        """ Method for extracting and injecting information """
        
        # First of all, we get all the data that we need to inject
        self._data_list = self._unit_of_work.input.sensor_store.get_sensors_data()

        # If we have chemical compositions, we do the extraction and injection work
        if any(self._data_list):
            # We put t0he boolean variable to true (iterate during the thread)
            self._run = True

            # We start a thread with the iteration and injection process
            extraction_and_injection_thread = Thread(target=self._iterate_and_inject)
            extraction_and_injection_thread.start()

    def stop_extract_and_inject_data(self):
        """ Method for stoping the injection process """
        self._run = False

    
    def log_info(self, message):
        # Configure the logging system (you can customize this based on your needs)
        logging.basicConfig(filename='logs/SqlServerExtractor.txt', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

        # Log the provided message at the INFO level
        logging.info(message)

    def _iterate_and_inject(self):
        """ Method to be launched from a Thread with the aim of making the injections  """ 

        data_counter = 0

        # it is running always
        while self._run:
            # we get the alarm and we send it
            data_to_send_l1 = self._data_list[data_counter][0]
            data_to_send_l2 = self._data_list[data_counter][1]
            data_counter += 1
            if(data_counter >= len(self._data_list)):
                data_counter = 0
            
            # Adjust data
            data_to_send_l1.timestamp = datetime.now(timezone.utc)
            data_to_send_l2.timestamp = datetime.now(timezone.utc)
            
            print("Notify sensor L1 - Timestamp = {}".format(data_to_send_l1.timestamp))
            self.log_info("Notify sensor L1 - Timestamp = {}".format(data_to_send_l1.timestamp))    
            
            json_data_l1 = json.dumps(data_to_send_l1.__dict__, indent=3, sort_keys=True, default=str)
            '''self._communication_manager.data_distribution(f"{self._config.sensor_data_topic}_l1", json_data_l1)'''
            data_distribution(f"{self._config.sensor_data_topic}_l1", json_data_l1)

            print("Notify sensor L2 - Timestamp = {}".format(data_to_send_l2.timestamp))
            self.log_info("Notify sensor L2 - Timestamp = {}".format(data_to_send_l2.timestamp))    

            json_data_l2 = json.dumps(data_to_send_l2.__dict__, indent=3, sort_keys=True, default=str)
            '''self._communication_manager.data_distribution(f"{self._config.sensor_data_topic}_l2", json_data_l2)'''
            data_distribution(f"{self._config.sensor_data_topic}_l2", json_data_l2)

            # We wait 7 senconds to simulate the real world
            sleep(7) 

