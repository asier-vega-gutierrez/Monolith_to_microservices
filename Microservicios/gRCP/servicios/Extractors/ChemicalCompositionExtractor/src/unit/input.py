from store.specific.input.ChemicalStore import *
'''from store.specific.input.AlarmStore import *
from store.specific.input.ArchiveModelsStore import *
from store.specific.input.ArchiveModelsStore import *
from store.specific.input.DataRecStore import *
from store.specific.input.SensorStore import *
from store.specific.input.MouldStore import *'''

from config.configuration import ApplicationConfiguration

class InputUnitOfWork():
    """ Class that defined the unit of work """

    def __init__(self) -> None:
        """ Defaul contructor creating all stores """

        # We get the configuration
        config = ApplicationConfiguration()

        # CSV file storage
        self.chemical_composition_store = ChemicalStore(config.composition_file_path)
        
        '''# MySQL storage
        self.alarm_store = AlarmStore()
        self.archive_model_store = ArchiveModelStore()
        self.data_rec_store = DataRecStore()

        # SqlServer storage
        self.sensor_store = SensorStore(config.sql_server_sensor_db)
        self.mould_store = MouldStore(config.sql_server_mould_db)'''