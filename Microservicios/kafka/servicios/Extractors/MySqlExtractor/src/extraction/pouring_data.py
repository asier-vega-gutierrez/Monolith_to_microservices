from config.configuration import ApplicationConfiguration
from unit.unit_of_work import UnitOfWork
from communication.producer import produce_msg
from communication.topics import create_topic

from datetime import datetime
from threading import Thread
from time import sleep 
from json import dumps 

import random
import json
import logging


class PouringDataExtractor():
    """ Class to manage the Pouring Data extraction  """

    def __init__(self) -> None:
        """ Defaul contructor creating all needed elements """

        self._config = ApplicationConfiguration()
        '''self._communication_manager =  DataCommunicationManager()'''
        self._unit_of_work = UnitOfWork()
        self._run = False
    
    def start_extract_and_inject_data(self):
        """ Method for extracting and injecting information """
        
        # First of all, we get all the data that we need to inject
        self._data_list = self._unit_of_work.input.data_rec_store.get_data_recs()

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

        # Create topic in kafka
        create_topic(self._config.pouring_data_topic)

        # it is running always
        while self._run:
            # we get the alarm and we send it
            data_to_send = self._data_list[data_counter]
            data_counter += 1
            if(data_counter >= len(self._data_list)):
                data_counter = 0
            
            # Adjust data
            data_to_send.time = datetime.now()
            if data_to_send.model_code is not None:
                data_to_send.archive_model_data = self._unit_of_work.input.archive_model_store.get_archive_model_by_code(data_to_send.model_code)

            
            print(f"Notify data rec - Pouring Mould = {data_to_send.nr_pouring_mould}")
            self.log_info(f"Notify data rec - Pouring Mould = {data_to_send.nr_pouring_mould}")
            
            json_data = json.dumps(data_to_send, default=lambda o: str(o) if getattr(o, '__dict__', None) is None else o.__dict__, indent=3, sort_keys=True)
            produce_msg(self._config.pouring_data_topic, json_data, data_to_send.nr_pouring_mould)

            # We wait 7 senconds to simulate the real world
            sleep(7) 

