from communication.distribution import DataCommunicationManager
from config.configuration import ApplicationConfiguration
from unit.unit_of_work import UnitOfWork
from observable.subscriber.base.observer import ObserverBase

from domain.Mould import MouldData

from datetime import datetime, timezone
from threading import Thread, Lock
from time import sleep 
from json import dumps 

import random
import json


class MouldDataWriter(ObserverBase):
    """ Class to manage the Mould Load process into Relational storage """

    def __init__(self, line:int) -> None:
        """ Default constructor creating all needed elements """

        self._config = ApplicationConfiguration()
        self._communication_manager =  DataCommunicationManager()
        self._unit_of_work = UnitOfWork()
        self._run = False
        self._line = line
        self._notify_lock = Lock()         
    
    def start_observe_and_load_data(self):
        """ Method to start to listen to new messages  """

        self._communication_manager.add_observer(f"{self._config.mould_data_topic}_l{self._line}", self)

    def stop_observe_and_load_data(self):
        """ Method to stop listen new messages  """
        
        self._communication_manager.remove_observer(f"{self._config.mould_data_topic}_l{self._line}", self)

    def notify(self, message):
        """ Method to be called when the message is received """

        # We check the sync between several calls. Enter the lock
        self._notify_lock.acquire()

        print(f"MOULD DATA OBSERVER: message received for line {self._line}")
        print(message)

        # We deserializae the JSON data
        decoded_data = MouldData(**json.loads(message))
        print(decoded_data)

        # We store the data into the relational store (making the relation to the chemical composition)
        chemical_composition_data, chemical_composition_id = self._unit_of_work.output.chemical_composition_store.get_last_chemical_composition()
        pouring_id = self._unit_of_work.output.pouring_data_rec_store.last_data_rec_id()

        self._unit_of_work.output.mould_store.add_mould_data(decoded_data, chemical_composition_id, pouring_id)
        
        # Exiting the lock
        self._notify_lock.release();
    

