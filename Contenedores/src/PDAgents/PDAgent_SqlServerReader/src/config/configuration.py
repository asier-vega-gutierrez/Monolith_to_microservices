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

class PDAgentSqlServerReaderConfig(metaclass=SingletonMeta):
    """ Class that will be get all especific information of the singleton"""
    
    def __init__(self):
        """ Constructor that get information form enviromente variables"""

        import os

        # Kafka configuration
        self.broker_ip = str('localhost' if os.getenv('KAFKA_BROKER_IP') == None else os.getenv('KAFKA_BROKER_IP'))
        self.broker_port = int(29092 if os.getenv('KAFKA_BROKER_PORT') == None else os.getenv('KAFKA_BROKER_PORT'))
        self.kafka_broker = '{}:{}'.format(self.broker_ip, self.broker_port)
        
        self.kafka_mould_data_topic = str('mould_data' if os.getenv('KAFKA_MOULD_DATA_TOPIC') == None else os.getenv('KAFKA_MOULD_DATA_TOPIC'))
        self.kafka_sensor_data_topic = str('sensor_data' if os.getenv('KAFKA_SENSOR_DATA_TOPIC') == None else os.getenv('KAFKA_SENSOR_DATA_TOPIC'))
        
        # Sql Server Storage
        self.sql_server_ip = str('localhost' if os.getenv('SQL_SERVER_IP') == None else os.getenv('SQL_SERVER_IP'))
        self.sql_server_port = int(1433 if os.getenv('SQL_SERVER_PORT') == None else os.getenv('SQL_SERVER_PORT'))
        self.sql_server_user = str('sa' if os.getenv('SQL_SERVER_USER') == None else os.getenv('SQL_SERVER_USER'))
        self.sql_server_pass = str('MUCSI_Deusto2022' if os.getenv('SQL_SERVER_PASS') == None else os.getenv('SQL_SERVER_PASS'))
        
        self.sql_server_mould_db = str('DB-MOULDING' if os.getenv('SQL_SERVER_MOULD_DB') == None else os.getenv('SQL_SERVER_MOULD_DB'))
        self.sql_server_sensor_db = str('DB-SENSORS' if os.getenv('SQL_SERVER_SENSOR_DB') == None else os.getenv('SQL_SERVER_SENSOR_DB'))

        # Detect if i am running on docker
        self.inside_docker = False if os.getenv('AM_I_IN_A_DOCKER_CONTAINER') == None else True

        


