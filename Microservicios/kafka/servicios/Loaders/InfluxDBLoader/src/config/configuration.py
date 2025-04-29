

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


class ApplicationConfiguration(metaclass=SingletonMeta):
    """ Class that will be get all especific information of the singleton"""

    def __init__(self):
        """ Constructor that get information form enviromente variables"""

        import os
        
        self.communcation_server = str('localhost' if os.getenv('GRPC_IP') == None else os.getenv('GRPC_IP'))
        self.communication_port = str('50051' if os.getenv('GRPC_PORT') == None else os.getenv('GRPC_PORT'))

        """
        DATA INPUT CONFIGURATION
        """

        # File to read
        self.composition_file_path = str('/Users/jnieves/Documents/Universidad de Deusto/2023/Cloud Computing/Practica/00 - Monolitico/Solucion/repositorios/storage/file_input/data/cq.csv' if os.getenv('COMPOSITION_FILE_PATH') == None else os.getenv('COMPOSITION_FILE_PATH'))
        
        # MySql storage
        self.mysql_ip = str('localhost' if os.getenv('MYSQL_IP') == None else os.getenv('MYSQL_IP'))
        self.mysql_port = int(3306 if os.getenv('MYSQL_PORT') == None else os.getenv('MYSQL_PORT'))
        self.mysql_user = str('root' if os.getenv('MYSQL_USER') == None else os.getenv('MYSQL_USER'))
        self.mysql_pass = str('MUCSI_Deusto2022' if os.getenv('MYSQL_PASS') == None else os.getenv('MYSQL_PASS'))
        self.mysql_db = str('pouring' if os.getenv('MYSQL_DB') == None else os.getenv('MYSQL_DB'))
        
        # Sql Server Storage
        self.sql_server_ip = str('localhost' if os.getenv('SQL_SERVER_IP') == None else os.getenv('SQL_SERVER_IP'))
        self.sql_server_port = int(1433 if os.getenv('SQL_SERVER_PORT') == None else os.getenv('SQL_SERVER_PORT'))
        self.sql_server_user = str('sa' if os.getenv('SQL_SERVER_USER') == None else os.getenv('SQL_SERVER_USER'))
        self.sql_server_pass = str('MUCSI_Deusto2022' if os.getenv('SQL_SERVER_PASS') == None else os.getenv('SQL_SERVER_PASS'))
        
        self.sql_server_mould_db = str('DB-MOULDING' if os.getenv('SQL_SERVER_MOULD_DB') == None else os.getenv('SQL_SERVER_MOULD_DB'))
        self.sql_server_sensor_db = str('DB-SENSORS' if os.getenv('SQL_SERVER_SENSOR_DB') == None else os.getenv('SQL_SERVER_SENSOR_DB'))

        """
        DATA OUTPUT CONFIGURATION
        """

        # Postgres storage
        self.postgres_ip = str('localhost' if os.getenv('POSTGRES_IP') == None else os.getenv('POSTGRES_IP'))
        self.postgres_port = int(5432 if os.getenv('POSTGRES_PORT') == None else os.getenv('POSTGRES_PORT'))
        self.postgres_user = str('postgres' if os.getenv('POSTGRES_USER') == None else os.getenv('POSTGRES_USER'))
        self.postgres_pass = str('MUCSI_Deusto2022' if os.getenv('POTSGRES_PASS') == None else os.getenv('POSTGRES_PASS'))
        self.postgres_db = str('Foundry_Relational_Storage' if os.getenv('POSTGRES_DB') == None else os.getenv('POSTGRES_DB'))
        

        # Influx DB configuration
        self.influx_token = str('_vunCmVedzTMarNJ4y4iwTGpFU84gerPj7sDyAlwJuHpMKFyjc187bhpGsYZwDVaTnJz4nZ2esU-MZ3UlNVFRA==' if os.getenv('INFLUX_TOKEN') == None else os.getenv('INFLUX_TOKEN'))
        self.influx_url = str('http://localhost:8086' if os.getenv('INFLUX_URL') == None else os.getenv('INFLUX_URL'))
        self.influx_org = str('Deusto' if os.getenv('INFLUX_ORG') == None else os.getenv('INFLUX_ORG'))
        self.influx_bucket = str('cloud-bucket' if os.getenv('INFLUX_BUCKET') == None else os.getenv('INFLUX_BUCKET'))
        
        # Topics for messages
        self.chemical_composition_topic = str('chemical_composition_file' if os.getenv('CHEMICAL_COMPOSITION_TOPIC') == None else os.getenv('CHEMICAL_COMPOSITION_TOPIC'))
        self.pouring_data_topic = str('pouring_mysql' if os.getenv('POURING_PROCESS_TOPIC') == None else os.getenv('POURING_PROCESS_TOPIC'))
        self.pouring_alarm_topic = str('pouring_alarm_mysql' if os.getenv('POURING_ALARM_PROCESS_TOPIC') == None else os.getenv('POURING_ALARM_PROCESS_TOPIC'))
        self.mould_data_topic = str('mould_data' if os.getenv('MOULD_DATA_TOPIC') == None else os.getenv('MOULD_DATA_TOPIC'))
        self.sensor_data_topic = str('sensor_data' if os.getenv('SENSOR_DATA_TOPIC') == None else os.getenv('SENSOR_DATA_TOPIC'))
        self.water_prediction_unified_belts_topic = str('water_prediction_unified_belts' if os.getenv('PREDICTION_UNIFIED_BELTS_TOPIC') == None else os.getenv('PREDICTION_UNIFIED_BELTS_TOPIC'))
        self.water_prediction_drum_topic = str('water_prediction_cooling_drum' if os.getenv('PREDICTION_DRUM_TOPIC') == None else os.getenv('PREDICTION_DRUM_TOPIC'))
        self.pouring_data_topic = str('pouring_mysql' if os.getenv('POURING_DATA_TOPIC') == None else os.getenv('POURING_DATA_TOPIC'))
        self.mould_for_belts_topic = str('mould_for_belts' if os.getenv('MOULD_FOR_BELTS_TOPIC') == None else os.getenv('MOULD_FOR_BELTS_TOPIC'))
        
        

