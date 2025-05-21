from store.specific.SensorStore import *
from store.specific.ChemicalCompositionStore import *
from store.specific.PredictionStore import *
from store.specific.PouringAlarm import *
from store.specific.PouringAchiveModel import *
from store.specific.PouringDataRec import *
from store.specific.MouldStore import *

class UnitOfWork():
    """ Class that defined the unit of work """

    def __init__(self) -> None:
        """ Defaul contructor creating all stores """

        self.sensor_store = SensorStore()
        self.chemical_composition_store = ChemicalCompositionStore()
        self.prediction_store = PredictionStore()
        self.pouring_alarm_store = PouringAlarmStore()
        self.pouring_archive_model_store = PouringArchiveModelStore()
        self.pouring_data_rec_store = PouringDataRecStore()
        self.mould_store = MouldStore()