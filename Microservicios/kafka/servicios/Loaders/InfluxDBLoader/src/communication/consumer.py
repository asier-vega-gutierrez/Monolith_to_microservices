from kafka import KafkaConsumer
from threading import Thread
import json

class Consumer():
    """ Class that is used for receiving messages from our Kafka server """

    def __init__(self):
        """ Constructor of the class that generates the basic structures for an observer/observable pattern """
        self._subscribers = {}
        self._kafka_consumers = {}

    def add_subscriber(self, topic, subscriber):
        """ Method that is focused on adding a new subscriber """
        if topic not in self._subscribers:
            self._subscribers[topic] = []
            self._kafka_consumers[topic] = KafkaConsumer(
                topic,
                bootstrap_servers=['localhost:29092'],
                value_deserializer=lambda v: json.loads(v.decode('utf-8')),
                key_deserializer=lambda v: json.loads(v.decode('utf-8')),
                group_id='ConsumerGroup'
            )

            Thread(target=self._consume_messages, args=(topic,)).start()

        self._subscribers[topic].append(subscriber)

    def _consume_messages(self, topic):
        """ Method to consume messages from Kafka """
        for message in self._kafka_consumers[topic]:
            self.broadcast(topic, message.value)

    def remove_subscriber(self, topic, subscriber):
        """ Method that is focused on removing a subscriber for a topic """
        if topic in self._subscribers and subscriber in self._subscribers[topic]:
            self._subscribers[topic].remove(subscriber)

            if len(self._subscribers[topic]) == 0:
                del self._subscribers[topic]
                self._kafka_consumers[topic].close()
                del self._kafka_consumers[topic]

    def broadcast(self, topic, message):
        """ Method to notify information to subscribers """
        for subscriber in self._subscribers[topic]:
            Thread(target=subscriber.notify, args=(message,)).start()
    