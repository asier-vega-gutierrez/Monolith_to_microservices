from dataconsumer.consumer import MUCSIConsumer
from threading import Thread
from subscribers.specific.sensor import SensorSubscriber
from subscribers.specific.chemical_composition import ChemicalCompositionSubscriber
from subscribers.specific.prediction import PredictionSubscriber
from subscribers.specific.pouring import PouringSubscriber
from subscribers.specific.mould import MouldSubscriber

from domain.pouring import PouringDataRecData
from domain.models import PouringArchiveModelsData
from domain.alarm import PouringAlarmData

from unit.unit_of_work import UnitOfWork

from config.configuration import PDAgentRelationDBWriterConfiguration

import json

import threading

class RelationalRecordingWorker:
    """ Class that represents the digital twin for water addition """

    def __init__(self) -> None:
        """ Constructor of the class """               

        # We create the object to manage data events
        self._data_consumer = MUCSIConsumer()

        # We create the unit of work
        self._unit_of_work = UnitOfWork()

        # we create lock for process
        self._sensor_lock = threading.Lock() 
        self._chemical_composition_lock = threading.Lock() 
        self._prediction_lock = threading.Lock()
        self._pouring_lock = threading.Lock()
        self._mould_lock = threading.Lock()
    
    def start_recording(self):
        """ Method to process all events in the plant """
   
        # We get the configuration 
        config = PDAgentRelationDBWriterConfiguration()

        # We configure the subscriptions        
        self._data_consumer.add_subscriber(f"{config.kafka_sensor_data_topic}l1", SensorSubscriber(self.store_sensor_data))     
        self._data_consumer.add_subscriber(f"{config.kafka_sensor_data_topic}l2", SensorSubscriber(self.store_sensor_data))        
        self._data_consumer.add_subscriber(f"{config.kafka_chemical_composition_topic}", ChemicalCompositionSubscriber(self.store_chemical_composition_data))        
        self._data_consumer.add_subscriber(f"{config.kafka_waterprediction_drum_data_topic}l1", PredictionSubscriber(self.store_prediction))        
        self._data_consumer.add_subscriber(f"{config.kafka_waterprediction_drum_data_topic}l2", PredictionSubscriber(self.store_prediction))        
        self._data_consumer.add_subscriber(f"{config.kafka_waterprediction_belt_data_topic}", PredictionSubscriber(self.store_prediction))        
        self._data_consumer.add_subscriber(f"{config.kafka_pouring_data_topic}", PouringSubscriber(self.manage_pouring_info))    
        self._data_consumer.add_subscriber(f"{config.kafka_mould_data_topic}l1", MouldSubscriber(self.store_mould_data))    
        self._data_consumer.add_subscriber(f"{config.kafka_mould_data_topic}l2", MouldSubscriber(self.store_mould_data))    
        

        # We launch the reading process
        t1 = Thread(target=self._data_consumer.start_listening_messages)
        t1.start()
        t1.join()
    
    def store_sensor_data(self, sensor_data):
        """ Method to update the value of the sensors (the current status of the plant) """
        self._sensor_lock.acquire()

        self._unit_of_work.sensor_store.add_sensor(sensor_data)

        self._sensor_lock.release();
    
    def store_chemical_composition_data(self, chemical_composition_data):
        """ Method to store the value of the chemical composition data """

        self._chemical_composition_lock.acquire()

        self._unit_of_work.chemical_composition_store.add_chemical_composition(chemical_composition_data)
    
        self._chemical_composition_lock.release()

    def store_prediction(self, prediction_data):
        """ Method to store the prediction data """

        self._prediction_lock.acquire()

        self._unit_of_work.prediction_store.add_prediction(prediction_data)

        self._prediction_lock.release()

    def manage_pouring_info(self, pouring_data):
        """ Method to store the prediction data """

        self._pouring_lock.acquire()

        # For alarms
        if isinstance(pouring_data, PouringAlarmData):
            id = self._unit_of_work.pouring_data_rec_store.last_data_rec_id()
            if id is not None:
                self._unit_of_work.pouring_alarm_store.add_alarm(pouring_data, id)
        # For Archive Models
        elif isinstance(pouring_data, PouringArchiveModelsData):
            if not self._unit_of_work.pouring_archive_model_store.exists_archive_model(pouring_data.id):
                self._unit_of_work.pouring_archive_model_store.add_archive_model(pouring_data)
        
        # For Data Rec
        elif isinstance(pouring_data, PouringDataRecData): 
            model_json = json.dumps(pouring_data.archive_model_data)
            model = PouringArchiveModelsData(**json.loads(model_json))

            if not self._unit_of_work.pouring_archive_model_store.exists_archive_model(model.id):

                self._unit_of_work.pouring_archive_model_store.add_archive_model(model)
            
            self._unit_of_work.pouring_data_rec_store.add_pouring_data_rec(pouring_data, model.id)
        
        else:
            print('ERROR: Pourng Data not defined in the software.')
        
        self._pouring_lock.release()

    def store_mould_data(self, mould_data):
        """ Method to store mould data """

        self._mould_lock.acquire()

        chemical_composition_data, chemical_composition_id = self._unit_of_work.chemical_composition_store.get_last_chemical_composition()
        pouring_id = self._unit_of_work.pouring_data_rec_store.last_data_rec_id()

        self._unit_of_work.mould_store.add_mould_data(mould_data, chemical_composition_id, pouring_id)

        self._mould_lock.release()
    
    