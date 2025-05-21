

from store.specific.chemical_store import *

class UnitOfWork():
    """ Class that defined the unit of work """

    def __init__(self, composition_file_path) -> None:
        """ Defaul contructor creating all stores """

        self.chemical_composition_store = ChemicalStore(composition_file_path)