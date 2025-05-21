from dataconsumer.consumer import MUCSIConsumer
from threading import Thread
from subscribers.specific.sensor import SensorSubscriber
from subscribers.specific.prediction import PredictionSubscriber

from unit.unit_of_work import UnitOfWork

import json

import threading

from config.configuration import PDAgentTemporlSeriesWriterConfiguration

class InfluxDBRecordingWorker:
    """ Class that represents the digital twin for water addition """

    def __init__(self) -> None:
        """ Constructor of the class """               

        # We create the object to manage data events
        self._data_consumer = MUCSIConsumer()

        # We create the unit of work
        self._unit_of_work = UnitOfWork()

        # we create lock for process
        self._sensor_lock = threading.Lock() 
        self._prediction_lock = threading.Lock()
    
    def start_recording(self):
        """ Method to process all events in the plant """
   
        # We configure the subscriptions
        config = PDAgentTemporlSeriesWriterConfiguration()
        
        self._data_consumer.add_subscriber(f"{config.kafka_sensor_data_topic}_l1", SensorSubscriber(self.store_sensor_data))     
        self._data_consumer.add_subscriber(f"{config.kafka_sensor_data_topic}_l2", SensorSubscriber(self.store_sensor_data))        
        self._data_consumer.add_subscriber(f"{config.kafka_drum_water_prediction_topic}_l1", PredictionSubscriber(self.store_prediction))        
        self._data_consumer.add_subscriber(f"{config.kafka_drum_water_prediction_topic}_l2", PredictionSubscriber(self.store_prediction))        
        self._data_consumer.add_subscriber(f"{config.kafka_belts_water_prediction_topic}", PredictionSubscriber(self.store_prediction))        
        
        # We launch the reading process
        t1 = Thread(target=self._data_consumer.start_listening_messages)
        t1.start()
        t1.join()
    
    def store_sensor_data(self, sensor_data):
        """ Method to update the value of the sensors (the current status of the plant) """
        self._sensor_lock.acquire()

        data = self._unit_of_work.sensor_store.add_sensor(sensor_data)
        
        self._sensor_lock.release();
       
    def store_prediction(self, prediction_data):
        """ Method to store the prediction data """

        self._prediction_lock.acquire()

        data = self._unit_of_work.prediction_store.add_prediction(prediction_data)
        
        self._prediction_lock.release()    