from observable.subscriber.base.observer import ObserverBase

from domain.Mould import MouldData

import json

class MouldMessageProcessor(ObserverBase):
    """ Class to process Moulds Messages in the Virtual Twin """

    def __init__(self,
                 virtual_twin_delegate_function) -> None:
        """ Constructor of the class """

        self._virtual_twin_delegate_function = virtual_twin_delegate_function

    def notify(self, message):
        """ Method to be called when the message is received """
        
        print("MOULD OBSERVER AT DIGITAL TWIN: message received.")
        print(message)

        # We deserializae the JSON data
        decoded_mould_data = MouldData(**json.loads(message))
        print(decoded_mould_data)

        # We call the function to make the work
        self._virtual_twin_delegate_function(decoded_mould_data)
