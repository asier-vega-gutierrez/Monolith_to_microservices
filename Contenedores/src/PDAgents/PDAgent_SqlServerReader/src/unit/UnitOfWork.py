

from store.specific.SensorStore import *
from store.specific.MouldStore import *

from config.configuration import PDAgentSqlServerReaderConfig

class UnitOfWork():
    """ Class that defined the unit of work """

    def __init__(self) -> None:
        """ Defaul contructor creating all stores """

        # We get the configuration
        config = PDAgentSqlServerReaderConfig()

        self.sensor_store = SensorStore(config.sql_server_sensor_db)
        self.mould_store = MouldStore(config.sql_server_mould_db)