from unit.UnitOfWork import *
from dataproducer.producer import notify_pouring_using_kafka
from time import sleep  
from threading import Thread
from datetime import datetime
from random import *

def send_data_rec():
    """ Procedure that manages the pouring data recs """

    data_rec_counter = 0
    
    # We get the unit of work
    unit_of_work = UnitOfWork()

    # We get 4000 data recs
    data_recs = unit_of_work.data_rec_store.get_data_recs()

    # it is running always
    while True:
        # we get the alarm and we send it
        data_rec_to_send = data_recs[data_rec_counter]
        data_rec_counter += 1
        if(data_rec_counter >= len(data_recs)):
            data_rec_counter = 0
        
        # Adjust data
        data_rec_to_send.time = datetime.now()
        if data_rec_to_send.model_code is not None:
            data_rec_to_send.archive_model_data = unit_of_work.archive_model_store.get_archive_model_by_code(data_rec_to_send.model_code)

        # Log and kafka notification
        print(f"Notify data rec - Pouring Mould = {data_rec_to_send.nr_pouring_mould}")
        notify_pouring_using_kafka(data_rec_to_send)

        # We wait 7 senconds to simulate the real world
        sleep(7) 

def send_alarms():
    """ Procedure that manages the alarms """
    
    alarm_counter = 0
    
    # We get the unit of work
    unit_of_work = UnitOfWork()

    # We get 80 alarms
    #alarms = unit_of_work.alarm_store.get_alarms()
    alarms = unit_of_work.alarm_store.get_num_alarms(80)

    # it is running always
    while True:
        # we get the alarm and we send it
        alarm_to_send = alarms[alarm_counter]
        alarm_counter += 1
        if(alarm_counter >= len(alarms)):
            alarm_counter = 0
        
        # We complere with datetiem information
        alarm_to_send.time = datetime.now()

        # Print as be used as log
        print(f"Notify alarm - Tra ID = {alarm_to_send.tra_id}")
        
        # Notify information through Kafka
        notify_pouring_using_kafka(alarm_to_send)

        # Wait 30 seconds, trying to simulate the real world
        sleep(30) 
    

def main():
    """ Main method of thge PDAgent for MySql Data Base """

    # We are going to simulate the concurrent work of two tasks, hence, 
    # we use threads to do it.

    # 1.-  Task to send alarms
    t1 = Thread(target=send_alarms)
    t1.start()

    # 2.- Task to send data
    t2 = Thread(target=send_data_rec)
    t2.start()

    # We join to both task to end the software
    t1.join()
    t2.join()

if __name__ == "__main__":
    main()