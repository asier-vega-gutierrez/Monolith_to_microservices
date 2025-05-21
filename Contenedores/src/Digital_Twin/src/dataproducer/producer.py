# importing the required libraries  
from kafka import KafkaProducer  
from time import sleep  
from json import dumps 
from domain.Mould import MouldData
from domain.Addition import WaterAdditionData
import json

from config.TwinConfiguration import WaterAdditionConfiguration

def notify_data_using_kafka(data):
    """ Method to produce the information  using kafka """

    # We get the configuration
    config = WaterAdditionConfiguration()

    # We try to connect several times
    print("STARTING to connect to kafka server for notifying pouring data...")
    server_ready = False
    while not server_ready:
        try:
            my_producer = KafkaProducer(
                # Using in a docker image
                bootstrap_servers=[config.kafka_broker], 
                # Using in test without docker
                #bootstrap_servers=['localhost:9092'], 
                value_serializer=lambda v: json.dumps(v).encode('utf-8'),
                key_serializer=lambda v: json.dumps(v).encode('utf-8')
                )
            server_ready = True
            print("KAFKA READY to notify pouring data...")
        except:
            print("KAFKA NOT READY to notify pouring data...")
            print("\tWaiting 5 seconds...")
            sleep(5)
    
    if type(data) is MouldData:
        my_key = {'type': 'mould', 'line': data.cod_linea, 'id': data.id_molde}
        my_topic = config.kafka_mould_for_belts_topic
    elif type(data) is WaterAdditionData:
        my_key = {'type' : 'prediction', 'line' : data.line}
        if data.type == 'DRUM':
            my_topic = f"{config.kafka_water_prediction_drum_topic}_l{data.line}"
        else:
            my_topic = config.kafka_water_prediction_unified_belts_topic
    else:
        my_key = {'type': 'unknown'}
        my_topic = "unknown"
        
    my_data = json.dumps(data.__dict__, indent=3, sort_keys=True, default=str)
   
    my_producer.send(
      my_topic, 
      key= my_key,
      value = my_data)  
    my_producer.flush()