from store.specific.SensorStore import *
from store.specific.PredictionStore import *

class UnitOfWork():
    """ Class that defined the unit of work """

    def __init__(self) -> None:
        """ Defaul contructor creating all stores """

        self.sensor_store = SensorStore()        
        self.prediction_store = PredictionStore()        