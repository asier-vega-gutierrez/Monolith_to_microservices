# Importing the required libraries  
import json
from json import dumps
from time import sleep

from kafka import KafkaProducer

def produce_msg(topic, data, id):
   # Creating a kafka producer connected to the server
   my_producer = KafkaProducer(
      bootstrap_servers=['localhost:29092'], 
      value_serializer=lambda v: json.dumps(v).encode('utf-8'),
      key_serializer=lambda v: json.dumps(v).encode('utf-8')
   )

   my_topic = topic  # Topic of the message
   my_key = {'id': id} # Key value for the message
   my_data = data  # Data value for the message
   
   my_producer.send(
      my_topic, 
      key= my_key,
      value = my_data)  
   my_producer.flush()
