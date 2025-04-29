# Importing the required libraries  
import json
from json import dumps
from time import sleep

from kafka import KafkaProducer

# Creating a kafka producer connected to the server
my_producer = KafkaProducer(
   bootstrap_servers=['localhost:29092'], 
   value_serializer=lambda v: json.dumps(v).encode('utf-8'),
   key_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# range for sending values
for n in range(5000):
   my_topic = 'hello_world_demo'  # Topic of the message
   my_key = {'id': 1} # Key value for the message
   my_data = {'num' : n}  # Data value for the message
   my_producer.send(
      my_topic, 
      key= my_key,
      value = my_data)  
   my_producer.flush()
   sleep(5)  