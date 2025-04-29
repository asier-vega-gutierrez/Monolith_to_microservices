from communication.distribution import DataCommunicationManager
from config.configuration import ApplicationConfiguration
from unit.unit_of_work import UnitOfWork

from datetime import datetime, timezone
from threading import Thread
from time import sleep 
from json import dumps 

import random
import json


class MouldDataExtractor():
    """ Class to manage the Mould Data extraction for a given line ID """

    def __init__(self, line:int) -> None:
        """ Defaul contructor creating all needed elements """

        self._config = ApplicationConfiguration()
        self._communication_manager =  DataCommunicationManager()
        self._unit_of_work = UnitOfWork()
        self._run = False
        self._line = line 
    
    def start_extract_and_inject_data(self):
        """ Method for extracting and injecting information """
        
        # First of all, we get all the data that we need to inject
        self._data_list = self._unit_of_work.input.mould_store.get_line_mould(self._line)

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
            
            print(f"Notify mould data - Line = {self._line} Ref = {data_to_send.reference}")   
            
            json_data = json.dumps(data_to_send.__dict__, indent=3, sort_keys=True, default=str)
            self._communication_manager.data_distribution(f"{self._config.mould_data_topic}_l{self._line}",
                                                          json_data)
            
            # We wait 7 senconds to simulate the real world
            sleep(7) 

