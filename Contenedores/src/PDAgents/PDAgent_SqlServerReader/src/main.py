from unit.UnitOfWork import *
from dataproducer.producer import notify_data_using_kafka
from time import sleep  
from threading import Thread
from datetime import datetime, timezone
from random import *

def send_moulds(line):
    """ Procedure that manages the pouring data recs """

    moulds_data_counter = 0
    
    # We get the unit of work
    unit_of_work = UnitOfWork()

    # We get 4000 data recs
    moulds_list = unit_of_work.mould_store.get_line_mould(line)

    # it is running always
    while True:
        # we get the alarm and we send it
        mould_to_send = moulds_list[moulds_data_counter]
        moulds_data_counter += 1
        if(moulds_data_counter >= len(moulds_list)):
            moulds_data_counter = 0
        
        # Adjust data
        print("Notify mould data - Line = {} Ref = {}".format(mould_to_send.cod_linea, mould_to_send.reference))
        notify_data_using_kafka(mould_to_send)

        sleep(7) 

def send_sensors():
    """Procedure that manages the sesnor data """
    
    sensor_counter = 0
    
    # We get the unit of work
    unit_of_work = UnitOfWork()

    # Get sensors data
    sensors_data = unit_of_work.sensor_store.get_sensors_data()

    # it is running always
    while True:
        # we get the alarm and we send it
        sensor_l1_to_send = sensors_data[sensor_counter][0]
        sensor_l1_to_send.timestamp = datetime.now(timezone.utc)

        sensor_l2_to_send = sensors_data[sensor_counter][1]
        sensor_l2_to_send.timestamp = datetime.now(timezone.utc)

        sensor_counter += 1
        if(sensor_counter >= len(sensors_data)):
            sensor_counter = 0
        try:
            print("Notify sensor L1 - Timestamp = {}".format(sensor_l1_to_send.timestamp))        
            notify_data_using_kafka(sensor_l1_to_send)
        except:
            print('ERROR sending sensor data for L1.')

        try:
            print("Notify sensor L2 - Timestamp = {}".format(sensor_l2_to_send.timestamp))
            notify_data_using_kafka(sensor_l2_to_send)
        except:
            print('ERROR sending sensor data for L2.')

        sleep(1) 
    

def main():

    print("***********************************************")
    print("              SQL SERVER AGENT                 ")
    print("***********************************************")
    print()
    print()

    print("Launching SENSORS thread...")
    t1 = Thread(target=send_sensors)
    t1.start()

    print("Launching L1 MOULDS thread...")
    t2 = Thread(target=send_moulds, args=[1])
    t2.start()

    print("Launching L2 MOULDS thread...")
    t3 = Thread(target=send_moulds, args=[2])
    t3.start()#

    t1.join()
    t2.join()
    t3.join()

if __name__ == "__main__":
    main()