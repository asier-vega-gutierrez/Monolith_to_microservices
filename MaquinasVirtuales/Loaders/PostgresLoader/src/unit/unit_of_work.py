'''from unit.input import InputUnitOfWork'''
from unit.output import OutputUnitOfWork

class UnitOfWork():
    """ Class that defined the unit of work """

    def __init__(self) -> None:
        """ Defaul contructor creating all stores """

        '''self.input = InputUnitOfWork()'''        
        self.output = OutputUnitOfWork()        