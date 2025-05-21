# importing the required libraries  
from kafka import KafkaProducer  
from time import sleep  
from json import dumps 
from domain.Mould import MouldData
from domain.Sensor import SensorData
import json

from config.configuration import PDAgentSqlServerReaderConfig

def notify_data_using_kafka(data):
    """ Method to produce the information  using kafka """

    # We get the configuration
    config = PDAgentSqlServerReaderConfig()

    # We try to connect several times
    print("STARTING to connect to kafka server for notifying pouring data...")
    server_ready = False
    while not server_ready:
        try:
            print(f"Trying to communicate to {config.kafka_broker} broker...")
            my_producer = KafkaProducer(
                bootstrap_servers=[config.kafka_broker], 
                value_serializer=lambda v: json.dumps(v).encode('utf-8'),
                key_serializer=lambda v: json.dumps(v).encode('utf-8')
                )
            server_ready = True
            print("KAFKA READY to notify SQL Server data...")
        except:
            print("KAFKA NOT READY to SQL Server data...")
            print("\tWaiting 5 seconds...")
            sleep(5)
    
    print("Checking time...")
    if type(data) is MouldData:
        my_key = {'type': 'mould', 'line': data.cod_linea, 'id': data.id_molde}
        my_topic = f"{config.kafka_mould_data_topic}_l{data.cod_linea}"
    elif type(data)  is SensorData:
        my_key = {'type': 'sensor', 'line': data.line}
        my_topic = f"{config.kafka_sensor_data_topic}_l{data.line}"
    else:
        my_key = {'type': 'unknown'}
        my_topic = "unknown"
        
    my_data = json.dumps(data.__dict__, indent=3, sort_keys=True, default=str)
   
    print("Trying to send: {}".format(my_key))
    my_producer.send(
      my_topic, 
      key= my_key,
      value = my_data)  
    my_producer.flush()
    print("DATA {} sent via kafka".format(my_key))