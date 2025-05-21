# importing the required libraries  
from kafka import KafkaProducer  
from time import sleep  
from json import dumps 
from domain.chemical import ChemicalComposition
import json

from config.configuration import CapturerConfiguration

def notify_chemical_composition_using_kafka(data):
    """ Method to produce the information  using kafka """

    # We get the configuration
    config = CapturerConfiguration()

    # We try to connect several times
    print("STARTING to connect to kafka server for notifying pouring data...")
    server_ready = False
    while not server_ready:
        try:
            my_producer = KafkaProducer(
                bootstrap_servers=[f'{config.kafka_broker}'],                 
                value_serializer=lambda v: json.dumps(v).encode('utf-8'),
                key_serializer=lambda v: json.dumps(v).encode('utf-8')
                )
            server_ready = True
            print("KAFKA READY to notify pouring data...")
        except:
            print("KAFKA NOT READY to notify pouring data...")
            print("\tWaiting 5 seconds...")
            sleep(5)
    
    if type(data) is ChemicalComposition:
        my_key = {'type': 'chemical_composition', 'id': data.id}   
    else:
        my_key = {'type': 'unknown'}
        
    my_data = json.dumps(data, default=lambda o: str(o) if getattr(o, '__dict__', None) is None else o.__dict__, indent=3, sort_keys=True)
   
    my_producer.send(
      config.kafka_chemical_composition_topic, 
      key= my_key,
      value = my_data)  
    my_producer.flush()