from threading import Thread

from config.TwinConfiguration import WaterAdditionConfiguration
from digitaltwin.WaterAdditionTwin import WaterAdditionDigitalTwin


def main():
    """ Main method to manage all """
    config = WaterAdditionConfiguration()

    print("***********************************************")
    print("   WATER ADDITION DIGITAL TWIN CONFIGURATION")
    print("***********************************************")
    print()
    print("Type: {}".format(config.type))
    print("Line: {}".format(config.line))
    print("Mould Size: {}".format(config.mould_size))
    print("Moulds to Calculate: {}".format(config.moulds_to_calculate))

    print()
    print("Creating the digital twin...")
    dt = WaterAdditionDigitalTwin()
    print()
    print("Starting data gathering for the digital twin...")

    t1 = Thread(target=dt.start_digital_twin_processing)
    t1.start()
    t1.join()    

if __name__ == "__main__":
    main()