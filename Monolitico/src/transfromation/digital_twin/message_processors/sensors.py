from observable.subscriber.base.observer import ObserverBase

from domain.Sensor import SensorData

import json

class SensorMessageProcessor(ObserverBase):
    """ Class to process Sensors Messages in the Virtual Twin """

    def __init__(self,
                 virtual_twin_delegate_function) -> None:
        """ Constructor of the class """

        self._virtual_twin_delegate_function = virtual_twin_delegate_function

    def notify(self, message):
        """ Method to be called when the message is received """
        
        print("SENSORS OBSERVER AT DIGITAL TWIN: message received.")
        print(message)

        # We deserializae the JSON data
        decoded_sensor_data = SensorData(**json.loads(message))
        print(decoded_sensor_data)

        # We call the function to make the work
        self._virtual_twin_delegate_function(decoded_sensor_data)