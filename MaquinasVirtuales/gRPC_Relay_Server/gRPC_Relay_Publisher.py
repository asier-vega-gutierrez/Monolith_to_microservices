

# generate the client stubs for service.proto file in python (using this command)
# python -m grpc_tools.protoc --proto_path=. ./relay.proto --python_out=. --grpc_python_out=.
import grpc
import relay_pb2 as pb2
import relay_pb2_grpc as pb2_grpc

def publish_message(stub):
    topic = input("Ingrese el tema del mensaje: ")
    value = input("Ingrese el valor del mensaje: ")

    message = pb2.Message(topic=topic, value=value)
    response = stub.Publish(message)
    
    print("Mensaje publicado con éxito.")

def run_publish_client():
    channel = grpc.insecure_channel('localhost:50051')
    stub = pb2_grpc.RelayServiceStub(channel)

    try:
        while True:
            publish_message(stub)
    except KeyboardInterrupt:
        print("Publicación de mensajes finalizada.")

if __name__ == '__main__':
    run_publish_client()
