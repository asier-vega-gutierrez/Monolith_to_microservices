class SingletonMeta(type):
    """ Base class for singleton implementation """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class CapturerConfiguration(metaclass=SingletonMeta):
    """ Class that will be get all especific information of the singleton"""
    
    def __init__(self):
        """ Constructor that get information form enviromente variables"""

        import os

        # Kafka configuration
        self.broker_ip = str('localhost' if os.getenv('KAFKA_BROKER_IP') == None else os.getenv('KAFKA_BROKER_IP'))
        self.broker_port = int(29092 if os.getenv('KAFKA_BROKER_PORT') == None else os.getenv('KAFKA_BROKER_PORT'))
        self.kafka_broker = '{}:{}'.format(self.broker_ip, self.broker_port)
        
        self.kafka_chemical_composition_topic = str('chemical_composition_file' if os.getenv('KAFKA_CHEMICAL_COMPOSITION_TOPIC') == None else os.getenv('KAFKA_CHEMICAL_COMPOSITION_TOPIC'))
    
        
        # File to read
        self.composition_file_path = str('/Users/jnieves/Documents/Universidad de Deusto/2023/Cloud Computing/Practica/03 - Docker/3.1 - Docker compose/Solucion/Storage/File_Input/data/cq.csv' if os.getenv('COMPOSITION_FILE_PATH') == None else os.getenv('COMPOSITION_FILE_PATH'))
        
        # Detect if i am running on docker
        self.inside_docker = False if os.getenv('AM_I_IN_A_DOCKER_CONTAINER') == None else True

        


