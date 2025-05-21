# importing the required libraries  
from kafka import KafkaProducer  
from time import sleep  
from json import dumps 
from domain.Alarm import Alarm
from domain.DataRec import DataRec
from domain.ArchiveModels import ArchiveModels
from config.configuration import PDAgentMySqlConfiguration
import json

def notify_pouring_using_kafka(data):
    """ Method to produce the information  using kafka """

    # We get the configuration (it is a singleton)
    config = PDAgentMySqlConfiguration()

    # We try to connect several times
    print("STARTING to connect to kafka server for notifying pouring data...")
    server_ready = False
    while not server_ready:
        try:
            my_producer = KafkaProducer(
                bootstrap_servers=[config.kafka_broker], 
                value_serializer=lambda v: json.dumps(v).encode('utf-8'),
                key_serializer=lambda v: json.dumps(v).encode('utf-8')
                )
            server_ready = True
            print("KAFKA READY to notify pouring data...")
        except:
            print("KAFKA NOT READY to notify pouring data...")
            print("\tWaiting 5 seconds...")
            sleep(5)
    

    # When connection is done, depending of the object, we send our message
    if type(data) is Alarm:
        my_key = {'type': 'alarm', 'id': data.tra_id}
    elif type(data)  is DataRec:
        my_key = {'type': 'data_rec', 'id': data.nr_pouring_mould}
    elif type(data)  is ArchiveModels:
        my_key = {'type': 'archive_models', 'id': data.model_code}
    else:
        my_key = {'type': 'unknown'}
      
    my_data = json.dumps(data, default=lambda o: str(o) if getattr(o, '__dict__', None) is None else o.__dict__, indent=3, sort_keys=True)

    # Sending data using kafka
    my_producer.send(
      config.kafka_mysql_data_topic, 
      key= my_key,
      value = my_data)  
    my_producer.flush()