from communication.distribution import DataCommunicationManager
from config.configuration import ApplicationConfiguration
from unit.unit_of_work import UnitOfWork
from observable.subscriber.base.observer import ObserverBase

from domain.Addition import WaterAdditionData

from datetime import datetime, timezone
from threading import Thread, Lock
from time import sleep 
from json import dumps 

import random
import json


class WaterBeltsDataPredictionWriter(ObserverBase):
    """ Class to manage the Water Prediction for Belts Load process into Relational storage """

    def __init__(self) -> None:
        """ Default constructor creating all needed elements """

        self._config = ApplicationConfiguration()
        self._communication_manager =  DataCommunicationManager()
        self._unit_of_work = UnitOfWork()
        self._run = False
        self._notify_lock = Lock()        
    
    def start_observe_and_load_data(self):
        """ Method to start to listen to new messages  """

        self._communication_manager.add_observer(f"{self._config.water_prediction_unified_belts_topic}", self)

    def stop_observe_and_load_data(self):
        """ Method to stop listen new messages  """
        
        self._communication_manager.remove_observer(f"{self._config.water_prediction_unified_belts_topic}", self)

    def notify(self, message):
        """ Method to be called when the message is received """

        # We check the sync between several calls. Enter the lock
        self._notify_lock.acquire()

        print(f"PREDICTION OBSERVER: message received for belts.")
        print(message)

        # We deserializae the JSON data
        decoded_data = WaterAdditionData(**json.loads(message))
        print(decoded_data)

        # We store the data        
        data = self._unit_of_work.output.prediction_store.add_prediction(decoded_data)
        
        # Exiting the lock
        self._notify_lock.release();
    

