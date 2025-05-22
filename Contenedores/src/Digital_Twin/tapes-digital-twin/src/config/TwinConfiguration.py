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


class WaterAdditionConfiguration(metaclass=SingletonMeta):
    """ Class that will be get all especific information of the singleton"""

    def __init__(self):
        """ Constructor that get information form enviromente variables"""

        import os

        # Digital twin configuration
        self.line = str(1 if os.getenv('DT_LINE') == None else os.getenv('DT_LINE'))
        self.mould_size = int(15 if os.getenv('DT_MOULD_SIZE') == None else os.getenv('DT_MOULD_SIZE'))
        self.moulds_to_calculate = int(5 if os.getenv('DT_MOULDS_TO_CALCULATE') == None else os.getenv('DT_MOULDS_TO_CALCULATE'))
        self.type = str('DRUM' if os.getenv('DT_TYPE') == None else os.getenv('DT_TYPE'))

        # Kafka configuration
        self.client_id = str('WaterAddition-DigitalTwin' if os.getenv('KAFKA_CLIENT_ID') == None else os.getenv('KAFKA_CLIENT_ID'))
        self.group_id = str('Digital-Twin-Group' if os.getenv('KAFKA_GROUP_ID') == None else os.getenv('KAFKA_GROUP_ID'))
        self.broker_ip = str('localhost' if os.getenv('KAFKA_BROKER_IP') == None else os.getenv('KAFKA_BROKER_IP'))
        self.broker_port = int(29092 if os.getenv('KAFKA_BROKER_PORT') == None else os.getenv('KAFKA_BROKER_PORT'))
        self.kafka_broker = '{}:{}'.format(self.broker_ip, self.broker_port)

        self.kafka_mould_for_belts_topic = str('mould_for_belts' if os.getenv('KAFKA_MOULD_FOR_BELTS_TOPIC') == None else os.getenv('KAFKA_MOULD_FOR_BELTS_TOPIC'))
        self.kafka_water_prediction_unified_belts_topic = str('water_prediction_unified_belts' if os.getenv('KAFKA_PREDICTION_UNIFIED_BELTS_TOPIC') == None else os.getenv('KAFKA_PREDICTION_UNIFIED_BELTS_TOPIC'))
        self.kafka_water_prediction_drum_topic = str('water_prediction_cooling_drum' if os.getenv('KAFKA_PREDICTION_DRUM_TOPIC') == None else os.getenv('KAFKA_PREDICTION_DRUM_TOPIC'))
        self.kafka_mould_data_topic = str('mould_data' if os.getenv('KAFKA_MOULD_DATA_TOPIC') == None else os.getenv('KAFKA_MOULD_DATA_TOPIC'))
        self.kafka_sensor_data_topic = str('sensor_data' if os.getenv('KAFKA_SENSOR_DATA_TOPIC') == None else os.getenv('KAFKA_SENSOR_DATA_TOPIC'))

        # API Rest URLs        
        self.cooling_drum_predictor_api_url_base = str('http://localhost:8080/cooling-drum-water-prediction' if os.getenv('COOLING_DRUM_API_BASE') == None else os.getenv('COOLING_DRUM_API_BASE'))
        self.belts_predictor_api_url_base = str('http://localhost:8090/unified_belt_prediction' if os.getenv('BELTS_API_BASE') == None else os.getenv('BELTS_API_BASE'))

        # Detect if i am running on docker
        self.inside_docker = False if os.getenv('AM_I_IN_A_DOCKER_CONTAINER') == None else True


        

