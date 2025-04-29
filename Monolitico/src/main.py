from extraction.management.extractor import DataExtractorManager
from load.management.loader import DataLoaderManager
from transfromation.digital_twin.management import DigitalTwinManagement
   
def main():
    """ Main method to claunch the full process of our MUCSI application """
    
    print("***********************************************")
    print("                MUCSI APP DEMO                 ")
    print("***********************************************")
    print()
    print()
    print("Creating Data Extractors...")
    dataExtractor = DataExtractorManager()
    print("Creating Data Transformers...")
    digitalTwin = DigitalTwinManagement()
    print("Creating Data Loaders...")
    dataLoader = DataLoaderManager()
    print()
    print("Starting all process work...")
    print("\t- Starting loading work...")
    dataLoader.start_loading_process()
    print("\t- Starting transformer work...")
    digitalTwin.start_digital_twin_processing()
    print("\t- Starting extraction work...")
    dataExtractor.start_extraction_process()
    print()
    print("Press <Enter> to end the execution of our system...")
    print("---------------------------------------------------")
    input()
    print()
    print()
    print()
    print()
    print()
    print()
    print("Stoping all process work...")
    print("\t- Stopping extraction work...")
    dataExtractor.stop_extraction_process()
    print("\t- Stopping loading work...")
    dataLoader.stop_loading_process()
    print("\t- Stopping transformer work...")
    digitalTwin.stop_digital_twin_processing()
    print("We are stoping the running threads (no cancelation tokens used, so we need to wait until each iteration value.)")
    print("BYE. ")

if __name__ == "__main__":
    main()