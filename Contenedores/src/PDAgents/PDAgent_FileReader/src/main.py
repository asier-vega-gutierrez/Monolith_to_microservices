from unit.unit_of_work import *
from dataproducer.producer import *
from time import sleep  
from threading import Thread
from datetime import datetime
import random

"""BEGIN


Variables de entorno: 

- composition_file_path 
- kafka_server
- kafka_port


FIN"""


def send_chemical_composition():
    """ Procedure that manages the pouring data recs """

    chemical_composition_counter = 0
    
    # We get the configuration
    config = CapturerConfiguration()

    # We get the unit of work
    unit_of_work = UnitOfWork(config.composition_file_path)

    # We get chemical compositions
    chemical_compositions = unit_of_work.chemical_composition_store.get_chemical_compistions()

    # it is running always
    while True:
        # we get the alarm and we send it
        chemical_composition_to_send = chemical_compositions[chemical_composition_counter]
        chemical_composition_counter += 1
        if(chemical_composition_counter >= len(chemical_compositions)):
            chemical_composition_counter = 0
        
        # Adjust data
        chemical_composition_to_send.date = datetime.now()
        
        print("Notify chemical composition - ID = {}".format(chemical_composition_to_send.id))
        notify_chemical_composition_using_kafka(chemical_composition_to_send)

        time_for_next = random.randint(60, 120)
        print("Time waiting to next message: {} s.".format(time_for_next))
        sleep(time_for_next) 

def main():

    t1 = Thread(target=send_chemical_composition)
    t1.start()

    t1.join()

if __name__ == "__main__":
    main()