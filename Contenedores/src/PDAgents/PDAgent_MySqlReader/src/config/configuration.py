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

class PDAgentMySqlConfiguration(metaclass=SingletonMeta):
    """ Class that will be get all especific information of the singleton"""
    
    def __init__(self):
        """ Constructor that get information form enviromente variables"""

        import os

        # Kafka configuration
        self.broker_ip = str('localhost' if os.getenv('KAFKA_BROKER_IP') == None else os.getenv('KAFKA_BROKER_IP'))
        self.broker_port = int(29092 if os.getenv('KAFKA_BROKER_PORT') == None else os.getenv('KAFKA_BROKER_PORT'))
        self.kafka_broker = '{}:{}'.format(self.broker_ip, self.broker_port)
        
        self.kafka_mysql_data_topic = str('pouring_mysql' if os.getenv('KAFKA_MYSQL_PROCESS_TOPIC') == None else os.getenv('KAFKA_MYSQL_PROCESS_TOPIC'))
        
        
        # MySql storage
        self.mysql_ip = str('mysql-input' if os.getenv('MYSQL_IP') == None else os.getenv('MYSQL_IP'))
        self.mysql_port = int(3306 if os.getenv('MYSQL_PORT') == None else os.getenv('MYSQL_PORT'))
        self.mysql_user = str('root' if os.getenv('MYSQL_USER') == None else os.getenv('MYSQL_USER'))
        self.mysql_pass = str('MUCSI_Deusto2022' if os.getenv('MYSQL_PASS') == None else os.getenv('MYSQL_PASS'))
        self.mysql_db = str('pouring' if os.getenv('MYSQL_DB') == None else os.getenv('MYSQL_DB'))
        
        # Detect if i am running on docker
        self.inside_docker = False if os.getenv('AM_I_IN_A_DOCKER_CONTAINER') == None else True

        


