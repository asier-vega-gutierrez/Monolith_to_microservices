# Importing the required libraries  
import json
from http import client

from kafka import KafkaConsumer

# Gropu id, a good way for scale our software
my_group_id = 'ConsumerGroup'

# We create a kafka consumer
consumer = KafkaConsumer(
    client_id='ClientConsumerTest',
    group_id=my_group_id,
    bootstrap_servers=['localhost:29092'], 
    value_deserializer=lambda v: json.loads(v.decode('utf-8')),
    key_deserializer=lambda v: json.loads(v.decode('utf-8')),
    max_poll_records=10 
)

# Info about topics
print("Available topics: \n")
print(consumer.topics())

# Subscribing to topics
consumer.subscribe(topics=['test'])

# Info about subscription
print("Current suscription:\n")
print(consumer.subscription())

# Infinite loop to consume messages
for message in consumer:
    print("------------------------------")
    print("Message:")
    print(f"\t - key={message.key}" ) 
    print(f"\t - Value={message.value}" ) 
    print("------------------------------")

    