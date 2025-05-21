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


class PDAgentTemporlSeriesWriterConfiguration(metaclass=SingletonMeta):
    """ Class that will be get all especific information of the singleton"""

    def __init__(self):
        """ Constructor that get information form enviromente variables"""

        import os

        # Kafka configuration
        self.client_id = str('Influx-DB-Storage-Agent' if os.getenv('KAFKA_CLIENT_ID') == None else os.getenv('KAFKA_CLIENT_ID'))
        self.group_id = str('TemporalSeries-Writer-Group' if os.getenv('KAFKA_GROUP_ID') == None else os.getenv('KAFKA_GROUP_ID'))
        self.broker_ip = str('localhost' if os.getenv('KAFKA_BROKER_IP') == None else os.getenv('KAFKA_BROKER_IP'))
        self.broker_port = int(29092 if os.getenv('KAFKA_BROKER_PORT') == None else os.getenv('KAFKA_BROKER_PORT'))
        self.kafka_broker = '{}:{}'.format(self.broker_ip, self.broker_port)

        self.kafka_drum_water_prediction_topic = str('water_prediction_cooling_drum' if os.getenv('KAFKA_DRUM_WATER_PREDICTION_TOPIC') == None else os.getenv('KAFKA_DRUM_WATER_PREDICTION_TOPIC'))
        self.kafka_belts_water_prediction_topic = str('water_prediction_unified_belts' if os.getenv('KAFKA_BELTS_WATER_PREDICTION_TOPIC') == None else os.getenv('KAFKA_BELTS_WATER_PREDICTION_TOPIC'))
        self.kafka_sensor_data_topic = str('sensor_data' if os.getenv('KAFKA_SENSOR_DATA_TOPIC') == None else os.getenv('KAFKA_SENSOR_DATA_TOPIC'))

        # Influx DB configuration
        self.influx_token = str('_vunCmVedzTMarNJ4y4iwTGpFU84gerPj7sDyAlwJuHpMKFyjc187bhpGsYZwDVaTnJz4nZ2esU-MZ3UlNVFRA==' if os.getenv('INFLUX_TOKEN') == None else os.getenv('INFLUX_TOKEN'))
        self.influx_url = str('http://localhost:8086' if os.getenv('INFLUX_URL') == None else os.getenv('INFLUX_URL'))
        self.influx_org = str('Deusto' if os.getenv('INFLUX_ORG') == None else os.getenv('INFLUX_ORG'))
        self.influx_bucket = str('cloud-bucket' if os.getenv('INFLUX_BUCKET') == None else os.getenv('INFLUX_BUCKET'))

        # Detect if i am running on docker
        self.inside_docker = False if os.getenv('AM_I_IN_A_DOCKER_CONTAINER') == None else True


        

