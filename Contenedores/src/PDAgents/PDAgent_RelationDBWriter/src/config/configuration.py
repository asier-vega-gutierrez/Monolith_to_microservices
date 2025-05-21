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

class PDAgentRelationDBWriterConfiguration(metaclass=SingletonMeta):
    """ Class that will be get all especific information of the singleton"""
    
    def __init__(self):
        """ Constructor that get information form enviromente variables"""

        import os

        # Kafka configuration
        self.client_id = str('DB-Relational-Storage-Agent' if os.getenv('KAFKA_CLIENT_ID') == None else os.getenv('KAFKA_CLIENT_ID'))
        self.group_id = str('DB-Relational-DB-Writer' if os.getenv('KAFKA_GROUP_ID') == None else os.getenv('KAFKA_GROUP_ID'))
        self.broker_ip = str('localhost' if os.getenv('KAFKA_BROKER_IP') == None else os.getenv('KAFKA_BROKER_IP'))
        self.broker_port = int(29092 if os.getenv('KAFKA_BROKER_PORT') == None else os.getenv('KAFKA_BROKER_PORT'))
        self.kafka_broker = '{}:{}'.format(self.broker_ip, self.broker_port)
        
        self.kafka_sensor_data_topic = str('sensor_data_' if os.getenv('KAFKA_SENSOR_DATA_TOPIC') == None else os.getenv('KAFKA_SENSOR_DATA_TOPIC'))
        self.kafka_chemical_composition_topic = str('chemical_composition_file' if os.getenv('KAFKA_CHEMICAL_COMPOSITION_TOPIC') == None else os.getenv('KAFKA_CHEMICAL_COMPOSITION_TOPIC'))
        self.kafka_waterprediction_drum_data_topic = str('water_prediction_cooling_drum_' if os.getenv('KAFKA_WATER_PREDICTION_DRUM_TOPIC') == None else os.getenv('KAFKA_WATER_PREDICTION_DRUM_TOPIC'))
        self.kafka_waterprediction_belt_data_topic = str('water_prediction_unified_belts' if os.getenv('KAFKA_WATER_PREDICTION_TAPES_TOPIC') == None else os.getenv('KAFKA_WATER_PREDICTION_TAPES_TOPIC'))
        self.kafka_pouring_data_topic = str('pouring_mysql' if os.getenv('KAFKA_POURING_DATA_TOPIC') == None else os.getenv('KAFKA_POURING_DATA_TOPIC'))
        self.kafka_mould_data_topic = str('mould_data_' if os.getenv('KAFKA_MOULD_DATA_TOPIC') == None else os.getenv('KAFKA_MOULD_DATA_TOPIC'))
        
        
        # MySql storage
        self.postgres_ip = str('localhost' if os.getenv('POSTGRES_IP') == None else os.getenv('POSTGRES_IP'))
        self.postgres_port = int(5432 if os.getenv('POSTGRES_PORT') == None else os.getenv('POSTGRES_PORT'))
        self.postgres_user = str('postgres' if os.getenv('POSTGRES_USER') == None else os.getenv('POSTGRES_USER'))
        self.postgres_pass = str('MUCSI_Deusto2022' if os.getenv('POTSGRES_PASS') == None else os.getenv('POSTGRES_PASS'))
        self.postgres_db = str('Foundry_Relational_Storage' if os.getenv('POSTGRES_DB') == None else os.getenv('POSTGRES_DB'))
        
        # Detect if i am running on docker
        self.inside_docker = False if os.getenv('AM_I_IN_A_DOCKER_CONTAINER') == None else True

        


