from communication.distribution import DataCommunicationManager
from config.configuration import ApplicationConfiguration
from unit.unit_of_work import UnitOfWork

from datetime import datetime
from threading import Thread
from time import sleep 
from json import dumps 

import random
import json


class ChemicalCompositionExtractor():
    """ Class to manage the Chemical Composition extraction """

    def __init__(self) -> None:
        """ Defaul contructor creating all needed elements """

        self._config = ApplicationConfiguration()
        self._communication_manager =  DataCommunicationManager()
        self._unit_of_work = UnitOfWork()
        self._run = False
    
    def start_extract_and_inject_data(self):
        """ Method for extracting and injecting information """
        
        # First of all, we get all the data that we need to inject
        self._chemical_compositions = self._unit_of_work.input.chemical_composition_store.get_chemical_compistions()

        # If we have chemical compositions, we do the extraction and injection work
        if any(self._chemical_compositions):
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

        chemical_composition_counter = 0

        # it is running always
        while self._run:
            # we get the alarm and we send it
            chemical_composition_to_send = self._chemical_compositions[chemical_composition_counter]
            chemical_composition_counter += 1
            if(chemical_composition_counter >= len(self._chemical_compositions)):
                chemical_composition_counter = 0
            
            # Adjust data
            chemical_composition_to_send.date = datetime.now()
            
            print(f"Notify chemical composition - ID = {chemical_composition_to_send.id}")
            
            json_data = json.dumps(chemical_composition_to_send, default=lambda o: str(o) if getattr(o, '__dict__', None) is None else o.__dict__, indent=3, sort_keys=True)
            self._communication_manager.data_distribution(self._config.chemical_composition_topic,
                                                          json_data)

            time_for_next = random.randint(60, 120)
            print(f"Time waiting to next chemical composition message: {time_for_next} s.")
            sleep(time_for_next) 

