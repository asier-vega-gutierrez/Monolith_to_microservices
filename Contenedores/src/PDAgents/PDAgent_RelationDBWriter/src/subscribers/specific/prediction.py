from subscribers.base.subscriber_base import SubscriberBase
from domain.addition import WaterAdditionData
import json

class PredictionSubscriber(SubscriberBase):
    """ Class for managing information from pouring data  """

    def __init__(self, delegate_function_to_process):
        """ Constructor of the class """
        
        # We assign the function to call when a new data is recived
        self._delegate_process_function = delegate_function_to_process

    def notify(self, message):
        """ Method to be called when the message is received """
        
        print("PREDICTION SUBSCRIBER: message received with key %s" % message.key )
        print(message.value)

        # We have to detect the type of message that we have
        key = message.key
        if str(key["type"]).upper() == "PREDICTION":
            self._process_prediction_data(message)
        else:
            print("UNKNOW status message detected. Please, watch it and manage it...")
            print("key: {}".format(message.key))
            print("data: {}".format(message.value)) 
        
    def _process_prediction_data(self, message):
        """ Method to process alarm data """

        # We deserializae the JSON data
        decoded_prediction_data = WaterAdditionData(**json.loads(message.value))
        print(decoded_prediction_data)

        # We call the function to make the work
        self._delegate_process_function(decoded_prediction_data)



    