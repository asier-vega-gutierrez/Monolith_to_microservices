

# generate the client stubs for service.proto file in python (using this command)
# python -m grpc_tools.protoc --proto_path=. ./relay.proto --python_out=. --grpc_python_out=.
import grpc
import communication.service.relay_pb2 as pb2
import communication.service.relay_pb2_grpc as pb2_grpc

from config.configuration import ApplicationConfiguration

def data_distribution(topic: str, 
                      value: str):
    """ Procedure to distribute information  """

    # We get the configuration to know the server
    config = ApplicationConfiguration()

    # We create the channel
    channel = grpc.insecure_channel(f'{config.communcation_server}:{config.communication_port}')
    stub = pb2_grpc.RelayServiceStub(channel)

    # We create the message
    message = pb2.Message(topic=topic, 
                          value=value)
    response = stub.Publish(message)
    
    # Feedback with the messahe
    print(f"Message with topic {topic} and data {value} published.")


