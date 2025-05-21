from store.specific.AlarmStore import *
from store.specific.ArchiveModelsStore import *
from store.specific.DataRecStore import *

class UnitOfWork():
    """ Class that defined the unit of work """

    def __init__(self) -> None:
        """ Defaul contructor creating all stores """

        self.alarm_store = AlarmStore()
        self.archive_model_store = ArchiveModelStore()
        self.data_rec_store = DataRecStore()