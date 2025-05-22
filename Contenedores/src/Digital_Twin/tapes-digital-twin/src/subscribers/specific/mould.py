from subscribers.base.subscriber_base import SubscriberBase
from domain.Mould import MouldData
import json

class MouldSubscriber(SubscriberBase):
    """ Class for managing information from moulds  """

    def __init__(self, delegate_function_to_process):
        """ Constructor of the class """
        
        # We assign the function to call when a new data is recived
        self._delegate_process_function = delegate_function_to_process

    def notify(self, message):
        """ Method to be called when the message is received """
        
        print("MOULD SUBSCRIBER: message received with key %s" % message.key )
        print(message.value)

        # We have to detect the type of message that we have
        key = message.key
        if str(key["type"]).upper() == "MOULD":
            self._process_mould_data(message)
        else:
            print("UNKNOW mould message detected. Please, watch it and manage it...")
            print("key: {}".format(message.key))
            print("data: {}".format(message.value))            

    
    def _process_mould_data(self, message):
        """ Method to process alarm data """

        # We deserializae the JSON data
        decoded_mould_data = MouldData(**json.loads(message.value))
        print(decoded_mould_data)

        # We call the function to make the work
        self._delegate_process_function(decoded_mould_data)
