# importing the required libraries  
from kafka import KafkaConsumer
from json import dumps 
import json
from time import sleep  
from threading import Thread
from config.TwinConfiguration import WaterAdditionConfiguration
import uuid

class MUCSIConsumer():
    """ Class that is used for receive messages from kafka """

    def __init__(self):
        """ Constructor of the class that generates the basic structures for an observer/observable pattern """

        config = WaterAdditionConfiguration()
        my_group_id = f'{config.group_id}-L{config.line}-{config.type}'

        self._subscribers = {}

        print("STARTING to connect to kafka server for consuming data...")
        server_ready = False
        while not server_ready:
            try:
                self._consumer = KafkaConsumer(
                    client_id=f'{config.client_id}-L{config.line}-{config.type}_{uuid.uuid4()}',
                    group_id=my_group_id,
                    bootstrap_servers=[config.kafka_broker],                     
                    value_deserializer=lambda v: json.loads(v.decode('utf-8')),
                    key_deserializer=lambda v: json.loads(v.decode('utf-8')),
                    max_poll_records=10
                )
                server_ready = True
                print("KAFKA READY to receive pouring data...")
            except:
                print("KAFKA NOT READY to notify pouring data...")
                print("\tWaiting 5 seconds...")
                sleep(5)
        
            
    def add_subscriber(self, topic, subscriber):
        """ Method that are focused on add a new subscriber """
        
        # We chech if the topic is in kafka
        if topic in self._consumer.topics():    
            # We check if the topic is already stored
            if topic not in self._subscribers:
                self._subscribers[topic] = []
        
            # We add the subscriber
            self._subscribers[topic].append(subscriber)

            # We resubscribe to the topics
            self._resubscribe_topics()
    
    def remove_subscriber(self, topic, subscriber):
        """ Methods that are focused on remove a subscriber for a topic """

        # We make the work only if the topic is there ans the subscriber is stored
        if topic in self._subscribers and subscriber in self._subscribers[topic]:
            # We remove the subscriber
            self._subscribers.remove(subscriber)

            # We resubscribe to the topics
            self.__resubscribe_topics()
 
    def _resubscribe_topics(self):
        """ Method that makes the resubscription to the topics """

        self._consumer.unsubscribe()
        self._consumer.subscribe(topics=list(self._subscribers.keys()))

    def start_listening_messages(self):
        """ Method to start receiving messages """

        print("Starting reading process...")
        print("Waiting for new Kafka messages... \n") 

        # Waitibng for messages
        for message in self._consumer:
            print("Received a message with topic=%s" % message.topic) 
            print("\tNotifiying to %d subscribers..." % len(self._subscribers[message.topic]) )

            # We make the notifications
            for subscriber in self._subscribers[message.topic]:
                processThread = Thread(target=subscriber.notify, args=(message,))  # <- note extra ','
                processThread.start()
