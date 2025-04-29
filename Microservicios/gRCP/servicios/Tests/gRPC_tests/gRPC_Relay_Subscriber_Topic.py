# generate the client stubs for service.proto file in python (using this command)
# python -m grpc_tools.protoc --proto_path=. ./relay.proto --python_out=. --grpc_python_out=.

import grpc
import service.relay_pb2 as pb2
import service.relay_pb2_grpc as pb2_grpc

class SubscriptionClient:
    def __init__(self, stub, topic):
        self.stub = stub
        self.topic = topic

    def on_message(self, message):
        print(f"Mensaje recibido - Tema: {message.topic}, Valor: {message.value}")

    def subscribe(self):
        request = pb2.SubscribeRequest(topic=self.topic)
        try:
            for message in self.stub.Subscribe(request):
                self.on_message(message)
        except grpc.RpcError as e:
            print(f"Error en la suscripción: {e}")

def run_subscribe_client():
    channel = grpc.insecure_channel('localhost:50051')
    stub = pb2_grpc.RelayServiceStub(channel)

    topic = input("Ingrese el tema al que desea suscribirse: ")
    subscription_client = SubscriptionClient(stub, topic)
    
    try:
        subscription_client.subscribe()
    except KeyboardInterrupt:
        print("Suscripción finalizada.")

if __name__ == '__main__':
    run_subscribe_client()
