from store.specific.output.SensorStore import *
from store.specific.output.PredictionStore import * 
from store.specific.output.ChemicalCompositionStore import *
from store.specific.output.PouringAlarm import *
from store.specific.output.PouringAchiveModel import *
from store.specific.output.PouringDataRec import *
from store.specific.output.MouldStore import *

'''from store.specific.output.SensorStoreTemporalSerie import *
from store.specific.output.PredictionStoreTemporalSerie import *'''

class OutputUnitOfWork():
    """ Class that defined the unit of work """

    def __init__(self) -> None:
        """ Default contructor creating all stores """

        # Correlated output storage (Postgres)
        self.sensor_store = SensorStore()
        self.chemical_composition_store = ChemicalCompositionStore()
        self.prediction_store = PredictionStore()
        self.pouring_alarm_store = PouringAlarmStore()
        self.pouring_archive_model_store = PouringArchiveModelStore()
        self.pouring_data_rec_store = PouringDataRecStore()
        self.mould_store = MouldStore()  

        '''# Temporal series output (InfluxDB)  
        self.sensor_store_ts = SensorStoreTS()        
        self.prediction_store_ts = PredictionStoreTS()'''        