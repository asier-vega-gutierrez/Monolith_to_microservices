from threading import Thread

from recorder.RecordingWorker import RelationalRecordingWorker
   
def main():
    """ Main method to confiure the consumer from kafka """
    
    print("***********************************************")
    print("        FOUNDRY RELATION STORAGE WORKER        ")
    print("***********************************************")
    print()
    print()
    print("Creating Recordig Worker...")
    rw = RelationalRecordingWorker()
    print()
    print("Starting data gathering for the digital twin...")

    t1 = Thread(target=rw.start_recording)
    t1.start()
    t1.join()    

if __name__ == "__main__":
    main()