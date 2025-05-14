import grpc
import communication.service.relay_pb2 as pb2
import communication.service.relay_pb2_grpc as pb2_grpc

import signal
from threading import Thread
from config.configuration import ApplicationConfiguration

class SubscriptionClient:
    def __init__(self, topic, consumer):
        """ Constructor of the class """

        # We get the configuration
        config = ApplicationConfiguration()

        self._channel = grpc.insecure_channel(f'{config.communcation_server}:{config.communication_port}')
        self._stub = pb2_grpc.RelayServiceStub(self._channel)

        self._topic = topic
        self._consumer = consumer

    def on_message(self, message):
        """ Event for message detection """

        print(f"Message received - Topic: {message.topic}, Value: {message.value}")
        self._consumer.broadcast(message.topic, message.value)

    def subscribe(self):
        """ Method to subscribe to the server """
        request = pb2.SubscribeRequest(topic=self._topic)
        try:
            # We need to get the responses to be able to cancel them
            self._responses = self._stub.Subscribe(request)
            for message in self._responses:
                self.on_message(message)
        except grpc.RpcError as e:
            if not e.cancelled():
                print(f"Error with the subscription of the topic {self._topic}: {e}")
    
    def unsuscribe(self):
        """ Method to unsuscribe """

        # The way to end the stream        
        self._responses.cancel()

class Consumer():
    """ Class that is used for receive messages from our gRPC server """

    def __init__(self):
        """ Constructor of the class that generates the basic structures for an observer/observable pattern """

        self._subscribers = {}
        self._grpc_subcription_clients = {}
    
    def add_subscriber(self, topic, subscriber):
        """ Method that are focused on add a new subscriber """
           
        # We check if the topic is already stored
        if topic not in self._subscribers:
            self._subscribers[topic] = []
            self._grpc_subcription_clients[topic] = SubscriptionClient(topic, self)

            # We need to launch the subscribe method in a thread because the stream is blocking the main thread
            Thread(target=lambda grpc_subcription_client: grpc_subcription_client.subscribe(), args=([self._grpc_subcription_clients[topic]])).start()    

        # We add the subscriber
        self._subscribers[topic].append(subscriber)
        
    def remove_subscriber(self, topic, subscriber):
        """ Methods that are focused on remove a subscriber for a topic """

        # We make the work only if the topic is there ans the subscriber is stored
        if topic in self._subscribers and subscriber in self._subscribers[topic]:
            # We remove the subscriber
            self._subscribers[topic].remove(subscriber)

            if len(self._subscribers[topic]) == 0:
                del self._subscribers[topic]
                self._grpc_subcription_clients[topic].unsuscribe() 
                del self._grpc_subcription_clients[topic]
    
    def broadcast(self, topic, message):
        """ Method to notify information to subscribers """

        for subscriber in self._subscribers[topic]:
            processThread = Thread(target=subscriber.notify, args=(message,))  # <- note extra ','
            processThread.start()