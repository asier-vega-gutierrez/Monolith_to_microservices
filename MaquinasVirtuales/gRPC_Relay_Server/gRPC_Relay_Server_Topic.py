import grpc
from concurrent import futures
import service.relay_pb2 as pb2
import service.relay_pb2_grpc as pb2_grpc
import logging

class SubscriptionClient:
    def __init__(self, topic):
        # TODO: Add topic to constructor and store as an attribute
        self.topic = topic #
        self.queue = []

    def on_message(self, message):
        # TODO: Send messages only if the topic of the message is our suscription topic
        if not self.topic or message.topic == self.topic: #
            self.queue.append(message)

    def subscribe(self):
        while True:
            if self.queue:
                yield self.queue.pop(0)

class RelayServicer(pb2_grpc.RelayServiceServicer):
    def __init__(self):
        self.subscribers = []

    def Publish(self, request, context):
        # TODO: When our request will be adapted with topic and value, this next line will be correct.
        print(f"Received Publish request with topic: {request.topic}, value: {request.value}")
        self.log_info(f"Received Publish request with topic: {request.topic}, value: {request.value}")

        for subscriber in self.subscribers:
            try:
                subscriber.on_message(pb2.Message(value=request.value, topic=request.topic))
            except Exception as e:
                print(f"Error sending message to subscriber: {str(e)}")

        return pb2.PublishConfirmed()

    def Subscribe(self, request, context):
        # TODO: Due to we have chenged the SubscriptionClient constructor, and also the request, this line will be ok.
        subscriber = SubscriptionClient(request.topic)
        self.subscribers.append(subscriber)

        try:
            for message in subscriber.subscribe():
                yield message
        except grpc.RpcError as e:
            print(f"Error in Subscribe: {e}")
        finally:
            self.subscribers.remove(subscriber)

    def log_info(self, message):
        # Configure the logging system (you can customize this based on your needs)
        logging.basicConfig(filename='logs/Grpc.txt', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

        # Log the provided message at the INFO level
        logging.info(message)

def empty_file(file_path):
    # Open the file in write mode, which truncates the file
    with open(file_path, 'w'):
        pass

def serve():
    print("***********************************************")
    print("               gRPC Relay Server               ")
    print("***********************************************")
    print()
    print()

    print("Creating Service...")
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=50))
    pb2_grpc.add_RelayServiceServicer_to_server(RelayServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print('Server running on port 50051')

    print('Type CRTL+C to finish...')
    server.wait_for_termination()

if __name__ == '__main__':
    empty_file('logs/Grpc.txt')
    serve()