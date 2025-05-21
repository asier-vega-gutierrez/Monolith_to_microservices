from subscribers.base.subscriber_base import SubscriberBase
from domain.alarm import PouringAlarmData
from domain.models import PouringArchiveModelsData
from domain.pouring import PouringDataRecData

import json

class PouringSubscriber(SubscriberBase):
    """ Class for managing information from pouring data  """

    def __init__(self, delegate_function_to_process):
        """ Constructor of the class """
        
        # We assign the function to call when a new data is recived
        self._delegate_process_function = delegate_function_to_process

    def notify(self, message):
        """ Method to be called when the message is received """
        
        print("POURING SUBSCRIBER: message received with key %s" % message.key )
        print(message.value)

        # We have to detect the type of message that we have
        key = message.key
        
        if str(key["type"]).upper() == "ALARM":
            self._process_pouring_alarm_data(message)
        elif str(key["type"]).upper() == "DATA_REC":
            self._process_pouring_data_rec_data(message)
        elif str(key["type"]).upper() == "ARCHIVE_MODELS":
            self._process_pouring_archive_model_data(message)
        else:
            print("UNKNOW status message detected. Please, watch it and manage it...")
            print("key: {}".format(message.key))
            print("data: {}".format(message.value)) 
        
    def _process_pouring_alarm_data(self, message):
        """ Method to process alarm data """

        # We deserializae the JSON data
        decoded_alarm_data = PouringAlarmData(**json.loads(message.value))
        print(decoded_alarm_data)

        # We call the function to make the work
        self._delegate_process_function(decoded_alarm_data)

    def _process_pouring_archive_model_data(self, message):
        """ Method to process archive model data """

        # We deserializae the JSON data
        decoded_archive_model_data = PouringArchiveModelsData(**json.loads(message.value))
        print(decoded_archive_model_data)

        # We call the function to make the work
        self._delegate_process_function(decoded_archive_model_data)
    
    def _process_pouring_data_rec_data(self, message):
        """ Method to process data rec data """

        # We deserializae the JSON data
        decoded_data_rec_data = PouringDataRecData(**json.loads(message.value))
        print(decoded_data_rec_data)

        # We call the function to make the work
        self._delegate_process_function(decoded_data_rec_data)



    