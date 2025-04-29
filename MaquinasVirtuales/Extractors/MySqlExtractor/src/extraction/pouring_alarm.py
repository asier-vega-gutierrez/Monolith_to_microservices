from config.configuration import ApplicationConfiguration
from unit.unit_of_work import UnitOfWork
from communication.publisher import data_distribution

from datetime import datetime
from threading import Thread
from time import sleep 
from json import dumps 

import random
import json
import logging


class PouringAlarmExtractor():
    """ Class to manage the Pouring Alarm extraction """

    def __init__(self) -> None:
        """ Defaul contructor creating all needed elements """

        self._config = ApplicationConfiguration()
        '''self._communication_manager =  DataCommunicationManager()'''
        self._unit_of_work = UnitOfWork()
        self._run = False
    
    def start_extract_and_inject_data(self):
        """ Method for extracting and injecting information """
        
        # First of all, we get all the data that we need to inject
        self._data_list = self._unit_of_work.input.alarm_store.get_num_alarms(80)

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
        logging.basicConfig(filename='logs/MySqlExtractor.txt', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

        # Log the provided message at the INFO level
        logging.info(message)

    def _iterate_and_inject(self):
        """ Method to be launched from a Thread with the aim of making the injections  """ 

        data_counter = 0

        # it is running always
        while self._run:
            # we get the alarm and we send it
            data_to_send = self._data_list[data_counter]
            data_counter += 1
            if(data_counter >= len(self._data_list)):
                data_counter = 0
            
            # Adjust data
            data_to_send.time = datetime.now()
            
            print(f"Notify alarm - Tra ID = {data_to_send.tra_id}")
            self.log_info(f"Notify alarm - Tra ID = {data_to_send.tra_id}")
            
            json_data = json.dumps(data_to_send, default=lambda o: str(o) if getattr(o, '__dict__', None) is None else o.__dict__, indent=3, sort_keys=True)
            '''self._communication_manager.data_distribution(self._config.pouring_alarm_topic, json_data)'''
            data_distribution(self._config.pouring_alarm_topic, json_data)

            sleep(30) 

