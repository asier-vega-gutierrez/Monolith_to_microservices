from threading import Thread

from recorder.RecordingWorker import InfluxDBRecordingWorker
   
def main():
    """ Main method to confiure the consumer from kafka """
    
    print("***********************************************")
    print("           INFLUX DB STORAGE WORKER           ")
    print("***********************************************")
    print()
    print()
    print("Creating Recordig Worker...")
    rw = InfluxDBRecordingWorker()
    print()
    print("Starting data gathering for the infllux db storage...")

    t1 = Thread(target=rw.start_recording)
    t1.start()
    t1.join()    

if __name__ == "__main__":
    main()